import statistics
import scipy.stats

# Questão 11:

# Declarando as amostras:

amostra01 = [0, 0, 2, 0, 1, 0, 0, 1, 1, 3]
amostra02 = [3, 4, 5, 1, 5, 3, 6, 1, 3, 9]
amostra03 = [1, 0, 14, 1, 4, 0, 8, 0, 4, 6]

# Calculando a Variancia de cada amostra:

varAmostra01 = statistics.variance(amostra01)
print("Variancia da Amostra 01:", round(varAmostra01, 3))
# output: 1.067

varAmostra02 = statistics.variance(amostra02)
print("Variancia da Amostra 02:", round(varAmostra02, 3))
# output: 5.778

varAmostra03 = statistics.variance(amostra03)
print("Variancia da Amostra 03:", round(varAmostra03, 3))
# output: 20.622

# Calculando o Desvio Padrão de cada amostra:

dvAmostra01 = statistics.stdev(amostra01)
print("\nDesvio Padrao da Amostra 01:", round(dvAmostra01, 3))

dvAmostra02 = statistics.stdev(amostra02)
print("Desvio Padrao da Amostra 02:", round(dvAmostra02, 3))

dvAmostra03 = statistics.stdev(amostra03)
print("Desvio Padrao da Amostra 03:", round(dvAmostra03, 3))

# Coeficiente de Variação == Distorção ??? (caso True, o codigo abaixo é válido):

cvAmostra01 = scipy.stats.skew(amostra01, bias=False)
print("\nCoef. Var. da Amostra 01:", round(cvAmostra01, 3))

cvAmostra02 = scipy.stats.skew(amostra02, bias=False)
print("Coef. Var. da Amostra 02:", round(cvAmostra02, 3))

cvAmostra03 = scipy.stats.skew(amostra03, bias=False)
print("Coef. Var. da Amostra 03:", round(cvAmostra03, 3))

# Questão 12:

serieEst = [1, 6, 6, 3, 7, 4, 10]

mediaSerieEst = statistics.mean(serieEst)
dvSerieEst = statistics.stdev(serieEst)
cvSerieEst = scipy.stats.skew(serieEst, bias=False)

print("\nMedia da serie estatistica:", round(mediaSerieEst, 3))
print("Desvio Padrao da serie estatistica:", round(dvSerieEst, 3))
print("Coef. Var. da serie estatistica:", round(cvSerieEst, 3))

# Questão 13:

salarios = [1190, 1190, 1190, 1230, 1230, 1230, 1370, 1370, 1370,
            1370, 1370, 1370, 2279, 2279, 2540, 2540, 3020, 3020]

# (a) - Salario mais frequente (moda):
print("\nSalario mais frequente: R$", statistics.mode(salarios))

# (b) - Salario medio dos funcionarios (média):
print("Media Salarial: R$", statistics.mean(salarios))

# (c) - Salario mediano dos funcionarios (mediana):
print("Salario mediano: R$", statistics.median(salarios))

# Questão 14:

numeracao = [36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37,
             37, 37, 37, 38, 38, 38, 38, 39, 39, 39, 39, 40, 40, 40]

print("\nMedia dos sapatos: Tamanho", statistics.mean(numeracao))
print("Mediana dos sapatos: Tamanho", statistics.median(numeracao))
print("Moda dos sapatos: Tamanho", statistics.mode(numeracao))

# Questão 15:

# Essa questão tem muita logica matematica envolvida, veja:

# Media2019 = (qtd. Gols)/(qtd. Partidas) -> 2,9 = (qtd. Gols)/(90)

print("\nQuant. Gols em 90 jogos em 2019:", 2.9 * 90)
# output: 261

print("Agora, na 8 rodada de 2020, temos", 2.525*80, "gols marcados")
# output: 202

print("Portanto, na 9 rodada, devem ser feitos",
      261 - 202, "gols para igualar a media de 2019")

# Questão 16:

# A mediana é dada por:

mediana = 8 + (((20/2) - 5) * 4)/(16)
print("\nResultado da mediana:", mediana)
