
# 🚀 Générateur d'Automates : De l'ε-NFA au DFA

Bienvenue dans ce projet de génération d'automates finis !  
Ce projet permet de :
- Créer un **ε-NFA** (Automate Fini Non Déterministe avec transitions ε)
- Le convertir automatiquement en **DFA** (Automate Fini Déterministe)
- Visualiser les graphes générés
- Tester si une chaîne est acceptée par le DFA

---

## ✨ Fonctionnalités

- **Création d'automates** à partir d'une interface utilisateur simple.
- **Visualisation graphique** des ε-NFA et DFA grâce à Graphviz.
- **Test interactif** de chaînes pour vérifier leur acceptation par le DFA.
- **Interface Web** conviviale développée avec Streamlit.

---

## 🖥️ Démo rapide

### 🔹 Interface principale


![image](https://github.com/user-attachments/assets/766ef6b1-428b-463f-a154-f1fb439c65ff)

### 🔹 Exemple de génération d'un automate

> *(Ajoutez ici une capture d'écran montrant un ε-NFA et un DFA généré)*

![Génération automates](PLACEHOLDER_AUTOMATE.png)

### 🔹 Test de chaînes

> *(Ajoutez ici une capture d'écran montrant le test d'une chaîne acceptée ou rejetée)*

![Test de chaînes](PLACEHOLDER_TEST.png)

---

## 🔧 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
# Puis activer l'environnement :
# Sous Windows :
.venv\Scripts\activate
# Sous Linux/Mac :
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 📦 Dépendances principales

- `streamlit`
- `graphviz`
- `networkx`

*(Graphviz doit également être installé sur votre système !)*

---

## 🚀 Lancer l'application

```bash
streamlit run streamlit_app.py
```

Puis ouvrez votre navigateur sur [http://localhost:8501](http://localhost:8501).

---

## 📂 Structure du projet

```
From-Mist-to-Machine/
├── main.py               # Script principal
├── nfa.py                 # Classe pour l'ε-NFA
├── dfa.py                 # Classe pour le DFA
├── visualize.py           # Fonctions pour dessiner les automates
├── streamlit_app.py       # Application Web Streamlit
├── outputs/               # Dossier des graphes générés (.png)
├── tests/                 # Tests unitaires (facultatif)
├── README.md              # Présentation du projet (ce fichier)
└── requirements.txt       # Liste des dépendances Python
```

---

## 🧠 Concepts abordés

- **Automates finis non déterministes (NFA)** avec transitions ε.
- **Déterminisation** : conversion automatique vers DFA.
- **Visualisation de graphes d'états**.
- **Interaction utilisateur Web**.

---

## 📌 Exemples

### Exemple de transitions entrées :

```
Q0,a->1
Q0,a->Q1
Q1,a->Q
Q1,b->Q
Q2,b->2
Q,b->Q
Q,a->Q
```

### Exemple de chaînes à tester :
| Chaîne | Résultat |
|:-------|:---------|
| `a`    | ✅ Acceptée |
| `aa`   | ❌ Rejetée |
| `ab`   | ❌ Rejetée |
| `b`    | ❌ Rejetée |

---



---



---
```

---


