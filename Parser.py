class HeaderFormatError(Exception):
  def __init__(self, num_of_column):
    self.num_of_column = num_of_column

  def __str__(self):
    return repr(self.num_of_column)


def line_to_dict(line):
  if line.count(':') >= 1:
    line_key = line.split(':')[0]
    line_value = line.replace(line_key, '')[1:].strip()
  else:
    raise HeaderFormatError(line.count(':'))
  return {line_key.lower(): line_value}


class Parser:
  def __init__(self, file_name):
    with open(file_name, 'r') as f_:
      self.email_text = f_.read()

  def get_header_text(self):
    return self.email_text.split('\n\n')[0]

  def get_headers(self):
    header_dict = {}
    header_text = self.get_header_text()
    for header in header_text.split('\n'):
      temp = line_to_dict(header)
      header_dict.update(temp)
    return header_dict

  def get_content_text(self):
    headers = self.get_headers()
    return self.email_text\
               .replace(headers, '')\
               .strip()

  def get_content(self):
    # content_encoding = self.headers['content-transfer-encoding']
    self.headers = self.get_headers()
    content_type = self.headers['content-type']
    print('content type is {}'.format(content_type))
    content_text = self.get_content_text()
    print('content text is {}'.format(content_text))
    # content_decoded = content_text.decode(content_type, 'ignore')
    # return content_decoded
