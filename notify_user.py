import smtplib, ssl
import email
from email_contacts import my_email, my_second_email, PASSWORD



def notify_user():
    # this function  can be used to send emails to a list of emails
    message = """Subject: Your Reports are not Updated

    Alert your reports seems is not recieving the raw data"""

    from_address = my_email
    password = PASSWORD
    #input("Type your password and press enter: ")

    li=[my_second_email, "ahmedehtesham609@gmail.com"]
    for reciever_email in li:
        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls

                # Create a secure Secure Socket Layer context
        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP(smtp_server,port)
            server.starttls(context=context) # Secure the connection
            server.login(from_address, password)
                    # TODO: Send email here
                    #server.sendmail(from_email, receiver_email, message)
            server.sendmail(from_address, reciever_email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
        
