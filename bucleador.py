#dos lineas agregadas especificamente
#para un nuevo branch en git . no afecta en nada al codigo
def run():
    contador = 0
    while contador < 1000 :
        print ('2 elevado a ' + str(contador) + ' es igual a ' + str(2 ** contador))
        contador = contador + 1
    


if __name__ == '__main__':
    run()
    
    #esta linea es agregada via GitHub
