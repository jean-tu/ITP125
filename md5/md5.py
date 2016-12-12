import hashlib
from datetime import datetime # to be able to time the functions
#Generating the code to read in from the file

'''Defining the Global Variables'''
startTime_Second  = 0.0
startTime_Milli = 0.0
endTime_Second = 0.0
endTime_Milli = 0.0
index = 0 # to keep track of the place
characters = 1 # to know of how many characters the string should have, starting w/ 1
alphabetSpecial = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,./<>?;:!@#$%^&*()"
md5 = hashlib.md5

def startTimer():
    startTime = datetime.now().time()
    global startTime_Second, startTime_Milli #import the global values to be able to modify them
    startTime_Second = float(str(startTime.second))
    startTime_Milli = float(str(startTime.microsecond))
    print(" start Timer " + str(startTime_Second) + " " + str(startTime_Milli))

def endTimer():
    endTime = datetime.now().time()
    global endTime_Second, endTime_Milli
    endTime_Second = float(str(endTime.second))
    endTime_Milli = float(str(endTime.microsecond))
    print(" end timer " + str(endTime_Second) + " " + str(endTime_Milli))

def guessPassHelper(index, guessed, hashedPass):
    global alphabetSpecial, characters
    print hashlib.md5(guessed.encode()).hexdigest())
    if hashlib.md5(guessed.encode()).hexdigest() == hashedPass:
        print "FOUND" + hashlib.md5(guessed.encode()).hexdigest()
        return #you've found the hash
    else:
       while index <= characters:
            index += 1 #increment for the guessed character
            """for i in alphabetSpecial:
                guessed = guessed +
                guessPassHelper(index, guessed, hashedPass) #recursive call
"""
def guessPass(hashedPass):
    global alphabetSpecial
    startTimer()      #call on start timer to grab time
    print('hashed', hashedPass)
    index = 0
    guessed = hashlib.md5(alphabetSpecial[index].encode()).hexdigest()
    index += 1
    guessPassHelper(index, guessed, hashedPass) #calling on the helper function
    endTimer()


#main function
#open up the file
passwords = open('hash.txt', 'r') #'r' to make it a read only
line = passwords.readline().rstrip() #grabbing the first string to guess
index = 0; #to keep track of how many characters are going to be in the string
           # for the hash guesser
while line != "":
    print line + " " + str(characters)
    guessPass(line) #call on the function to do the hashing
    """print(line, hashlib.md5(line.encode('utf-8')).hexdigest()) #hashing the password string"""
    line = passwords.readline().rstrip()
    if startTime_Second - endTime_Second > 0:
        print("Seconds" + str(startTime_Second - endTime_Second))
    print str(endTime_Milli) + " " + str(startTime_Milli)
    if endTime_Milli - startTime_Milli > 0:
        print("MicroSEC " + str(endTime_Milli - startTime_Milli))
    print(" ") #line with nothing so it's more clear
    characters += 1 # to know how many words to work up to the next gues
#close the file
passwords.close()
