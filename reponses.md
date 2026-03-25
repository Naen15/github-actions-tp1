# Réponses au TP GitHub Actions

## Question 3 (Utilité du répertoire)
Le répertoire `.github/workflows` est l'endroit où GitHub va chercher les fichiers YAML de configuration. C'est grâce à ça qu'il peut lancer automatiquement les scripts de test ou de déploiement (CI/CD) dès qu'on fait un push.

## Question 8 (Onglet Actions - Hello World)
J'ai bien mon premier workflow qui s'affiche sous le nom "Hello World". Y a un petit check vert à côté, donc l'étape avec le echo a fonctionné sur la machine Ubuntu de GitHub.

## Question 10 (Exécution pytest)
Le workflow s'est bien lancé. Dans les logs, on voit que ça a installé les dépendances puis les 3 tests de `test_model.py` sont bien passés (vert).

## Question 11 (Introduction d'un bug)
Le push est passé en rouge (Fail). C'est logique parce que j'ai fait exprès de mettre "positif" au lieu de "positive" dans le code. Le test a vu la différence et a bloqué le pipeline.

## Question 14 (Matrice de versions)
Y a eu 3 jobs lancés en même temps pour les 3 versions de Python (3.8, 3.9, 3.10). C'est pratique pour vérifier d'un coup que notre code marche sur plusieurs versions sans tout refaire 3 fois.

## Question 21 (Badge de statut)
Le badge est devenu vert dans le README. C'est utile pour voir tout de suite si le dernier build est bon sans avoir à chercher dans les menus.

## Question 24 (Construction Docker)
Le build de l'image Docker a bien réussi. Dans les logs de l'étape de test, on voit que le conteneur a bien lancé la prédiction de sentiment comme prévu.

## Question 27 (Contenu de l'artifact)
L'artifact contient un fichier `metrics.json` avec les scores du modèle (accuracy, f1-score, etc.). Ça permet de garder une trace des performances de chaque version du modèle.

## Question 30 (Seuil d'accuracy)
Oui, le workflow a planté parce que l'accuracy était trop basse (en dessous de 0.9). On voit bien le message d'erreur rouge dans la console GitHub.

## Question 33 (Workflow Manuel)
Je l'ai lancé moi-même avec le bouton "Run workflow". J'ai pu choisir l'environnement (dev, staging ou prod) dans une petite liste déroulante avant de valider.

## Question 36 (Releases)
Oui, une nouvelle release a été créée automatiquement dans l'onglet dès que j'ai fait le push de mon tag (v1.0.0).

## Question 38 (Documentation)
Oui, l'artifact contient un fichier `model.md` qui récapitule bien ma fonction et les commentaires que j'ai écrits dans le code.

## Question 40 (Cache des dépendances)
Oui, c'est plus rapide la deuxième fois car GitHub réutilise les librairies déjà téléchargées au lieu de tout réinstaller du début.

## Question 42 (Jobs Parallèles)
On voit sur le graphe que `lint` et `test` partent en même temps. Par contre, `build` attend que les deux finissent, et `deploy` attend la fin de `build`.

## Question 44 (Avis sur la structure MLOps)
C'est hyper puissant car ça permet de sécuriser tout le projet. On peut pas envoyer un modèle qui bug ou qui n'est pas performant sans s'en rendre compte. Tout est vérifié tout seul.



