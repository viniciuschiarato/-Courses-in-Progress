import string
from random import choice
database = string.ascii_letters + string.punctuation + string.digits
length = int(input('Characters length: '))
password = ''
for v in range(0, length):
    password += choice(database)
print(password)
