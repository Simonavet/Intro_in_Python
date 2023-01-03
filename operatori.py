#operatori:
#aritmetici: +, -, *, /, %
#de comparare: <, >, =, != (diferit), <=, >=
#logici: and, or, ! (not)

#Flow control - if else

a = 3
b = 5

print(a+b) # 3+5 => 8
print(a == b) # 3==5 => false
print(a<b and a < 4) # 3<5 true si 3<4 true => true
print(a<b or a < 2) # 3<5 true sau 3<2 false => true

# cu mama sau tata sau (cu bunicul si bunica)
mama = True
tata = False
bunicul = False
bunica = False
print(mama or tata or (bunicul and bunica))

mama = False
tata = False
bunicul = True
bunica = False
print(mama or tata or (bunicul and bunica))

mama = False
tata = False
bunicul = True
bunica = True
print(mama or tata or (bunicul and bunica))

mama = True
tata = True
bunicul = True
bunica = True
print(mama or tata or (bunicul and bunica))
