import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from collections import Counter
from tqdm.notebook import tqdm

# for spliting data into train and test
from sklearn.model_selection import train_test_split, GridSearchCV

# load method
from sklearn.metrics import accuracy_score

# load model method
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB


def lr(X_train, y_train, X_test, y_test):
    # Logistic Regression
    # =================train model================
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
    return lr_train_acc, lr_acc


def lda(X_train, y_train, X_test, y_test):
    # LDA
    # =================train model================
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
    return lda_train_acc, lda_acc


def qda(X_train, y_train, X_test, y_test):
    # QDA
    # =================train model================
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
    return qda_train_acc, qda_acc

def nb(X_train, y_train, X_test, y_test):
    # Naïve Bayes
    # =================train model================
    # train
    nb_model = GaussianNB()
    nb_model.fit(X_train, y_train)

    # predict
    nb_y_train = nb_model.predict(X_train)
    nb_y_test = nb_model.predict(X_test)
    # ============================================

    # ==================Accuracy==================
    nb_train_acc = round(accuracy_score(y_train, nb_y_train)*100, 2)
    nb_test_acc = round(accuracy_score(y_test, nb_y_test)*100, 2)
    # ============================================
    return nb_train_acc, nb_test_acc


def dt(X_train, y_train, X_test, y_test):
    # Decision Tree
    # =================train model================
    # train
    clf_dt = DecisionTreeClassifier(random_state=42, max_depth=10, ccp_alpha=0.01)
    clf_dt.fit(X_train, y_train)

    # predict
    clf_y_train = clf_dt.predict(X_train)
    clf_y_test = clf_dt.predict(X_test)
    # ============================================

    # ==================Accuracy==================
    clf_dt_train_acc = accuracy_score(y_train, clf_y_train)
    clf_dt_test_acc = accuracy_score(y_test, clf_y_test)
    # ============================================

    # Pruning
    path = clf_dt.cost_complexity_pruning_path(X_train, y_train)

    ccp_alphas, impurities = path.ccp_alphas, path.impurities
    ccp_alphas = np.abs(ccp_alphas)  # 부동 소수점에 의한 음수값 없애기 위한 작업

    clfs = []
    for ccp_alpha in ccp_alphas:
        clf_dt = DecisionTreeClassifier(random_state=42, max_depth=10, ccp_alpha=ccp_alpha)
        clf_dt.fit(X_train, y_train)
        clfs.append(clf_dt)

    clfs = clfs[:-1]
    ccp_alphas = ccp_alphas[:-1]

    node_counts = [clf.tree_.node_count for clf in clfs]
    depth = [clf.tree_.max_depth for clf in clfs]

    train_acc = []
    test_acc = []
    for clf in clfs:
        y_train_pred = clf.predict(X_train)
        y_test_pred = clf.predict(X_test)
        train_acc.append(round((accuracy_score(y_train, y_train_pred) * 100), 2))
        test_acc.append(round((accuracy_score(y_test, y_test_pred) * 100), 2))

    best_alpha = round(ccp_alphas[test_acc.index(min(test_acc))], 5)

    # Best model
    best_clf_dt = DecisionTreeClassifier(random_state=42, max_depth=10, ccp_alpha=best_alpha)
    best_clf_dt.fit(X_train, y_train)

    clf_y_train = best_clf_dt.predict(X_train)
    clf_y_test = best_clf_dt.predict(X_test)

    best_clf_dt_train_acc = accuracy_score(y_train, clf_y_train)
    best_clf_dt_test_acc = accuracy_score(y_test, clf_y_test)

    return clf_dt_train_acc, clf_dt_test_acc, best_clf_dt_train_acc, best_clf_dt_test_acc, best_alpha


def bagging(X_train, y_train, X_test, y_test, best_alpha):
    # Bagging
    # =================train model================
    # train
    bagging_clf = BaggingClassifier(base_estimator=DecisionTreeClassifier(random_state=42, max_depth=10, ccp_alpha=best_alpha), n_estimators=5, random_state=42)
    bagging_clf.fit(X_train, y_train)

    # predict
    bagging_clf_y_train = bagging_clf.predict(X_train)
    bagging_clf_y_test = bagging_clf.predict(X_test)
    # ============================================

    # ==================Accuracy==================
    bagging_clf_train_acc = accuracy_score(y_train, bagging_clf_y_train)
    bagging_clf_test_acc = accuracy_score(y_test, bagging_clf_y_test)
    # ============================================
    return bagging_clf_train_acc, bagging_clf_test_acc


