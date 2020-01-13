#! /usr/bin/env python3
import ftplib
import os

'''
A FTP client made for a bootcamp. 
Basic functionality.
List directory, traverse file system, download and upload files.
'''
SERVER = "ENTER SERVER HERE"
USERNAME = "ENTER YOUR USERNAME HERE"
PASSWORD = "********"

def print_data(data):
    # Print out data from the FTP query
    for line in data:
        print(f"-{line}")

def ftp_login(user, password, host):
    # Start up an instance and log in.
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        return ftp
    except ftplib.all_errors as e:
        print(f"Errors: {e}")

def change_dir(ftp_session, dir):
    # Change the current directory
    ftp_session.cwd(dir)

def list_dir(ftp_session):
    # List out the current directory
    data = []
    ftp_session.dir(data.append)
    print_data(data)

def ftp_close(ftp_session):
    # Close the session
    ftp_session.quit()

def get_file(ftp_session, file_name):
    # Grabbing a file from the FTP server.
    try:
        with open(file_name, 'wb') as fp:
            ftp_session.retrbinary(f"RETR {file_name}", fp.write)
    except:
        print(f"Error downloading file: {file_name}!")

def upload_file(ftp_session, file):
    # Uploading a file to the FTP server.
    try:
        fp = open(file, 'rb')
        ftp_session.storbinary(f"STOR {file}", fp)
    except ftplib.all_errors as e:
        print(f"Errors: {e}")

def print_commands():
    commands = ["ls", "get", "put", "cd", "help", "bye"]
    for com in commands:
        print(com)

print("Welcome to the FTP client!")
session = ftp_login(USERNAME, PASSWORD, SERVER)
# Main logic loop
while True:
    cmd = input("FTP> ")
    halves = cmd.split(" ")
    if cmd == "bye":
        print("Thank you for using the client.")
        ftp_close(session)
        break
    elif cmd == "help":
        print_commands()
    elif cmd == "ls":
        list_dir(session)
    elif halves[0] == "get":
        get_file(session, halves[1])
    elif halves[0] == "cd":
        change_dir(session, halves[1])
    elif halves[0] == "put":
        upload_file(session, halves[1])
    else:
        print("Error with your command. \nType 'Help' to list all commands.")
