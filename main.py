import string
import secrets

temp_list = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
# all_elements = list(map(str, all_elements.split(" ")))
all_elements = []

for i in temp_list:
    all_elements.append(i)

password = ""
lenght = int(input('Choose password lenght: '))

for i in range(lenght):
    password += secrets.choice(all_elements)

print(password)