#mini 2.0 date 18.01.2022

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import math
import wikipedia
import warnings
import warnings
import random

warnings.filterwarnings('ignore') #this will ignore any unnessary warnings

def text_password(text): #funtion to check password/wake word
    wake_word =["heye mini","mini","yo mini"] # words take can be used by the user as password/wakewords
    
    for phrase in wake_word:
        if phrase in wake_word:
            print("hellow user!!! :)")
            return True #return true if the password entered by the user is correct
        else:
            print("you have entered a wrong password, mini won't work BYE.....")
            return False # the program will not work of the passowrd is wrong





def voice_password():
    print("working 2")








# this is the main part 
allowences=5
print(":::::_WELLCOME USER_:::::")
print()
print("please select how you want to run me(mi_ni)")
print("Enter: 1: for text command")
print("  or   2: for voice command")
while allowences>0:
    choice = input("enter choice: ")
    if choice=="1":
        print("you have selcted to procced with text commands")
        text = input("enter password: ") # its for entering the password/wake word using keyboard
        text = text.lower() #converting the input data to lower case 
        text_password(text)
        break
    elif choice=="2":
        voice_password() 
        break
    else:
        print("invalid input you have more "+p+" out of 5 tries left") 
    
    allowences = allowences-1
