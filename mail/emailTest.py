import smtplib
import imaplib
import poplib
import email
from email.mime.text import MIMEText
from datetime import datetime

# 보낼 곳과 연동할 이메일 계정
sendto = '받는사람@이메일.com'
user = '보내는사람@이메일.com'
password = "보내는사람 이메일 패스워드"

# 메일을 보내는 함수(smtp)
def send_mail(user, password, sendto, msg_body):

    # smtp server
    smtpsrv = "smtp.office365.com" # 발신 메일서버 주소
    smtpserver = smtplib.SMTP(smtpsrv, 587) # 발신 메일서버 포트

    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(user, password)

    msg = MIMEText(msg_body)
    msg['From'] = user
    msg['To'] = sendto
    msg['Subject'] = "Module Testing email Subject"

    smtpserver.sendmail(user, sendto, msg.as_string())
    print('done!')
    smtpserver.close()

# 메일을 받는 함수(imap4)
def check_mail_imap(user, password):

    # imap server
    imapsrv = "outlook.office365.com"
    imapserver = imaplib.IMAP4_SSL(imapsrv, "993")
    imapserver.login(user, password)
    imapserver.select('INBOX')
    res, unseen_data = imapserver.search(None, '(UNSEEN)')

    ids = unseen_data[0]
    id_list = ids.split()
    latest_email_id = id_list[-10:]

    # 메일리스트를 받아서 내용을 파일로 저장하는 함수
    for each_mail in latest_email_id:
        # fetch the email body (RFC822) for the given ID
        result, data = imapserver.fetch(each_mail, "(RFC822)")

        msg = email.message_from_bytes(data[0][1])

        while msg.is_multipart():
            msg = msg.get_payload(0)

        content = msg.get_payload(decode=True)
        f = open("email_" + str(datetime.now()) + ".html", "wb")
        f.write(content)
        f.close()

    imapserver.close()
    imapserver.logout()

# 메일을 받는 함수(pop)
def check_mail_pop(user, password):

    # imap server
    popsrv = "pop.test.kr"
    popserver = poplib.POP3(popsrv, "110")
    popserver.user(user)
    popserver.pass_(password)
    numMsg = len(popserver.list()[1])

    for i in range(numMsg):

        raw_email = b"\n".join(popserver.retr(i + 1)[1])
        msg = email.message_from_bytes(raw_email)

        while msg.is_multipart():
            msg = msg.get_payload(0)

        content = msg.get_payload(decode=True)
        f = open("email_" + str(datetime.now()) + ".html", "wb")
        f.write(content)
        f.close()

    popserver.close()

if __name__ == '__main__':

    # imap형식 수신 함수
    check_mail_imap(user, password)

    # pop형식 수신 함수
    check_mail_pop(user, password)

    # 메일을 보내는 함수 smtp
    send_mail(user, password, sendto, "안녕하세요 코코넛이 이메일을 보냅니다.")