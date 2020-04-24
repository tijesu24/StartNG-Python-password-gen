# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:28:10 2020

@author: Tijesunimi.Adebiyi
"""
import random
import string

def generate_password(strength):
    lettersAndDigits = string.ascii_letters + string.digits+string.punctuation.replace('.', '')
    rand_str =  ''.join(random.choice(lettersAndDigits) for i in range(16))
    
    return rand_str


def main():
    #ask for the level from one to three
    while True:
        strength = input('Please select the password strength you need from 1-3 where 1 is easy: \n')
        
        if ((str(strength) != '1') and (str(strength) != '2') and (str(strength) != '3')):
            print('Invalid input')
            continue
        
        break
    
    password = generate_password(strength)
    
    print(password)
    
    pass

if __name__ == '__main__':
    main()