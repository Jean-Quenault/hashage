import bcrypt

def hash_password(password):
    """Hash un mot de passe avec bcrypt."""
    # Générer un sel et hasher le mot de passe
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def check_password(hashed_password, user_password):
    """Vérifie si un mot de passe correspond au hash."""
    return bcrypt.checkpw(user_password.encode(), hashed_password)

def main():
    # Saisie du mot de passe et affichage du hash
    password = input("Entrez le mot de passe : ")
    hashed_password = hash_password(password)
    print(f"Mot de passe hashé : {hashed_password}")

    # Saisie du mot de passe pour la vérification
    password_to_check = input("\nEntrez à nouveau le mot de passe pour vérifier : ")

    # Vérification du mot de passe
    if check_password(hashed_password, password_to_check):
        print("Les mots de passe correspondent.")
    else:
        print("Les mots de passe ne correspondent pas.")

if __name__ == "__main__":
    main()
