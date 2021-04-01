#!/usr/bin/env python3

login_fail = 0

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

keystone_file_lines = keystone_file.readlines()

for line in keystone_file_lines:
    if "- - - - -] Authorization failed" in line:
        print("IP where failed attempt is from: ",line.split(" ")[-1])
        login_fail +=1
print("The number of failed log in attemps is: ", login_fail)

keystone_file.close()


