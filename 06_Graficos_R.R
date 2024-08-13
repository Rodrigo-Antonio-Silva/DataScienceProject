png("C:/Users/Rodrigo & Familia/Documents/R_Scripts/barplot.png", width = 480, height = 480)
# Estatística Básica

# Parte 5 - Gráfico

# Gráficos em R - BarPlot, Pie Chart, Line Chart, Scatter Plot, Histograma e Treemap
# http://www.r-graph-gallery.com/

# Mais detalhes no Curso visualização de Dados e Design de Dashboads
# http://www.datascienceacademy.com.br/pages/todos-os-cursos-dsa

# Definindo a pasta de trabalho
# Substitua o caminho abaixo pela pasta no seu computador

setwd("C:/Users/Rodrigo & Familia/Documents/R_Scripts")
getwd()

#Dados
vetor_total_resultados = c(3, 12, 5, 18, 45)
names(vetor_total_resultados) = c("A", "B", "C", "D", "E")
vetor_total_resultados

##### Barplot ####

?barplot
barplot(vetor_total_resultados)
barplot(vetor_total_resultados, col = c(1, 2, 3, 4, 5))

# Salvando o gráfico em disco
barplot(vetor_total_resultados, 
        col = rgb(0.5, 0.1, 0.6, 0.6),
        xlab = "Categorias",
        ylab = "Valores",
        main = "Barplot em R",
        ylim = c(0, 60) )
dev.off()

# Ggplot2
install.packages("ggplo2")
library(ggplot2)
View(mtcars)

# Barplot
ggplot(mtcars, aes(x = as.factor(cyl) )) +
  geom_bar()

ggplot(mtcars, aes(x= as.factor(cyl), fill = as.factor(cyl) )) +
  geom_bar() +
  scale_fill_manual(values = c("red", "green", "blue"))

# Criando dados dummy (fictícios)
dados = data.frame(group = c("A ", "B ", "C ", "D "), value = c(33, 62, 56, 67))

# Barplot
ggplot(dados, aes(x = group, y = value, fill = group)) +
  geom_bar(width = 0.85, stat = 'identity')

