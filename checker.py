#!/usr/local/bin/python3
import user
import launchd

def main():
    try:
        while 1:
            mode = input("Which mode do you want? Or ctrl+c to leave.\n")
            if mode == "a":
                user.listuser()
                print("You can find the report in /report/user.csv now!!")
                print("Please check whether there is a strange username.")
            elif mode == "b":
                launchd.listjob()
                print("You can find the report in /report/job.csv now!!")
                print("Please check whether there is a strange job.")
            else:
                print("No such option!")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()