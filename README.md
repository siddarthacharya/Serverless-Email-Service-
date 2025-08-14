# Serverless Email Service (Python)

This project demonstrates a **Serverless REST API** in **Python** that sends emails. The API accepts `receiver_email`, `subject`, and `body_text` as input and sends an email accordingly.

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Setup](#setup)  
- [Running Locally](#running-locally)  
- [API Endpoint](#api-endpoint)  
- [Error Handling](#error-handling)  
- [Technologies](#technologies)  

---

## Features

- REST API for sending emails using Python  
- Input: receiver email, subject, and body text  
- Proper error handling with HTTP response codes  
- Offline testing with Serverless offline plugin  

---

## Prerequisites

- Python 3.10+  
- pip  
- Serverless Framework (`npm install -g serverless`)  
- Email service credentials (e.g., Gmail SMTP, SendGrid, etc.)  

---

## Setup

1. **Clone the repository**

```bash
git clone <repository_url>
cd <repository_folder>
```

2. **Create a virtual environment**


```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a .env file:
```bash
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_password_or_app_password
```
> Note: For Gmail, generate an App Password if 2FA is enabled.


---

## Running Locally

To run offline with Serverless:
```bash
serverless offline
```
The API will be available at 
```bash
http://localhost:3000.
```

---

## API Endpoint

POST /send-email

Request Body (JSON):
```bash
{
  "receiver_email": "recipient@example.com",
  "subject": "Test Email",
  "body_text": "Hello, this is a test email from Python Serverless API."
}
```
## Response:

200 OK: Email sent successfully

```bash
{
  "message": "Email sent successfully"
}
```

400 Bad Request: Missing or invalid input

```bash
{
  "error": "receiver_email is required"
}
```
500 Internal Server Error: Error sending email
```bash

{
  "error": "Failed to send email"
}
```

---

## Error Handling

Missing input fields → 400 Bad Request

Invalid email format → 400 Bad Request

Email sending failure → 500 Internal Server Error



---

## Technologies

Python 3

Flask (or FastAPI)

Serverless Framework

serverless-wsgi (if using Flask with Lambda)

smtplib / email.message for sending emails

python-dotenv



---

## License

MIT License
