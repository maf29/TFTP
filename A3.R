##    Ejercicio 1
#Datos:
RTT<-c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
# a)Muestra_RTT
mostraRTT <- c(205,198,121,150,127,176,183,167,223,150,239,165,147,150,156,102,240,193,161,162,169,180,108,118,142,212,150,150,150,150,150,150,150,150,150,150,150,150,83,127,168,136,223,171,192,170,209,107,163,248,218,242,244,194,54,73,86,198,86,56)

alfa = 0.125
beta = 0.25

#b) c) d)
estimadoRTT <- c()
estimadoRTT[1]<- mostraRTT[1]
desvRTT <- c()
desvRTT[1] <- mostraRTT[1]/2
TOut <- c()
TOut[1] <- estimadoRTT[1] + 4 * desvRTT[1]
i = 1
for(i in 2:length(mostraRTT)){
    estimadoRTT[i] <- (1 - alfa) * estimadoRTT[i-1] + alfa * mostraRTT[i]
    desvRTT[i] <- (1 - beta) * desvRTT[i-1] + beta * abs(mostraRTT[i]-estimadoRTT[i])
    TOut[i] <- estimadoRTT[i] + 4 * desvRTT[i]
}
representacion<-function(datos){
    plot( c(3,60), c(0,750), type = "n", xlab = "Tiempo",
          ylab="RTT", main = "Líneas temporales" )
    
    lines( datos$RTT,  datos$mostraRTT,
           lwd = 0.7,
           lty = 1,
           col = "blue",
           pch = 1 )
    lines( datos$RTT,  datos$estimadoRTT,
          lwd = 1.5,
          lty = 2,
          col = "darkorange1" )
    datos$TOut
    lines( datos$RTT, datos$TOut,
          lwd = 1.3,
          lty = 3,
          col = "green4")
    lines( datos$RTT,  datos$desvRTT ,
           lwd = 2,
           lty = 4,
           col = "pink")
    
    # leyenda
    legend( 10, 700, names(datos[2:5]), cex=0.5, col = c("blue", "darkorange1", "pink","green4" ),
            pch = 1:4, lty=1:4, title="Tratamiento: ", horiz = TRUE)
}

datos <- data.frame(RTT,mostraRTT, estimadoRTT, desvRTT, TOut)
representacion(datos)
#e) TOut sustituye el coeficiente 4 por los valores 3, 2 i 1
# coeficiente 3
TOut3 <- estimadoRTT + 3 * desvRTT
#representar
dat3 <- data.frame(RTT,mostraRTT, estimadoRTT, desvRTT, TOut3)
representacion(dat3)

# coeficiente 2
TOut2 <- estimadoRTT + 2 * desvRTT
#representar
dat2 <- data.frame(RTT,mostraRTT, estimadoRTT, desvRTT, TOut2)
representacion(dat2)

# coeficiente 1
TOut1 <- estimadoRTT + 1 * desvRTT
#representar
dat1 <- data.frame(RTT,mostraRTT, estimadoRTT, desvRTT, TOut1)
representacion(dat1)

##    Ejercicio 2
mostra <- sample(100:299,60,replace=F)
estimado <- c()
estimado[1]<- mostra[1]
desv <- c()
desv[1] <- mostra[1]/2
TO <- c() #Time out
TO[1] <- estimado[1] + 4 * desv[1]
i = 1
for(i in 2:length(mostra)){
  estimado[i] <- (1 - alfa) * estimado[i-1] + alfa * mostra[i]
  desv[i] <- (1 - beta) * desv[i-1] + beta * abs(mostra[i]-estimado[i])
  TO[i] <- estimado[i] + 4 * desv[i]
}

dat <- data.frame(RTT,mostra, estimado, desv, TO)

plot( c(0,60), c(0,700), type = "n", xlab = "Tiempo",
      ylab="RTT", main = "Líneas temporales" )

lines( dat$RTT,  dat$mostra,
       lwd = 0.7,
       lty = 1,
       col = "blue",
       pch = 1 )
lines( dat$RTT,  dat$estimado,
       lwd = 1.5,
       lty = 2,
       col = "darkorange1" )
lines( dat$RTT, dat$TO,
       lwd = 1.3,
       lty = 3,
       col = "green4")
lines( dat$RTT,  dat$desv ,
       lwd = 2,
       lty = 4,
       col = "pink")

# leyenda
legend( 10, 650, names(datos[2:5]), cex=0.5, col = c("blue", "darkorange1", "pink","green4" ),
        pch = 1:4, lty=1:4, title="Tratamiento: ", horiz = TRUE)
