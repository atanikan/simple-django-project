import string
import random

from django.core.mail import EmailMessage

def otp_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_otp_email(email, otp):
    try:
        message = f"Your otp is {otp}"
        email = EmailMessage('OTP for panorbit login', message, to=[email])
        email.send()
    except Exception:
        return False

    return True
    
def validate_otp(otp, sent_otp, email, sent_email):
    if not sent_otp or not sent_email:
        return {"success": False, "message": "session expired"}
    if not email or not otp:
        return {"success": False, "message": "didnot recieve proper data"}
    if otp != sent_otp:
        return {"success": False, "message": "wrong otp"}
    if email != sent_email:
        return {"success": False, "message": "wrong email"}
    return {"success": True, "message": "validated"}

