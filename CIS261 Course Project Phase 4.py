from datetime import datetime

def CreateUsers():
    print("Create users, passwords, and roles")
    UserFIle = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()

        UserDetail = username + "|" + userpwd + "|" userrole + "\n"
        UserFile.write(UserDetail)

    UserFile.close()
    printuserinfo()
  
def GetUserName():
    username = input("Enter a username or 'End' to quit: ")
    return username

def GetUserPassword():
