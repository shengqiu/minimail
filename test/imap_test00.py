import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('myusername@gmail.com', 'mypassword')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox")
# connect to inbox.
