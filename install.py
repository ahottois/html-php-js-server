#!/bin/bash

# Script d'installation d'un serveur LAMP (Linux, Apache, MySQL, PHP)
# Auteur: Claude
# Date: 17 Mars 2025
# Description: Ce script installe et configure un serveur web complet avec Apache, MySQL et PHP sur Ubuntu Server

# Définition des couleurs pour le terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Définition du fichier de log
LOG_FILE="installation_lamp_server.log"
GUIDE_FILE="guide_utilisation_lamp.md"

# Fonction pour écrire dans le log
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Fonction pour afficher les messages
print_message() {
    echo -e "${BLUE}[INFO]${NC} $1" | tee -a "$LOG_FILE"
}

print_success() {
    echo -e "${GREEN}[SUCCÈS]${NC} $1" | tee -a "$LOG_FILE"
}

print_error() {
    echo -e "${RED}[ERREUR]${NC} $1" | tee -a "$LOG_FILE"
}

print_warning() {
    echo -e "${YELLOW}[ATTENTION]${NC} $1" | tee -a "$LOG_FILE"
}

# Fonction pour vérifier si l'utilisateur est root
check_root() {
    if [ "$(id -u)" -ne 0 ]; then
        print_error "Ce script doit être exécuté en tant que root ou avec sudo."
        exit 1
    fi
}

# Fonction pour créer le fichier guide
create_guide() {
    cat > "$GUIDE_FILE" << 'EOF'
# Guide d'utilisation du serveur LAMP

## Introduction
Ce document explique comment utiliser votre nouveau serveur LAMP (Linux, Apache, MySQL, PHP) installé par le script d'installation automatique.

## Structure des répertoires
- `/var/www/html/` : Répertoire racine du serveur web
- `/etc/apache2/` : Configuration d'Apache
- `/etc/php/8.1/apache2/` : Configuration de PHP (la version peut varier)
- `/etc/mysql/` : Configuration de MySQL

## Comment utiliser le serveur

### Déployer un site web
1. Placez vos fichiers HTML, CSS, JavaScript et PHP dans le répertoire `/var/www/html/`
2. Vous pouvez créer des sous-répertoires pour organiser plusieurs sites

Exemple pour un site simple:
```
/var/www/html/monsite/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── script.js
└── images/
```

### Base de données MySQL
- L'administrateur MySQL a été configuré avec les identifiants que vous avez fournis pendant l'installation
- Pour créer une nouvelle base de données:
  ```sql
  CREATE DATABASE mabasededonnees;
  CREATE USER 'monutilisateur'@'localhost' IDENTIFIED BY 'monmotdepasse';
  GRANT ALL PRIVILEGES ON mabasededonnees.* TO 'monutilisateur'@'localhost';
  FLUSH PRIVILEGES;
  ```

### PHP
- PHP est configuré et prêt à l'emploi
- Créez des fichiers .php dans le répertoire `/var/www/html/`
- Exemple de connexion à la base de données:
  ```php
  <?php
  $servername = "localhost";
  $username = "monutilisateur";
  $password = "monmotdepasse";
  $dbname = "mabasededonnees";

  $conn = new mysqli($servername, $username, $password, $dbname);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  echo "Connexion réussie à la base de données!";
  ?>
  ```

### Commandes utiles
- Redémarrer Apache: `sudo systemctl restart apache2`
- Redémarrer MySQL: `sudo systemctl restart mysql`
- Vérifier le statut d'Apache: `sudo systemctl status apache2`
- Vérifier le statut de MySQL: `sudo systemctl status mysql`
- Accéder à la console MySQL: `mysql -u root -p`

### Dépannage
- Consultez les logs d'Apache: `/var/log/apache2/error.log`
- Consultez les logs MySQL: `/var/log/mysql/error.log`
- Vérifiez la configuration PHP: `php -i`

### Sécurité
- Assurez-vous de mettre à jour régulièrement vos logiciels: `sudo apt update && sudo apt upgrade`
- Configurez correctement les permissions des fichiers:
  ```bash
  sudo chown -R www-data:www-data /var/www/html/
  sudo find /var/www/html/ -type d -exec chmod 755 {} \;
  sudo find /var/www/html/ -type f -exec chmod 644 {} \;
  ```

## Ressources additionnelles
- Documentation Apache: https://httpd.apache.org/docs/
- Documentation PHP: https://www.php.net/docs.php
- Documentation MySQL: https://dev.mysql.com/doc/
EOF

    print_success "Guide d'utilisation créé: $GUIDE_FILE"
}

