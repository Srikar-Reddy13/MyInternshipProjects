
#Importing random module
import random

#Asking user for password length
lenght =int(input('Enter password length: '))
#Asking user for the total number off passwords to generate
inp=int(input('Number of passwords: '))
#Looping 'inp' times to generate the total number of passwords.
for i in range(inp):    
# Defining numbers,lowercase,uppercase and spec5
ial characters
    numbers = '0123456789'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    characters = '@#$%=:?./|~>*()'
#Creating a combined list of characters to be used in the password.
    all =  numbers + lowercase + uppercase + characters
#Generating random characters from  numbers,lowercase,uppercase and special characters
    rd = random.choice(numbers)
    ru = random.choice(uppercase)
    rl = random.choice(lowercase)
    rc = random.choice(characters)
#Creating a temporary password by combining the randomly chosen characters
    temp = rd + ru + rl + rc
    
# Generating the remaining characters of desired length for the password
    for _ in range(lenght - 4):
         temp += random.choice(all)
#Shuffling the characters in the temporary password  
    shuffled_pass = ''.join(random.sample(str(temp), len(temp)))   
# Assigning the shuffled password to the 'password' variable
    password = ''.join(shuffled_pass)
#Printing the generated password
    print('Generrated passwords: ',password)