def rf(X_train, y_train, X_test, y_test):
    # Random Forest
    # =================train model================
    # train
    clf_rf = RandomForestClassifier(random_state=42, max_depth=10, ccp_alpha=0.01)
    clf_rf.fit(X_train, y_train)

    # predict
    clf_y_train = clf_rf.predict(X_train)
    clf_y_test = clf_rf.predict(X_test)
    # ============================================

    # ==================Accuracy==================
    clf_rf_train_acc = accuracy_score(y_train, clf_y_train)
    clf_rf_test_acc = accuracy_score(y_test, clf_y_test)
    # ============================================

    # Hyper-parameter Tuning
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_features': ['auto', 'sqrt'],
        'max_depth': [10, 20, 30, None],
        'ccp_alpha':[0.1, 0.05, 0.01, 0.005]
    }

    # 그리드 서치 객체 생성 및 학습
    grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='neg_mean_squared_error', verbose=0)
    grid_search.fit(X_train, y_train)

    # Best Model
    # =================train model================
    # train
    best_clf_rf = RandomForestClassifier(random_state=42, **grid_search.best_params_)
    best_clf_rf.fit(X_train, y_train)

    # predict
    clf_y_train = best_clf_rf.predict(X_train)
    clf_y_test = best_clf_rf.predict(X_test)
    # ============================================

    # ==================Accuracy==================
    best_clf_rf_train_acc = accuracy_score(y_train, clf_y_train)
    best_clf_rf_test_acc = accuracy_score(y_test, clf_y_test)
    # ============================================
    return clf_rf_train_acc, clf_rf_test_acc, best_clf_rf_train_acc, best_clf_rf_test_acc


def ab(X_train, y_train, X_test, y_test, best_alpha):
    # AdaBoosting
    # =================train model================
    # train
    ada = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(random_state=42, max_depth=10, ccp_alpha=0.1), n_estimators=10, random_state=42)
    ada.fit(X_train, y_train)

    # predict
    ada_y_train = ada.predict(X_train)
    ada_y_test = ada.predict(X_test)

    # ==================Accuracy==================
    ada_train_acc = accuracy_score(y_train, ada_y_train)
    ada_test_acc = accuracy_score(y_test, ada_y_test)
    # ============================================

    # Pruning
    # =================train model================
    # train
    ada = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(random_state=42, max_depth=10, ccp_alpha=best_alpha), n_estimators=10, random_state=42)
    ada.fit(X_train, y_train)

    # predict
    ada_y_train = ada.predict(X_train)
    ada_y_test = ada.predict(X_test)

    #==================Accuracy==================
    best_ada_train_acc = accuracy_score(y_train, ada_y_train)
    best_ada_test_acc = accuracy_score(y_test, ada_y_test)
    # ============================================
    return ada_train_acc, ada_test_acc, best_ada_train_acc, best_ada_test_acc


def gb(X_train, y_train, X_test, y_test, best_alpha):
    # Gradient Boosting
    # =================train model================
    # train
    gb = GradientBoostingClassifier(random_state=42, ccp_alpha=best_alpha)
    gb.fit(X_train, y_train)

    # predict
    gb_y_train = gb.predict(X_train)
    gb_y_test = gb.predict(X_test)

    # ==================Accuracy==================
    gb_train_acc = accuracy_score(y_train, gb_y_train)
    gb_test_acc = accuracy_score(y_test, gb_y_test)
    # ============================================
    return gb_train_acc, gb_test_acc


def lsvm(X_train, y_train, X_test, y_test):
    # Linear SVM Classifier
    # =================train model================
    # train
    linear_svm = LinearSVC(random_state=42) # defalut C=1.0
    linear_svm.fit(X_train, y_train)

    # predict
    linear_svm_y_train = linear_svm.predict(X_train)
    linear_svm_y_test = linear_svm.predict(X_test)

    # ==================Accuracy==================
    linear_svm_train_acc = accuracy_score(y_train, linear_svm_y_train)
    linear_svm_test_acc = accuracy_score(y_test, linear_svm_y_test)
    # ============================================
    return linear_svm_train_acc, linear_svm_test_acc


def ksvm(X_train, y_train, X_test, y_test):
    # Kernel SVM Classifier
    # =================train model================
    # train
    kernel_svm = SVC(C=1) # defalut C=1.0 / default kernel=radial / default gamma='scale'
    kernel_svm.fit(X_train, y_train)

    # predict
    kernel_svm_y_train = kernel_svm.predict(X_train)
    kernel_svm_y_test = kernel_svm.predict(X_test)

    # ==================Accuracy==================
    kernel_svm_train_acc = accuracy_score(y_train, kernel_svm_y_train)
    kernel_svm_test_acc = accuracy_score(y_test, kernel_svm_y_test)
    # ============================================

    # Hyper-parameter Tuning
    param_grid = {
        'C': [0.1, 0.5, 1, 5, 10, 50, 100],
        'gamma': ['scale', 'auto']
    }

    # 그리드 서치 객체 생성 및 학습
    grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='neg_mean_squared_error', verbose=0)
    grid_search.fit(X_train, y_train)

    # Best model
    # =================train model================
    # train
    kernel_svm = SVC(**grid_search.best_params_) # defalut C=1.0 / default kernel=radial / default gamma='scale'
    kernel_svm.fit(X_train, y_train)

    # predict
    kernel_svm_y_train = kernel_svm.predict(X_train)
    kernel_svm_y_test = kernel_svm.predict(X_test)

    # ==================Accuracy==================
    best_kernel_svm_train_acc = accuracy_score(y_train, kernel_svm_y_train)
    best_kernel_svm_test_acc = accuracy_score(y_test, kernel_svm_y_test)
    # ============================================
    return kernel_svm_train_acc, kernel_svm_test_acc, best_kernel_svm_train_acc, best_kernel_svm_test_acc


