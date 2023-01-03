#listele in python pot sa cuprinda elemente de tipuri diferite
#au dimensiune dinamica
fructe = ['mar', 'banana', 'portocala', 3, True, 3]

#afisam o lista
print(fructe)

#accesam un element in functie de index
print(fructe[1])

#adaugam un element
fructe.append('rosie')

#suprascriem
fructe[0] = 'para'

#afisam lista
print(fructe)

#aflam dimensiune
print(len(fructe))

# scoate si ne returneaza ultimul elemet
last = fructe.pop()
print(last)
print(fructe)
#sau
print('ultimul element:', last)
print('lista:', fructe)

# de cate ori apare un element
print(fructe.count(3))

# extindem o lista cu o alta lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)