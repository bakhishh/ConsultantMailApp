import smtplib

sender_mail = 'example@gmail.com'
portnumber = 1212 #example
def send_to_consultant(consultant_mail, message):
    server = smtplib.SMTP("smtp.gmail.com", portnumber) #portnumber is example
    server.starttls()
    server.login(sender_mail, "apppassword")  #apppasword is example
    server.sendmail(sender_mail, consultant_mail, message)

def send_to_consultant_and_assistant(consultant_mail, assistant_list, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_mail, "apppasword")
    receivers = assistant_list 
    send_to_consultant(consultant_mail , message)
    for receiver in receivers:
        server.sendmail(sender_mail, receiver, message)
    