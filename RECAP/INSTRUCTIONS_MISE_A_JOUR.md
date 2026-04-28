# Instructions — Mise à jour du site jlegallo.github.io

Site en ligne : https://jlegallo.github.io  
Dépôt GitHub : https://github.com/jlegallo/jlegallo.github.io  
Fichiers source : dossier `site-perso` sur votre ordinateur

---

## 1. Mettre à jour le site depuis CE PC (Windows, configuration déjà faite)

1. Ouvrez PowerShell
2. Allez dans le dossier du site :
   ```
   cd C:\Users\jlega\Documents\site-perso
   ```
3. Modifiez les fichiers `.qmd` avec votre éditeur habituel
4. Regénérez le site :
   ```
   quarto render
   ```
5. Envoyez les modifications sur GitHub :
   ```
   git add .
   git commit -m "description de la modification"
   git push
   ```
6. Patientez 2-3 minutes → le site est mis à jour en ligne.

---

## 2. Mettre à jour le site depuis un AUTRE PC (Windows)

### Installation (une seule fois sur ce PC)

1. Installez **Git** : https://git-scm.com/download/win (options par défaut)
2. Installez **Quarto** : https://quarto.org/docs/get-started/ (téléchargez l'installateur Windows)
3. Ouvrez PowerShell et configurez votre identité Git :
   ```
   git config --global user.email "votre-email@example.com"
   git config --global user.name "Julie Le Gallo"
   ```
4. Récupérez le dépôt depuis GitHub :
   ```
   git clone https://github.com/jlegallo/jlegallo.github.io.git site-perso
   cd site-perso
   ```
   → Cela crée un dossier `site-perso` avec tous vos fichiers.

### Modifier et publier (depuis ce PC)

1. Ouvrez PowerShell et allez dans le dossier :
   ```
   cd chemin\vers\site-perso
   ```
2. Récupérez les dernières modifications (important si vous travaillez sur plusieurs PC) :
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

## 3. Mettre à jour le site depuis un MAC

### Installation (une seule fois sur ce Mac)

1. Installez **Git** : ouvrez le Terminal et tapez `git --version` → si Git n'est pas installé, macOS propose de l'installer automatiquement, acceptez.
2. Installez **Quarto** : https://quarto.org/docs/get-started/ (téléchargez l'installateur macOS .pkg)
3. Configurez votre identité Git dans le Terminal :
   ```
   git config --global user.email "votre-email@example.com"
   git config --global user.name "Julie Le Gallo"
   ```
4. Récupérez le dépôt depuis GitHub :
   ```
   git clone https://github.com/jlegallo/jlegallo.github.io.git site-perso
   cd site-perso
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
- **Erreur `git push`** : vérifiez que vous avez bien fait `git pull` avant, et que vous êtes connecté à GitHub.
- **Erreur `quarto render`** : vérifiez la syntaxe du fichier `.qmd` modifié (indentation, guillemets).
