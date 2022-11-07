import smtplib

fromaddr = 'ktop1017@naver.com'
toaddrs  = ['ktop101777@gmail.com']
# string inside msg below must have "Subject: <subject line>\n"
# for a subject to be sent, and "To: " for the recipient to be shown in the email
msg = '''To: receiving@gmail.com
    Subject: Subject line here\n
    The body goes here
    .
'''

msg = msg.format(fromaddr =fromaddr, toaddr = toaddrs[0])
# The actual mail send
server = smtplib.SMTP('gmail-smtp-in.l.google.com:25')
server.starttls()
server.ehlo("example.com")
server.mail(fromaddr)
server.rcpt(toaddrs[0])
server.data(msg)
server.quit() 