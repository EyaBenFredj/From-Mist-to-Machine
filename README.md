

# 🚀 Générateur d'Automates : De l'ε-NFA au DFA

Bienvenue dans ce projet interactif de génération et de visualisation d'automates finis !  
Cette application vous permet de :
- Construire un **ε-NFA** (automate non déterministe avec transitions ε)
- Le convertir automatiquement en **DFA** (automate déterministe)
- Visualiser graphiquement les deux automates
- Tester des chaînes de caractères sur le DFA
- Télécharger les graphes générés

---

## ✨ Fonctionnalités principales

- 🎯 Interface Web simple et intuitive avec Streamlit.
- 🧠 Conversion automatique d'un ε-NFA en DFA.
- 🖼️ Visualisation des graphes avec Graphviz.
- 🧪 Test interactif de chaînes sur le DFA.
- 📥 Boutons pour télécharger les graphes générés (PNG).
- 🧹 Bouton pour réinitialiser les champs facilement.

---

##  Aperçu

### Interface de création d'automate :

![image](https://github.com/user-attachments/assets/7d70f241-105e-4b4b-8dcf-9ddd0375f8eb)

### Visualisation des graphes générés :
![image](https://github.com/user-attachments/assets/83fa8b15-30a1-44f5-8831-fe8b8a9df08d)


### Test d'une chaîne sur le DFA :
![image](https://github.com/user-attachments/assets/db3ad0c9-3c93-448e-9b8e-4f50e9b632bd)
![image](https://github.com/user-attachments/assets/96d609d6-77f8-447a-bb53-9c64322bfcec)


---

## 🔧 Installation rapide

### 1. Cloner le projet

```bash
git clone https://github.com/EyaBenFredj/From-Mist-to-Machine.git
cd votre-repo
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 3. Installer toutes les dépendances

```bash
pip install -r requirements.txt
```

---

## 📦 Dépendances principales

- `streamlit`
- `graphviz`
- `networkx`
- `pillow` (PIL)

*(Pensez aussi à installer Graphviz sur votre machine pour la génération des graphes.)*

---

## 🚀 Lancer l'application

```bash
streamlit run streamlit_app.py
```

Puis ouvrez votre navigateur sur :  
👉 [http://localhost:8501](http://localhost:8501)

---

## 📂 Structure du projet

```
From-Mist-to-Machine/
├── .streamlit/
│   └── config.toml         # Désactive les warnings Streamlit
├── outputs/                # Graphes générés (.png)
├── nfa.py                  # Classe ε-NFA
├── dfa.py                  # Classe DFA
├── visualize.py            # Outils de visualisation Graphviz
├── requirements.txt        # Dépendances Python
├── streamlit_app.py         # Application Web principale
└── README.md                # Ce fichier !
```

---

## 🧠 Concepts abordés

- **Automates Finis Non Déterministes (ε-NFA)**.
- **Déterminisation** : conversion vers DFA.
- **Graphes d'états** : visualisation via Graphviz.
- **Interaction utilisateur Web** avec Streamlit.

---

## 📌 Exemple de transitions entrées :

```
Q0,a->1
Q0,a->Q1
Q1,a->Q
Q1,b->Q
Q2,b->2
Q,b->Q
Q,a->Q
```

## 📋 Exemple de chaînes testées :

| Chaîne | Résultat |
|:-------|:---------|
| `a`    | ✅ Acceptée |
| `aa`   | ❌ Rejetée |
| `ab`   | ❌ Rejetée |
| `b`    | ❌ Rejetée |

---




