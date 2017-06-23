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
        self.to_addrs = []
        self.msg = ''

    def compose(self):
        lines = []
        print('======    message   ====== (end msg with ;)')
        line = ''
        while line != ';':
            lines.append(line)
            line = input()
        self.msg = '\r\n'.join(lines)

    def get_to_addr(self):
        addr = 'first address will be droped'
        print('======    addresss   ======')
        while addr != '':
            self.to_addrs.append(addr)
            addr = input()

    def send(self):
        server = smtplib.SMTP(self.smtp_server, self.smtp_tls)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.to_addrs, self.msg)
        server.quit()


if __name__ == '__main__':
  new = sender()
  new.get_to_addr()
  new.compose()
  new.send()
