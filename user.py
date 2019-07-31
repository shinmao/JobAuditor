import os
import re
import pandas as pd
import numpy as np

def longest_ele(l, size):
    # return longest length of element
    leng = []
    for i in range(size):
        leng.append(len(l[i]))
    return max(leng)

def convert2df(l, max_length):
    # convert array to dataframe
    # title of dataframe
    col = ["usrname", "PID"]
    index = 2
    while index < max_length:
        col.append("logging since/idle for/using")
        index += 1
    for i in range(len(l)):
        while len(l[i]) != max_length:
            l[i].append("x")
    df = pd.DataFrame(np.array(l), columns=col)
    return df

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

def write2file(result):
    result.to_csv(r"../report/user.csv")

def listuser():
    cmd = "dscl . list /Users UniqueID"
    usr = os.popen(cmd).readlines()
    usr_size = len(usr)
    l = [[0]*2 for i in range(usr_size)]
    for i in range(usr_size):
        l[i][0] = re.split(r"\W+", usr[i])[0]  # usrname
        l[i][1] = re.split(r"\W+", usr[i])[1]  # PID
    online_usr_list = online_usr()
    for i in range(usr_size):
        for j in range(len(online_usr_list)):
            if l[i][0] == online_usr_list[j][0]:
                # still login since / idle for / using what
                l[i].append(online_usr_list[j][1] + "/" + online_usr_list[j][2] + "/" + online_usr_list[j][3])
    max_length = longest_ele(l, usr_size)
    result = convert2df(l, max_length)
    write2file(result)
    return result