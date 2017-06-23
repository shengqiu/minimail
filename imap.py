import imaplib
from Account import Account


def get_tag(tag_byte):
  tag_byte_as_str = str(tag_byte, encoding='utf-8')
  # the name is better the last and the second last quotes
  return tag_byte_as_str.split(' ')[-2]


class imap(Account):
  def __init__(self):
    self.load_profile()
    self.conn_info = ''

  def receive(self):
    server = imaplib.IMAP4_SSL('imap.gmail.com')
    server.login(self.email, self.password)
    self.conn_info = server.list()[0]

# there are some problem in getting tags
    
    self.tags = [*map(get_tag, server.list()[1])]
    # Out: list of "folders" aka labels in gmail.
    print('======   There are the following tags in your gmail   ======')
    for tag in self.tags:
      print(tag)
    server.select("inbox")
    # connect to inbox.
    result, data = server.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    result, data = server.fetch(latest_email_id, "(RFC822)")
    # msg = data[0][1]
    server.close()
    # print(msg)


if __name__ == '__main__':
  new = imap()
  new.receive()
