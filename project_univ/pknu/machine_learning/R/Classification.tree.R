

library(tree)
library(tre)
library(DAAG)
head(spam7)


set.seed(3)
n <- nrow(spam7)
spam <- spam7[sample(1:n, n/2, replace=F), ]

# Fit the decision tree
fit.tree <- rpart(yesno~., data=spam, control=rpart.control(cp=.001))
rpart.plot(fit.tree)

# Pruning
plotcp(fit.tree)
printcp(fit.tree)

# best regression tree with the minimum cv error
fit.tree$cptable

bestcp <- fit.tree$cptable[which.min(fit.tree$cptable[,"xerror"]),"CP"]
pruned.tree <- prune(fit.tree, cp = bestcp)
rpart.plot(pruned.tree)


### mtcars data (Y: am)
mtcars

