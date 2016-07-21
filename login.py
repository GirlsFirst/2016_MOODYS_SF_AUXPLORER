import io

log_user = input('Please type in your username: ')
log_pass = input('Please type in your password: ')

with open("users.txt") as f:
    content= f.readlines()
    
# users=[]
# for c in content:
     # new_c = c.strip('\n')
     # u = new_c.split(',')[0]
     # p = new_c.split(',')[1]
     # info = (u,p)
     # users.append(info)
     #print(users)
     
users= {}
for c in content:
     new_c = c.strip('\n')
     u = new_c.split(',')[0]
     p = new_c.split(',')[1]
     users[u] = p
     #print(users)

# for c in range(len(users)):
    # print(users[c][1])
    # if users[c][0]==log_user and users[c][1]==log_pass:
        # print("Login Succesful")
    # else:
        # print("Try Again")
        
for key in users.keys():
    if log_user == key:
        print("Login successful")
