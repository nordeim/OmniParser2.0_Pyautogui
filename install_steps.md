conda create -n "omni" python==3.12 -y && conda activate omni

git clone https://github.com/microsoft/OmniParser.git

cd OmniParser

pip install -r requirements.txt

# 下载V2模型权重
rm -rf weights/icon_detect weights/icon_caption weights/icon_caption_florence 
for f in icon_detect/{train_args.yaml,model.pt,model.yaml} icon_caption/{config.json,generation_config.json,model.safetensors}; do
    huggingface-cli download microsoft/OmniParser-v2.0 "$f" --local-dir weights
done
mv weights/icon_caption weights/icon_caption_florence

# 启动UI
python gradio_demo.py

# 服务端配置

cd ~/OmniParser

pip install fastapi uvicorn python-multipart pillow requests

nano main.py

python main.py
