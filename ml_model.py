import numpy as np
from sklearn.ensemble import RandomForestClassifier

class ShipmentStorageLocationPredictor:
    def __init__(self, X_train, y_train):
        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)

    def predict(self, X):
        predictions = self.model.predict_proba(X)
        return predictions[:, np.argmax(predictions, axis=1)]

# Load the training data
X_train = np.loadtxt('training.csv', delimiter=',')
y_train = X_train[:, -1]

# Train the model
predictor = ShipmentStorageLocationPredictor(X_train, y_train)

# Load the test data
X_test = np.loadtxt('shipment_storage_location_test_data.csv', delimiter=',')

# Make predictions on the test data
predictions = predictor.predict(X_test)

# Calculate the accuracy of the model
accuracy = np.mean(predictions == y_test)

print('Accuracy:', accuracy)