#import random module for random selection 
import random

#import string module for lower,upper and symbols used for password
import string

password=""   #creating a empty password 

length=int(input("Enter the length of your password:"))    #user input for length of the password

lower_case=string.ascii_lowercase
upper_case=string.ascii_uppercase
symbols=string.punctuation
numbers=string.digits

whole_password=lower_case+upper_case+symbols+numbers   #adding lowercase,uppercase,symbols and numbers

temporary_variable=random.sample(whole_password,length)

password+="".join(temporary_variable)

print(f"Your password is : {password}")