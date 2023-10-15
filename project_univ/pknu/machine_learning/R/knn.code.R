library(class)
head(iris)

set.seed(2)
n <- nrow(iris)
tr.ind <- sample(1:n, size=n*0.8, replace=F)

train <- iris[tr.ind, ]
test  <- iris[-tr.ind, ]

fit.knn <- knn(train=train[,-5], test=test[,-5], cl=train[,5], k=5)
table(fit.knn, test$Species)


