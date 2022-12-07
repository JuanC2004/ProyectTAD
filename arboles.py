from collections import defaultdict
from node import Nodo

class arbol:
    def __init__ (self):
        self.raiz = None
        self.recorrido = []

    def recursive_add (self, nodo:Nodo, valor):
        if self.raiz == None:
            self.raiz = Nodo(valor)
        elif valor <nodo.valor:
            if nodo.izquierda == None:
                nodo.izquierda = Nodo(valor)
            else:
                self.recursive_add(nodo.izquierda, valor)
        else:
            if nodo.derecha == None:
                nodo.derecha = Nodo(valor)
            else:
                self.recursive_add(nodo.derecha , valor)
        
    def search(self, nodo:Nodo, search_value):
        if nodo == None:
            return
        elif nodo.valor == search_value:
            return nodo
        if search_value < nodo.valor:
            return self.search(nodo.izquierda, search_value)
        else:
            return self.search(nodo.derecha, search_value)
        
    def add (self, valor):
        self.recursive_add(self.raiz, valor)
    
    def inorder(self):
        arreglo = []
        def recorrido(node:Nodo):
            if node != None:
                recorrido(node.izquierda)
                arreglo.append(node.valor)
                recorrido(node.derecha)
        recorrido(self.raiz)
        self.recorrido = arreglo

    def preoreder(self):
        arreglo = []
        def recorrido(node:Nodo):
            if node != None:
                arreglo.append(node.valor)
                recorrido(node.izquierda)
                recorrido(node.derecha)
        recorrido(self.raiz)
        self.recorrido = arreglo
    
    def postorder(self):
        arreglo = []
        def recorrido(node:Nodo):
            if node != None:
                recorrido(node.izquierda)
                recorrido(node.derecha)
                arreglo.append(node.valor)
        recorrido(self.raiz)
        self.recorrido = arreglo
    
    def amplitud(self):
        #Creacion del manejo de los datos
        route = defaultdict(list) 
        #Funcion que añade los valores al manejo de los datos
        def dfs(nodo:Nodo, level):
            route[level].append(nodo.valor)
            #Funcion recursiva por cada hijo
            if nodo.izquierda != None:
                dfs(nodo.izquierda, level+1)
            if nodo.derecha != None:
                dfs(nodo.derecha , level+1)
        
        #Primer llamado recursivo
        dfs(self.raiz,0) 
        self.recorrido = [ans for k, ans in sorted(route.items())]
        return [ans for k, ans in sorted(route.items())]