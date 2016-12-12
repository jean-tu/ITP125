import hashlib
import itertools
import string
from datetime import datetime # to be able to time the functions
#Generating the code to read in from the file

'''Defining the Global Variables'''
startTime_Minute = 0.0
startTime_Second  = 0.0
endTime_Minute = 0.0
endTime_Second = 0.0
index = 0 # to keep track of the place
characters = 1 # to know of how many characters the string should have, starting w/ 1
alphabetSpecial = string.printable
md5 = hashlib.md5

def startTimer(): #updating the global variables for the startTime in seconds
    startTime = datetime.now().time()
    global startTime_Minute, startTime_Second #import the global values to be able to modify them
    startTime_Minute = float(str(startTime.minute))
    startTime_Second = float(str(startTime.second))
    #print " start Timer " + str(startTime_Minute) + " . " + str(startTime_Second)

def endTimer():#updating the global variables for the endTime in seconds
    endTime = datetime.now().time()
    global endTime_Minute, endTime_Second
    endTime_Minute = float(str(endTime.minute))
    endTime_Second = float(str(endTime.second))
    #print " end timer " + str(endTime_Minute) + " . " + str(endTime_Second)

def totalTime():
    global startTime_Second, endTime_Second
    if endTime_Minute - startTime_Minute > 0:
        minuteDifference = endTime_Minute - startTime_Minute
        minuteDifference = minuteDifference*60 #converting it to seconds
        if endTime_Second - startTime_Second > 0:
            secondDifference = (endTime_Second - startTime_Second) + minuteDifference
            print "Total TIme" + str(secondDifference)
    elif endTime_Second - startTime_Second > 0:
            print "Total Time: " + str(endTime_Second - startTime_Second)
    else: #if there was no time difference
        print "Time = 0 seconds"

def guessPass(hashedPass):
    global alphabetSpecial, characters
    startTimer()      #call on start timer to grab time
    perms =  list(map("".join, itertools.permutations(alphabetSpecial, characters))) #generate all the permutations for the number of characters
    for per in perms:
        if hashlib.md5(per.encode()).hexdigest() == hashedPass:
            print "FOUND THE WORD: " + per +  " WITH THE HASH " + hashlib.md5(per.encode()).hexdigest()
            endTimer()
            totalTime()
            return #you've found the hash
    endTimer() #end the timer even if it's not able to find the word 

#main function
#open up the file
passwords = open('hash.txt', 'r') #'r' to make it a read only
line = passwords.readline().rstrip() #grabbing the first string to guess
while line != "":
    guessPass(line) #call on the function to do the hashing
    line = passwords.readline().rstrip()
    print(" ") #line with nothing so it's more clear
    characters += 1 # to know how many words to work up to the next gues
passwords.close() #close the file
