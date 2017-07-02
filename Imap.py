import imaplib
from Account import Account
import email
import re
import base64


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
        # tag_selected_index = get_numeric_input(len(self.tags))
        # tag_selected = self.tags[int(tag_selected_index)]
        print('Selected {} tag'.format('inbox'))
        server.select('inbox')
        # connect to inbox.
        result, data = server.uid('search', None, "ALL")
        uid_list = data[0].split()
        for inbox_uid in uid_list:
            result, data = server.uid('fetch', inbox_uid, '(RFC822)')
            # raw_email = data[0][1]
            # id = data[0][0]
            raw = str(data[0][1])
            email_text = get_email_text(raw)
            with open('emails/{}.txt'.format(inbox_uid), 'w') as f_:
                f_.write(email_text)
        server.close()


def get_tag(tag_byte):
    tag_byte_as_str = str(tag_byte, encoding='utf-8')
    # the name is better the last and the second last quotes
    return tag_byte_as_str.split('"')[-2]


def get_email_text(raw_emails):
    email_message = email.message_from_string(raw_emails)
    email_string_list = []
    for line in str(email_message).strip()[2:-1].split('\\r\\n'):
        email_string_list.append(line)
    return '\n'.join(email_string_list)


if __name__ == '__main__':
    new = Imap()
    new.receive()
