from datetime import datetime

# Name, Email, Subject, Content
def format_message(data):
    now = datetime.now()
    curr_date = now.strftime("%d %b %Y, %I:%M %p")

    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject') or 'None'
    content = data.get('content')

    message = f"From: {name} \nEmail: {email} \nSubject: {subject} \n \n{content} \n\nDate: {curr_date}"
    return message