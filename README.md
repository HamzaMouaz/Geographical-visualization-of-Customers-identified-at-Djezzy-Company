# Système d'Analyse d'Identification Client

Ce projet est une application de tableau de bord interactive développée avec **Dash** et **Plotly**. Elle permet d'analyser les données de campagnes d'identification, de visualiser les revenus par région et de suivre l'évolution des identifications clients dans le temps.



## 📁 Structure du Projet

L'architecture suit les meilleures pratiques de développement Python pour assurer la modularité et la maintenance :

* **app.py** : Point d'entrée principal de l'application Dash.
* **data/** : Contient les fichiers sources (Excel/CSV).
* **src/** : Cœur de la logique métier.
    * `config.py` : Configuration globale et chemins de fichiers.
    * `data_processor.py` : Nettoyage et transformation des données (Pandas).
    * `visualizations.py` : Génération des graphiques interactifs.
* **requirements.txt** : Liste des dépendances Python nécessaires.

## 🚀 Installation

1.  **Cloner le dépôt :**
    ```bash
    git clone <url-du-projet>
    cd identification_project
    ```

2.  **Créer un environnement virtuel (recommandé) :**
    ```bash
    python -m venv venv
    # Sur Windows
    .\venv\Scripts\activate
    # Sur macOS/Linux
    source venv/bin/activate
    ```

3.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

## 📊 Utilisation

1.  Assurez-vous que votre fichier de données `POS_IDENTIFCIATION_CAMPAGNE_STAT.xlsx` est placé dans le dossier `data/`.
2.  Lancez l'application :
    ```bash
    python app.py
    ```
3.  Ouvrez votre navigateur et accédez à l'adresse : `http://127.0.0.1:8050`

## 🛠️ Fonctionnalités

-   **Analyse de Revenus** : Visualisation comparative des revenus générés par Business Unit (BU).
-   **Suivi Temporel** : Graphique d'évolution du nombre de clients identifiés par année.
-   **Filtrage Spécifique** : Analyse ciblée sur des offres particulières (ex: HAYLA Maxi).
-   **Interface Interactive** : Graphiques Plotly permettant le zoom, le survol et l'exportation.

## 📦 Dépendances Principales

-   [Dash](https://dash.plotly.com/) - Framework pour l'interface utilisateur.
-   [Pandas](https://pandas.pydata.org/) - Manipulation et analyse de données.
-   [Plotly](https://plotly.com/python/) - Bibliothèque de graphiques interactifs.
-   [Openpyxl](https://openpyxl.readthedocs.io/) - Lecture des fichiers Excel.

## 📝 Auteur
- **Votre Nom** - *Développement Initial*