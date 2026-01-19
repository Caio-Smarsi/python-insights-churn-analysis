
import pyautogui 
import time

# Guia rápido:
# 1. pyautogui.click - clica
# 2. pyautogui.write - escrever texto
# 3. pyautogui.press - apertar tecla
# 4. pyautogui.hotkey - apertar atalhos do teclado (hotkey) 


pyautogui.PAUSE = 0.5 # por padrão ele vem em 0 de pause  
link= 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' 

# passo 1 -  Entrar no sistema da empresa - abriria o navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter') 
# fazer uma pausa maior - carregar o site # import time -  natural python (biblioteca padrão)
time.sleep(3)

# passo 2 -  Fazer o login no sistema
pyautogui.click(x=847, y=373)
pyautogui.write('pythoninpressionador@gmail.com')
pyautogui.press('tab')          #Passar para o proximo campo
pyautogui.write('sua senha muito muito muito dificilima')
pyautogui.click(x=961, y=532)   #Clicar no Botão 'login'
# fazer uma pausa maior - carregar o site
time.sleep(3)

# passo 3 -  Abrir a base de dados (importar o arquivo para dentro do codigo)
# pip install pandas openpyxl
import pandas                   #usar ele para ler a base de dados

tabela= pandas.read_csv(r'C:\python\Developer_Ini\python-insights-churn-analysis\01_Automacao_e_Processos\produtos.csv') 
print(tabela)

# passo 4 - Cadastrar um Produto


for linha in tabela.index:     # Index (índice) - Percorrer a Tabela Pelas Linhas (linha 0, linha 1...)
    
    
    #Código do produto
    pyautogui.click(x=726, y=248)  # Clica no Primeiro Campo
    codigo= str(tabela.loc [linha, 'codigo'])

    pyautogui.write(codigo)
    pyautogui.press('tab')         # Passa Para o Prox Produto

    #Marca  MOUSE   
    marca= str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

    #Tipo do Produto
    tipo= str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    #Categoria do Produto
    categoria= str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    #Preço Unitário do Produto
    Preco_Uni= str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(Preco_Uni)
    pyautogui.press('tab')

    #Custo 
    custo= str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    #OBS
    obs= str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.click(x=881, y=908)  # Clicar No Enviar

# passo 5 - Copiar o Passo 4 Até Acabar a Lista




