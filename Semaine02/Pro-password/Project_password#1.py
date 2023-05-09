password=input("Choose password  ")
car_spec=["!","#","$","%","&","*"]
if len(password) <8:
    print("Password must contains more than 8 caracters.")
elif not any(char.isdigit() for char in password):
    print("Password needs at least 1 chiffre.")
elif not any(char.isupper() for char in password):
    print("Password needs at least 1 majuscule letter.")
elif not any(char.islower() for char in password):
    print("Password needs at least 1 miniscule letter.")
elif not any(char in car_spec for char in password):
    print("Password needs at least 1 caracter special.")
else:
    print("Password is valide.")
