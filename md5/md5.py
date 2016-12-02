import hashlib
from datetime import datetime # to be able to time the functions
#Generating the code to read in from the file

#ask the user for the file with the information that is supposed to be read in
md5 = hashlib.md5
#open up the file
passwords = open('passwords.txt', 'r') #'r' to make it a read only
line = passwords.readline()
startTime = datetime.now().time()
startTime_Second = float(str(startTime.second))
startTime_Milli = float(str(startTime.microsecond))
print(startTime_Second)
while line != "":
    print(line, hashlib.md5(line.encode('utf-8')).hexdigest()) #hashing the password string
    line = passwords.readline()
endTime = datetime.now().time()
endTime_Second = float(str(endTime.second))
endTime_Milli = float(str(endTime.microsecond))


if startTime_Second - endTime_Second > 0:
    print(startTime_Second - endTime_Second)
print("Microseconds: " , endTime_Milli - startTime_Milli)


#close the file
passwords.close()
