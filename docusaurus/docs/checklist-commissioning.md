---
id: checklist-commissioning
title: Checklist de mise en service
---

# Checklist de mise en service (commissioning)

Utilisez cette checklist lors d'une installation client.

## 1) Préparation matériel

- [ ] Lecteur UHF alimenté et stable
- [ ] Antenne connectée correctement
- [ ] Adaptateur USB-série **FTDI** validé
- [ ] Tag(s) ISRA disponibles pour test

## 2) Préparation PC

- [ ] Driver série installé
- [ ] Port COM détecté
- [ ] Python installé
- [ ] Dépendances installées (`pyserial` minimum)

## 3) Validation communication

- [ ] Mini-app inventaire EPC OK
- [ ] Trames RX cohérentes observées
- [ ] Aucun timeout récurrent

## 4) Validation capteur

- [ ] Lecture Temp/Hum OK
- [ ] Valeurs plausibles et stables
- [ ] Répétabilité confirmée (plusieurs lectures)

## 5) Validation intégration client

- [ ] Format sortie validé (JSON/CSV)
- [ ] Protocole cible validé (Modbus/MQTT/OPC UA/REST)
- [ ] Données visibles côté supervision
- [ ] Horodatage validé

## 6) Livrable fin de mise en service

- [ ] Script final livré
- [ ] Paramètres documentés (port, vitesse, adresse, timeout)
- [ ] Procédure de redémarrage fournie
- [ ] Procédure de diagnostic fournie

### 📷 Illustration recommandée
Photo de l'installation finale + capture supervision affichant Temp/Hum en temps réel.
