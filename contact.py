# contact.py

import streamlit as st
import smtplib
# from captcha.image import ImageCaptcha
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError

# TODO: Add captach to the form

# Email sending function
def send_email(sender_email, sender_name, message):
    # Email configuration (use your email credentials)
    # TODO: need to figure out how to handle this so it is not in my code
    recipient_email = st.secrets.email.address
    password = st.secrets.email.password
    subject = "New Contact Form Submission"
    
    # Create the email message
    msg = MIMEMultipart()
    msg["from"] = sender_email
    msg["to"] = recipient_email
    msg["subject"] = subject
    
    body = f"Name: {sender_name}\nEmail: {sender_email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))
    
    # SMTP server configuration (e.g., Gmail SMTP)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(recipient_email, password)  # Replace with your credentials
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

st.title(":mailbox: Get In Touch With Me!")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    submitted = st.form_submit_button("Send")

    if submitted:
        if not name or not email or not message:
            st.error("Please fill in all fields.")
        else:
            try:
                valid = validate_email(email, check_deliverability = True)
                success = send_email(email, name, message)
                if success:
                    st.success("Your message has been sent!")
                else:
                    st.error("There was an error sending your message. Please try again.")
            except EmailNotValidError as e:
                st.error(f"Invalid email address. {e}") # error in case any of the email validation checks have not passed