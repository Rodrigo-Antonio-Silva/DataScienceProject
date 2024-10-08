# Exerc�cio de Estat�stica B�sica

setwd("C:/Users/Rodrigo & Familia/Documents/R_Scripts")
getwd()

notas <- read.csv("Notas.csv", fileEncoding = "windows-1252")


# Exerc�cio 1

str(notas)
summary(notas)

# Exerc�cio 2

meana <- mean(notas$TurmaA) #66.11111
meanb <- mean(notas$TurmaB) #61.61111

#Exerc�cio 3

sda <- sd(notas$TurmaA) #14.4828
sdb <- sd(notas$TurmaB) #6.184791

#R: Turma A que tem o maior desvio padr�o


#Exerc�cio 4
cva <- sda / meana * 100 
print(cva) #21.90676
cvb <- sdb / meanb * 100
print(cvb) #10.03843


#Exerc�cio 5
moda <- function(v){
  valor_u = unique(v)
  valor_u[which.max(tabulate(match(v, valor_u)))]
}

res <- moda(notas$TurmaA)
print(res) # Moda Turma A = 82

resB <- moda(notas$TurmaB)
print(resB) # Moda Turma B = 60




