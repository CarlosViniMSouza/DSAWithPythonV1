import statistics
import scipy.stats

# Questão 11:

# Declarando as amostras:

amostra01 = [0, 0, 2, 0, 1, 0, 0, 1, 1, 3]
amostra02 = [3, 4, 5, 1, 5, 3, 6, 1, 3, 9]
amostra03 = [1, 0, 14, 1, 4, 0, 8, 0, 4, 6]

# Calculando a Variancia de cada amostra:

print("Variancia da Amostra 01:", round(statistics.variance(amostra01), 3))
print("Variancia da Amostra 02:", round(statistics.variance(amostra02), 3))
print("Variancia da Amostra 03:", round(statistics.variance(amostra03), 3))

# Calculando o Desvio Padrão de cada amostra:

print("\nDesvio Padrao da Amostra 01:", round(statistics.stdev(amostra01), 3))
print("Desvio Padrao da Amostra 02:", round(statistics.stdev(amostra02), 3))
print("Desvio Padrao da Amostra 03:", round(statistics.stdev(amostra03), 3))

# Coeficiente de Variação == Distorção ??? (caso True, o codigo abaixo é válido):

print("\nCoef. Var. da Amostra 01:", round(
    (statistics.stdev(amostra01)/statistics.mean(amostra01))*100, 3))
print("Coef. Var. da Amostra 02:", round(
    (statistics.stdev(amostra02)/statistics.mean(amostra02))*100, 3))
print("Coef. Var. da Amostra 03:", round(
    (statistics.stdev(amostra02)/statistics.mean(amostra02))*100, 3))

# removendo da memoria as listas da questão 11:
del amostra01, amostra02, amostra03

# Questão 12:

serieEst = [1, 6, 6, 3, 7, 4, 10]

print("\nMedia da serie estatistica:", round(statistics.mean(serieEst), 3))

print("Desvio Padrao da serie estatistica:",
      round(statistics.stdev(serieEst), 3))

print("Coef. Var. da serie estatistica:", round(
    (statistics.stdev(serieEst)/statistics.mean(serieEst))*100, 3))

# removendo da memoria as listas da questão 12:
del serieEst

# Questão 13:

salarios = [1190, 1190, 1190, 1230, 1230, 1230, 1370, 1370, 1370,
            1370, 1370, 1370, 2279, 2279, 2540, 2540, 3020, 3020]

# (a) - Salario mais frequente (moda):
print("\nSalario mais frequente: R$", statistics.mode(salarios))

# (b) - Salario medio dos funcionarios (média):
print("Media Salarial: R$", statistics.mean(salarios))

# (c) - Salario mediano dos funcionarios (mediana):
print("Salario mediano: R$", statistics.median(salarios))

# removendo da memoria a lista da questão 13:
del salarios

# Questão 14:

numeracao = [36, 36, 36, 36, 36, 37, 37, 37,
             37, 37, 37, 37, 37, 37, 38, 38,
             38, 38, 39, 39, 39, 39, 40, 40, 40]

print("\nMedia dos sapatos: Tamanho", statistics.mean(numeracao))
print("Mediana dos sapatos: Tamanho", statistics.median(numeracao))
print("Moda dos sapatos: Tamanho", statistics.mode(numeracao))

# removendo da memoria a lista da questão 13:
del numeracao

# Questão 15:

# -> Essa questão tem muita logica matematica envolvida, veja:

# Media2019 = (qtd. Gols)/(qtd. Partidas) -> 2,9 = (qtd. Gols)/(90)
print("\nQuant. Gols em 90 jogos em 2019:", 2.9 * 90)

# Quant. Gols (em 2020) = Media * Quant. Partidas
print("Agora, na 8 rodada de 2020, temos", 2.525*80, "gols marcados")

print("Portanto, na 9 rodada, devem ser feitos",
      261 - 202, "gols para igualar a media de 2019")

# Questão 16:

# A media é dada por:
print("\nResultado da media:", 184/20)

# A mediana é dada por:
print("Resultado da mediana:", 8 + (((20/2) - 5) * 4)/(16))

# Questão 17:

# A media é dada por:
print("\nResultado da media:", 700/100)

# A mediana é calculada por:
print("Resultado da mediana:", 5 + (((100)/2 - 20) * 5)/(50))

# Questão 18:

print("Resultado da Variancia:", (1/(200 - 1)) *
      ((2.204 * (10 ** 8)) - ((0.00206 * (10 ** 8)) ** 2)/200))

print("Resultado do Coef. Variacao:", round((203.24/1030)*100, 3))
