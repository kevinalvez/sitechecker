import csv

def read():
    ficheiro =  open('sites.csv', 'rt')
    reader = csv.reader(ficheiro)
    for linha in reader:
        print(linha)

read()