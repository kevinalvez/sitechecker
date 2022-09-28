Este programa tem como função checar a disponibilidade de um site (Online ou Offline)

Passos de Execução:

1º Passo

Verificar dependências e libs no arquivo requirements.txt*
*Utilização do Venv

2º Passo

Execução do arquivo __main__.py via terminal com os seguintes comandos:

Python3* -m sitechecker --url
    Comando que verifica uma url digitada diretamente no terminal.
    Exemplo: Python3* -m sitechecker --url google.com

Python3* -m sitechecker --file
    Comando que recebe um arquivo do tipo .csv e verifica a disponibilidade de todos os sites descritos no arquivo
    Exemplo Python3* -m sitechecker --file sites.csv

*Versão do python utilizada durante a construção.