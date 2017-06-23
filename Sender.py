import smtplib
from Account import Account


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
