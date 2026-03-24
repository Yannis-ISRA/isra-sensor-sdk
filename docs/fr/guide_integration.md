# 🛠 Guide d'Intégration des Capteurs ISRA pour l'Industrie

Bienvenue dans l'écosystème **ISRA Sensor RFID**.  
Ce guide est conçu pour les automaticiens, techniciens et ingénieurs qui souhaitent intégrer des capteurs sans fil et sans pile dans leurs environnements industriels.

---

## 🏗 Architecture du système

Le système ISRA se décompose en 3 briques simples :

1.  **Le Capteur ISRA** : Positionné sur votre matériel (moteur, câble, bac). Il capte la température et l'humidité sans **aucune pile**.
2.  **Le Lecteur UHF** : L'antenne qui envoie de l'énergie au capteur et récupère ses données par ondes radio. 
3.  **Le SDK ISRA** : Le logiciel sur votre PC, Serveur ou Automate qui traduit les signaux radio en valeurs physiques lisibles (°C, %).

---

## 📡 Choisir son Interface de Communication

Pour relier vos lecteurs ISRA à votre système, plusieurs options s'offrent à vous :

| Interface | Distance Max | Avantage | Usage recommandé |
| :--- | :--- | :--- | :--- |
| **RS-232** | 15 m | Simple / Standard | Liaison directe avec un seul PC. |
| **RS-485** | 1200 m | Bus Multi-lecteurs | Usine, entrepôt, installations distantes. |
| **Ethernet/IP** | 100 m+ | Réseau Standard | Utilisation de l'infrastructure réseau existante. |

---

## 🔌 Conseils de Câblage (RS-485)

En milieu industriel, les parasites électriques sont fréquents. Pour garantir la fiabilité ISRA :
- Utilisez un **câble blindé torsadé** spécial série.
- Identifiez bien les bornes A et B de votre lecteur ISRA.
- Pour les bus de plus de 100m, ajoutez une **résistance de terminaison de 120 Ω** sur le dernier équipement.

---

## 📂 Exploitation des données

Une fois la mesure effectuée, voici comment l'exploiter dans votre métier :

### 📊 Archivage (CSV / Excel)
Générez des rapports automatiques en enregistrant les données dans des fichiers `.csv`. C'est la méthode la plus simple pour tracer vos températures sur le long terme.

### ⚙️ Automatisation (Automate / PLC)
Notre SDK peut communiquer directement avec vos automates via des fichiers d'échanges (JSON) ou via des passerelles **Modbus** ou **MQTT**. Idéal pour déclencher des alertes machines.

### 🌐 Supervision Web
Visualisez vos capteurs en temps réel sur des tableaux de bord interactifs (Dashboard) consultables depuis n'importe quel smartphone ou tablette sur le terrain.
