import argparse

def read_user_cli_args():

    parse = argparse.ArgumentParser(
        prog= "sitechecker", description="Verifica a disponibilidade da URL"
    )
    parse.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="insira uma ou mais URLs",
    )
    parse.add_argument(
        "--file",
        metavar="paths",
        nargs="+",
        type=str,
        default=[],
        help="insira o caminho do arquivo"
    )
    return parse.parse_args()

def display_check_result(result, url, error=""):
    """Mostra o resultado do teste de conexão."""

    print(f'O status da "{url}" é:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Erro: "{error}"')