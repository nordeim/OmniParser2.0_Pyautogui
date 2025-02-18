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
