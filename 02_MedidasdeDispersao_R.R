#Estatística Básica 

#Parte 02 - Medidas de Dispersão

#Definindo pasta de trabalho
#Substitua o caminho abaixo pela pasta no seu pc

setwd("C:/Users/Rodrigo & Familia/Documents/R_Scripts")
getwd()

#Carregando Dataset
vendas <- read.csv("vendas.csv", fileEncoding = "windows-1252")

#Resumo do Dataset
View(vendas)
str(vendas)
summary(vendas$Valor)

#Variancia
var(vendas$Valor)

#Desvio Padrao
sd(vendas$Valor)
