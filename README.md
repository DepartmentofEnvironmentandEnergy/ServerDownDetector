# Website Status Checker

This script is designed to continuously monitor a website and send an email alert if the website is down or returns an unexpected response code. It uses Python with the requests and smtplib libraries.

## Features

- Continuously monitors a specific website at 5-minute intervals.
- Sends an email alert if the website returns a status code other than 200 (OK).
- Customizable email sender, recipient, and SMTP server settings.

## Installation

You need Python 3.x installed on your machine.

To install the required libraries, run:
```sh
pip install requests
```

## Usage

1. Clone this repository or copy the script to your local machine.

2. Replace the placeholders for sender_email, sender_password, and recipient_email with the appropriate values.

3. If needed, change the SMTP server settings.

4. Replace the URL in the `check_response` function call at the bottom of the script with the URL you want to monitor.

5. Run the script:
```sh
python <script_name.py>
```

## Code Overview

### Sending Email

The `send_email` function is responsible for sending an email. It takes two parameters: `subject` and `body`, which represent the subject and body of the email.

### Checking Website Response

The `check_response` function checks the response of the given URL. If the response code is not 200, it calls the `send_email` function to send an alert email.

### Continuous Monitoring

The script uses an infinite `while` loop to continuously monitor the website. It waits for 5 minutes between each check.

## Important Notes

- Be cautious with your email credentials. Avoid hardcoding them into the script, especially if you plan to share it. Consider using environment variables or a configuration file.

- Depending on the configuration of your email account and SMTP server, you might need to allow less secure apps or generate an app-specific password.

- The script will continue to run indefinitely. To stop it, you will need to manually interrupt it (e.g., by pressing Ctrl+C).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
