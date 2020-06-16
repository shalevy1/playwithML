# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:51:12 2020

@author: Akash
"""
from playwithML import preprocessing_for_classification as pfc
import xgboost
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from pandas_profiling import profile_report
from sklearn.metrics import f1_score, precision_score, jaccard_score
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier


## Function for RandomForestClassifier
def randomforestclassifier(X_train,X_test,y_train,y_test):
    
    classifier = RandomForestClassifier()
    classifier.fit(X_train, y_train)
    return classifier.predict(X_test)
    

## Function for DecisionTreeCLassifier
def decisiontreeclassifier(X_train,X_test,y_train,y_test):
    
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train,y_train)
    return classifier.predict(X_test)


## Function for SVC
def svc(X_train,X_test,y_train,y_test):
    
    classifier = SVC()
    classifier.fit(X_train,y_train)
    return classifier.predict(X_test)


## Function for xgboost
def xgboostclassifier(X_train,X_test,y_train,y_test):
    
    classifier = xgboost.XGBClassifier()
    classifier.fit(X_train,y_train)
    return classifier.predict(X_test)


## Function for sgdclassifier
def sgdclassifier(X_train,X_test,y_train,y_test):
    
    classifier = SGDClassifier(loss='hinge', penalty='l2')
    classifier.fit(X_train,y_train)
    return classifier.predict(X_test)


## Function for gradientboostingclassifier
def gradientboostingclassifier(X_train,X_test,y_train,y_test):
    
    classifier = GradientBoostingClassifier()
    classifier.fit(X_train,y_train)
    return classifier.predict(X_test)
