# Instructions — Mise à jour du site jlegallo.github.io

Site en ligne : https://jlegallo.github.io  
Dépôt GitHub : https://github.com/jlegallo/jlegallo.github.io  
Fichiers source : dossier `site-perso` sur votre ordinateur

---

## Important : authentification GitHub par SSH

Depuis 2021, GitHub n'accepte plus les mots de passe pour `git push` / `git pull`. Il faut configurer une **clé SSH** sur chaque ordinateur (à faire **une seule fois** par machine). La procédure est décrite plus bas, dans la section dédiée à chaque système d'exploitation.

---

## 1. Mettre à jour le site depuis le MacBook Air (configuration déjà faite, SSH OK)

1. Ouvrez le Terminal
2. Allez dans le dossier du site :
   ```
   cd ~/site-perso
   ```
3. Récupérez les dernières modifications :
   ```
   git pull
   ```
4. Modifiez les fichiers `.qmd` avec votre éditeur habituel
5. Regénérez le site :
   ```
   quarto render
   ```
6. Envoyez les modifications sur GitHub :
   ```
   git add .
   git commit -m "description de la modification"
   git push
   ```
7. Patientez 2-3 minutes → le site est mis à jour en ligne.

---

## 2. Mettre à jour le site depuis le PC Windows

### Installation (une seule fois sur ce PC)

