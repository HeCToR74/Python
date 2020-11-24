import pandas as pd
from sklearn.linear_model import LogisticRegression
import warnings

warnings.simplefilter("ignore")

train = pd.read_csv('leaf/train_data.csv')
y_train  = train['class']
X_train = train.drop('class', axis=1)

test = pd.read_csv('leaf/test_data.csv')
y_test  = test['class']
X_test = test.drop('class', axis=1)

validation = pd.read_csv('leaf/validation_data.csv')
y_validation  = validation['class']
X_validation = validation.drop('class', axis=1)

max_par = ''
max_score = 0
for par in ['liblinear', 'newton-cg', 'lbfgs', 'sag', 'saga']:
    model_log = LogisticRegression(C=1000, solver=par)
    model_log.fit(X_train, y_train)
    score = model_log.score(X_validation, y_validation)
    print("Parameter: criterion =", par, "; Accuracy:", score)
    if score >= max_score:
        max_par = par
        max_score = score

print("\nCriterion:", max_par)
model_log = LogisticRegression(C=1000, solver=max_par)
model_log.fit(X_train, y_train)
score = model_log.score(X_test, y_test)
print("Accuracy:", score)








