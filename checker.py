#!/usr/local/bin/python3
import user
import launchd

def main():
    mode = input("Which mode do you want? ")
    while mode != "x":
        if mode == "a":
            user.listuser()
            print("You can find the report in /report/user.csv now!!")
            print("Please check whether there is a strange username.")
        elif mode == "b":
            launchd.listjob()
            print("You can find the report in /report/job.csv now!!")
            print("Please check whether there is a strange job.")
        elif mode == "c":
            pass
        mode = input("Which mode do you want? ")

if __name__ == "__main__":
    main()