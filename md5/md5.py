import hashlib
import time # to be able to time the functions
#Generating the code to read in from the file

#ask the user for the file with the information that is supposed to be read in
md5 = hashlib.md5
#open up the file
passwords = open('passwords.txt', 'r') #'r' to make it a read only
line = passwords.readline()
while line != "":
    print(hashlib.md5(line.encode('utf-8')).hexdigest()) #hashing the password string
    line = passwords.readline()


#close the file
passwords.close()
