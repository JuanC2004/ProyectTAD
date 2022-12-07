from re import T
from imagenes import Imagen
from botones import *
from pygame import *
from casos import *
import sys
import pygame as pg


class game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.SCREEN = pg.display.set_mode((self.width, self.height))
        self.poker = poker(self.SCREEN, self.width, self.height)
        self.arbol = arbol(self.SCREEN, self.width, self.height)
        self.grafo = grafo(self.SCREEN, self.width, self.height)
        
    def run(self):
        pg.init()
        pg.time.Clock().tick(60)
        btn_solitario = boton(self.width - 160, self.height-240, 150, 50, 'SOLITARIO')
        btn_arbol = boton(self.width - 160, self.height-180, 150, 50, 'ARBOL')
        btn_grafo = boton(self.width - 160, self.height - 120, 150, 50, 'GRAFOS')
        btn_menu = boton(self.width - 160, self.height-60, 150, 50, 'MENU')

        self.fondo_pantalla()
        while True:
            '''Eventos'''
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if btn_solitario.rectangulo.collidepoint(pg.mouse.get_pos()):
                        self.poker.active = True
                        self.arbol.active = False
                        self.grafo.active = False
                    if btn_arbol.rectangulo.collidepoint(pg.mouse.get_pos()):
                        self.arbol.active = True
                        self.poker.active = False
                        self.grafo.active = False
                    if btn_menu.rectangulo.collidepoint(pg.mouse.get_pos()):
                        self.poker.active = False
                        self.arbol.active = False
                        self.grafo.active = False
                        self.run()
                    if btn_grafo.rectangulo.collidepoint(pg.mouse.get_pos()):
                        self.grafo.active = True
                        self.arbol.active = False
                        self.poker.active = False
                self.poker.eventos(event)
                self.arbol.eventos(event)
                self.grafo.eventos(event)
            if self.poker.active:
                self.poker.draw()
            if self.arbol.active:
                self.arbol.draw()
            if self.grafo.active:
                self.grafo.draw()
            btn_solitario.draw(self.SCREEN)
            btn_arbol.draw(self.SCREEN)
            btn_menu.draw(self.SCREEN)
            btn_grafo.draw(self.SCREEN)
            pg.display.update()
    
    def fondo_pantalla(self):
        fondo = Imagen(0, 0, self.width, self.height, 'img/fondoprincipal.jpg', 0)
        temp = image.load(fondo.route)
        temp = pg.transform.scale(temp, (fondo.width, fondo.height))
        self.SCREEN.blit(temp, (fondo.x, fondo.y))


GAME = game(1000,800)
GAME.run()



    
