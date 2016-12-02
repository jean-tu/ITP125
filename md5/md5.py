import hashlib
from datetime import datetime # to be able to time the functions
#Generating the code to read in from the file

def guessPass(hashedPass):
    
    print('hashed', hashedPass)





#main function
md5 = hashlib.md5
#open up the file
passwords = open('hash.txt', 'r') #'r' to make it a read only
line = passwords.readline().rstrip() #grabbing the first string to guess
while line != "":
    print(line)
    guessPass(line) #call on the function to do the hashing
    #print(line, hashlib.md5(line.encode('utf-8')).hexdigest()) #hashing the password string
    line = passwords.readline().rstrip()



if startTime_Second - endTime_Second > 0:
    print(startTime_Second - endTime_Second)
print("Microseconds: " , endTime_Milli - startTime_Milli)


#close the file
passwords.close()
