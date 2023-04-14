password=input("Choose password : ")
import re
def Valide_Password(password):
    if len(password)<8:
        return False 
    if not re.search("[a-z]", password):
         return False
    if not re.search("[A-z]",password):
        return False
    if not re.search("[0-9]",password):
        return False
    if not re.search("[!@#$%^&*]",password):
        return False
    return True

while not Valide_Password(password):
    print("Pass needs to contain at least 1 big , 1 small letter and at least 1 number")
    password=input("Choose new password : ")
print("Password is valide")