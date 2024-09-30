"""23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;

[169]

d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles."""


from arbol_avl import BinaryTree
arbol = BinaryTree()

datos = [
    {'name': 'Ceto', 'derrotado': None},
    {'name': 'Tifon', 'derrotado': 'Zeus'},
    {'name': 'Equidna', 'derrotado': 'Argos Panoptes'},
    {'name': 'Dino', 'derrotado': None},
    {'name': 'Pefredo', 'derrotado': None},
    {'name': 'Enio', 'derrotado': None},
    {'name': 'Escila', 'derrotado': None},
    {'name': 'Caribdis', 'derrotado': None},
    {'name': 'Euriale', 'derrotado': None},
    {'name': 'Esteno', 'derrotado': None},
    {'name': 'Medusa', 'derrotado': 'Perseo'},
    {'name': 'Ladon', 'derrotado': 'Heracles'},
    {'name': 'Aguila del Caucaso', 'derrotado': None},
    {'name': 'Quimera', 'derrotado': 'Belerofonte'},
    {'name': 'Hidra de Lerna', 'derrotado': 'Heracles'},
    {'name': 'Leon de Nemea', 'derrotado': 'Heracles'},
    {'name': 'Esfinge', 'derrotado': 'Edipo'},
    {'name': 'Dragon de la Colquida', 'derrotado': None},
    {'name': 'Cerbero', 'derrotado': None},
    {'name': 'Cerda de Cromion', 'derrotado': 'Teseo'},
    {'name': 'Ortro', 'derrotado': 'Heracles'},
    {'name': 'Toro de Creta', 'derrotado': 'Teseo'},
    {'name': 'Jabali de Calidon', 'derrotado': 'Atalanta'},
    {'name': 'Garcinos', 'derrotado': None},
    {'name': 'Gerion', 'derrotado': 'Heracles'},
    {'name': 'Cloto', 'derrotado': None},
    {'name': 'Laquesis', 'derrotado': None},
    {'name': 'Atropos', 'derrotado': None},
    {'name': 'Minotauro de Creta', 'derrotado': 'Teseo'},
    {'name': 'Harpias', 'derrotado': None},
    {'name': 'Argos Panoptes', 'derrotado': 'Hermes'},
    {'name': 'Aves de Estinfalo', 'derrotado': None},
    {'name': 'Talos', 'derrotado': 'Medea'},
    {'name': 'Sirenas', 'derrotado': None},
    {'name': 'Piton', 'derrotado': "Apolo"},
    {'name': 'Cierva de Cerinea', 'derrotado': None},
    {'name': 'Basilisco', 'derrotado': None},
    {'name': 'Jabali de Erimanto', 'derrotado': None},

]

for criatura in datos:
    arbol.insert_node(criatura['name'], {'derrotado': criatura['derrotado']})

print("-----------------------")
arbol.inorden_add_field()


print("-----------------------")
print("a. listado inorden de las criaturas y quienes las derrotaron:")
dic_ranking = {}
arbol.inorden_ranking(dic_ranking)
print(dic_ranking)
print("-----------------------")

print("c. información de la criatura Talos:")
talos_info = arbol.search('Talos')
if talos_info:
    print("NOMBRE:", talos_info.value)
    print("DERROTADO POR:", talos_info.other_values['derrotado'])
print("-----------------------")

def order_por(item):
    print(item)
    return item[1]
dic_ranking = {}
arbol.inorden_ranking(dic_ranking)
ordenados = list(dic_ranking.items())
ordenados.sort(key=order_por, reverse=True)
print("-----------------------")
print("d. 3 dioses que derrotaron a mayor cantidad de criaturas")
print(ordenados[:3])
print("-----------------------")

print("e. Criaturas derrotadas por Heracles:")
heracles_derrotas = []
for criatura in datos:
    if criatura['derrotado'] == 'Heracles':
        heracles_derrotas.append(criatura['name'])
print(heracles_derrotas)


print("-----------------------")


print("f. criaturas que no han sido derrotadas:")
criaturas_no_derrotadas = [criatura['name'] for criatura in datos if criatura['derrotado'] is None]
print(criaturas_no_derrotadas)


print("-----------------------")



arbol.delete_node('Basilisco')
arbol.delete_node('Sirenas')
print("j. el Basilisco y a las Sirenas han sido eliminados. ")


print("-----------------------")


#k.
aves_del_estinfalo = arbol.search('Aves de Estinfalo')
if aves_del_estinfalo:
    aves_del_estinfalo.other_values['derrotado'] = 'Heracles'

value = ('Ladon')
pos = arbol.search(value)
if pos:
    is_hero = pos.other_values
    arbol.delete_node(value)
    new_value = ('Ladon Dragon')
    arbol.insert_node(new_value, is_hero)
    print('l. Ladon ha sido modificado por Ladon Dragon')
else:
    print('no esta')


print("m. listado por nivel del árbol:")
arbol.by_level()

#n
print("n. Criaturas capturadas por Heracles:")
heracles_capturados= arbol.search_by_coincidence('Heracles')
print(heracles_capturados)