'''
Condiçoes compostos
exemplo :
     intervalo numerico
     
     0<= x and x < 100

Operadores logicos

not

and

or

'''
n1 = float(input('n1:'))
n2 = float(input('n2:'))
n3 = float(input('n3:'))
m = (n1+n2+n3)/3

'''
Notaçao simples
'''
'''
if m<=0 and m<3:
    print('reprovado')
    
else :    
    if m<=3 and m<7 :
        print('recuperaçao')
    
    else:
        print('aprovado')
'''
'''
Notaçao ELIF
'''
if 0<=m and m<3:
    print('reprovado')
elif 3<=m and m<7:
    print('recuperaçao')
else:
    print('aprovado')


    

    




