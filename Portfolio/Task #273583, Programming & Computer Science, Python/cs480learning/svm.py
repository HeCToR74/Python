import pandas as pd
from sklearn import svm
from sklearn import metrics
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

max_kernel = ''
max_gamma = ''
max_score = 0
model_SVM = svm.SVC()
model_SVM.fit(X_train, y_train)
max_score = model_SVM.score(X_validation, y_validation)
print("Parameter: kernel =", max_kernel, ", gamma =", max_gamma,"; Accuracy:", max_score)

for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
    for gamma in ['scale', 'auto']:
        model_SVM = svm.SVC(C=10000, kernel=kernel, gamma=gamma)
        model_SVM.fit(X_train, y_train)
        score = model_SVM.score(X_validation, y_validation)
        print("Parameter: kernel =", kernel, ", gamma =", gamma,"; Accuracy:", score)
        if score >= max_score:
            max_kernel = kernel
            max_gamma = gamma
            max_score = score

print("\nKernel:", max_kernel, ", gamma:", max_gamma)
model_SVM = svm.SVC(C=10000, kernel=max_kernel, gamma=max_gamma)
model_SVM.fit(X_train, y_train)
score = model_SVM.score(X_test, y_test)
print("Accuracy:", score)










