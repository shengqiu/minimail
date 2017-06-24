import imaplib
from Account import Account


def get_tag(tag_byte):
  tag_byte_as_str = str(tag_byte, encoding='utf-8')
  # the name is better the last and the second last quotes
  return tag_byte_as_str.split('"')[-2]


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

# there are some problem in getting tags

    self.tags = [*map(get_tag, server.list()[1])]
    # Out: list of "folders" aka labels in gmail.
    print('========================================')
    print(' There are following tags in your gmail ')
    print('========================================')
    tag_index = 0
    for tag in self.tags:
      print('{}\t{}'.format(tag_index, tag))
      tag_index += 1
    print('========================================')
    print(' Choose the tag, but key in the number  ')
    print('========================================')
    tag_selected_index = get_numeric_input(len(self.tags))
    tag_selected = self.tags[int(tag_selected_index)]
    print('Selected {} tag'.format(tag_selected))
    server.select(tag_selected.lower())
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
  new = Imap()
  new.receive()
