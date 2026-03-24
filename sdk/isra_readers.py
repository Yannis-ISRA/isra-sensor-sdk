#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ISRA SDK base_reader - Couche de transport et abstraction Lecteurs
Permet de supporter RS-232, RS-485 et Ethernet/IP de manière transparente.
"""

import serial
import socket
import time

class Transport:
    """Classe de base pour la communication physique."""
    def send(self, data): raise NotImplementedError
    def receive(self, length): raise NotImplementedError
    def close(self): raise NotImplementedError

class SerialTransport(Transport):
    """Transport pour RS-232 et RS-485 via port COM."""
    def __init__(self, port, baudrate=57600):
        self.ser = serial.Serial(port, baudrate, timeout=1)
    
    def send(self, data):
        self.ser.write(data)
    
    def receive(self, length):
        return self.ser.read(length)
    
    def close(self):
        self.ser.close()

class TcpTransport(Transport):
    """Transport pour Ethernet/IP via Socket TCP."""
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(2.0)
        self.sock.connect((ip, port))
    
    def send(self, data):
        self.sock.send(data)
    
    def receive(self, length):
        return self.sock.recv(length)
    
    def close(self):
        self.sock.close()

class BaseReader:
    """Classe d'abstraction pour les lecteurs UHF."""
    def __init__(self, transport):
        self.transport = transport

    def inventory(self):
        """Retourne la liste des EPC détectés."""
        raise NotImplementedError

    def read_user_bank(self, epc, start, count):
        """Lit la banque USER et retourne une liste de mots (16-bit)."""
        raise NotImplementedError

class RU5417Reader(BaseReader):
    """Implémentation spécifique pour le lecteur RU5417."""
    
    def read_user_bank(self, epc, start, count):
        # 1. Construction de la trame binaire (simplifiée pour l'exemple SDK)
        # Note: Dans une version complète, on inclurait le calcul de CRC ici.
        
        # Exemple de simulation de lecture pour que le code client puisse être testé
        print(f"DEBUG: Lecture USER Bank sur {epc} (start={start}, count={count})")
        
        # Simulation de retour de calibration ISRA réaliste
        # Word 0: Hum, Word 1: Temp, Word 2/3: Cal Hum, Word 4/6: Cal Temp
        return [1500, 2400, 1000, 2000, 3000, 0, 2000] 
