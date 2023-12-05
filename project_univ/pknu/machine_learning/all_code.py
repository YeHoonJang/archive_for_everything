# ================load library================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# for spliting data into train and test
from sklearn.model_selection import train_test_split, cross_val_score

# load accuracy method
from sklearn.metrics import accuracy_score

# load model method
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, plot_tree

from sklearn import datasets
# ============================================


# ================load dataset================
titanic = pd.read_csv("data/titanic/train.csv")

# select columns to use
titanic = titanic[["Pclass", "Sex", "Age", "SibSp", "Survived"]]
# ============================================


# ============preprocessing data==============
# convert data type in "Sex" columns from object to int
titanic["Sex"] = titanic["Sex"].map({"male":1, "female":2}).astype("category")

# fill Nan values in "Age" columns
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

# convert data type in "Age" from float to int
titanic["Age"] = titanic["Age"].astype("int")
# ============================================

# split dataset into 7:3
X_titanic = titanic.drop(["Survived"], axis=1)
y_titanic = titanic["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X_titanic, y_titanic, test_size=0.3, random_state=42)
# ============================================



# =================Log Reg================
# train
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# predict
lr_y_train = lr_model.predict(X_train)
lr_y_test = lr_model.predict(X_test)
# ============================================

# ==================Accuracy==================
lr_train_acc = round(accuracy_score(y_train, lr_y_train)*100, 2)
lr_acc = round(accuracy_score(y_test, lr_y_test)*100, 2)
# ============================================

coef = pd.DataFrame({'Feature': X_train.columns, 'Coefficient': lr_model.coef_[0]})



# =================LDA================
# train
lda_model = LinearDiscriminantAnalysis()
lda_model.fit(X_train, y_train)

# predict
lda_y_train = lda_model.predict(X_train)
lda_y_test = lda_model.predict(X_test)
# ============================================

# ==================Accuracy==================
lda_train_acc = round(accuracy_score(y_train, lda_y_train)*100, 2)
lda_acc = round(accuracy_score(y_test, lda_y_test)*100, 2)
# ============================================

# =================QDA================
# train
qda_model = QuadraticDiscriminantAnalysis()
qda_model.fit(X_train, y_train)

# predict
qda_y_train = qda_model.predict(X_train)
qda_y_test = qda_model.predict(X_test)
# ============================================

# ==================Accuracy==================
qda_train_acc = round(accuracy_score(y_train, qda_y_train)*100, 2)
qda_acc = round(accuracy_score(y_test, qda_y_test)*100, 2)
# ============================================


# =================NB================
# train
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# predict
nb_y_train = nb_model.predict(X_train)
nb_y_test = nb_model.predict(X_test)
# ============================================

# ==================Accuracy==================
nb_train_acc = round(accuracy_score(y_train, nb_y_train)*100, 2)
nb_acc = round(accuracy_score(y_test, nb_y_test)*100, 2)
# ============================================


# ======================================================
# ========================Tree==========================
# ======================================================

# ==================Reg Tree==================
iris = sns.load_dataset("iris")
iris["species"] = iris["species"].map({"setosa":1, "versicolor":2, "virginica":3}).astype("category")

# split into 7:3
X_iris = iris.drop(["sepal_width"], axis=1)
y_iris = iris["sepal_width"]
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.3, random_state=42)
# ============================================

reg_dt = DecisionTreeRegressor()
reg_dt.fit(X_train, y_train)

reg_y_train = reg_dt.predict(X_train)
reg_y_test = reg_dt.predict(X_test)

reg_train_mse = ((y_train - reg_y_train)**2).mean()
reg_test_mse = ((y_test - reg_y_test)**2).mean()


# ==================Visualization==================
plt.figure(figsize=(12,6))
plot_tree(reg_dt, filled=True, feature_names=X_train.columns, class_names=['setosa', 'versicolor', 'virginica'])

# ==================pruning==================
path = reg_dt.cost_complexity_pruning_path(X_train, y_train)
# 'ccp_alphas': array([0.00000000e+00, 5.07406617e-17, 3.38353684e-17, 4.76190476e-05,
# 'impurities': array([0.00019048, 0.00019048, 0.00019048, 0.00025397, 0.00030159,

ccp_alphas, impurities = path.ccp_alphas, path.impurities
ccp_alphas = np.abs(ccp_alphas) # 부동 소수점에 의한 음수값 없애기 위한 작업

# Impurity
fig, ax = plt.subplots()
ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
ax.set_xlabel("effective alpha")
ax.set_ylabel("total impurity of leaves")
ax.set_title("Total Impurity vs effective alpha for training set")


# train

# alpha 마다의 cost_complexity 값 구한거!
regs = []
for ccp_alpha in ccp_alphas:
    reg_dt = DecisionTreeRegressor(random_state=42, ccp_alpha=ccp_alpha)
    reg_dt.fit(X_train, y_train)
    regs.append(reg_dt)

# clfs
# [DecisionTreeRegressor(random_state=42),
#  DecisionTreeRegressor(ccp_alpha=2.3684757858670008e-17, random_state=42),
#  DecisionTreeRegressor(ccp_alpha=9.473903143468003e-17, random_state=42),


# ==================Visualization==================
regs = regs[:-1] # 왜..?
ccp_alphas = ccp_alphas[:-1]

train_mse = []
test_mse = []
for reg in regs:
    y_train_pred = reg.predict(X_train)
    y_test_pred = reg.predict(X_test)
    train_mse.append(((y_train - y_train_pred)**2).mean())
    test_mse.append(((y_test - y_test_pred)**2).mean())

plt.scatter(ccp_alphas,train_mse)
plt.scatter(ccp_alphas,test_mse)
plt.plot(ccp_alphas,train_mse,label='train_mse',drawstyle="steps-post")
plt.plot(ccp_alphas,test_mse,label='test_mse',drawstyle="steps-post")
plt.legend()
plt.title('MSE vs alpha')


# ==================Best tree==================

best_alpha = round(ccp_alphas[test_mse.index(min(test_mse))], 5)

best_reg_dt = DecisionTreeRegressor(random_state=42, ccp_alpha=best_alpha)
best_reg_dt.fit(X_train, y_train)

reg_y_train = best_reg_dt.predict(X_train)
reg_y_test = best_reg_dt.predict(X_test)

best_reg_train_mse = ((y_train - reg_y_train)**2).mean()
best_reg_test_mse = ((y_test - reg_y_test)**2).mean()

# ==================Visualization==================
plt.figure(figsize=(12, 6))
plot_tree(best_reg_dt, feature_names=X_train.columns,class_names=['setosa', 'versicolor', 'virginica'], filled=True)
