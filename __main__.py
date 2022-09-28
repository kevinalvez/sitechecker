import sys
import pandas as pd
import csv

from sitechecker.checker import site_is_online
from sitechecker.cli import read_user_cli_args, display_check_result



def main():
    """Run Site Checker."""
    user_args = read_user_cli_args()
    if len(user_args.urls) < 1:  
        urls = read(user_args.file)
    #read(user_args.file)
    else:
        urls = user_args.urls 

    if not urls:
        print("Erro: sem URLs para analisar.", file=sys.stderr)
        sys.exit(1)
    _site_check(urls)

def read(file):
    print(type(file))
    for i in file:
        ficheiro =  open(i, 'rt')
        reader = csv.reader(ficheiro)
        for linha in reader:
            _site_check(linha)

def _site_check(urls):

    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

if __name__ == "__main__" :
    main()