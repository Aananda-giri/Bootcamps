import pandas as pd
import numpy as np
import pickle

from sklearn import tree

def convert_to_text(y):
	if y[0]==0:
		y='setosa'
	elif y[0]==1:
		y='versicolor'
	else:
		y='virginica'
	
	return y
if __name__=="__main__":
	choose_option = input("1. train model \n2. test model")
	if int(choose_option) == 1:
			try:
				dataset=pd.read_csv('Dataset\IRIS.csv')	# for windows
			except:
				dataset=pd.read_csv('Dataset/IRIS.csv')	# for linux
			# dataset=lower_case_all(dataset)
			
			# dataset=numerize_all(dataset)
			
			#print(dataset)
			X=np.array(dataset.drop(['species'],True))
			Y=np.array(dataset['species']).reshape(-1,1)
			model=tree.DecisionTreeClassifier()
			model=model.fit(X,Y)
			pickle.dump(model,open('iris_flower_decision_tree.model','wb'))
		
	else:
			model = pickle.load(open('iris_flower_decision_tree.model', 'rb'))
			parameters=['sepal_length','sepal_width','petal_length','petal_width']
			inputs=[]
			
			# taking parameters to predict
			for i in parameters:
				inputs.append(float(input('Enter value for '+i+': ')))
			
			inputs=[inputs]	# 2d array because model.predict() expects 2d array
			y=convert_to_text(model.predict(inputs))
			
			print(y)

