import json
import sys
def leer(ruta):
    llista=[]
    with open(ruta,'r') as arxiu:
        contingut = arxiu.readline()
        while contingut != "":
            contingut = arxiu.readline()
            if contingut != "":
                camps_contingut = contingut.split(",")
                id = camps_contingut[0]
                nom = camps_contingut[1]
                cognoms = camps_contingut[2].strip()
                alumne = {"id":id,
                           "nom":nom,
                           "cognoms":cognoms}
                llista.append(alumne)
    return llista

def escribir(ruta_json,llista):
    with open(ruta_json,'w') as arxiu:
        contingut = json.dumps(llista, indent=4)
        arxiu.write(contingut)
        
        
def main(ruta_csv,ruta_json):
    info_alumnes = leer(ruta_csv)
    escribir(ruta_json,info_alumnes)
    
if __name__ == "__main__":
    parametro1 = sys.argv[1]
    parametro2 = sys.argv[2]
    main(parametro1,parametro2)