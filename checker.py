#!/usr/local/bin/python3
import user
import launchd

def main():
    mode = input("Which mode do you want? ")
    while mode != "x":
        if mode == "a":
            user.listuser()
            print("You can find the report in /report/usr.txt now!!")
            print("Please check whether there is a strange username.")

if __name__ == "__main__":
    main()