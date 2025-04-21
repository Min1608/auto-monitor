import requests

def check_website():
    try:
        res = requests.get("https://httpstat.us/500", timeout=5)
        if res.status_code == 200:
            return "OK"
        else:
            return f"⚠️ Server trả về mã lỗi: {res.status_code}"
    except Exception as e:
        return f"❌ Lỗi khi kiểm tra hệ thống: {e}"

status = check_website()
print("Kết quả kiểm tra:", status)
 
 #check mail

import smtplib
from email.mime.text import MIMEText

def send_email(message):
    sender = "minhthu1608@dudaji.vn"
    password = "kuqk lhzy cqhj mdmj"  # App password chứ không phải pass thường
    receiver = ["minhthu1608@dudaji.vn" , "huyenntt@dudaji.vn"]

    msg = MIMEText(message)
    msg["Subject"] = "⚠️ Cảnh báo hệ thống"
    msg["From"] = sender
    msg['To'] = ", ".join(receiver) 

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

# Check + Gửi mail nếu cần
status = check_website()
print("Kết quả:", status)
if status != "OK":
    send_email(status)
