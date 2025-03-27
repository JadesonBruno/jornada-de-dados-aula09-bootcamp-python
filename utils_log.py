# Importando bibliotecas nativas
from functools import wraps
from sys import stderr

# Importando bibliotecas de terceiros
from loguru import logger

# Exemplo de uso do logger
# logger.info("Este é um log de informação.")
# logger.error("Este é um log de erro.")

# Configuração do logger para exibir logs no stderr e salvar em arquivo,
# com filtragem e formatação específicas

logger.remove()  # Remove handler padrão

logger.add(sink=stderr, format="{time} <r>{level}</r> <g>{message}</g> {file}", level="INFO")

logger.add("meu_arquivo_de_logs.log", format="{time} {level} {message} {file}", level="INFO")  # Arquivo onde os logs serão salvos

logger.add("meu_arquivo_de_logs_critical.log", format="{time} {level} {message} {file}", level="ERROR")  # Arquivo onde os logs serão salvos


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise e

    return wrapper


""" @log_decorator
def dividir(a, b):
    return a / b

dividir(10,0) """
