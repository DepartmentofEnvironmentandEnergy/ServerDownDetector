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

Please note that this script is provided under the following license terms:

**License:** [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

The license restricts the selling or commercial usage of the script without obtaining appropriate permissions and may entitle the original author to royalties. Please refer to the license for more details.

Feel free to use, modify, and distribute this script in accordance with the license terms.

## Legal Disclaimer
Disclaimer of Warranty and Limitation of Liability:

The software script provided here ("Software") is distributed on an "AS IS" basis, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. The user assumes all responsibility for the selection of the Software to achieve the intended results, and for the installation, use, and results obtained from the Software. In no event shall the author, contributors or copyright holders be liable for any damages whatsoever, including - but not restricted to - lost revenue or profits or other direct, indirect, special, incidental or consequential damages, even if they have been advised of the possibility of such damages, except to the extent invariable law, if any, provides otherwise.

The Software should not be relied upon as the sole means to make decisions or take actions that could result in harm, financial loss, or violations of law. The user is solely responsible for using the Software in compliance with applicable laws and regulations.

By using the Software, you acknowledge that you understand and agree to the terms of this disclaimer. You further agree to indemnify and hold harmless the author, contributors, and copyright holders from any and all claims, demands, actions, liabilities, damages, or losses arising out of your use or misuse of the Software.

Furthermore, it is important to be cautious and responsible with your email credentials. Avoid hardcoding them into the script, especially if you plan to share it. Consider using environment variables or a configuration file. Depending on the configuration of your email account and SMTP server, you might need to allow less secure apps or generate an app-specific password. Do not use the Software for spamming, harassment, or any illegal activities.

This Disclaimer is governed by the laws in effect in the jurisdiction where you are using the Software.
