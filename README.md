# PhantomAI 🤖

[![Abhishek LinkedIn](https://img.shields.io/badge/Abhishek-LinkedIn-blue.svg?style=for-the-badge)](https://www.linkedin.com/in/abhi5h3k/) [![Abhishek StackOverflow](https://img.shields.io/badge/Abhishek-StackOverflow-orange.svg?style=for-the-badge)](https://stackoverflow.com/users/6870223/abhi?tab=profile)

This is a fun **Sunday AI experiment!** I wanted to explore how AI and LLMs could be used to **silently assist** in interviews, exams, and meetings—without anyone noticing. This project is purely conceptual and serves as a **demonstration of potential risks** and security concerns in AI-driven automation.

PhantomAI is something I put together as a solo project, designed to operate discreetly, allowing users to issue commands and receive responses without a visible interface. The original idea was to see if AI could listen to live audio feeds from meetings (such as interviews), detect specific questions, and generate responses—all while staying invisible during screen sharing.

This concept is intentionally not fully refined to the point where it poses a serious challenge for recruiters, but it remains stealthy and demonstrates how silent AI tools can operate discreetly. While it's just a fun experiment, it also raises important questions about the **future of virtual interviews and the traditional approach to interview and coding challenges**.

<img src="https://github.com/user-attachments/assets/dd47208d-5c17-4844-8806-d404167bd7fe" width="200px">

## 📺 Demo (Click for YouTube Video)

### 🤖 All responses are played as audio output, which you can listen to through your connected headset 🎧. Notifications are enabled only for demonstration purposes; by default, they are turned off 💡.

### 🎧 [Stereo Mode](https://www.wintips.org/how-to-enable-stereo-mix-if-not-showing-as-recording-device-in-windows-11-10/) – AI Listens to Interviewer Directly  
This mode allows PhantomAI to listen to the interviewer's voice directly from the system audio instead of the microphone. This ensures that the AI captures exactly what the interviewer is saying and generates responses accordingly.  

[![Stereo Mode, Listen to Interviewer / Output Voice](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYndwcG1sZjF2MXVqdmU3ZjI5eWpvcGN5ZWxtN3VnYWVjNDgyb2s5ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6KziBOVNrsZ5eURBBh/giphy.gif)](https://www.youtube.com/watch?v=xPOmbY0iaVE)  

---

### 📝 On-Screen Text Extraction (OCR) – Extract Interview Questions  
OCR mode is helpful when you need to extract a question from the interviewer's chat, a coding screen, or an online test. PhantomAI reads the text displayed on the screen and processes it for AI-assisted responses.  

[![On-Screen Text Extraction](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXJ2cGhhb2JvdGwyZWVqdjYzZGhhMDFpZXFxNzR2eWdrdmNmZmFteiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6vlTYvfqtczqtn2QBY/giphy.gif)](https://www.youtube.com/watch?v=YCq53T8dCfE)  

---

### 📋 Clipboard Jacking – Quick & Silent AI Assistance  
Clipboard Jacking is the fastest way to get help from the AI without any visible UI activity. If an interviewer shares a coding question in chat or an online IDE, and you're stuck on syntax or logic, simply copy the part you need help with and press a hotkey. PhantomAI will silently send it to the LLM and provide a response.  

[![Clipboard Jacking](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWhmdWNub201eG1vZzF6OWxpbzM0ZTRuaTdrcHNhMXRyYmxqc2RwMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vlALsXIGWhAbVHClyJ/giphy.gif)](https://www.youtube.com/watch?v=fHlCZ1uN0qo)  


---

### 👨‍💻 AI-Assisted Response  
**Active Listening Mode**  

![Active Listening Mode](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzliMG5iandsdTMzcjNzbThnZXhtNTFmZXpjcW81bjhuOHZkdjV5NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fuM4l6Yxhzz2QcYKu1/giphy.gif)

---

## 👀 What’s in this Project?

✅ **On-Screen Text Extraction** – Using EasyOCR to capture and process text from your screen.  
✅ **AI-Assisted Response Automation** – Simulating realistic typing for coding and text-based questions.  
✅ **Phantom Mode** – Operates entirely with hotkey shortcuts, eliminating the need for a visible GUI.  
✅ **Active Listening Mode** – AI stays alert for real-time interactions and responses.  
✅ **Clipboard Jacking** – Silently captures copied text, sends it to an LLM, and retrieves a response without detection.  
✅ **Ethical Concerns & Security Risks** – Exploring both the potential and dangers of AI-driven automation.  
✅ **Future of AI in Productivity & Cheating Prevention** – Discussing real-world implications and countermeasures.  

**💡 Note:** This project uses an open-source LLM on CPU. Performance and accuracy can be significantly improved with GPU acceleration, larger models, or by switching to GPT API with optimized prompts.

**💡 Disclaimer:** This is a proof-of-concept and does not promote unethical behavior. The goal is to highlight how AI can be both a tool for productivity and a potential security concern.

---

## 👨‍💻 Technical Details

- **Live Audio Processing**: Uses Vosk for real-time speech recognition.
- **File-Based Transcription**: Uses Whisper for processing recorded audio files.
- **Customizable Hotkeys**: Modify key bindings via `config.ini` to trigger AI commands silently.
- **Screen Capture**: Uses EasyOCR to read input from screen.

---

## 💡 System Requirements

- **Tested on:** Windows 11
- **Processor:** Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz 2.30GHz
- **RAM:** 32.0 GB (31.8 GB usable)

---

## 🚀 Installation & Setup

### Folder Structure
Your project directory should be structured as follows:

```
Phantom-AI-Interview/
│── whisper-bin-x64/          # Download [whisper-bin-x64](https://github.com/ggerganov/whisper.cpp/actions/runs/13716448084/) (Place at root)
    │── Some whisper files
    │── models
        │── ggml-base.en.bin  # Download ggml-base.en.bin [Whisper Models on Hugging Face](https://huggingface.co/ggerganov/whisper.cpp/tree/main)
│── vosk-model-en-in-0.5/     # Downloaded Vosk model (Place at root)
│── src/                      # Source code
│── config                    # Config folder containing Configuration file for hotkeys
│── requirements.txt          # Dependencies
│── run.py                    # Main script
```
### Setup Instructions
Since some required files are large and cannot be pushed to GitHub, follow these steps to set up your environment:

1. Extract Whisper **whisper-bin-x64.7z**
Extract it to the root directory of the project
2. Download the [Vosk Model](https://alphacephei.com/vosk/models)
Get the Vosk model (**vosk-model-en-in-0.5**)

![image](https://github.com/user-attachments/assets/145d0bd6-42bf-464e-8072-78824ff0dec0)



### **1. Install Python 3.11.0**
Ensure you have Python 3.11.0 installed. You can download it from [python.org](https://www.python.org/downloads/release/python-3110/).

### **2. Create a Virtual Environment**
```sh
py -m venv phantomAI_venv
```

### **3. Activate the Virtual Environment**
- **Windows:**
  ```sh
  phantomAI_venv\Scripts\activate
  ```

### **4. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **5. Configure Hotkeys**
Check `config.ini` for hotkey shortcuts. You can update them as per your preference.

### **6. Run PhantomAI**
```sh
py run.py
```

---

## 📝 Technologies Used

### **1. Vosk for Real-Time Speech Recognition**
- Uses `vosk-model-en-in-0.5` for live transcription.
- Find better models here: [Vosk Models](https://alphacephei.com/vosk/models)

### **2. Whisper for File-Based Transcription**
- Uses `whisper-bin-x64` and `ggml-base.en.bin` for processing recorded audio.
- Find the latest builds: [Whisper.cpp Artifacts](https://github.com/ggerganov/whisper.cpp/actions/runs/13716448084/)
- More models available here: [Whisper Models on Hugging Face](https://huggingface.co/ggerganov/whisper.cpp/tree/main)

### **3. Ollama for LLM Inference**
- Docker setup:
  ```sh
  docker-compose up -d
  ```
- Pull the model:
  ```sh
  docker exec -it ollama ollama pull qwq
  ```
- Find more models: [Ollama Search](https://ollama.com/search)

---

## 🌍 Disclaimer
This project is purely for educational purposes and ethical AI research. It highlights the potential risks associated with silent AI in virtual environments but is not intended to be used for unethical activities.

---

## 📚 License
Feel free to use and modify as needed.

---

