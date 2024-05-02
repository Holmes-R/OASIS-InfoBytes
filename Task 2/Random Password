import random 
import string 
length=int(input("Enter the password length :"))
print('''Choose the password criteria :
        1.Letters
        2.Numbers
        3.Symbols''')
characterList=" "

choice=int(input("Enter the choice :"))
if(choice ==1):
    characterList += string.ascii_letters
elif(choice == 2):
        characterList += string.digits
elif(choice == 3):
    characterList += string.punctuation
else:
    print("Please pick a valid option!")
 
password = []

for i in range(length):
    randomchar = random.choice(characterList)
     
    password.append(randomchar)
 
print("The random password is " + "".join(password))
