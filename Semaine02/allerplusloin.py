import hashlib

PASSWORD_FILE = "passwords.txt"

def hash_password(password):
    return hashlib.sha256(password).hexdigest()

def add_password():

    website = input("Site Web: ")
    username = input("Nom d'utilisateur: ")
    password = input("Mot de passe: ")
    hashed_password = hash_password(password)
    
    with open(PASSWORD_FILE, 'a') as f:
        f.write(f"{website} {username} {hashed_password}\n")
    
    print("Mot de passe ajouté avec succès.")

def list_passwords():
    try:
        with open(PASSWORD_FILE, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Aucun mot de passe enregistré.")
        return
    
    for line in lines:
        website, username, hashed_password = line.strip().split()
        print(f"{website}: {username} - {hashed_password}")

# Programme principal
while True:
    print("Que souhaitez-vous faire ?")
    print("1. Ajouter un nouveau mot de passe")
    print("2. Afficher les mots de passe enregistrés")
    print("3. Quitter")
    choix = input("Entrez votre choix (1/2/3): ")
    
    if choix == "1":
        add_password()
    elif choix == "2":
        list_passwords()
    elif choix == "3":
        break
    else:
        print("Choix invalide.")
