import numpy as np
import pandas as pd
from sklearn import linear_model
import warnings

warnings.simplefilter("ignore")


train = pd.read_csv('auto_mpg/train_data.csv')
y_train  = train['mpg']
X_train = train.drop('mpg', axis=1)


test = pd.read_csv('auto_mpg/test_data.csv')
y_test  = test['mpg']
X_test = test.drop('mpg', axis=1)

validation = pd.read_csv('auto_mpg/validation_data.csv')
y_validation  = validation['mpg']
X_validation = validation.drop('mpg', axis=1)

max_loss = ''
max_score = 0
max_penalty = ''
for loss in ['squared_loss', 'huber', 'epsilon_insensitive', 'squared_epsilon_insensitive']:
    for penalty in [None, 'l2', 'l1', 'elasticnet']:
        model1 = linear_model.SGDRegressor(loss=loss, penalty=penalty, max_iter=10000)
        model1.fit(X_train, y_train)
        score1 = model1.score(X_validation, y_validation)
        print("Parameter: loss =", loss, ", penalty:", penalty, "; Accuracy:", score1)
        # if score1 >= max_score:
        #     max_loss = loss
        #     max_penalty = penalty
        #     max_score = score1

print("\nSGDRegressor // Parameter: loss =", max_loss, ", penalty:", max_penalty)

# model1 = linear_model.SGDRegressor(loss=max_loss, penalty=max_penalty, max_iter=10000)
# model1.fit(X_train, y_train)
# score1 = model1.score(X_test, y_test)
# print("Accuracy:", score1)

max_solver = ''
max_score = 0
max_iter = 0
for solver in ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg']:
    for iter in [1000, 2000, 5000, 10000]:
        model2 = linear_model.Ridge(solver=solver, max_iter=iter)
        model2.fit(X_train, y_train)
        score2 = model2.score(X_validation, y_validation)
        print("Parameter: solver =", solver, ", max_iter:", iter, "; Accuracy:", score2)
        if score2 >= max_score:
            max_solver = solver
            max_iter = iter
            max_score = score2

print("\nRidge regression // Parameter: solver =", max_solver, ", max_iter:", max_iter)

model2 = linear_model.Ridge(solver=max_solver, max_iter=max_iter)
model2.fit(X_train, y_train)
score2 = model2.score(X_test, y_test)
print("Accuracy:", score2)


