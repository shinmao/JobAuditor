import os
import pandas as pd
import numpy as np
import re
import plistlib

def convert2df(result):
    col = ["Path", "Label", "Daemon/Agent", "Program", "Argument", "maxCPU", "UserName", "GroupName", "Permission(8)"]
    df = pd.DataFrame(np.array(result), columns=col)
    df.to_csv(r"./report/job.csv")

def complete_path(path, parentdir):
    return parentdir + "/" + path

def parsePlist(path):
    # label, program, argument, maxCPU, username, groupname, permission
    attrib = ["x", "x", "x", "x", "x", "x", "x"]
    key = ["Label", "Program", "ProgramArguments", "CPU", "UserName", "GroupName", "Umask"]
    with open(path, 'rb') as f:
        l = plistlib.load(f)
        for i in range(len(key)):
            try:
                k = key[i]
                attrib[i] = l[k]
            except:
                pass
    f.close()
    return attrib

def appendProfile(path, job_kind, data):
    profile = []
    profile.append(path)
    profile.append(data[0])
    profile.append(job_kind)
    profile.append(data[1])
    profile.append(data[2])
    profile.append(data[3])
    profile.append(data[4])
    profile.append(data[5])
    profile.append(data[6])
    return profile

def listjob():
    service = []
    # agent launching on user login
    usr_agent_path = os.path.expanduser("~/Library/LaunchAgents")
    usr_agent= os.listdir(usr_agent_path)
    for i in range(len(usr_agent)):
        path = complete_path(usr_agent[i], usr_agent_path)
        job_kind = "agent"
        data = parsePlist(path)
        profile1 = appendProfile(path, job_kind, data)
        service.append(profile1)
    # agent launching on user login
    glob_agent_path = "/Library/LaunchAgents"
    glob_agent= os.listdir(glob_agent_path)
    for i in range(len(glob_agent)):
        path = complete_path(glob_agent[i], glob_agent_path)
        job_kind = "agent"
        data = parsePlist(path)
        profile2 = appendProfile(path, job_kind, data)
        service.append(profile2)
    # daemon running on startup
    glob_daemon_path = "/Library/LaunchDaemons"
    glob_daemon = os.listdir(glob_daemon_path)
    for i in range(len(glob_daemon)):
        path = complete_path(glob_daemon[i], glob_daemon_path)
        job_kind = "daemon"
        data = parsePlist(path)
        profile3 = appendProfile(path, job_kind, data)
        service.append(profile3)
    # agent launching on user login
    sys_agent_path = "/System/Library/LaunchAgents"
    sys_agent = os.listdir(sys_agent_path)
    for i in range(len(sys_agent)):
        path = complete_path(sys_agent[i], sys_agent_path)
        job_kind = "agent"
        data = parsePlist(path)
        profile4 = appendProfile(path, job_kind, data)
        service.append(profile4)
    # daemon running on startup
    sys_daemon_path = "/System/Library/LaunchDaemons"
    sys_daemon = os.listdir(sys_daemon_path)
    for i in range(len(sys_daemon)):
        path = complete_path(sys_daemon[i], sys_daemon_path)
        job_kind = "daemon"
        data = parsePlist(path)
        profile5 = appendProfile(path, job_kind, data)
        service.append(profile5)
    convert2df(service)
