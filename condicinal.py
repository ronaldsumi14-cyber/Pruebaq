# sentencia if
temperatura = int(input("indicar la temperatura:"))
if temperatura > 28:
    print("esta haciendo calr:")
else:
    print("hace frio")

if temperatura > 28:
    print("esta haciendo calr:")
elif temperatura > 20:
    print("un dia agradable")
elif temperatura > 10:
    print("hace un pco de frio")
else:
    print("hace frio , brbrbrr")

print ("proceso concluido:")