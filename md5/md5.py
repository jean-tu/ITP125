import hashlib
from datetime import datetime # to be able to time the functions
#Generating the code to read in from the file

def guessPass(hashedPass):
    startTimer()
    print('hashed', hashedPass)
    for i in xrange(0, index): #loop through all the possible character slots
        #loop through the string.printable = 128 length
        for j in xrange(0, 128):
            while(hashed != guessed)
        #endTimer()


def startTimer():
    startTime = datetime.now().time()
    startTime_Second = float(str(startTime.second))
    startTime_Milli = float(str(startTime.microsecond))
    print("start Timer")

def endTimer():
    endTime = datetime.now().time()
    endTime_Second = float(str(endTime.second))
    endTime_Milli = float(str(endTime.microsecond))
    print("end timer")

#main function
md5 = hashlib.md5
#open up the file
passwords = open('hash.txt', 'r') #'r' to make it a read only
line = passwords.readline().rstrip() #grabbing the first string to guess
index = 0; #to keep track of how many characters are going to be in the string
           # for the hash guesser
while line != "":
    print(line)
    index += 1
    guessPass(line) #call on the function to do the hashing
    #print(line, hashlib.md5(line.encode('utf-8')).hexdigest()) #hashing the password string
    line = passwords.readline().rstrip()



"""if startTime_Second - endTime_Second > 0:
    print(startTime_Second - endTime_Second)
print("Microseconds: " , endTime_Milli - startTime_Milli)

"""
#close the file
passwords.close()
