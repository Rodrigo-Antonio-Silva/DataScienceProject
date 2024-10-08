# Estat�stica B�sica

# Parte 3 - Medidas de dispers�o

# Cuidado: A linguagem R � case sensitive

# Definindo pasta de trabalho

setwd("C:/Users/Rodrigo & Familia/Documents/R_Scripts")
getwd()

# Carregando o dataset
vendas <- read.csv("vendas.csv", fileEncoding = "windows-1252")

# Resumo dos dados
head(vendas)
tail(vendas)
View(vendas)

# Medidas de tendencia central
summary(vendas$Valor)
summary(vendas[c('Valor', 'Custo')])

# Explorando variaveis numericas
mean(vendas$Valor)
median(vendas$Valor)
quantile(vendas$Valor)
quantile(vendas$Valor, probs = c(0.01, 0.99))
quantile(vendas$Valor, seq(from= 0, to= 1, by=0.20))
IQR(vendas$Valor) # Diferen�a entre Q3 e Q1
range(vendas$Valor)
summary(vendas$Valor)
diff(range(vendas$Valor))






