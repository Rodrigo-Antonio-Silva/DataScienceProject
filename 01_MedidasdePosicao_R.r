setwd("C:/Users/Rodrigo & Familia/Documents/R_Scripts")
getwd()

vendas <- read.csv("Vendas.csv", fileEncoding = "windows-1252")

#View(vendas)
#str(vendas)
#summary(vendas$Valor)
summary(vendas$Custo)