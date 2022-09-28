from http.client import HTTPConnection
from tkinter import E
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    """Retorna True se estiver online e trata exceptions"""

    #erro genérico
    error = Exception("Algo errado no procedimento!")

    #define URL e busca o host
    parse = urlparse(url)
    host = parse.netloc or parse.path.split("/")[0]

    #Loop portas 80 e 443 (HTTP e HTTPS)
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e 
        finally:
            connection.close()
    raise error