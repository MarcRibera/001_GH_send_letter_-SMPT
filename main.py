import pandas as pd
import datetime as dt
import os
import random
from smtp_service import send_email

def get_letters_content():
    path ='./letter_templates'
    # get files names in a directory
    files_names = [file_name for file_name in os.listdir(path) if file_name.endswith('.txt')]
    content = []

    for name in files_names:
        route = path +'/' + name
        with open(route, 'r+') as letter:
            content.append(letter.read())
    return content

def get_people():
    # Get birthdays.csv
    people_df = pd.read_csv('birthdays.csv')
    # Check if today matches a birthday in the birthdays.csv
    now = dt.datetime.now()
    return people_df.loc[(people_df['month'] == now.month) & (people_df['day'] == now.day)]

def send_emails(people_list_df, letters_content):
    if people_list_df.empty:
        print('No birthdays today 😕')
    else:
        print(f"Sending {len(people_list_df)} Emails...")
        for person in people_list_df.iterrows():
            name = person[1]['name']
            email = person[1]['email']
            content = random.choice(letters_content) # get random letter
            msg = content.replace('[NAME]', name) # replace to real name
            try:
                send_email(body=msg, to_email=email)
                print('Email Sent')
            except Exception as error:
                print(f"Error sending email to {name}, {email}")
                print(f"Error type -> {error}")
        

send_emails(
    people_list_df=get_people(), 
    letters_content=get_letters_content()
)

