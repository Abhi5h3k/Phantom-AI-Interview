## 🚀 Phantom-AI-Interview: Exploring AI Assistance in Technical Interviews 


[![Abhishek LinkedIn](https://img.shields.io/badge/Abhishek-LinkedIn-blue.svg?style=for-the-badge)](https://www.linkedin.com/in/abhi5h3k/) [![Abhishek StackOverflow](https://img.shields.io/badge/Abhishek-StackOverflow-orange.svg?style=for-the-badge)](https://stackoverflow.com/users/6870223/abhi?tab=profile)


## **AI is disrupting tech hiring… but how far can it go? 🤖💻**  

<br>

With modern **LLMs** and AI-powered tools, **getting AI assistance in coding interviews is easier than ever**. This project explores **how AI could seamlessly assist in real-time technical interviews**—and what it means for hiring in the future.  

<br>

> **🔍 Disclaimer:** *This project is an experimental exploration of AI's capabilities in real-time assistance. It is meant to **study AI-human interaction** in technical settings and **not** to promote unfair practices in interviews or assessments.*  


## 📌 Why This Project?  

<br>

With the rise of **large language models (LLMs)** and AI-powered tools, **how could AI assist in real-time coding interviews?**  

Phantom-AI-Interview is a **proof-of-concept** that explores AI's ability to listen, read, and respond to technical questions in a virtual setting. This project aims to understand the boundaries of AI assistance and its implications in hiring and technical assessments.  

<br>

<img src="https://github.com/user-attachments/assets/dd47208d-5c17-4844-8806-d404167bd7fe" width="200px">

---

## 👀 What’s in this Project?

✅ **On-Screen Text Extraction** – Using EasyOCR to capture and process text from your screen.  
✅ **AI-Assisted Response Automation** – Simulating realistic typing for coding and text-based questions.  
✅ **Phantom Mode** – Operates entirely with hotkey shortcuts, eliminating the need for a visible GUI.  
✅ **Active Listening Mode** – AI stays alert for real-time interactions and responses.  
✅ **Clipboard Jacking** – Silently captures copied text, sends it to an LLM, and retrieves a response without detection.  

**💡 Note:** This project uses an open-source LLM on CPU. Performance and accuracy can be significantly improved with GPU acceleration, larger models, or by switching to GPT API with optimized prompts.

---

## 🌍 AI’s Impact on Tech Hiring  
AI-powered tools like **LLMs, automated assessments, and interview assistants** are changing the way hiring works. Some key trends:  
- **Faster Screening:** AI can analyze candidates and recommend top matches.  
- **Bias Concerns:** AI-driven hiring tools risk **reinforcing biases** in decision-making.  
- **Real-Time Assistance:** Tools like Phantom-AI-Interview show how AI could provide **live support** in technical interviews.  

🔗 **Read more:** [How AI is disrupting tech hiring](https://www.linkedin.com/news/story/how-ai-is-disrupting-tech-hiring-6342252/)  

## 📢 Ethical Considerations  
This project is **not intended to be used for unethical purposes, including interview fraud**. It is a **conceptual study** on how AI could integrate into virtual hiring processes and technical assessments.  

<br>

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

## 🚀Project Setup

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

![image](https://github.com/user-attachments/assets/145d0bd6-42bf-464e-8072-78824ff0dec0)

1. Download Whisper **[whisper-bin-x64](https://github.com/ggerganov/whisper.cpp/actions/runs/13716448084/)**

    <img src="https://github.com/user-attachments/assets/9448bb51-c713-4bb2-83a2-829e80748134">

    Extract it to the **root directory** of the project

2. Download ggml-base.en.bin [Whisper Models on Hugging Face](https://huggingface.co/ggerganov/whisper.cpp/tree/main)

    <img src="https://github.com/user-attachments/assets/6cd0c7ba-2e4e-4670-9788-39619c23e48e">

3. Download the [Vosk Model](https://alphacephei.com/vosk/models)
Get the Vosk model (**vosk-model-en-in-0.5**)



## 📂 Installation & Usage  :

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

## 🚀 Future Improvements & Suggestions

If you want to enhance PhantomAI for better performance and a more seamless experience, consider these improvements:

- **Use GPU & Larger Models** – For faster and more accurate responses, switch to a GPU-powered setup with a bigger local LLM.
- **Switch to GPT API** – If local inference is slow, using the GPT API provides better performance and higher accuracy.
- **Better Prompt Engineering** – Optimize response quality by designing improved prompt templates or dynamically selecting templates based on the question type.
- **Move to Containers** – This project was a quick Windows-based concept. For better portability and stability, consider switching to Docker/Linux-based deployment.
- **Bundle into a Single Executable** – Improve usability by packaging everything into a standalone .exe file for easy distribution.

---

## 🌍 Disclaimer
This project is purely for educational purposes and ethical AI research. It highlights the potential risks associated with silent AI in virtual environments but is not intended to be used for unethical activities.

---

## 📚 License
Feel free to use and modify as needed.

---

