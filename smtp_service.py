import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def load_env_vars():
    env_vars = {}
    with open('.env','r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key,value = line.split('=')
                env_vars[key] = value
    return env_vars

env_vars = load_env_vars()
FROM_EMAIL = env_vars.get('FROM_EMAIL')
PASS = env_vars.get('PASS')

def send_email(body:str, to_email:str):
    # Create a MIMEText object to represent the email
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = " 🎉 Happy Birthday 🎉"
    msg.attach(MIMEText(body, 'plain'))
    
    # Start SMTP session
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls() # tls -> Security layer, encryption
    connection.login(user=FROM_EMAIL,password=PASS)
    
    # Send Email
    connection.sendmail(
        from_addr=FROM_EMAIL, 
        to_addrs=to_email, 
        msg=msg.as_string()
    )
    connection.close()