import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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
max_d = 0
max_score = 0
for par in ["entropy", "gini"]:
    for d in range(2, 21):
        model_rand_forest = RandomForestClassifier(criterion=par, max_depth=d, random_state=0)
        model_rand_forest.fit(X_train, y_train)
        score = model_rand_forest.score(X_validation, y_validation)
        print("Parameter: criterion =", par, ", max_depth =", d, "; Accuracy:", score)
        if score >= max_score:
            max_par = par
            max_d = d
            max_score = score
print("\nCriterion:", max_par, ", max_depth:", max_d)
model_rand_forest = RandomForestClassifier(criterion=max_par, max_depth=max_d, random_state=0)
model_rand_forest.fit(X_train, y_train)
score = model_rand_forest.score(X_test, y_test)
print("Accuracy:", score)







