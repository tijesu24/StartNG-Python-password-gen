# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:39:45 2020

@author: Tijesunimi.Adebiyi
"""
import random
import string

def get_password(firstname,lastname):
    #Generate random password for the user joining the 
    #first 2 letters of the first name and last 2 letters of 
    #the last name with a random string of length 5
    lettersAndDigits = string.ascii_letters + string.digits
    rand_str =  ''.join(random.choice(lettersAndDigits) for i in range(5))
    password = firstname[0:2]+rand_str+lastname[-2:]
    
    while True: 
            answer = input(f'Are you satisfied with this password? (y/n) {password}: ')
            if (answer.lower() == 'y'):
                break
            elif (answer.lower() == 'n'):
                while True:
                    password = input('Enter your preferred password (At least 7 characters): ')
                    if (len(password) < 7):
                        print('Invalid length of string!')
                        continue
                    break
            else:
                print('Invalid response!')
                    
               
    return password

def print_user_details(user_details):
        
    user_no = 1
    for email in user_details.keys():
        firstname = user_details[email]['firstname']
        lastname = user_details[email]['lastname']
        password = user_details[email]['password']
        
        print('User ', user_no)
        print(f'Firstname: {firstname}')
        print(f'Lastname: {lastname}')
        print(f'Email: {email}')
        print(f'Password: {password}\n')
        
        user_no = user_no+1

def main():
    #The user details are saved in a dictionary with the email as the key and a 
    #list of the user details as the value
    user_details = {} 
    
    while True:
        print('\nWelcome!')
        firstname=lastname=email = ''
        firstname = str(input('Enter your firstname: '))
        lastname = str(input('Enter your lastname: '))
        email = str(input('Enter your email: '))
        
        password = get_password(firstname, lastname)
        
        
        user_details[email] = {'firstname': firstname,
                               'lastname':lastname,
                               'password':password}
        
        response = str(input('Type 0 to exit else any other key to run for another user: '))
        
        if response == '0':
            break
        
    
    print_user_details(user_details)
         
    
    


if __name__ == '__main__':
    main()
