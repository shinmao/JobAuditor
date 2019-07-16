import os

def listjob():
    usr_agent_path = os.path.expanduser('~/Library/LaunchAgents')
    usr_agent= os.listdir(usr_agent_path)
    glob_agent_path = "/Library/LaunchAgents"
    glob_agent= os.listdir(glob_agent_path)
    glob_daemon_path = "/Library/LaunchDaemons"
    glob_daemon = os.listdir(glob_daemon_path)
    sys_agent_path = "/System/Library/LaunchAgents"
    sys_agent = os.listdir(sys_agent_path)
    sys_daemon_path = "/System/Library/LaunchDaemons"
    sys_daemon = os.listdir(sys_daemon_path)
    print(usr_agent)

listjob()