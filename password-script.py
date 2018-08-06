# Program to check a user's password against a system
# Written by Pavon Dunbar using Python v3.7.0

password = 'williams'
for i in range(3):
    pwd = input('Please enter your password: ')
    j = 2
    if(pwd==password):
           print('Thank you and welcome to the application!')
    else:
           print('The password you entered is incorrect. Please try again. You have' ,j-i, 'chances left.')
           continue
   
print('Sorry.  You have entered the wrong password 3 times.  You are locked out the application.  Try again in one hour.')

print('Press ENTER to exit the application. ')

# END
