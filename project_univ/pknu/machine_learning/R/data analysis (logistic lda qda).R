
library(MASS)

# Load Titanic Data
train = read.csv("train.csv", na.strings = "")
test = read.csv("test.csv", na.strings = "")

head(train)
head(test)

tr.data <- train[, c(2,3,5,6,7)]
tr.data <- na.omit(tr.data)

mean(tr.data$Survived == 1)
mean(tr.data$Survived == 0)


###### Logistic
logist.fit <- glm(Survived ~., data=tr.data, family="binomial")
logist.fit

logist.pred <- predict(logist.fit, tr.data, type="response")
logist.class <- ifelse(logist.pred>0.5, 1, 0)

logist.tb <- table(pred=logist.class, true=tr.data$Survived)
logist.tb

sum(diag(logist.tb)) / sum(logist.tb)



###### LDA
lda.fit <- lda(Survived ~ ., data=tr.data)
lda.fit
plot(lda.fit)

# predict the response
lda.pred <- predict(lda.fit ,tr.data)
lda.class <- lda.pred$class

# estimated delta_k
lda.pred$posterior


# confusion table
lda.tb <- table(pred=lda.class, true=tr.data$Survived)
lda.tb

sum(diag(lda.tb)) / sum(lda.tb)



###### QDA
qda.fit <- qda(Survived ~ ., data=tr.data)
qda.fit

# predict the response
qda.pred <- predict(qda.fit, tr.data)
qda.class <- qda.pred$class

# confusion table
qda.tb <- table(pred=qda.class, true=tr.data$Survived)
qda.tb

sum(diag(qda.tb)) / sum(qda.tb)



###### Naive Bayes
library(e1071)
NB.fit <- naiveBayes(Survived ~., data=tr.data)
NB.fit

NB.pred <- predict(NB.fit, tr.data)
NB.class <- NB.pred

# confusion table
NB.tb <- table(pred=NB.class, true=tr.data$Survived)
NB.tb

sum(diag(NB.tb)) / sum(NB.tb)


