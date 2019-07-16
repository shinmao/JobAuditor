import os
import pandas as pd
import numpy as np
import re
import xml.etree.ElementTree as ET

def convert2df(result):
    col = ["Path", "Label", "Daemon/Agent", "Program", "Argument", "runtime", "maxCPU", "UserName", "GroupName", "Permission(8)"]
    df = pd.DataFrame(np.array(result), columns=col)
    df.to_csv(r"./report/job.csv")

def complete_path(path, parentdir):
    return parentdir + "/" + path

def parsexml(path):
    label, program, argument, runtime, maxCPU, username, groupname, permission = "x", "x", "x", "x", "x", "x", "x", "x"
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        time = ["RunAtLoad", 
            "StartInterval", 
            "StartCalendarInterval", 
            "StartOnMount", 
            "WatchPaths", 
            "QueueDirectories", 
            "KeepAlive"]
        name = ["UserName",
            "GroupName"]
        for i in range(len(root[0])):
            if root[0][i].text == "Label":
                label = root[0][i+1].text
            elif root[0][i].text == "Program":
                program = root[0][i+1].text
            elif root[0][i].text == "ProgramArguments":
                program = root[0][i+1][0].text
                argument = ""
                j = 1
                while j < len(root[0][i+1]):
                    argument += root[0][i+1][j].text
                    j += 1
            elif root[0][i].text in time:
                runtime = ""
                runtime += root[0][i].text
                runtime += "/"
            elif root[0][i].text == "CPU":
                maxCPU = root[0][i+1].text
            elif root[0][i].text == "UserName":
                username = root[0][i+1].text
            elif root[0][i].text == "GroupName":
                groupname = root[0][i+1].text
            elif root[0][i].text == "Umask":
                b10 = int(root[0][i+1].text)
                permission = str(oct(b10))
    except:
        print("some invalid xml")
    return label, program, argument, runtime, maxCPU, username, groupname, permission

def appendProfile(path, job_kind, xmldata):
    profile = []
    profile.append(path)
    profile.append(xmldata[0])
    profile.append(job_kind)
    profile.append(xmldata[1])
    profile.append(xmldata[2])
    profile.append(xmldata[3])
    profile.append(xmldata[4])
    profile.append(xmldata[5])
    profile.append(xmldata[6])
    profile.append(xmldata[7])
    return profile
    
def listjob():
    service = []
    # agent
    usr_agent_path = os.path.expanduser("~/Library/LaunchAgents")
    usr_agent= os.listdir(usr_agent_path)
    for i in range(len(usr_agent)):
        path = complete_path(usr_agent[i], usr_agent_path)
        job_kind = "agent"
        xmldata = parsexml(path)
        profile1 = appendProfile(path, job_kind, xmldata)
        service.append(profile1)
    # agent
    glob_agent_path = "/Library/LaunchAgents"
    glob_agent= os.listdir(glob_agent_path)
    for i in range(len(glob_agent)):
        path = complete_path(glob_agent[i], glob_agent_path)
        job_kind = "agent"
        xmldata = parsexml(path)
        profile2 = appendProfile(path, job_kind, xmldata)
        service.append(profile2)
    # daemon
    glob_daemon_path = "/Library/LaunchDaemons"
    glob_daemon = os.listdir(glob_daemon_path)
    for i in range(len(glob_daemon)):
        path = complete_path(glob_daemon[i], glob_daemon_path)
        job_kind = "daemon"
        xmldata = parsexml(path)
        profile3 = appendProfile(path, job_kind, xmldata)
        service.append(profile3)
    # agent
    sys_agent_path = "/System/Library/LaunchAgents"
    sys_agent = os.listdir(sys_agent_path)
    for i in range(len(sys_agent)):
        path = complete_path(sys_agent[i], sys_agent_path)
        job_kind = "agent"
        xmldata = parsexml(path)
        profile4 = appendProfile(path, job_kind, xmldata)
        service.append(profile4)
    # daemon
    sys_daemon_path = "/System/Library/LaunchDaemons"
    sys_daemon = os.listdir(sys_daemon_path)
    for i in range(len(sys_daemon)):
        path = complete_path(sys_daemon[i], sys_daemon_path)
        job_kind = "daemon"
        xmldata = parsexml(path)
        profile5 = appendProfile(path, job_kind, xmldata)
        service.append(profile5)
    convert2df(service)