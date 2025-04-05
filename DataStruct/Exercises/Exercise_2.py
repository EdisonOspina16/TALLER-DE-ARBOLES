from DataStruct.Classes.BinaryTree import BinarySearchTree, Node
import json


def cargar_arbol(archivo="arbol_adivinanza.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró el archivo JSON.")
        exit()


def guardar_arbol(arbol, archivo="arbol_adivinanza.json"):
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(arbol, file, indent=2, ensure_ascii=False)


def recorrido_preorden(nodo):
    if "pregunta" in nodo:
        print(nodo["pregunta"])
        if "si" in nodo:
            recorrido_preorden(nodo["si"])
        if "no" in nodo:
            recorrido_preorden(nodo["no"])


arbol = cargar_arbol("arbol_adivinanza.json")