# Fonction pour créer une page web de test
create_test_page() {
    local dir="/var/www/html/test"
    mkdir -p "$dir"

    # Création d'une page d'accueil
    cat > "$dir/index.php" << 'EOF'
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test du serveur LAMP</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .success {
            color: #27ae60;
            font-weight: bold;
        }
        .error {
            color: #e74c3c;
            font-weight: bold;
        }
        .card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <h1>Test du serveur LAMP</h1>
    
    <div class="card">
        <h2>État des composants</h2>
        <ul>
            <li>Serveur: <span class="success">Apache fonctionne</span></li>
            <li>PHP: <span class="success">Version <?php echo phpversion(); ?></span></li>
            <li>MySQL: 
                <?php
                try {
                    $db = new PDO('mysql:host=localhost', 'root', 'root_password');
                    echo '<span class="success">Connecté</span>';
                } catch (PDOException $e) {
                    echo '<span class="error">Erreur de connexion</span>';
                }
                ?>
            </li>
        </ul>
    </div>
    
    <div class="card">
        <h2>Test PHP</h2>
        <p>Heure du serveur: <?php echo date('Y-m-d H:i:s'); ?></p>
        
        <h3>Modules PHP installés</h3>
        <table>
            <tr>
                <th>Module</th>
                <th>État</th>
            </tr>
            <?php
            $required_extensions = ['mysqli', 'pdo_mysql', 'gd', 'json', 'xml', 'mbstring'];
            foreach ($required_extensions as $ext) {
                echo '<tr>';
                echo '<td>' . $ext . '</td>';
                echo '<td>' . (extension_loaded($ext) ? '<span class="success">Installé</span>' : '<span class="error">Non installé</span>') . '</td>';
                echo '</tr>';
            }
            ?>
        </table>
    </div>
    
    <div class="card">
        <h2>Test JavaScript</h2>
        <p>Cliquez sur le bouton pour tester JavaScript:</p>
        <button id="testButton">Tester JavaScript</button>
        <p id="jsResult"></p>
        
        <script>
            document.getElementById('testButton').addEventListener('click', function() {
                document.getElementById('jsResult').innerHTML = '<span class="success">JavaScript fonctionne correctement!</span>';
                
                // Afficher la date et l'heure côté client
                const now = new Date();
                document.getElementById('jsResult').innerHTML += '<br>Heure du client: ' + now.toLocaleString();
            });
        </script>
    </div>
    
    <div class="card">
        <h2>Informations système</h2>
        <p>Système d'exploitation: <?php echo php_uname(); ?></p>
        <p>Serveur web: <?php echo $_SERVER['SERVER_SOFTWARE']; ?></p>
        <p>Adresse IP du serveur: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
    </div>
</body>
</html>
EOF

    print_success "Page de test créée dans $dir/index.php"
}

# Fonction pour installer les packages nécessaires
install_packages() {
    print_message "Mise à jour des paquets..."
    apt update -y >> "$LOG_FILE" 2>&1
    
    print_message "Installation d'Apache, MySQL, PHP et extensions..."
    apt install -y apache2 mysql-server php libapache2-mod-php php-mysql php-gd php-json php-xml php-mbstring php-curl unzip >> "$LOG_FILE" 2>&1
    
    # Vérifier si l'installation a réussi
    if [ $? -eq 0 ]; then
        print_success "Installation des paquets réussie."
    else
        print_error "Erreur lors de l'installation des paquets. Consultez $LOG_FILE pour plus de détails."
        exit 1
    fi
}

# Fonction pour configurer MySQL
configure_mysql() {
    print_message "Configuration de MySQL..."
    
    # Créer un mot de passe root sécurisé
    MYSQL_ROOT_PASSWORD="root_password"  # Dans un script réel, vous pourriez générer un mot de passe aléatoire
    
    # Sécuriser l'installation MySQL
    mysql --user=root <<_EOF_
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '${MYSQL_ROOT_PASSWORD}';
DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
FLUSH PRIVILEGES;
_EOF_

    print_success "MySQL configuré avec succès."
    log "Mot de passe root MySQL: ${MYSQL_ROOT_PASSWORD}"
}

