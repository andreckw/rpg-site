import os
from dotenv import load_dotenv

load_dotenv()

class EnvVariables:
    """
        Contem as Variaveis do .env

        ambiente: 0 = DEV; 1 = PROD
        nome: Nome do app
        secret_key: nao mostre para ngm :b
    """

    ambiente = int(os.environ.get("AMBIENTE"))
    nome = os.environ.get("NOME")
    secret_key = os.environ.get("SECRET_KEY")
    rota_prod = os.environ.get("ROTA_PROD")