1. Installez **Git** : https://git-scm.com/download/win (options par défaut). Cela installe aussi **Git Bash**, qu'on utilisera pour SSH.
2. Installez **Quarto** : https://quarto.org/docs/get-started/ (téléchargez l'installateur Windows)
3. Ouvrez **Git Bash** (clic droit dans n'importe quel dossier → « Git Bash Here ») et configurez votre identité :
   ```
   git config --global user.email "jlegallo07@gmail.com"
   git config --global user.name "Julie Le Gallo"
   ```

### Configuration SSH sur ce PC (une seule fois)

1. Dans **Git Bash**, générez une clé SSH (laissez la passphrase vide en appuyant deux fois sur Entrée) :
   ```
   ssh-keygen -t ed25519 -C "jlegallo07@gmail.com"
   ```
2. Démarrez l'agent SSH et ajoutez la clé :
   ```
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```
3. Copiez la clé publique dans le presse-papier :
   ```
   clip < ~/.ssh/id_ed25519.pub
   ```
4. Allez sur https://github.com/settings/keys → **New SSH key**
   - Title : `PC Windows Julie` (ou autre nom au choix)
   - Key type : `Authentication Key`
   - Key : collez (Ctrl+V)
   - Cliquez **Add SSH key**
5. Testez la connexion :
   ```
   ssh -T git@github.com
   ```
   Réponse attendue : `Hi jlegallo! You've successfully authenticated...`

### Récupérer le dépôt (une seule fois)

```
git clone git@github.com:jlegallo/jlegallo.github.io.git site-perso
cd site-perso
```

### Modifier et publier (depuis ce PC)

1. Ouvrez Git Bash ou PowerShell et allez dans le dossier :
   ```
   cd chemin/vers/site-perso
   ```
2. Récupérez les dernières modifications :
   ```
   git pull
   ```
3. Modifiez vos fichiers `.qmd`
4. Regénérez et publiez :
   ```
   quarto render
   git add .
   git commit -m "description de la modification"
   git push
   ```

---

## 3. Mettre à jour le site depuis l'autre Mac

### Installation (une seule fois sur ce Mac)

1. Installez **Git** : ouvrez le Terminal et tapez `git --version` → si Git n'est pas installé, macOS propose de l'installer automatiquement, acceptez.
2. Installez **Quarto** : https://quarto.org/docs/get-started/ (téléchargez l'installateur macOS .pkg)
3. Configurez votre identité Git dans le Terminal :
   ```
   git config --global user.email "jlegallo07@gmail.com"
   git config --global user.name "Julie Le Gallo"
   ```

### Configuration SSH sur ce Mac (une seule fois)

1. Dans le Terminal, générez une clé SSH (sans passphrase) :
   ```
   ssh-keygen -t ed25519 -C "jlegallo07@gmail.com" -f ~/.ssh/id_ed25519 -N ""
   ```
2. Créez le fichier de configuration SSH pour intégrer la clé au trousseau macOS :
   ```
   cat > ~/.ssh/config <<'EOF'
   Host github.com
     HostName github.com
     User git
     IdentityFile ~/.ssh/id_ed25519
     UseKeychain yes
     AddKeysToAgent yes
   EOF
   chmod 600 ~/.ssh/config
   ```
3. Ajoutez la clé à l'agent SSH avec stockage dans le trousseau :
   ```
   ssh-add --apple-use-keychain ~/.ssh/id_ed25519
   ```
4. Copiez la clé publique dans le presse-papier :
   ```
   pbcopy < ~/.ssh/id_ed25519.pub
   ```
5. Allez sur https://github.com/settings/keys → **New SSH key**
   - Title : `Mac Bureau Julie` (ou autre nom au choix)
   - Key type : `Authentication Key`
   - Key : collez (Cmd+V)
   - Cliquez **Add SSH key**
6. Testez la connexion :
   ```
   ssh -T git@github.com
   ```
   Réponse attendue : `Hi jlegallo! You've successfully authenticated...`

### Récupérer le dépôt (une seule fois)

```
git clone git@github.com:jlegallo/jlegallo.github.io.git ~/site-perso
cd ~/site-perso
```

### Modifier et publier (depuis ce Mac)

1. Ouvrez le Terminal et allez dans le dossier :
   ```
   cd ~/site-perso
   ```
2. Récupérez les dernières modifications :
   ```
   git pull
   ```
3. Modifiez vos fichiers `.qmd`
4. Regénérez et publiez :
   ```
   quarto render
   git add .
   git commit -m "description de la modification"
   git push
   ```

---

## Si le dépôt utilise encore une URL HTTPS (bascule en SSH)

Si vous avez déjà cloné le dépôt avant en HTTPS et que `git push` demande un mot de passe, basculez l'URL distante en SSH :

```
cd chemin/vers/site-perso
git remote set-url origin git@github.com:jlegallo/jlegallo.github.io.git
git remote -v
```

Le résultat doit afficher `git@github.com:...` (et non plus `https://...`).

---

## Règle importante : toujours commencer par `git pull`

Si vous travaillez sur plusieurs ordinateurs, commencez **toujours** par `git pull` avant de modifier quoi que ce soit. Cela évite les conflits entre les versions.

---

## Structure des fichiers

| Fichier | Contenu |
|---------|---------|
| `index.qmd` | Page d'accueil |
| `cv.qmd` | CV |
| `research.qmd` | Recherche et projets |
| `publications.qmd` | Liste complète des publications |
| `supervision.qmd` | Encadrement doctoral |
| `teaching.qmd` | Enseignements |
| `presentations.qmd` | Présentations vidéo et interviews |
| `links.qmd` | Profils académiques et co-auteurs |
| `_quarto.yml` | Configuration générale du site |
| `styles.css` | Style visuel |
| `docs/` | Site généré (ne pas modifier à la main) |

---

## En cas de problème

- **Le site ne se met pas à jour** : vérifiez sur https://github.com/jlegallo/jlegallo.github.io/actions que le déploiement est bien passé (coche verte).
- **`git push` demande un mot de passe** : la clé SSH n'est pas configurée ou le dépôt est encore en HTTPS. Voir la section « bascule en SSH » plus haut.
- **`Permission denied (publickey)`** : la clé SSH n'a pas été ajoutée à GitHub. Refaites l'étape 4/5 de la configuration SSH (https://github.com/settings/keys).
- **Erreur `git pull` (conflit)** : un fichier a été modifié sur deux machines en même temps. Ouvrez le fichier indiqué, gardez la bonne version, puis `git add .` + `git commit` + `git push`.
- **Erreur `quarto render`** : vérifiez la syntaxe du fichier `.qmd` modifié (indentation, guillemets).
