import pygame as pg

class elementos:
    def __init__(self):
        self.fuente = pg.font.Font(None,18)


class CuadroTxt:
    def __init__(self, nombre, l,t,w,h):
        self.nombre = nombre
        self.input = ""
        self.hitbox = pg.Rect(l,t,w,h)
        self.activo = False

    def dibujar_cuadro_texto(self, screen):
        fuente = pg.font.Font(None,24)
        text_surface = fuente.render(self.input, True, (0,0,0))
        if self.hitbox.collidepoint(pg.mouse.get_pos):
            pg.draw.rect(screen, (255,255,255),self.hitbox, 2)
        else:
            pg.draw.rect(screen, (0,0,0), self.hitbox, 2)
        screen.blit(text_surface, (self.hitbox.centerx - text_surface.get_width()//2, self.hitbox.centery - text_surface.get_height()//2))

    
class comboBox:
    def __init__(self, name, l, t, w, h):
        self.name = name
        self.opciones = []
        self.combo_rects = []
        self.tamaño = pg.Rect(l,t,w,h)
        self.item_seleccionado = self.name
        self.desplegado = False
    
    def desplegar(self, screen):
        fuente = pg.font.Font(None, 20)
        temp_rect = self.tamaño.copy()
        temp_text = fuente.render(self.item_seleccionado, True, (0,0,0))
        if temp_rect.collidepoint(pg.mouse.get_pos()):
            temp_rect = pg.draw.rect(screen, (255,255,255), self.tamaño, 2)
        else:
            temp_rect = pg.draw.rect(screen, (0,0,0), self.tamaño, 2)
        
        screen.blit(temp_text, (self.tamaño.centerx - temp_text.get_width()//2, self.tamaño.centery - temp_text.get_height()//2))
        if self.desplegado:
            yDelta = self.tamaño.height
            pg.draw.rect(screen, (255,255,255), (self.tamaño.x, self.tamaño.y + self.tamaño.height, self.tamaño.width, self.tamaño.height+ (len(self.opciones)-1)*yDelta),0)
            for i in range (len(self.opciones)):
                temp_rect.y += yDelta
                if len(self.combo_rects) < len(self.opciones):
                    self.combo_rects.append(temp_rect)
                if temp_rect.collidepoint(pg.mouse.get_pos()):
                    temp_rect = pg.draw.rect(screen, (0,255,0), temp_rect, 2)
                else:
                    temp_rect = pg.draw.rect(screen, (0,0,0), temp_rect, 2)
                temp_text = fuente.render(self.opciones[i],True,(0,0,0))
                screen.blit(temp_text, (temp_rect.centerx - temp_text.get_width()//2, temp_text.get_height()//2))

    def select_item(self):
        for option in self.combo_rects:
            if option.collidepoint(pg.mouse.get_pos()):
                self.item_seleccionado = self.opciones[self.combo_rects.index(option)]
                self.desplegado = False

