import os
import re

def online_usr():
    cmd = "w"
    usr = os.popen(cmd).readlines()
    usr_size = len(usr) - 2
    # start with idx + 2 for ignoring title
    l = [[0]*4 for i in range(usr_size)]
    for i in range(usr_size):
        l[i][0] = usr[i+2].split()[0]  # usrname
        l[i][1] = usr[i+2].split()[3]  # login at
        l[i][2] = usr[i+2].split()[4]  # idle for
        l[i][3] = usr[i+2].split()[5]  # use what
    return l

def listuser():
    cmd = "dscl . list /Users UniqueID"
    usr = os.popen(cmd).readlines()
    usr_size = len(usr)
    l = [[0]*2 for i in range(usr_size)]
    for i in range(usr_size):
        l[i][0] = re.split(r"\W+", usr[i])[0]  # usrname
        l[i][1] = re.split(r"\W+", usr[i])[1]  # PID
    online_usr_list = online_usr()
    write_path = "./report/usr.txt"
    f = open(write_path, "w", encoding="utf-8")
    for i in range(usr_size):
        f.write("username: " + l[i][0] + " with PID: " + l[i][1])
        for j in range(len(online_usr_list)):
            if l[i][0] == online_usr_list[j][0]:
                f.write("\n")
                f.write("|___ still login since " + online_usr_list[j][1] + ", idle for " + online_usr_list[j][2] + ", and using " + online_usr_list[j][3])
        f.write("\n")
    f.close()
    return l