#exercitii pentru variabile si tipuri de date
# rasa = 'Malinois'
# varsta = 2
# print(f'Jessy este o fetita {rasa} de {varsta} ani')

# exercitii pentru operatori
# a = 6
# b = 4
# print(a+b)
# print(a-b)
# print(a==b)
# print(a>=b)
# print(5 + a - b)
# print(b<=a + 2)
# print(a!=b)
# print(a/b)
# print(a>b and 4>b)
# print(a>b or b>a)
# print(a<b and b>2)
# print(a<b or b>2)
# print(not(a>b))

# if_else
# persoana = 24
# if (persoana < 18):
#     print('nu are voie sa parieze')
# else:
#     print('poate paria')
#
# melodia = int(input('alege melodia'))
# if melodia == 1:
#     print('Good bye!')
# elif melodia == 2:
#     print('I love you')
# elif melodia == 3:
#     print('Welcome')
# elif melodia == 4:
#     print('Oh my heart')
# elif melodia == 5:
#     print('See you soon')
# else:
#     print('nu exista')

#liste
# plante = ['menta', 'patrunjel', 'marar', 12, True, 12]
# print(plante)
# print(plante[2])
# plante.append('lumanarica')
# print(plante)
# print(len(plante))
# print(plante.count(12))
# plante[5] = False
# print(plante)
# last = plante.pop()
# print(last)
# print(plante)
# plante.pop()
# print(plante)
# mirodenii = ['piper', 'boia', 'cuisoare']
# plante.extend(mirodenii)
# print(plante)

#dict
# animale = {'cal': 20, 'caine': 60, 'vaca': 30, 'pisica': 70}
# print(animale)
# print(animale.keys())
# print(animale.values())
# print(len(animale))
# print(animale.get('cal'))
# valoarea = int(input('introdu valoarea'))
# if valoarea == 20:
#     print('cal')
# elif valoarea == 60:
#     print('caine')
# elif valoarea == 30:
#     print('vaca')
# elif valoarea == 70:
#     print('pisica')
# else:
#     print('nu exista')

#while
# litri_apa = 5
# while litri_apa > 0:
#     print('curge')
#     litri_apa = litri_apa - 1
#     # if litri_apa <= 2:
#     #     print('gata')
# print('gata!')

#for
for i in range(1, 11):
    print(f'numarul {i}')

for i in range(1, 11, 3):
    print(f'num{i}')

numere = [2, 4, 6, 8, 10]
# for i in range(0, len(numere)):
#     print(f'numarul numerelor este {i}')
#     print(f'numarul este {numere[i]}')

# for each
# s=1
# for numar in numere:
#     print(f'valoarea este {numar}')
#     s= s + numar
#     print(f'suma este {s}')

# for (i==1; i<20; i == i+3):
#     print(i)
for i in range (1, 20, 3):
    print(i)


#String
planta = 'Busuioc'
#Integer
ziua = 26
#Float
metri_lungime = 152,50
#Boolean
lungimea_corecta = False


