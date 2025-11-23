from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

iris = load_iris()
x, y = iris.data, iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

acc = accuracy_score(y_pred, y_test)
print(f"Decision tree accuracy: {acc:.4f}")

tree_rules = export_text(clf, feature_names = iris.feature_names)
print("\nDecision Tree Classifer rules:\n")
print(tree_rules)