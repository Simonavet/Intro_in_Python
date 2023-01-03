# specia = str(input('introdu specia'))
# respiratia = int(input('introdu valoarea'))
# if specia == 'vaca':
#     if respiratia < 30:
#         print('valoare scazuta')
#     elif respiratia <= 40:
#         print('valoare normala')
#     else:
#         print('valoare crescuta')
# elif specia == 'cal':
#     if respiratia < 20:
#         print('valoare scazuta')
#     elif respiratia <= 30:
#         print('valoare normala')
#     else:
#         print('valoare crescuta')
# else:
#     print('nu exista')

specia and respiratia = str+int('introdu specia si valoarea')
if specia == 'vaca' and respiratia < 30:
    print('valoare scazuta')
elif specia == 'vaca' and respiratia <= 40:
    print('valoare normala')
elif specia == 'vaca' and respiratia > 40:
    print('valoare crescuta')
elif specia == 'cal' and respiratia < 20:
    print('valoare scazuta')
elif specia == 'cal' and respiratia <= 30:
    print('valoare normala')
elif specia == 'cal' and respiratia > 30:
    print('valoare crescuta')
else:
    print('nu exista')

