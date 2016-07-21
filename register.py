import io

reg_user = input('Please type in your username: ')
reg_pass = input('Please type in your password: ')
info = reg_user + "," + reg_pass + "\n"

with open("users.txt", "a") as myfile:
    myfile.write(info)
    