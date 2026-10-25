# SmartCare — Healthcare Information Assistant

A beginner-friendly healthcare information website built with Python and Streamlit. It does not require a paid API key. It can run locally or be deployed for free with Streamlit Community Cloud.

## Features
- Home dashboard
- General symptom information and safe next-step guidance
- Health library with common topics
- BMI calculator
- Emergency warning-sign guidance
- FAQs and clear medical-safety disclaimers

## Important limitations
SmartCare is an educational, rule-based prototype. It does not diagnose, predict disease, or replace professional medical care. Its content is illustrative and should be reviewed by qualified healthcare professionals before real-world use. Do not enter personal or sensitive health information.

## Requirements
- Python 3.10 or newer
- Internet connection only to install packages (the app itself runs locally)

## Setup on Windows (PowerShell)

1. Extract this project folder.
2. Open PowerShell in the `SmartCare_Healthcare_Assistant` folder.
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

4. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, you can instead run the commands below using `.venv\Scripts\python.exe`, or use Command Prompt with `.venv\Scripts\activate.bat`.

5. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

6. Start the website:

   ```powershell
   streamlit run app.py
   ```

7. Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser.

## Troubleshooting
- If `py` is not recognised, try `python -m venv .venv`.
- If `streamlit` is not recognised, activate the virtual environment and run `python -m streamlit run app.py`.
- To stop the app, focus the terminal and press `Ctrl+C`.

## Suggested demo
1. Show the home dashboard and explain that no paid API is used.
2. Open Symptom Information and choose one symptom category.
3. Select an urgent warning sign and show the safety message.
4. Open Health Library and browse a topic.
5. Use BMI Calculator with sample values.
6. Open Emergency Guidance and FAQs.
7. Explain the app's limitations and future enhancements.

## Possible future enhancements
- Add multilingual information after reviewing translations.
- Add an appointment-request form without storing sensitive medical details.
- Add citations and review dates for all health content from authoritative public health sources.
- Add accessibility improvements and automated tests.


## Free online publishing (GitHub + Streamlit Community Cloud)

1. Create a GitHub repository and upload `app.py`, `requirements.txt`, `README.md`, and `.gitignore`.
2. Sign in to Streamlit Community Cloud at https://share.streamlit.io/ using GitHub.
3. Choose **Create app**, select your repository and branch, set the main file to `app.py`, then choose **Deploy**.
4. When deployment finishes, Streamlit provides a public `*.streamlit.app` URL.

No payment method is required for the standard Community Cloud free workflow. Availability and platform limits can change.

## Safety notice

This is a student demonstration, not a medical device. Do not use it to diagnose, treat, or triage a real person. The educational content should be reviewed by qualified healthcare professionals before any real-world use.
