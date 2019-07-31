# Job auditor
Important!! Pls run with 
```
$ sudo python3 checker.py
```  
Goal: Make the information of daemons/agents friendly to users.  

## Requirement
1. Your python version need to be at least 3.
2. You need to install pandas module for python, I use it to export the reports.

## Important
1. Should run with sudo, or you would lost many information.
2. This auditor is best for Mojave.

### Option a.
This option is used to list the all users on current machine. The report would show the username and corresponding PID. If the user is still logged in, there would be some information showed in the last two columns.
If you want to see **who** and **what they have done** in last several days. Use following command:  
```
$ last
```

### Option b.
This option is used to list the all daemons and agents on current machine including user's and system's. The report would show several information for you to judge whether to dig into the plist file. And I also have already given the completed path of plist file. So here, how do you know the file is suspicious or not? I found am amazing discussion on Stackoverflow: 
[Where can I find a list of Apple preferences/plist files & what they're used for?](https://apple.stackexchange.com/questions/50422/where-can-i-find-a-list-of-apple-preferences-plist-files-what-theyre-used-for)  
[OS X Lion Artifacts v1.0](https://docs.google.com/spreadsheets/d/1VobbmKTw8h_wKr0fpNXiyqOc1eCTuqiRkhIguVk_eXA/edit?hl=en_US&hl=en_US#gid=0)  
[OSX 10.10 /System/Library/LaunchDaemons/](http://cirrusj.github.io/Yosemite-Stop-Launch/)  
Even this is for Lion version, it is still worthy of refering to.  
Please work with `$ lsappinfo list`.  