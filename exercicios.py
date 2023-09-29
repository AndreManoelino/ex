#Importando Bibliotecas para chamadas do arquivo e dos comandos a serem executados posteriormente.

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
#arquivo chamado (arquivo pego na api kagle para realizar analise de dados para correção dos exercícios)
data = pd.read_csv('/content/AB_NYC_2019 (1).csv')
