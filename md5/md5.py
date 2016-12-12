import hashlib
from datetime import datetime # to be able to time the functions
#Generating the code to read in from the file

startTime_Second = 0
startTime_Milli = 0
endTime_Second = 0
endTime_Milli = 0
md5 = hashlib.md5

def startTimer():
    startTime = datetime.now().time()
    startTime_Second = float(str(startTime.second))
    startTime_Milli = float(str(startTime.microsecond))
    print(" start Timer " + str(startTime_Second) + " " + str(startTime_Milli))

def endTimer():
    endTime = datetime.now().time()
    endTime_Second = float(str(endTime.second))
    endTime_Milli = float(str(endTime.microsecond))
    print(" end timer " + str(endTime_Second) + " " + str(endTime_Milli))

def guessPassHelper(index, guessed, hashedPass):
    alphabetSpecial = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,./<>?;:!@#$%^&*()"
    if guessed == hashedPass:
        return #you've found the hash
    for i in alphabetSpecial:
        print i

def guessPass(hashedPass):
    startTimer()      #call on start timer to grab time
    print('hashed', hashedPass)
    endTimer()





#main function
#open up the file
passwords = open('hash.txt', 'r') #'r' to make it a read only
line = passwords.readline().rstrip() #grabbing the first string to guess
index = 0; #to keep track of how many characters are going to be in the string
           # for the hash guesser
while line != "":
    print(line)
    index += 1
    guessPass(line) #call on the function to do the hashing
    """print(line, hashlib.md5(line.encode('utf-8')).hexdigest()) #hashing the password string"""
    line = passwords.readline().rstrip()
    if startTime_Second - endTime_Second > 0:
        print("Seconds" + str(startTime_Second - endTime_Second))
    if endTime_Milli - startTime_Milli > 0:
        print("MicroSEC " + str(endTime_Milli - startTime_Milli))
    else:
        print("MicroEND " +  str(startTime_Milli - endTime_Milli))
    print(" ") #line with nothing so it's more clear

#close the file
passwords.close()
