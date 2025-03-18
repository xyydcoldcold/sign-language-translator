# Sign Language Translator (MVP)

A simple real-time sign language recognition tool using **MediaPipe**, **OpenCV**, and **pyttsx3**.  
It detects basic hand gestures via webcam, converts them into text, and reads them aloud for better accessibility.

---

## 🧠 Features

- ✋ Real-time hand tracking using [MediaPipe Hands](https://developers.google.com/mediapipe)
- 📝 Displays gesture text alongside webcam feed
- 🔊 Text-to-speech using `pyttsx3`
- 🎯 Simple, intuitive UI layout (left = video, right = recognized gesture)

---

## 🧰 Tech Stack

- Python 3.9 (via Miniforge / Conda)
- MediaPipe
- OpenCV
- pyttsx3

---

## 🖥️ Demo

<img width="200" alt="image" src="https://github.com/user-attachments/assets/c3177858-f405-452b-9dff-c3ed1132530c" />


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/sign-language-translator.git
cd sign-language-translator
```

### 2. Set up Conda environment

Option 1: Use `requirements.txt`

```bash
conda create -n gesture-env python=3.9
conda activate gesture-env
pip install -r requirements.txt
```

Option 2: Manual install

```bash
conda create -n gesture-env python=3.9
conda activate gesture-env
pip install mediapipe opencv-python pyttsx3
```

### 3. Run the app

```bash
python main.py
```

> Press `Q` to quit the webcam window

---

## 📁 Project Structure

```
.
├── main.py             # Main application file
├── README.md
└── .gitignore
```

---

## 📌 Future Ideas

- Add support for more gestures (✌️ OK 🖐️ etc.)
- Dynamic sentence construction
- Export gesture logs
- GUI using Tkinter or PyQt
- Deploy as standalone app (desktop or web)

---

## 🙌 Credits

Created with ❤️ using Python + OpenCV + MediaPipe  
Inspired by accessibility and real-time interaction

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
