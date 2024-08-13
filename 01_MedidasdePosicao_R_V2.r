#Primairo código em R

setwd("C:/Users/Rodrigo & Familia/Documents/R_Scripts")
getwd()

vendas <- read.csv("Vendas.csv", fileEncoding = "windows-1252")

View(vendas)
str(vendas)
summary(vendas$Valor)
summary(vendas$Custo)

#Media
?mean
mean(vendas$Valor)
mean(vendas$Custo)

#Media Ponderada
?weighted.mean
weighted.mean(vendas$Valor, w = vendas$Custo)

#Mediana
?median
median(vendas$Valor)
median(vendas$Custo)

#Moda
moda <- function(v) {
  valor_u <- unique(v)
  valor_u[which.max(tabulate(match(v, valor_u)))]
}
resultado <- moda(vendas$Valor)
print(resultado)

resultado_custo <- moda(vendas$Custo)
print(resultado_custo)

#ggplot2
install.packages("ggplot2")
library(ggplot2)

#grafico
ggplot(vendas) +
  stat_summary(aes(x = Estado,
                   y = Valor),
               fun = mean,
               geom = "bar",
               fill = "lightgreen",
               col = "grey50") +
  labs(title = "Média de Valor por Estado")


