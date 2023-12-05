
library(rpart)
library(rpart.plot)

n <- nrow(iris); p <- ncol(iris)

######## Fit the Regression Tree
fit.tree <- rpart(Sepal.Width ~ Sepal.Length + Petal.Length + Petal.Width + Species, 
                  method = "anova", data = iris, , control=rpart.control(cp=.0001))
rpart.plot(fit.tree)


# prediction
tree.pred <- predict(fit.tree)
sum((tree.pred-iris$Petal.Width)^2) / n # MSE

# Pruning
plotcp(fit.tree)
printcp(fit.tree)

# best regression tree with the minimum cv error
bestcp <- fit.tree$cptable[which.min(fit.tree$cptable[,"xerror"]),"CP"]
pruned.tree <- prune(fit.tree, cp = bestcp)
rpart.plot(pruned.tree)


library(yarrr)
head(diamonds)

data("diamonds")

fit.tree <- rpart( medv ~ ., data = boston, control=rpart.control(cp=.0001))
rpart.plot(fit.tree)

# Pruning
plotcp(fit.tree)
printcp(fit.tree)

# best regression tree with the minimum cv error
bestcp <- fit.tree$cptable[which.min(fit.tree$cptable[,"xerror"]),"CP"]
pruned.tree <- prune(fit.tree, cp = bestcp)
rpart.plot(pruned.tree)


























