# TAD LISTA

def createList() -> list:
    #Crea una list vacia
    list=[]
    return list

def addToList(list,elem):
    #Agrega un elemento al final de la list
    list.append(elem)

def removePosList(list,pos):
    list.pop(pos)

def removeElemList(list,elem):
    list.remove(elem)

def sortList(list):
    list.sort()

def clearList(list):
    list.clear()

def reverseList(list):
    list.reverse()

def copyList(list1):
    return list1.copy()

def countElemList(list, elem):
    return list.count(elem)

def isEmpty(list):
    #Retorna Verdadero si la list no tiene elementos
    return len(list)==0

def size(list) -> int:
    #Retorna la cantidad de elementos de la list
    return len(list)

def exists(list, elem):
    #Retorna True o False si el producto "prod" pertenece al supermercado
    return elem in list
