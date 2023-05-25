import numpy as np
from fastapi import APIRouter, Depends, HTTPException, Query
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from fastapi.responses import JSONResponse
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

iris_router = APIRouter()

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
data = iris.data

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# Initialize and train the models
models = {
    'logistic': LogisticRegression(max_iter=1000),
    'xgboost': XGBClassifier(),
    'decision_tree': DecisionTreeClassifier(),
    'random_forest': RandomForestClassifier(),
    'adaboost': AdaBoostClassifier(),
    'svm': SVC(),
    'knn': KNeighborsClassifier()
}

for model in models.values():
    model.fit(X_train, y_train)


@iris_router.get('/predict')
def predict_classifier(classifier: str = Query(...), sepal_length: float = Query(...),
                       sepal_width: float = Query(...),
                       petal_length: float = Query(...),
                       petal_width: float = Query(...)):
    # Convert query parameters to numpy array
    X_test = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Perform prediction based on the selected classifier
    if classifier in models:
        model = models[classifier]
        y_pred = model.predict(X_test)
        return {'classifier': classifier, 'prediction': int(y_pred[0])}
    else:
        return {'error': 'Invalid classifier'}


@iris_router.get('/clusters/{n_clusters}')
def get_clusters(n_clusters: int):
    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    labels = kmeans.labels_

    # Plot the data and clustering results
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.title(f'Iris Dataset - K-Means Clustering (n_clusters={n_clusters})')
    plt.show()

    return {'message': 'Clustering completed and visualization displayed.'}
