Ethical Phishing Simulation Platform
An educational web application for simulating ethical phishing campaigns to train users and test an organization's human-level security. Built with Python and Flask, this platform provides a safe and controlled environment to demonstrate the mechanics of social engineering and analyze user behavior without causing harm.

Key Features
Customizable Email Templates: Send realistic, tailored phishing emails using a customizable HTML template.

Credential Harvesting: Capture and securely store user-submitted data on a convincing, fake landing page.

SMTP Integration: Uses a safe, sandboxed SMTP service (Mailtrap) to handle email delivery, ensuring no emails are sent to real inboxes.

Analytics Dashboard: Visualize key metrics, such as email delivery status and captured credentials, to analyze the simulation's effectiveness.

Secure Logging: Logs all activities and captured data to an SQLite database for ethical analysis and reporting.

Technologies
Backend: Python, Flask, smtplib

Database: SQLite

Frontend: HTML, CSS

Environment: python-dotenv for secure credential management
