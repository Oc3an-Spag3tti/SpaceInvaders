import pygame
import random  # necessaire pour charger les images et les sons

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 0.3

    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
           self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"

class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse = 5
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse 
        
        if self.hauteur < 0:
            self.etat = "chargee"

class Ennemi() :
    def __init__(self):
        self.depart = random.randint(0, 740)
        self.hauteur = 0
        self.type = random.randint(1,2)
        if self.type == 1:
         self.image = pygame.image.load('invader1.png')
         self.vitesse = 0.1
        if self.type == 2:
            self.image = pygame.image.load('invader2.png')
            self.vitesse = 0.2
    for i in range(10):
        NbEnnemis = i
    def avancer(self):
        self.hauteur += self.vitesse
        
                    
        
        
            
        