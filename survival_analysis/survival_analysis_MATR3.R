library(survival)

#for MATR3
tp_mut <- read.table(file.choose(), header = TRUE, sep = '\t')
colnames(tp_mut)
mtime <- tp_mut$Time
mevent <- tp_mut$Event
mgroup <- tp_mut$Group
# KM survival: mutated
kmsurvival_mut <- survfit(Surv(mtime,mevent)~mgroup, data=tp_mut)
summary(kmsurvival_mut)
# regular plot
plot(kmsurvival_mut,lty=2:3, col=3:2, xlab="Time", ylab="Survival Probability", main=toupper("MATR3"))
legend(
  "topright",
  legend=unique(mgroup),
  col=3:2,
  lty=2:3,
  horiz=FALSE,
  bty='n')
# p-value
msdf=survdiff(Surv(mtime, mevent) ~ mgroup, data=tp_mut, rho=0)
mpval=1-pchisq(msdf$chisq,length(msdf$n)-1)
mpval
#High_tp53 P-val: 0.242