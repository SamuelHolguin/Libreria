# -*- coding: utf-8 -*-
class Libreria:

    f= open ('libros.txt','r')
    mensaje=f.read();
    infile=mensaje.split();
    nombres=[]
    paginas=[]
    for i in [0, 5, 10, 15, 20, 25, 30, 35, 40]:   
          nombres.append(infile[i]);              
    nombres.sort()
    nom = '\n'.join(nombres)
    for i in [3, 8, 13, 18, 23, 28, 33, 38, 43]:   
           paginas.append(infile[i]);
    paginas.sort()
    pag = '\n'.join(paginas)

    print ("Libreria: \n")
    print (mensaje)
    print ("\nOrganizados por nombres:")
    print (nom)
    print ("\nOrganizados por paginas:")
    print (pag)
