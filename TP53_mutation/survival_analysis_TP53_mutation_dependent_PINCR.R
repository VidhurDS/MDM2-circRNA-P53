
library(survival)

#for mutated
tp_mut <- read.table(file.choose(), header = TRUE, sep = '\t')
colnames(tp_mut)
mtime <- tp_mut$Time
mevent <- tp_mut$Event
mgroup <- tp_mut$Group
# KM survival: mutated
kmsurvival_mut <- survfit(Surv(mtime,mevent)~mgroup, data=tp_mut)
summary(kmsurvival_mut)
# regular plot
plot(kmsurvival_mut,lty=2:3, col=3:2, xlab="Time", ylab="Survival Probability", main=toupper("LINC01021 (TP53 Mutated)"))
legend(
  "top",
  legend=unique(mgroup),
  col=3:2,
  lty=2:3,
  horiz=FALSE,
  bty='n')
# p-value
msdf=survdiff(Surv(mtime, mevent) ~ mgroup, data=tp_mut, rho=0)
mpval=1-pchisq(msdf$chisq,length(msdf$n)-1)
mpval
#Mutated P-val:  1

#for wildtype
tp_wild <- read.table(file.choose(), header = TRUE, sep = '\t')
colnames(tp_wild)
wtime <- tp_wild$Time
wevent <- tp_wild$Event
wgroup <- tp_wild$Group
# KM survival: wild type
kmsurvival_wild <- survfit(Surv(wtime,wevent)~wgroup, data=tp_wild)
summary(kmsurvival_wild)
# regular plot
plot(kmsurvival_wild,lty=2:3, col=2:3, xlab="Time", ylab="Survival Probability", main=toupper("PINCR (TP53 Wild Type)"))
legend(
  "topright",
  legend=unique(wgroup),
  col=2:3,
  lty=2:3,
  horiz=FALSE,
  bty='n')
# p-value
wsdf=survdiff(Surv(wtime, wevent) ~ wgroup, data=tp_wild, rho=0)
wpval=1-pchisq(wsdf$chisq,length(wsdf$n)-1)
wpval
#Wildtype P-val: 0.317