# Fonction pour configurer Apache
configure_apache() {
    print_message "Configuration d'Apache..."
    
    # Activer les modules nécessaires
    a2enmod rewrite >> "$LOG_FILE" 2>&1
    
    # Ajuster la configuration pour permettre les fichiers .htaccess
    cat > /etc/apache2/sites-available/000-default.conf << 'EOF'
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html
    
    <Directory /var/www/html>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF

    # Redémarrer Apache pour appliquer les changements
    systemctl restart apache2 >> "$LOG_FILE" 2>&1
    
    print_success "Apache configuré avec succès."
}

# Fonction pour configurer PHP
configure_php() {
    print_message "Configuration de PHP..."
    
    # Récupérer la version de PHP installée
    PHP_VERSION=$(php -r "echo PHP_MAJOR_VERSION.'.'.PHP_MINOR_VERSION;")
    
    # Créer une copie de sauvegarde du fichier de configuration
    cp /etc/php/${PHP_VERSION}/apache2/php.ini /etc/php/${PHP_VERSION}/apache2/php.ini.bak
    
    # Modifier les paramètres PHP pour de meilleures performances et sécurité
    sed -i 's/memory_limit = .*/memory_limit = 256M/' /etc/php/${PHP_VERSION}/apache2/php.ini
    sed -i 's/upload_max_filesize = .*/upload_max_filesize = 64M/' /etc/php/${PHP_VERSION}/apache2/php.ini
    sed -i 's/post_max_size = .*/post_max_size = 64M/' /etc/php/${PHP_VERSION}/apache2/php.ini
    sed -i 's/max_execution_time = .*/max_execution_time = 300/' /etc/php/${PHP_VERSION}/apache2/php.ini
    sed -i 's/;date.timezone.*/date.timezone = UTC/' /etc/php/${PHP_VERSION}/apache2/php.ini
    
    # Redémarrer Apache pour appliquer les changements
    systemctl restart apache2 >> "$LOG_FILE" 2>&1
    
    print_success "PHP configuré avec succès."
}

# Fonction pour configurer le pare-feu
configure_firewall() {
    print_message "Configuration du pare-feu..."
    
    # Vérifier si ufw est installé
    if ! command -v ufw &> /dev/null; then
        apt install -y ufw >> "$LOG_FILE" 2>&1
    fi
    
    # Configurer les règles de base
    ufw allow OpenSSH >> "$LOG_FILE" 2>&1
    ufw allow 'Apache Full' >> "$LOG_FILE" 2>&1
    
    # Activer le pare-feu s'il n'est pas déjà actif
    if ! ufw status | grep -q "Status: active"; then
        print_warning "Le pare-feu va être activé. Assurez-vous que la règle SSH est ajoutée pour éviter d'être bloqué."
        echo "y" | ufw enable >> "$LOG_FILE" 2>&1
    fi
    
    print_success "Pare-feu configuré avec succès."
}

# Fonction principale
main() {
    clear
    echo -e "${GREEN}============================================${NC}"
    echo -e "${GREEN}  Installation Automatique Serveur LAMP${NC}"
    echo -e "${GREEN}============================================${NC}"
    echo ""
    
    # Vérifier si l'utilisateur est root
    check_root
    
    # Créer le fichier de log
    log "Démarrage de l'installation du serveur LAMP"
    
    # Installer les packages
    install_packages
    
    # Configurer les services
    configure_mysql
    configure_apache
    configure_php
    configure_firewall
    
    # Créer une page de test
    create_test_page
    
    # Créer le guide d'utilisation
    create_guide
    
    # Afficher les informations de connexion
    echo ""
    echo -e "${GREEN}============================================${NC}"
    echo -e "${GREEN}  Installation terminée avec succès !${NC}"
    echo -e "${GREEN}============================================${NC}"
    echo ""
    echo -e "Votre serveur LAMP est prêt à l'emploi!"
    echo -e "Adresse du serveur web: http://$(hostname -I | awk '{print $1}')"
    echo -e "Page de test: http://$(hostname -I | awk '{print $1}')/test/"
    echo -e "Guide d'utilisation: ${GUIDE_FILE}"
    echo -e "Journal d'installation: ${LOG_FILE}"
    echo ""
    echo -e "Mot de passe MySQL root: ${MYSQL_ROOT_PASSWORD}"
    echo -e "${YELLOW}IMPORTANT: Notez ce mot de passe et changez-le dès que possible!${NC}"
    echo ""
    
    log "Installation terminée avec succès."
}

# Exécuter la fonction principale
main
