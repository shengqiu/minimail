import smtplib
import json


class Account(object):

    def __init__(self):
        pass

    def load_profile(self):
        self.profile = json.load(open('gmail.json', 'rb'))
        self.email = self.profile.get('email')
        self.password = self.profile.get('password', '')
        self.smtp_server = self.profile\
                               .get('smtp', {})\
                               .get('server', 'smtp.gmail.com')
        self.smtp_tls = self.profile\
                            .get('smtp', {})\
                            .get('tls', 587)
        self.smtp_ssl = self.profile\
                            .get('smtp', {})\
                            .get('ssl', 465)
        self.imap_server = self.profile\
                               .get('smtp', {})\
                               .get('server', 'smtp.gmail.com')
        self.imap_tls = self.profile\
                            .get('imap', {})\
                            .get('tls', 587)


class sender(Account):

    def __init__(self):
        self.load_profile()
        self.to_addr = []
        self.msg = ''

    def compose(self):
        lines = []
        line = 'first line will be droped'
        while line == '':
            lines.append(line)
            line = input()
        self.msg = '\n'.join(lines[1:])

    def get_to_addr(self):
        addr = 'first address will be droped'
        while addr == '':
            self.to_addr.append(addr)
            addr = input()

    def send(from_addr, password, smtp_server, to_addr):
        server = smtplib.SMTP(smtp_server, 25)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr])
        server.quit()


if __name__ == '__main__':
    from_addr = input('From: ')
    password = input('Password: ')
    smtp_server = input('SMTP server: ')
    to_addr = input('To: ')
