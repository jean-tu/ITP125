import hashlib
from datetime import datetime # to be able to time the functions
#Generating the code to read in from the file

#ask the user for the file with the information that is supposed to be read in
md5 = hashlib.md5
#open up the file
passwords = open('passwords.txt', 'r') #'r' to make it a read only
line = passwords.readline()
start_Time = str(datetime.now().time())
print(start_Time)
while line != "":
    print(line, hashlib.md5(line.encode('utf-8')).hexdigest()) #hashing the password string
    line = passwords.readline()
end_Time = str(datetime.now().time())
print(end_Time)
#print(end_Time - start_Time)

#close the file
passwords.close()
