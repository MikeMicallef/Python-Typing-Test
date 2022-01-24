# Coded by Mike Micallef
from time import time
import random

# getting random sentences from .txt document 
def get_sentence(Sentence):
        f = open('sentences.txt').read() #Calling .txt file
        sentences = f.split('\n') #splitting sentences according to new line
        Sentence = random.choice(sentences) # randomly picking a sentence from .txt 
        return Sentence
    
# calculate the accuracy of input Sentence   
def typingNumErrors(Sentence):
    global SentenceSplit

    words = Sentence.split()# Splitting sentence into individual words
    NumErrors = 0

    for i in range(len(SentenceSplit)):
        if i in (0, len(SentenceSplit)-1):
            if SentenceSplit[i] == words[i]: #Checking if word inputted by user matches word from generated sentence
                continue
            else:
                NumErrors = NumErrors + 1  #If letter does not match Number of Errors is incremented
        else:
            if SentenceSplit[i] == words[i]:
                if (SentenceSplit[i+1] == words[i+1]) & (SentenceSplit[i-1] == words[i-1]): #Checking if previous and next word inputted matches generated sentence woord letters
                    continue
                else:
                    NumErrors = NumErrors + 1 #If letters do not match Number of Errors is incremented
            else:
                NumErrors = NumErrors + 1
    return NumErrors

# calculate the speed in words per minute
def typingSpeed(UserSentence, StartTime, ElapsedTime):
    global time
    global SentenceSplit

    SentenceSplit = UserSentence.split()
    speed = len(SentenceSplit)*60/(time) #Calculating the words per minute

    return speed

def TypingError(UserSentence,Sentence):

        SentenceSplit = Sentence.split()
        UserSentenceSplit = UserSentence.split()
        TypingErrors = [] # Array for Typing Errors
        Model = []      # Array for Typing Errors modal form

        for i in range(len(SentenceSplit)):
                if (SentenceSplit[i] != UserSentenceSplit[i]): # Comparing if letters are typed different
                        TypingErrors.append(UserSentenceSplit[i])
                        Model.append(SentenceSplit[i])
                        
                
                 
        return TypingErrors,Model
        
# calculate total time elapsed
def timeElapsed(StartTime, ElapsedTime):
    time = ElapsedTime - StartTime #Getting time taken for the user to type the sentence

    return time

if __name__ == '__main__':
    
    
    print("Welcome to a typing test")
    print("In this test your typing speed and accuracy will be calculated")
    Sentence = ' '
    Sentence = get_sentence(Sentence) #Calling getSentence method
    print("Type the following Sentence:- '", Sentence, "'") #Printing Sentence to be re typed by user
    
    # Waiting for user to press enter to start program
    input("press ENTER when you are ready!")

    # Starting time for user inputting sentence
    StartTime = time()
    UserSentence = input()
    ElapsedTime = time()
    
    
    time = round(timeElapsed(StartTime, ElapsedTime), 2)  
    wpm = typingSpeed(UserSentence, StartTime, ElapsedTime) # Calling typingSpeed method and passing parameters
    speed = round(wpm)   # Rounding wpm
    NumErrors = typingNumErrors(Sentence)
    
    TypingErrors,Model = TypingError(UserSentence,Sentence)
    
    accuracy1 = (len(UserSentence)-NumErrors)/len(Sentence)*100  # calculating accuracy
    accuracy = round(accuracy1)

    if(accuracy>60): # If accuracy is less than 60 percent performance is not printed as User can just press enter and be scored a good typing average
        # printing typing performance
        print("Total Time elapsed : ", time, "s")
        print("Accuracy of: ", accuracy, "%")
        print("Your Average Typing Speed was : ", round(speed), "words / minute")
        print("With a total of : ", NumErrors, "Errors")

        if(NumErrors>0): # Array for Typing Errors modal form
                print("The following were the errors made")
                for i in range(len(TypingErrors)):
                         print("You typed: '",TypingErrors[i],"' instead of '",Model[i],"'")

        if(speed>25 and speed<55):
            print(" You are in the range of an average typist, with the average being of 41 words/minute compared to your performance of ",speed, " words/minute")
        elif(speed<25):
            print("You are ranked a slow typist, with an average speed of ",speed," words/minute. Try improve and mantain a good posture, type in good lightning and most of all practice!")
        elif(speed>55):
            print("Congratulations,  with an average speed of ",speed," words/minute you are ranked as a fast typist!")
    else:
        print("Reduce the number of typong errors before to obtain an accurate result about your typing ability! Your current accuracy is: ",accuracy,"%. You need atleast 60%")

    
