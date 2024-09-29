''' El modulo argparse es una herramienta de Python que facilita la creación de interfaces interactivas en la terminal. 
    Define los argumentos que se esperan que el usuario ingrese, además de proporcionar automáticamente mensajes de ayuda, 
    manejo de errores y validaciones.'''

import argparse                                                         # no es necesaria instalarla, pero si importarla

parser = argparse.ArgumentParser(prog='Programa para sumar enteros',            # inicializar parser con parametros de uso
                                 description='Sumar enteros',
                                epilog='')

parser.add_argument('Entero1', type=int,help='Primer numero para sumar') # método parser.add_argument() da especificaciones al argumento requerido
parser.add_argument('Entero2', type=int,help='Segndo numero para sumar')
# Pueden haber mas especificaciones de argumento: metavars,nargs,dest,const,choices,required,action,etc 

args = parser.parse_args()                                              # Coloca los argumentos en el objeto, para luego agregarlo a alguna fncion

def funcion(args):                                                      # funcion que tomara los argumentos 
    suma = args.Entero1 + args.Entero2
    print(f'la suma de {args.Entero1} + {args.Entero2} es {suma}')

funcion(args)                                                           # llamar a la funcion

''' Para ejecutar este ejemplo se abre una terminal y se escribe "python Ejemplo_argparse.py 5 5" 
    donde "5 5" son dos argumentos de ejemplo, si se escribe algun dato no entero abra un mensaje de argumento inválido.
    
    Tambien se puede ejecutar "python Ejemplo_argparse.py -h" el cual nos proporcionará mensajes útiles de ayuda '''