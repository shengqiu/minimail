import imaplib
from Account import Account


class imap(Account):
  def __init__(self):
    self.load_profile()

  def receive(self):
    server = imaplib.IMAP4_SSL('imap.gmail.com')
    server.login(self.email, self.password)
    server.list()
    # Out: list of "folders" aka labels in gmail.
    server.select("inbox")
    # connect to inbox.
    server.close()
