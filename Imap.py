import imaplib
from Account import Account
import email


def get_numeric_input(upper_limit):
  raw = input()
  try:
    numeric_input = int(raw)
    if numeric_input < upper_limit:
      return numeric_input
    else:
      print("Numbuer is too big")
      return get_numeric_input(upper_limit)
  except ValueError:
    print("Please input a numeric value")
    return get_numeric_input(upper_limit)


class Imap(Account):
  def __init__(self):
    self.load_profile()
    self.conn_info = ''

  def receive(self):
    server = imaplib.IMAP4_SSL('imap.gmail.com')
    server.login(self.email, self.password)
    self.conn_info = server.list()[0]
    self.tag_byte = server.list()[1]
    self.tags = [*map(get_tag, server.list()[1])]
    # Out: list of "folders" aka labels in gmail.
    print('==========================')
    print(' There are following tags ')
    print('==========================')
    tag_index = 0
    for tag in self.tags:
      print('{}\t{}'.format(tag_index, tag))
      tag_index += 1
    print('======================================')
    print(' Choose the tag, by key in the number ')
    print('======================================')
    tag_selected_index = get_numeric_input(len(self.tags))
    tag_selected = self.tags[int(tag_selected_index)]
    print('Selected {} tag'.format(tag_selected))
    server.select(tag_selected.lower())
    # connect to inbox.
    result, data = server.uid('search', None, "ALL")
    latest_email_uid = data[0].split()[-1]
    result, data = server.uid('fetch', latest_email_uid, '(RFC822)')
    # raw_email = data[0][1]
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    result, data = server.fetch(latest_email_id, "(RFC822)")
    msg = data[0][1]
    print('msg is {}'.format(msg))
    server.close()
    # print(msg)


def get_tag(tag_byte):
  tag_byte_as_str = str(tag_byte, encoding='utf-8')
  # the name is better the last and the second last quotes
  return tag_byte_as_str.split('"')[-2]


def parse_raw_email(raw_email):
  email_message = email.message_from_string(raw_email)
  print(email_message['To'])
  print(email.utils.parseaddr(email_message['From']))
  # for parsing "Yuji Tomita" <yuji@grovemade.com>
  print(email_message.items())
  # print all headers
  # note that if you want to get text content (body) and the email contains
  # multiple payloads (plaintext/ html), you must parse each message separately
  # use something like the following: (taken from a stackoverflow post)


def get_first_text_block(self, email_message_instance):
  maintype = email_message_instance.get_content_maintype()
  if maintype == 'multipart':
      for part in email_message_instance.get_payload():
          if part.get_content_maintype() == 'text':
              return part.get_payload()
  elif maintype == 'text':
      return email_message_instance.get_payload()


if __name__ == '__main__':
  new = Imap()
  new.receive()
