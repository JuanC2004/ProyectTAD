import pygame as pg


class boton:
    def __init__(self, x,y,w,h, palabra):
        self.rectangulo = pg.Rect(x,y,w,h)
        self.palabra = palabra
        self.activo = False
    
    def dibujar(self, SCREEN):
        fuente = pg.font.Font(None, 18)
        if self.rectangulo.collidepoint(pg.mouse.get_pos()):
            pg.draw.rect(SCREEN, (45, 56, 58), self.rectangulo, 0)
        else:
            pg.draw.rect(SCREEN, (95,120,122), self.rectangulo, 0)
        txt = fuente.render(self.palabra, True, (0,0,0))
        SCREEN.blit(txt, (self.rectangulo.x+(self.rectangulo.width-txt.get_width))/2,self.rectangulo.y+(self.rectangulo.height-txt.get_height)) 
        