# Modulos
from config import *
import logging
import traceback

# Serviços
from .core import record_analysed_listing_data

# Executa a análise e gravação dos dados
import time
import random
wait_for = list(range(30,120))
logger.info(f"Iniciado processamento do Condominio: {adress['idCondominio']} ")
try:
    record_analysed_listing_data(adress['logradouro'], adress['numero'], adress['idCondominio'])
except Exception as excpt:
    error = f"{30*'---'}\nIdCondominio: {adress['idCondominio']}\nEndereço: {adress['logradouro']},{adress['numero']}\nDescrição da exceção: {excpt}. \n\n Log: {traceback.format_exc()}"
    logger.critical(error)
time.sleep(random.choice(wait_for))