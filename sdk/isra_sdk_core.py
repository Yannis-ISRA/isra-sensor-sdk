#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ISRA SDK Core - Logique métier et conversion des données capteurs
Ce fichier contient la 'science' de conversion des puces ISRA Sensor RFID.
Simple, robuste et sans fioritures pour les intégrateurs.
"""

class IsraMetrics:
    """Outils de conversion des données brutes (registres) en valeurs réelles."""

    @staticmethod
    def calculate_temperature(raw_temp, t30_calib, t60_calib):
        """
        Calcule la température réelle à partir des données de calibration.
        Formule linéaire basée sur deux points (30°C et 60°C).
        """
        try:
            if (t60_calib - t30_calib) != 0:
                temp_c = 30 + 30 * (raw_temp - t30_calib) / (t60_calib - t30_calib)
                return round(temp_c, 2)
            return 0.0
        except Exception:
            return 0.0

    @staticmethod
    def calculate_humidity(raw_hum, h30_calib, h70_calib):
        """
        Calcule l'humidité réelle à partir des données de calibration.
        Formule linéaire basée sur deux points (30% et 70%).
        """
        try:
            if (h70_calib - h30_calib) != 0:
                hum_p = 30 + 40 * (raw_hum - h30_calib) / (h70_calib - h30_calib)
                return round(hum_p, 2)
            return 0.0
        except Exception:
            return 0.0

    @staticmethod
    def parse_13bit_word(word_16bit):
        """
        Extrait la valeur réelle d'un mot de calibration 16 bits.
        Conforme à la spécification 'Format de calibration ISRA'.
        """
        val = word_16bit & 0x1FFF      # Les 13 bits de donnée (0-12)
        div_exp = (word_16bit >> 14) & 0x03 # L'exposant du diviseur (bits 14-15)
        return val / (2 ** div_exp)

class IsraSensor:
    """Classe de haut niveau pour manipuler un capteur RFID ISRA."""

    def __init__(self, reader, epc):
        """
        Initialise un accès au capteur.
        :param reader: Une instance d'un lecteur compatible (SDK Reader)
        :param epc: L'identifiant unique (EPC) du tag capteur
        """
        self.reader = reader
        self.epc = epc.replace(" ", "")

    def get_readings(self):
        """
        Lit les registres du capteur et retourne la température et l'humidité.
        :return: (temperature, humidite) ou (None, None) en cas d'échec.
        """
        # La puce ISRA stocke ses données de calibration et mesures dans la banque USER (3)
        # On lit 7 mots à partir de l'adresse 0x00
        raw_words = self.reader.read_user_bank(self.epc, start=0, count=7)
        
        if not raw_words or len(raw_words) < 7:
            return None, None

        # 1. Extraction des mesures brutes et calibration du capteur
        h_raw = IsraMetrics.parse_13bit_word(raw_words[0])
        t_raw = IsraMetrics.parse_13bit_word(raw_words[1])
        
        h30_cal = IsraMetrics.parse_13bit_word(raw_words[2])
        h70_cal = IsraMetrics.parse_13bit_word(raw_words[3])
        
        t60_cal = IsraMetrics.parse_13bit_word(raw_words[4])
        t30_cal = IsraMetrics.parse_13bit_word(raw_words[6])

        # 2. Calcul des valeurs réelles
        temperature = IsraMetrics.calculate_temperature(t_raw, t30_cal, t60_cal)
        humidity = IsraMetrics.calculate_humidity(h_raw, h30_cal, h70_cal)

        return temperature, humidity

    def to_json(self):
        """Retourne les mesures au format JSON prêt pour l'intégration."""
        import json
        t, h = self.get_readings()
        return json.dumps({
            "epc": self.epc,
            "temperature": t,
            "humidity": h,
            "brand": "ISRA",
            "unit_temp": "°C",
            "unit_hum": "%"
        })
