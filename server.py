# pip install fastapi uvicorn python-multipart pillow requests

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import torch
from PIL import Image
import io
import base64
from typing import Optional
import numpy as np

from util.utils import check_ocr_box, get_yolo_model, get_caption_model_processor, get_som_labeled_img

app = FastAPI()

# 初始化模型
yolo_model = get_yolo_model(model_path='weights/icon_detect/model.pt')
caption_model_processor = get_caption_model_processor(
    model_name="florence2", 
    model_name_or_path="weights/icon_caption_florence"
)

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

@app.post("/process_image")
async def process_image(
    file: UploadFile = File(...),
    box_threshold: float = 0.05,
    iou_threshold: float = 0.1,
    use_paddleocr: bool = True,
    imgsz: int = 640
):
    try:
        # 读取上传的图片
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # 临时保存图片
        image_save_path = 'imgs/temp_image.png'
        image.save(image_save_path)
        
        # 配置绘制边界框的参数
        box_overlay_ratio = image.size[0] / 3200
        draw_bbox_config = {
            'text_scale': 0.8 * box_overlay_ratio,
            'text_thickness': max(int(2 * box_overlay_ratio), 1),
            'text_padding': max(int(3 * box_overlay_ratio), 1),
            'thickness': max(int(3 * box_overlay_ratio), 1),
        }

        # OCR处理
        ocr_bbox_rslt, is_goal_filtered = check_ocr_box(
            image_save_path,
            display_img=False,
            output_bb_format='xyxy',
            goal_filtering=None,
            easyocr_args={'paragraph': False, 'text_threshold': 0.9},
            use_paddleocr=use_paddleocr
        )
        text, ocr_bbox = ocr_bbox_rslt

        # 获取标记后的图片和解析内容
        dino_labled_img, label_coordinates, parsed_content_list = get_som_labeled_img(
            image_save_path,
            yolo_model,
            BOX_TRESHOLD=box_threshold,
            output_coord_in_ratio=True,
            ocr_bbox=ocr_bbox,
            draw_bbox_config=draw_bbox_config,
            caption_model_processor=caption_model_processor,
            ocr_text=text,
            iou_threshold=iou_threshold,
            imgsz=imgsz,
        )

        # 格式化解析结果
        parsed_content = '\n'.join([f'icon {i}: {str(v)}' for i, v in enumerate(parsed_content_list)])

        return JSONResponse({
            "status": "success",
            "labeled_image": dino_labled_img,  # base64编码的图片
            "parsed_content": parsed_content,
            "label_coordinates": label_coordinates
        })

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
