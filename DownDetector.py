import smtplib
from email.mime.text import MIMEText
import requests
import time

def send_email(subject, body):
    sender_email = 'your_email@example.com'  # Replace with your email address
    sender_password = 'YourPasswordHere'  # Replace with your email password
    # Replace with recipient's email address
    recipient_email = 'recipient_email@example.com'

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    server = smtplib.SMTP('MailServer.website.gov', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()


def check_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    error_message = None
    try:
        response = requests.get(url, headers=headers)
        response_code = response.status_code
    except Exception as e:
        error_message = f"An error occurred while retrieving the response code: {e}"
        print(error_message)
        response_code = None

    if response_code is None:
        error_message = "Unable to retrieve the response code"
    elif response_code != 200:
        error_message = f"The server responded with status code {response_code}"
        send_email('Server Error', error_message)
    else:
        print("Server is running fine.")

    if error_message:
        print("Error Message:", error_message)


while True:
    # Call the function with your URL
    check_response('https://cloudflare.com/')

    # Sleep for 5 minutes (300 seconds)
    time.sleep(300)
