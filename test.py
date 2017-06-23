import smtplib
import json


def deep_get(dictionary, *keys):
  return reduce(lambda d, key: d.get(key) if d else None, keys, dictionary)


class Account(object):

  def __init__(self):
    # self.profile = {}
    # self.email = ''
    # self.password = ''
    # self.smtp_server = 'smtp.gmail.com'
    # self.smtp_tls = 587
    # self.smtp_ssl = 465
    # self.imap_server = 'imap.gmail.com'
    # self.imap_tls = 465
    return

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

  def compose(self):
    lines = []
    line = 'first line will be droped'
    while line == '':
      lines.append(line)
      line = raw_input()

  def send(from_addr, password, smtp_server, to_addr):
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    # server.sendmail(from_addr, [to_addr], msg.as_string())
    server.sendmail(from_addr, [to_addr])
    server.quit()


if __name__ == '__main__':
  from_addr = raw_input('From: ')
  password = raw_input('Password: ')
  smtp_server = raw_input('SMTP server: ')
  to_addr = raw_input('To: ')
