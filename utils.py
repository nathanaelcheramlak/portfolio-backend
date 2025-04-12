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

# data = {
#     'name': 'Yonas Getachew', 
#     'email': 'yonibord@mail.com',
#     'subject': 'Request for a Job',
#     'content': 'Lorem Ipsum for the rest of the day and you have to finish alot of tasks so be expreienced.'
# }
# print(format_message(data))