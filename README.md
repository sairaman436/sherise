# SheRise

**Empowering Women, One Task at a Time**

SheRise is a platform built to connect women offering skills and services (such as Tailoring, Handicrafts, Tutoring, Beauty Services, Elderly Care, Data Entry, etc.) with people seeking those services. It features an AI-powered matching algorithm to recommend jobs based on user skills and locations.

## Features

- **Skill-Based Job Matching:** AI algorithms recommend the best fitting jobs based on a user's skills and location.
- **Secure Authentication:** OTP-based login via Email, keeping user accounts secure.
- **Verification:** Digilocker integration for verifying identities (Aadhaar).
- **Communication:** Built-in messaging system between job creators and workers.
- **Real-Time Notifications:** Stay updated on job applications and messages.

## Tech Stack

- **Backend:** Python, Flask, SQLAlchemy, SQLite
- **AI/ML:** Groq API for intelligent matching and recommendations
- **Authentication:** Twilio, Email SMTP, Digilocker API
- **Frontend:** Pre-built distribution served statically via Flask (`frontend_dist`)

## Getting Started

### Prerequisites

- Python 3.8+
- [Groq API Key](https://console.groq.com/)
- Gmail App Password (for email OTP)
- Digilocker API Credentials (optional, for verification)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sairaman436/sherise.git
   cd sherise
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory based on the following template:
   ```env
   GROQ_API_KEY=your_groq_api_key
   
   SMTP_EMAIL=your_email@gmail.com
   SMTP_PASSWORD=your_16_char_app_password
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587

   DIGILOCKER_BASE=https://sandbox.digilocker.gov.in
   DIGILOCKER_CLIENT_ID=your_client_id
   DIGILOCKER_SECRET=your_client_secret
   DIGILOCKER_REDIRECT=http://localhost:5175/digilocker-callback
   ```

5. **Run the Application:**
   ```bash
   python app.py
   ```
   The Flask app will serve the backend API and the static frontend simultaneously.

## Deployment (PythonAnywhere)

This application uses SQLite, which requires a persistent filesystem. [PythonAnywhere](https://www.pythonanywhere.com/) provides a free tier with persistent storage, making it an excellent choice.

1. **Create an account** on [PythonAnywhere](https://www.pythonanywhere.com/).
2. **Open a Bash Console** from the PythonAnywhere dashboard and clone your repository:
   ```bash
   git clone https://github.com/sairaman436/sherise.git
   cd sherise
   ```
3. **Create a virtual environment and install dependencies:**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```
4. **Set up Environment Variables:**
   Create a `.env` file in `/home/yourusername/sherise` with all your secrets (Groq, Twilio, SMTP).
5. **Configure the Web App:**
   - Go to the **Web** tab and click **Add a new web app**.
   - Choose **Manual configuration** and select **Python 3.10**.
   - Under the **Virtualenv** section, enter the path to your virtual environment (e.g., `/home/yourusername/.virtualenvs/myenv`).
   - Under the **Code** section, open the **WSGI configuration file**.
6. **Update WSGI File:**
   Replace the default WSGI file content with the content from `pythonanywhere_wsgi.py` in this repository (make sure to replace `yourusername` with your actual username!).
7. **Reload the web app** and visit your live site!

## Contribution

Contributions are welcome! Please create an issue or submit a Pull Request.

## License

This project is licensed under the MIT License.
