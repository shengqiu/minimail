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
