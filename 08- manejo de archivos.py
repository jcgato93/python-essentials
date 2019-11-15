

def writeFile():

    # si el archivo no existe lo crea 
    with open('numeros.txt','w') as f:
        for i in range(10):
            # sobre escribe el archivo
            f.write(str(i)+'\n')
        
    
    readFile()        


def readFile():
    with open('numeros.txt') as f:
        for line in f:
            print(line)
        

if __name__ == "__main__":
    writeFile()    