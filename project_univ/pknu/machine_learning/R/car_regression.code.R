
############# Univariate
fit.lm <- lm(dist ~ speed, data=cars)
coef.lm <- coef(fit.lm)
abline(a=coef.lm[1], b=coef.lm[2], col="red", lty=2, lwd=2)

predict(fit.lm)



############## Multivariate
library(MASS)
head(Boston)

fit.lm <- lm(medv ~ ., data=Boston)
summary(fit.lm)










