# diccionarios -> almacenar a pares de clave valro
mi_dic ={'nombre':'bruno diaz','edad':'25','ciudad':'la paz'}
print(mi_dic)

#acceder a un valor 
print(mi_dic['nombre'])
print(mi_dic['edad'])
# agregar elementos

mi_dic['profesioc']= 'ingeniero'
print(mi_dic)
# eliminar un elemento
del mi_dic['ciudad']
print(mi_dic)
# obteer la claves del diccionario

print(mi_dic.keys())
# obtener valores del dic

print (mi_dic.values())

# verificar si una clave existe

if 'ciudad' in mi_dic:
    print("clave encontrada")

# recorrido de un diccionario
for clave,valor in mi_dic.items():
    print("[clave:]",clave,"[valor:]",valor)