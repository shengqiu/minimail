#!/usr/bin/env python
from minimail import Parser
from os import listdir
from os.path import isfile, join


def test_header_parser():
  mypath = '/Users/f/minimail/emails/'
  email_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  for email_file in email_files:
    print('Start parsing file {}'.format(mypath + email_file))
    new = Parser(mypath + email_file)
    print(new.get_headers())


if __name__ == '__main__':
  test_header_parser()
