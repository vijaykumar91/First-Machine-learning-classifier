#   wait      texture  label
#   150g      Bumpy     Orange
#   170g      Bumpy     Orange
#   140g      Smooth    Apple
#   130g       Smooth   Apple
#features=[[140,"Smooth"],[130,"Smooth"],[150,"Bumpy"],[170,"Bumpy"],[100,"Smooth"]]
#labels=["Apple","Apple","Orange","Orange","Apple"]
#When we will write code in ML then we need to numeric value


from sklearn import tree
features=[[140,1],[130,1],[150,0],[170,0],[100,0]]
labels=[0,0,1,1,0]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[150,0]]))
if clf.predict([[150,0]])==1:
    print("---------######--------  Apple   ---------######--------")
else:
    print("---------######--------  Orange   ---------######--------")
#Ans will generate 1 means apple ,pridiction is good