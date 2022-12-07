class Stack:
    def __init__(self, lista):
        self.pila = lista
        self.head = self.pila[len(self.pila)-1]
        
    def agregar(self, card):
        self.head = card
        self.pila.append(card)
    
    def eliminar(self):
        if len(self.pila) == 0:
            return
        elif len(self.pila) == 1:
            self.pila.pop()
            self.head = None
        else:
            self.pila.pop()
            self.head = self.pila[len(self.pila)-1]
            
    def ganador(self, lista:list):
        if self.pila == lista:
            return True
        else:
            return False