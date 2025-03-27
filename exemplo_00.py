# Importando bibliotecas nativas
from sys import stderr

# Importando libs de terceiros
from loguru import logger

# Importando módulos
from decorador_inutil import hello
from time_decorator import time_decorator
from utils_log import log_decorator

# Adiciona o log com o handler padrão do logger em um arquivo
logger.add("meu_log.log", level="CRITICAL")

# Remove o handler padrão do logger, sem ele seria reproduzido
# no terminal o logger.add() e logger.info() da função
logger.remove()

# Configura logs personalizados para reprodução em terminal e
# armazenamento em arquivos
logger.add(sink=stderr, format="{time} <r>{level}</r> <g>{message}</g> {file}", level="INFO")
logger.add(sink="meu_arquivo_de_logs.log", format="{time} {level} {message} {file}", level="INFO")


""" def soma(x, y):
    try:
        soma = x + y
        # Mostra no terminal o handler padrão info
        logger.info(f"Você digitou valores corretos, soma = {soma}")
        return soma
    except Exception:
        # Mostra no terminal o handler padrão critical
        logger.critical("Você tem que digitar valores corretos!") """


@log_decorator
def soma_1(x, y):
    return x + y


# Chamadas da função decorada
soma_1(2, 3)
soma_1(100, 5)
soma_1(2, "y")  # Esta chamada causará uma exceção


@hello
def soma_2(x, y):
    return x + y


soma_2(2, 3)


@time_decorator
def soma_3(x, y):
    return x + y


soma_3(2, 3)
