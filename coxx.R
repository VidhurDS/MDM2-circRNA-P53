#Cox regression:
library(survival)
file_egfr <- read.table("coxx matrix output.txt", header = TRUE, sep = '\t')
colnames(file_egfr)

time <- file_egfr$Time
event <- file_egfr$Event

file_egfr_1 <- coxph(Surv(time,event)~ MATR3, data= file_egfr)
summary(file_egfr_1)

# KM survival:

kmsurvival <- survfit(Surv(time,event)~1)
summary(kmsurvival)
plot(kmsurvival,xlab="Time",ylab="Survival Probablity", col=c("Red", "blue", "green"))
