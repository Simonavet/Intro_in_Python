#functie = def
# nu trebuie sa spunem ce return type are
# def printGreeting():
#     print('Buna ziua! Bine ati venit!')
#
# def printGreetingByName(nume, prenume):
#     print(f'Buna ziua {nume} {prenume}')
#
# def mediaNr(a, b, c):
#     return (a + b + c) / 3
#
# def piValue():
#     return 3.14
# orice cod dupa return nu se citeste

#exercitiu
# daca pers e majora, altfel false
# def verificareMajor(varsta):
#     if varsta>=18:
#         return True
#     else:
#         return False
#
#
#
# # zona de apelare (desktop)
# printGreeting()
# printGreeting()
# printGreetingByName('S', 'Andy')
# printGreetingByName('S', 'Crina')
# printGreetingByName('S', 'Ares')
# print(mediaNr(3, 3, 4))
# print(piValue())
# print(verificareMajor(18))
#
# # se ia varsta utilizatorului
# age = int(input('introduceti varsta dvs'))
# if verificareMajor(age):
#     print('cont creat. bine ai venit in aplicatie')
# else:
#     print('nu ai varsta minima necesara')

# exercitiu facut de mine
def printGreeting():
    print('Buna seara catel!')
def printGreetingByName(nume, prenume):
    print(f'buna seara {nume} {prenume}')

printGreeting()
printGreetingByName('jessy', 'hassanein')

def mediaNumerelor(x, y, z, w):
    return (x + y + z + w)/4
print(mediaNumerelor(1, 2, 3, 4))
