# Home / LLMs / 🚀 Local Deployment of OmniParser v2.0 with pyautogui for True Automated Clicking! Supports macOS, Windows, and Linux! Easily Automate Computer Operations! From Server Deployment to Client Development, from API Design to Full Automation Control Workflow

🚀 **Local Deployment of OmniParser v2.0 with pyautogui for True Automated Clicking!**  
Supports macOS, Windows, and Linux! Easily automate computer operations! From server deployment to client development, from API design to full automation control workflow.

[Read on the website](https://www.aivi.fyi//llms/deploy-omniparser2.0)

⏱️ **4-minute read**

OmniParser V2.0 is an advanced open-source AI tool developed by Microsoft, designed to convert GUI (Graphical User Interface) screenshots into structured data. This functionality enhances the interaction between large language models (LLMs) and visual elements on the screen, enabling smarter automation and user assistance.

OmniParser V2.0 represents a significant advancement in AI vision parsing technology. It not only improves the interaction between users and digital interfaces but also enhances automation capabilities across various applications.

### Related Video Links:
- [Watch on Bilibili](https://www.bilibili.com/video/BV1u3AaeqEtm/)
- [Watch on YouTube](https://youtu.be/aBcedtGCA9I)
- [My Open Source Project](https://github.com/win4r/AISuperDomain)
- [Buy Me a Coffee](https://ko-fi.com/aila)

Contact me via WeChat: stoeng [Please specify your intention when adding me]  
Available for projects related to large model fine-tuning, RAG, AI agents, and AI application development.

---

## Key Features

- **Speed & Efficiency**: Compared to its previous version, OmniParser V2.0 significantly reduces processing latency by about 60%. The average processing time on high-end GPUs like A100 is 0.6 seconds, and 0.8 seconds on the 4090 model.
  
- **Enhanced Accuracy**: The tool achieves an average accuracy rate of 39.6% in detecting interactive elements, a significant improvement over earlier versions. This accuracy is achieved through the use of a finely tuned YOLOv8 model and an expanded training dataset covering various UI components.
  
- **Powerful Input/Output Capabilities**: OmniParser supports screenshots from multiple platforms, including Windows and mobile devices. It can generate structured representations of UI elements, detailing clickable areas and their functionalities.
  
- **Seamless Integration with LLMs**: The tool integrates with multiple AI models via a unified interface called OmniTool, such as OpenAI's GPT-4o, DeepSeek R1, Qwen 2.5VL, and Anthropic Sonnet. This integration enables the creation of automated testing tools and assistive technology solutions.

---

## Application Areas

OmniParser V2.0 has a wide range of application scenarios:

- **UI Automation**: Automate repetitive tasks by allowing AI agents to interact with GUIs.
- **Assistive Technology Solutions**: Provide structured data to assistive technologies, helping users with disabilities.
- **User Interface Analysis**: Analyze UI designs based on data extracted from screenshots to improve usability.

---

## 🚀 Installation Steps

```bash
conda create -n "omni" python==3.12 -y && conda activate omni
git clone https://github.com/microsoft/OmniParser.git
cd OmniParser
pip install -r requirements.txt

# Download V2 model weights
rm -rf weights/icon_detect weights/icon_caption weights/icon_caption_florence
for f in icon_detect/{train_args.yaml,model.pt,model.yaml} icon_caption/{config.json,generation_config.json,model.safetensors}; do
    huggingface-cli download microsoft/OmniParser-v2.0 "$f" --local-dir weights
done
mv weights/icon_caption weights/icon_caption_florence

# Start UI
python gradio_demo.py

---
```markdown
# Home / LLMs / 🚀 Local Deployment of OmniParser v2.0 with pyautogui for True Automated Clicking! Supports macOS, Windows, and Linux! Easily Automate Computer Operations! From Server Deployment to Client Development, from API Design to Full Automation Control Workflow

🚀 **Local Deployment of OmniParser v2.0 with pyautogui for True Automated Clicking!**  
Supports macOS, Windows, and Linux! Easily automate computer operations! From server deployment to client development, from API design to full automation control workflow.

[Read on the website](https://www.aivi.fyi//llms/deploy-omniparser2.0)

⏱️ **4-minute read**

OmniParser V2.0 is an advanced open-source AI tool developed by Microsoft, designed to convert GUI (Graphical User Interface) screenshots into structured data. This functionality enhances the interaction between large language models (LLMs) and visual elements on the screen, enabling smarter automation and user assistance.

OmniParser V2.0 represents a significant advancement in AI vision parsing technology. It not only improves the interaction between users and digital interfaces but also enhances automation capabilities across various applications.

### Related Video Links:
- [Watch on Bilibili](https://www.bilibili.com/video/BV1u3AaeqEtm/)
- [Watch on YouTube](https://youtu.be/aBcedtGCA9I)
- [My Open Source Project](https://github.com/win4r/AISuperDomain)
- [Buy Me a Coffee](https://ko-fi.com/aila)

Contact me via WeChat: stoeng [Please specify your intention when adding me]  
Available for projects related to large model fine-tuning, RAG, AI agents, and AI application development.

---

## Key Features

- **Speed & Efficiency**: Compared to its previous version, OmniParser V2.0 significantly reduces processing latency by about 60%. The average processing time on high-end GPUs like A100 is 0.6 seconds, and 0.8 seconds on the 4090 model.
  
- **Enhanced Accuracy**: The tool achieves an average accuracy rate of 39.6% in detecting interactive elements, a significant improvement over earlier versions. This accuracy is achieved through the use of a finely tuned YOLOv8 model and an expanded training dataset covering various UI components.
  
- **Powerful Input/Output Capabilities**: OmniParser supports screenshots from multiple platforms, including Windows and mobile devices. It can generate structured representations of UI elements, detailing clickable areas and their functionalities.
  
- **Seamless Integration with LLMs**: The tool integrates with multiple AI models via a unified interface called OmniTool, such as OpenAI's GPT-4o, DeepSeek R1, Qwen 2.5VL, and Anthropic Sonnet. This integration enables the creation of automated testing tools and assistive technology solutions.

---

## Application Areas

OmniParser V2.0 has a wide range of application scenarios:

- **UI Automation**: Automate repetitive tasks by allowing AI agents to interact with GUIs.
- **Assistive Technology Solutions**: Provide structured data to assistive technologies, helping users with disabilities.
- **User Interface Analysis**: Analyze UI designs based on data extracted from screenshots to improve usability.

---

## 🚀 Installation Steps

```bash
conda create -n "omni" python==3.12 -y && conda activate omni
git clone https://github.com/microsoft/OmniParser.git
cd OmniParser
pip install -r requirements.txt

# Download V2 model weights
rm -rf weights/icon_detect weights/icon_caption weights/icon_caption_florence
for f in icon_detect/{train_args.yaml,model.pt,model.yaml} icon_caption/{config.json,generation_config.json,model.safetensors}; do
    huggingface-cli download microsoft/OmniParser-v2.0 "$f" --local-dir weights
done
mv weights/icon_caption weights/icon_caption_florence

# Start UI
python gradio_demo.py

# Server Configuration
cd ~/OmniParser
pip install fastapi uvicorn python-multipart pillow requests
nano main.py
python main.py
```

---

## 🚀 Pyautogui Example

```python
# pip install pyautogui
from time import sleep
import pyautogui
import time

def bbox_to_coords(bbox, screen_width, screen_height):
    """Convert bbox coordinates to screen coordinates."""
    xmin, ymin, xmax, ymax = bbox
    x_center = int((xmin + xmax) / 2 * screen_width)
    y_center = int((ymin + ymax) / 2 * screen_height)
    return x_center, y_center

def click_bbox(bbox):
    """Click on the specified bbox."""
    screen_width, screen_height = pyautogui.size()
    x, y = bbox_to_coords(bbox, screen_width, screen_height)

    # Move the mouse to the specified position
    pyautogui.moveTo(x, y, duration=0.2)  # duration is the movement time in seconds

    # Click the mouse
    pyautogui.click()
    print(f"Clicked at coordinates: x={x}, y={y}")

if __name__ == '__main__':
    sleep(5)
    # Example bbox (from provided data)
    bbox = [0.36728453636169434, 0.9408491849899292, 0.39909330010414124, 0.9875121712684631]  # chrome
    # Click bbox
    click_bbox(bbox)
```

---

## 🚀 Server Code Example

```python
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

# Initialize models
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
        # Read uploaded image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # Temporarily save the image
        image_save_path = 'imgs/temp_image.png'
        image.save(image_save_path)

        # Configure bounding box drawing parameters
        box_overlay_ratio = image.size[0] / 3200
        draw_bbox_config = {
            'text_scale': 0.8 * box_overlay_ratio,
            'text_thickness': max(int(2 * box_overlay_ratio), 1),
            'text_padding': max(int(3 * box_overlay_ratio), 1),
            'thickness': max(int(3 * box_overlay_ratio), 1),
        }

        # OCR Processing
        ocr_bbox_rslt, is_goal_filtered = check_ocr_box(
            image_save_path,
            display_img=False,
            output_bb_format='xyxy',
            goal_filtering=None,
            easyocr_args={'paragraph': False, 'text_threshold': 0.9},
            use_paddleocr=use_paddleocr
        )
        text, ocr_bbox = ocr_bbox_rslt

        # Get labeled image and parsed content
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

        # Format parsed results
        parsed_content = '\n'.join([f'icon{i}: {str(v)}' for i, v in enumerate(parsed_content_list)])

        return JSONResponse({
            "status": "success",
            "labeled_image": dino_labled_img,  # base64 encoded image
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
```

---

## 🚀 Client Code Example

```python
import requests
from PIL import Image
import base64
import io
import pyautogui
from time import sleep
import json
import ast  # For parsing string-formatted dictionaries

def process_image(
    image_path: str,
    api_url: str = "http://192.168.1.105:8000/process_image",
    box_threshold: float = 0.05,
    iou_threshold: float = 0.1,
    use_paddleocr: bool = True,
    imgsz: int = 640
):
    files = {
        'file': ('image.png', open(image_path, 'rb'), 'image/png')
    }

    params = {
        'box_threshold': box_threshold,
        'iou_threshold': iou_threshold,
        'use_paddleocr': use_paddleocr,
        'imgsz': imgsz
    }

    response = requests.post(api_url, files=files, params=params)

    if response.status_code == 200:
        result = response.json()

        if result['status'] == 'success':
            labeled_image = Image.open(io.BytesIO(base64.b64decode(result['labeled_image'])))
            return {
                'status': 'success',
                'labeled_image': labeled_image,
                'parsed_content': result['parsed_content'],
                'label_coordinates': result['label_coordinates']
            }
        else:
            return {'status': 'error', 'message': result.get('message', 'Unknown error')}
    else:
        return {'status': 'error', 'message': f'HTTP error {response.status_code}'}

def parse_icon_data(content_str):
    """Parse a string containing icon data into a list."""
    icons = []
    lines = content_str.strip().split('\n')
    for line in lines:
        if line.startswith('icon'):
            try:
                # Extract content within curly braces
                dict_str = line[line.index('{'):line.rindex('}') + 1]
                # Parse string into dictionary
                icon_data = ast.literal_eval(dict_str)
                icons.append(icon_data)
            except Exception as e:
                print(f"Parsing error: {e}")
                continue
    return icons

def bbox_to_coords(bbox, screen_width, screen_height):
    """Convert bbox coordinates to screen coordinates."""
    xmin, ymin, xmax, ymax = bbox

    # Consider Mac top menu bar offset
    menu_bar_height = 25

    # Offset upwards to avoid clicking on the filename
    y_offset = -15  # Offset upwards by 15 pixels

    # Calculate relative coordinates
    x_center = int((xmin + xmax) / 2 * screen_width)
    y_center = int((ymin + ymax) / 2 * (screen_height - menu_bar_height)) + menu_bar_height + y_offset

    # Ensure coordinates are within screen bounds
    x_center = max(0, min(x_center, screen_width))
    y_center = max(0, min(y_center, screen_height))

    return x_center, y_center

def click_bbox(bbox):
    """Double-click on the specified bbox."""
    # Get screen resolution
    screen_width, screen_height = pyautogui.size()
    print(f"Current screen resolution: {screen_width}x{screen_height}")

    # Get click coordinates
    x, y = bbox_to_coords(bbox, screen_width, screen_height)

    print(f"\nAbout to perform double-click:")
    print(f"Target coordinates: x={x}, y={y}")
    print("3 seconds preparation time...")

    sleep(3)

    # Move mouse to specified position
    pyautogui.moveTo(x, y, duration=0.5)

    print("Mouse is in position, double-clicking in 1 second...")

    sleep(1)

    # Perform double-click
    pyautogui.doubleClick()
    print(f"Double-clicked at coordinates: x={x}, y={y}")

def find_dog_avif_coordinates(icons):
    """Find the dog.avif icon in the parsed content."""
    for i, icon in enumerate(icons):
        if isinstance(icon, dict) and 'content' in icon:
            content = icon['content'].strip().lower()
            if 'dog.avif' in content:
                print(f"Found dog.avif, icon index: {i}")
                return icon['bbox']
    return None

if __name__ == "__main__":
    # Get and print screen resolution
    screen_width, screen_height = pyautogui.size()
    print(f"Current screen resolution: {screen_width}x{screen_height}")

    image_path = "s.png"
    result = process_image(
        image_path=image_path,
        box_threshold=0.05,
        iou_threshold=0.1,
        use_paddleocr=True,
        imgsz=640
    )

    if result['status'] == 'success':
        icons = parse_icon_data(result['parsed_content'])
        dog_avif_bbox = find_dog_avif_coordinates(icons)

        if dog_avif_bbox:
            print("Found dog.avif coordinates:", dog_avif_bbox)
            click_bbox(dog_avif_bbox)
        else:
            print("Dog.avif icon not found")
    else:
        print("Error:", result['message'])
```

---

## Tags:
`multimodal`, `OmniParser`, `OmniParser v2.0`, `pyautogui`

## Categories:
`LLMs`

📅 Updated: February 18, 2025
```

# Server Configuration
cd ~/OmniParser
pip install fastapi uvicorn python-multipart pillow requests
nano main.py
python main.py
