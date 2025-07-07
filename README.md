# QR Code Generator from URL

This project showcases two approaches to creating a Python script that generates a QR Code from a user-provided URL. The main goal is to compare a **manually written** solution with an **AI-assisted** version generated using **GitHub Copilot**.

## 🧠 Purpose

To explore the productivity gains and different coding approaches between traditional development and an AI-assisted workflow, using a simple and practical task: generating a QR Code from a valid URL.

---

## ⚙️ Technologies Used

- **Python 3.11+**
- `qrcode` library
- `Pillow` library (for image manipulation and display)
- `urllib.parse` (used by Copilot for URL validation)
- `.venv` virtual environment

---

## 📂 Project Structure

This repository contains:

 `qrcode_manual.py`: manually written implementation
- `qrcode_lowcode.py`: GitHub Copilot-generated implementation
- `.venv/`: pre-configured virtual environment
- `requirements.txt`: list of required packages

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/gbpefernandes/qrcode_python
cd your-repository

2. Activate the virtual environment:

Windows:

```bash
.venv\Scripts\activate

Run one of the implementations:

```bash
python qrcode_manual.py/qrcode_lowcode.py

---

## Comparison of Approaches

| Aspect            | Manual Implementation    | GitHub Copilot (AI) Implementation   |
| ----------------- | ------------------------ | ------------------------------------ |
| URL validation    | Built from scratch       | Used standard library `urllib.parse` |
| Development speed | Standard                 | Much faster                          |
| Code complexity   | Slightly higher          | More concise and direct              |
| Final result      | Functional and effective | Functional and effective             |

Both versions generate a QR Code from a valid URL, display the image, and save it in the same directory as the script.

## 📸 Screenshots

**Manual Implementation Output**

![Manual Implementation](manual_qrcode.png)

**GitHub Copilot Implementation Output**

![Copilot Implementation](lowcode_qrcode.png)