def main():
    # data load
    data = pd.read_csv("/home/yehoon/workspace/archive_for_everything/project_univ/pknu/machine_learning/Assignment_02/data/diabetes.csv")

    # data split
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    lr_train_acc, lr_acc = lr(X_train, y_train, X_test, y_test)
    lda_train_acc, lda_acc = lda(X_train, y_train, X_test, y_test)
    qda_train_acc, qda_acc = qda(X_train, y_train, X_test, y_test)
    nb_train_acc, nb_test_acc = nb(X_train, y_train, X_test, y_test)
    clf_dt_train_acc, clf_dt_test_acc, best_clf_dt_train_acc, best_clf_dt_test_acc, best_alpha = dt(X_train, y_train, X_test, y_test)
    bagging_clf_train_acc, bagging_clf_test_acc = bagging(X_train, y_train, X_test, y_test, best_alpha)
    clf_rf_train_acc, clf_rf_test_acc, best_clf_rf_train_acc, best_clf_rf_test_acc= rf(X_train, y_train, X_test, y_test)
    ada_train_acc, ada_test_acc, best_ada_train_acc, best_ada_test_acc = ab(X_train, y_train, X_test, y_test, best_alpha)
    gb_train_acc, gb_test_acc = gb(X_train, y_train, X_test, y_test, best_alpha)
    linear_svm_train_acc, linear_svm_test_acc = lsvm(X_train, y_train, X_test, y_test)
    kernel_svm_train_acc, kernel_svm_test_acc, best_kernel_svm_train_acc, best_kernel_svm_test_acc = ksvm(X_train, y_train, X_test, y_test)

    # Result
    print("=================Accuracy===============")
    print("Model\t\t\t| Train\t| Test")
    print("------------------------|-------|-------")
    print(f"Logistic Regression\t| {lr_train_acc}\t| {lr_acc}")
    print(f"LDA\t\t\t| {lda_train_acc}\t| {lda_acc}")
    print(f"QDA\t\t\t| {qda_train_acc}\t| {qda_acc}")
    print(f"Naïve Bayes\t\t| {nb_train_acc}\t| {nb_test_acc}")
    print(f"Decision Tree\t\t| {round(clf_dt_train_acc * 100, 2)}\t| {round(clf_dt_test_acc * 100, 2)}")
    print(f"Decision Tree (Pruned)\t| {round(best_clf_dt_train_acc * 100, 2)}\t| {round(best_clf_dt_test_acc * 100, 2)}")
    print(f"Bagging\t\t\t| {round(bagging_clf_train_acc * 100, 2)}\t| {round(bagging_clf_test_acc * 100, 2)}")
    print(f"Random Forest\t\t| {round(clf_rf_train_acc * 100, 2)}\t| {round(clf_rf_test_acc * 100, 2)}")
    print(f"Random Forest (Tuned)\t| {round(best_clf_rf_train_acc * 100, 2)}\t| {round(best_clf_rf_test_acc * 100, 2)}")
    print(f"Ada Boosting\t\t| {round(ada_train_acc * 100, 2)}\t| {round(ada_test_acc * 100, 2)}")
    print(f"Ada Boosting (Pruned)\t| {round(best_ada_train_acc * 100, 2)}\t| {round(best_ada_test_acc * 100, 2)}")
    print(f"Gradient Boosting\t| {round(gb_train_acc * 100, 2)}\t| {round(gb_test_acc * 100, 2)}")
    print(f"Linear SVM\t\t| {round(linear_svm_train_acc * 100, 2)}\t| {round(linear_svm_test_acc * 100, 2)}")
    print(f"Kernel SVM\t\t| {round(kernel_svm_train_acc * 100, 2)}\t| {round(kernel_svm_test_acc * 100, 2)}")
    print(f"Kernel SVM (Tuned)\t| {round(best_kernel_svm_train_acc * 100, 2)}\t| {round(best_kernel_svm_test_acc * 100, 2)}")
    print("========================================")


if __name__ == "__main__":
    main()
