from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import warnings
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
service = Service()  
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # Apenas para erros de log
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.climatempo.com.br/" 
driver.get(url)

time.sleep(5)

today = datetime.now().strftime("%d/%m/%Y") # Obter a data atual
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y") # Obter a data de amanhã
after_tomorrow = (datetime.now() + timedelta(days=2)).strftime("%d/%m/%Y") # Obter a data de depois de amanhã

elements = driver.find_elements(By.XPATH, '//p[contains(@class, "-gray") and contains(@class, "_flex") and contains(@class, "_align-center")]') # Capturando o elemento do HTML da pagina do clima tempo
tempsToday = elements[0].text
tempsTomorrow = elements[1].text
tempsAfterTomorrow = elements[2].text


def format_temperature(): # Função para criar o Dataframe em pandas 
    global df
    dictDF = { # Criando o dicionário com as temperaturas mínimas e máximas
        "Temperatura Mínima": [tempsToday[:3].replace("°", ""), tempsTomorrow[:3].replace("°", ""), tempsAfterTomorrow[:3].replace("°", "")], # Retirando º para converter em int para o matplotlib fazer o gráfico 
        "Temperatura Máxima": [tempsToday[-3:].replace("°", ""), tempsTomorrow[-3:].replace("°", ""), tempsAfterTomorrow[-3:].replace("°", "")] 
    }
    datas = [today, tomorrow, after_tomorrow]
    df = pd.DataFrame(dictDF, index=datas)




def plotar_grafico(): # Função para criar o gráfico
    df_int = df.astype(int) 
    ax = df_int.plot(kind='bar', figsize=(8, 5))
    plt.title("Previsão de Temperaturas")
    plt.ylabel("Temperatura (°C)")
    plt.xlabel("Data")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.legend()
    plt.show()


def menu(): # Função para o menu inicial
    S = 0
    while S == 0:
        
        print("\nMenu:")
        resposta = input("1 - Ver o clima dos próximos 3 dias \n2 - Ver Gráfico do clima \n3 - Sair\nEscolha uma opção: ")
        
        match resposta:
            case "1":
                os.system('cls') # Eu utilizei windows para este web-scraping, se for utilizar Linux substitua por 'clear'
                print("Gerando previsão de temperatura...")
                time.sleep(1)
                print("Clima dos próximos 3 dias:")
                print(df)                
            case "2":
                os.system('cls') # Eu utilizei windows para este web-scraping, se for utilizar Linux substitua por 'clear'
                print("Gerando gráfico...")
                print("Clima dos próximos 3 dias:")
                plotar_grafico()
            case "3":
                os.system('cls') # Eu utilizei windows para este web-scraping, se for utilizar Linux substitua por 'clear'
                print("Saindo...")
                S = 1
            case _:
                print("Opção inválida. Tente novamente.")

format_temperature()
driver.quit()
menu()