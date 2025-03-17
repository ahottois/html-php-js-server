# EasyLAMP - Installation automatique de serveur LAMP

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**EasyLAMP** est un script d'installation automatique qui configure un serveur web complet LAMP (Linux, Apache, MySQL, PHP) avec support HTML et JavaScript sur Ubuntu Server. Conçu pour être extrêmement facile à utiliser, ce script s'occupe de tous les aspects de l'installation pour que vous puissiez vous concentrer sur le développement de votre site web.

## 📋 Fonctionnalités

- ✅ Installation complète d'Apache, MySQL, PHP et extensions nécessaires
- ✅ Configuration sécurisée de tous les composants
- ✅ Configuration automatique du pare-feu (UFW)
- ✅ Page de test pour vérifier le bon fonctionnement de l'installation
- ✅ Guide d'utilisation détaillé en français
- ✅ Journalisation complète du processus d'installation

## 🚀 Installation

### Prérequis

- Ubuntu Server (18.04, 20.04, 22.04 ou plus récent)
- Accès root ou sudo
- Connexion internet

### Étapes d'installation

1. Clonez ce dépôt sur votre serveur :
   ```bash
   git clone https://github.com/ahottois/html-php-js-server.git
   cd easylamp
   ```

2. Rendez le script exécutable :
   ```bash
   chmod +x lamp-server-setup.sh
   ```

3. Exécutez le script avec les privilèges d'administrateur :
   ```bash
   sudo ./lamp-server-setup.sh
   ```

4. Suivez les instructions à l'écran. L'installation est entièrement automatisée !

## 🔍 Vérification de l'installation

Après l'exécution du script, vous pouvez vérifier que tout fonctionne correctement en accédant à :

- `http://adresse-ip-du-serveur/` - Page d'accueil d'Apache
- `http://adresse-ip-du-serveur/test/` - Page de test complète vérifiant tous les composants

## 📚 Guide d'utilisation

Le script génère automatiquement un guide d'utilisation détaillé (`guide_utilisation_lamp.md`) qui explique :

- Comment déployer vos sites web
- Comment gérer vos bases de données MySQL
- Exemples de code PHP pour connecter vos applications à MySQL
- Commandes utiles pour gérer votre serveur
- Conseils de sécurité et de dépannage

## 🛠 Personnalisation

Vous pouvez personnaliser l'installation en modifiant le script avant de l'exécuter. Les principaux paramètres sont clairement identifiés au début du fichier.

## 📝 Journal d'installation

Le script crée un fichier journal détaillé (`installation_lamp_server.log`) qui enregistre toutes les étapes de l'installation. Ce fichier est utile pour le dépannage en cas de problème.

## 🔒 Sécurité

Le script configure automatiquement :

- Un mot de passe MySQL sécurisé
- Les règles de pare-feu pour protéger votre serveur
- Les permissions appropriées pour les fichiers web
- Des paramètres PHP sécurisés

⚠️ **Important** : Bien que le script configure une installation sécurisée, il est recommandé de modifier le mot de passe MySQL root dès que possible après l'installation.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork ce dépôt
2. Créer une branche pour votre fonctionnalité (`git checkout -b nouvelle-fonctionnalite`)
3. Commit vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin nouvelle-fonctionnalite`)
5. Ouvrir une Pull Request

## 📧 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur ce dépôt GitHub.

---

⭐ **N'oubliez pas de mettre une étoile à ce dépôt si vous l'avez trouvé utile !** ⭐
