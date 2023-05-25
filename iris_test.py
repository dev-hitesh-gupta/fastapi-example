import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "classifier, sepal_length, sepal_width, petal_length, petal_width, expected_classifier, expected_prediction",
    [
        ('xgboost', 5.1, 3.5, 1.4, 0.2, 'xgboost', 0),
        ('decision_tree', 6.2, 2.8, 4.8, 1.8, 'decision_tree', 2),
        ('random_forest', 4.9, 3.0, 1.4, 0.2, 'random_forest', 0),
        ('adaboost', 7.2, 3.2, 6.0, 1.8, 'adaboost', 2),
        ('svm', 5.5, 4.2, 1.4, 0.2, 'svm', 0),
        ('knn', 6.0, 3.0, 4.8, 1.8, 'knn', 2)
    ])
def test_predict_classifier(classifier, sepal_length, sepal_width, petal_length,
                            petal_width, expected_classifier, expected_prediction):
    response = client.get(
        "/predict",
        params={
            "classifier": classifier,
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }
    )
    data = response.json()
    assert response.status_code == 200
    assert data['classifier'] == expected_classifier
    assert data['prediction'] == expected_prediction


def test_invalid_classifier():
    response = client.get(
        "/predict",
        params={
            "classifier": "invalid_classifier",
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )
    data = response.json()
    assert response.status_code == 200
    assert 'error' in data
