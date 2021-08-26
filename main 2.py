import random
password = input("Enter your password: ")
length = len(password)

finalpassword = ""
for i in password:
  finalpassword += chr(random.randint(65,90))
print(finalpassword)