---
id: diagnostic-depannage
title: Diagnostic & dépannage
---

# Diagnostic & dépannage (terrain)

Cette page regroupe les pannes les plus fréquentes observées en mise en service.

## 1) Aucun port COM visible

**Causes probables**
- Driver USB-série absent ou incorrect
- Adaptateur USB défectueux
- Câble USB de mauvaise qualité

**Actions recommandées**
- Vérifier le gestionnaire de périphériques
- Réinstaller le driver du chipset
- Tester un adaptateur **FTDI** validé

## 2) Port COM visible mais impossible d'ouvrir le port

**Causes probables**
- Port déjà utilisé par une autre appli
- Paramètres série incohérents
- Instabilité adaptateur low-cost

**Actions recommandées**
- Fermer les autres logiciels série
- Vérifier baudrate/parité/stopbits
- Changer d'adaptateur (FTDI)

## 3) Trames RX vides ou aléatoires

**Causes probables**
- Mauvais câblage RX/TX/GND
- Mauvaise vitesse série
- Perturbations CEM

**Actions recommandées**
- Vérifier le brochage réel constructeur
- Tester à courte distance
- Utiliser câble blindé et masse propre

## 4) Aucun tag détecté

**Causes probables**
- Antenne non connectée
- Puissance trop basse
- Tag hors champ / orientation défavorable

**Actions recommandées**
- Vérifier connectique RF
- Ajuster positionnement antenne/tag
- Confirmer l'inventaire EPC avant lecture mémoire

## 5) Valeurs Temp/Hum incohérentes

**Causes probables**
- Mauvais parsing de la réponse
- Erreur de conversion des mots mémoire
- Lecture incomplète (timeout)

**Actions recommandées**
- Logger les trames RX brutes
- Valider l'ordre des mots (endianness)
- Ajouter retry + timeout clair

## 6) Tableau “Symptôme -> Action rapide”

| Symptôme | Action 1 | Action 2 |
| :--- | :--- | :--- |
| COM absent | Réinstaller driver | Tester autre câble/adaptateur |
| COM occupé | Fermer autre outil série | Redémarrer PC si besoin |
| Pas de tag | Vérifier antenne | Repositionner tag |
| Valeurs instables | Logger RX/TX | Vérifier conversion |

### 📷 Illustration recommandée
Photo annotée du câblage série correct + capture gestionnaire de périphériques.
