#fazer o passo a passo

import pandas as pd

#passo 1: pegar a base de dados e importar, mesma pasta
tabela = pd.read_csv("telecom_users.csv")


#Passo 2: Vizualizar a base de dados


#filtrar informações

#entender as informações que você tem disponível

#corrigir os problemas da base de dados

#Passo 2.1: não tem colunas úteis, então o ideal é retirar

#(nome, eixo)
#axis=0 eixo para excluir linha, =1 exclui coluna
tabela = tabela.drop("Unnamed: 0", axis=1)

#display(tabela)

#passo 3: Tratamento de dados

#Passo 3.1: para fazer o tratamento, tem que saber os erros 

#Pensar como tratar (valores vazias, colunas vazias, linhas com valores vazios)

#Passo 3.2:Exibir
#print(tabela.info())
#20  Churn                   5985 non-null   object - um valor vazio
#21  Codigo                  0 non-null      float64 - todos vazios
#19  TotalGasto              5986 non-null   object - está reconhecendo como texto, mas é um valor numerico

#Passo 3.3: tranformar em numerico

#[nome da coluna] = to_numeric[quem quer transformar] e pode acontecer erros, então tem que dizer o que fazer se encontrar. Coerce deixa vazio quando da erro
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors = "coerce")


#TRATAR COLUNAS VAZIAS, COMPLETAMENTE VAZIA EXCLUIR, qual o impacto? Não são úteis

#how = "any" ou "all"
tabela = tabela.dropna(how ="all", axis = 1) #1 coluna completa ALL

#LINHAS COM VALORES VAZIOS(Imagina que tivesse na linha da coluna meses como clientes vazio, qual o impacto na base de dados? Seria dificil analizar ele)
#Todas as linhas que tiverem, pelo menos, um valor vazio vou jogar fora PORQUE EXISTE POUCOS VALORES VAZIOS PARA UMA BASE MT GRANDE

tabela = tabela.dropna(how = "any", axis = 0) #0 - linhas que tem algum valor vazio ANY

#print(tabela.info())


#Passo 4: Análise simples -> entender como estão acontecendo os cancelamentos

#26%

#26% de 5k de clientes é bastante para olhar de um a um e tem que verificar realmente a porcentagem

#analisar a coluna, contar os valores

print(tabela["Churn"].value_counts(normalize=True))#normalize é percentual

#Passo 5: Análise completa -> entender a causa dos cancelamentos/possíveis soluções
#é para criar histogramas
import plotly.express as px

#Para criar uma análise e mostrar:

#1 - cria o gráfico (px . tipo de grafico(a base de dados, o eixo x e a cor))
#entender os cancelamentos, então quer ver o que as colunas impactam a coluna de cancelamento churn

#grafico = px.histogram(tabela, x="TotalGasto", color = "Churn", color_discrete_sequence=["green", "red"]) #divisão de cor do total gasto com churn
                                                                #para mudar as cores
#2 - exibe/mostra o gráfico

#Mostra quanto as pessoas gastaram em vermelho quem cancelou e azul não cancelou

#Para criar todas colunas, criar processo automatizado
#PARA CADA COLUNA DA BASE DE DADOS VOU CRIAR UM GRAFICO COMPARANDO COM CANCELAMENTO
for coluna in tabela.columns: #para cada coluna dentro das colunas da minha tabela, coluna é um nome qualquer que o python reconhece pois fez tabela.columns
                              #se fosse analisar as linhas, trocaria o nome por linhas e tabela.rows
    grafico = px.histogram(tabela, x=coluna, color = "Churn")
    grafico.show() #mini dashboard, pode selecionar um periodo que quer analisar

    
    #######RELATÓRIO##########
#Comparar cada uma das colunas com os cancelamentos, procurando coisas que saltam os olhos
#ex comparar o azul com o vermelho entre dois grupos da mesma tabela

#em casado: tem um numero significativo menor que são solteiros

#uma pessoa n casada tende a cancelar mais

#em outra tabela, dependente: quem tem dependentes cancela mais dos que já possuem

#OBS FAMILIAS MAIORES TENDEM A CANCELAR MENOS
    #PODEMOS OFERECER UM SEGUNDO NÚMERO DE GRAÇA
    #FAMILIAS COM O MESMO PLANO DE CELULAR COM VARIAS PESSOAS, CANCELAM MENOS 
    
#Em meses como cliente: no primeiro mês, mais cancelam do que permanecem 
#No final do gráfico quanto mais tempo como cliente, menor a chance de cancelar
    #Como ação, da para bonificar o cliente nos primeiros 12 meses, ex planos de 12 meses são mais baratos
    #Nos primeiros meses os clientes cancelam muito, podemos estar com um problema no início
    #Podemos estar fazendo uma ação de marketing ruim
    
    
#Problemas no serviço da fibra
    #olhar mais a fundo o pqe

#QUANTO MENOS SERVIÇOS TEM, MAIOR A CHANCE DE CANCELAR
    #PODE OFERECER UM SERVIÇO EXTRA DE GRAÇA
    
#PODEMOS INCENTIVAR PAGAMENTO NO DÉBITO AUTOMÁTICO, TX DE CANCELAMENTOS MENORES
    #INCENTIVOS PARA CONTRATO ANUAL



get_ipython().system('pip install plotly')






