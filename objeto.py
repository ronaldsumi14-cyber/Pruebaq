#objeto range
num= range(5)
print(num)

for item in num:
    print (item)

for item in range(5,10):
    print(item)

for item in range(10,20,2):
    print(item)

# tuplas (inmutables)

nume=(1,2,5,4,5,6)
#imprimiendo un elemento
print(nume[3])
# ocurrencias
print(nume.count(5))

print(nume.index(5))