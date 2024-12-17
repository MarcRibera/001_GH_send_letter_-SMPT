# Birthday Email Automation 🎉

This project is a Python-based automation script that sends personalized birthday emails to people whose birthdays match the current date. It leverages CSV files for managing birthday data, customizable email templates, and a simple SMTP service for email delivery.

---

## Features 🚀

- **Dynamic Email Content**: Customize email templates with recipient names.
- **Birthday Matching**: Reads a CSV file to identify birthdays matching today's date.
- **SMTP Integration**: Sends emails via an SMTP server (default: Gmail).
- **Customizable Templates**: Store and manage multiple email templates in the `letter_templates` directory.
- **Environment Variables**: Securely store sensitive credentials (email and password) using a `.env` file.

---

## Project Structure 📂

```
.
|-- main.py               # Main script to send birthday emails
|-- smtp_service.py       # Handles email sending using SMTP
|-- birthdays.csv         # CSV file with birthday details
|-- letter_templates/     # Directory containing email templates
|   |-- template1.txt     # Example email template
|   |-- template2.txt
|-- .env                  # Environment variables for email credentials
|-- README.md             # Documentation
```

---

## Prerequisites 🛠️

Make sure you have the following tools installed:

- Python 3.8+
- Pandas library
- SMTP server credentials (e.g., Gmail account)

Install necessary Python libraries:

```bash
pip install pandas
```

---

## Setup ⚙️

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/birthday-email-automation.git
cd birthday-email-automation
```

2. **Prepare the CSV File**
   Create a `birthdays.csv` file with the following structure:

```csv
name,email,year,month,day
John Doe,john@example.com,1990,6,10
Jane Smith,jane@example.com,1995,6,10
```

3. **Create Email Templates**
   Add `.txt` files in the `letter_templates` folder. Use `[NAME]` as a placeholder for the recipient's name:
   Example (`template1.txt`):

```
Happy Birthday [NAME]! 🎂
Wishing you a fantastic day full of joy and laughter.
Best wishes,
[Your Name]
```

4. **Add Environment Variables**
   Create a `.env` file in the root directory to store email credentials:

```env
FROM_EMAIL=youremail@gmail.com
PASS=yourpassword
```

> **Note**: If using Gmail, ensure that "Allow less secure apps" is enabled or use an App Password.

5. **Run the Script**
   Execute the script using Python:

```bash
python main.py
```

---

## How It Works 🛠️

1. **`main.py`**:
   - Reads `birthdays.csv` and checks for birthdays matching today's date.
   - Loads email templates from the `letter_templates` directory.
   - Sends personalized emails using the SMTP service.
2. **`smtp_service.py`**:
   - Handles the SMTP email connection.
   - Sends the email securely using credentials from the `.env` file.

---

## Example Output 📧

```
Sending 2 Emails...
Email Sent
Email Sent
```

If there are no birthdays:

```
No birthdays today 😕
```

---

## Notes 📝

- Ensure the `.env` file is secure and never push it to a public repository.
- Emails are sent using Gmail's SMTP server by default.

---

## License 📜

This project is licensed under the MIT License.

---

## Contributing 🤝

Pull requests are welcome! If you'd like to improve this project, feel free to fork the repository and submit a PR.

---

## Contact 📬

For any questions or feedback, please contact [Your Name] at [Your Email].

---

Happy Coding! 🎉
