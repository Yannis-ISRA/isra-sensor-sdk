# 🚀 Assistant de Création de Driver pour Lecteur UHF

**Version :** ISRA SDK v1.0  
**Rôle :** Copiez ce prompt dans ChatGPT ou Claude pour transformer n'importe quelle documentation technique de lecteur en driver Python compatible avec l'écosystème ISRA.

---

## 📝 PROMPT À COPIER :

> "Agis en tant qu'expert en développement de protocoles de communication matérielle (RS232/TCP). Je souhaite créer un driver Python pour un nouveau lecteur RFID UHF.
>
> Ce driver doit hériter de la classe `BaseReader` et implémenter la méthode suivante : 
> `read_user_bank(self, epc, start_word, word_count)`.
>
> Voici les contraintes du protocole :
> 1. La trame doit inclure une longueur au début.
> 2. Le CRC calculé doit être de type [NOM DU CRC].
> 3. L'adresse par défaut du lecteur est [ADRESSE].
>
> **Voici la documentation technique du lecteur :**
> [COLLER ICI LE TEXTE DE LA DOC TECHNIQUE OU LE PDF]
>
> **Tâche :**
> Fournis-moi le code Python complet pour une classe nommée `MonNouveauLecteur` qui utilise `self.transport.send()` et `self.transport.receive()` pour effectuer une lecture de la banque USER (Bank 3) afin de récupérer les données des capteurs ISRA."

---

## 🛠 Conseils pour l'intégrateur :
- Identifiez bien la **méthode de calcul du CRC** dans la doc (souvent CRC-16/MCRF4XX ou CRC-16/CCITT).
- Vérifiez si le lecteur attend les données en **Hexadécimal** ou en **Binaire**.
- Une fois le code généré, placez-le simplement dans votre dossier `sdk/isra_readers.py`.
