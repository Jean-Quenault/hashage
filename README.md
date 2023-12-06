# Comparateur de mot de passe avec l'algorithme bcrypt

Ce projet est un exemple simple de script Python pour démontrer l'utilisation de l'algorithme bcrypt pour hasher et vérifier les mots de passe. Il utilise la bibliothèque `bcrypt` pour offrir une méthode sécurisée non obsolète (en date de 2023) de traitement des mots de passe.

## Installation

Pour utiliser ce script, vous devez avoir Python installé sur votre système. De plus, le module `bcrypt` est requis. Vous pouvez l'installer en utilisant pip :

`python3 install bcrypt`

## Utilisation
Le script fonctionne en deux étapes :

1. **Hasher un mot de passe** entré par l'utilisateur.
2. **Vérifier** si un second mot de passe entré correspond au hash du premier.

Exécutez le script dans un terminal ou un environnement Python. Suivez les instructions à l'écran pour entrer et vérifier les mots de passe.

## Fonctionnalités

- **Hashage de mot de passe** : Utilise `bcrypt` pour créer un hash sécurisé du mot de passe.
- **Vérification de mot de passe** : Compare un mot de passe entré avec le hash stocké pour confirmer s'ils correspondent.

## Références

Pour plus d'informations sur le hashage, le salage et l'encryption, vous pouvez consulter l'article suivant : [Encryption vs Hashing vs Salting](https://www.pingidentity.com/fr/resources/blog/post/encryption-vs-hashing-vs-salting.html).

## Licence

Ce projet est distribué sous la Licence MIT.