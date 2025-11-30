from life360 import TrainModel
from life360 import ValidationModel
from typing import List

print('abcd')

model = TrainModel()

sample_inputs: List[List[float]] = [
[25.0, 50000.0, 0.8],   # Sample 1: age=25, income=50k, score=0.8
[32.0, 75000.0, 0.6],   # Sample 2
[45.0, 90000.0, 0.9],   # Sample 3
[28.0, 60000.0, 0.5],   # Sample 4
[55.0, 30000.0, 0.7],  # Sample 5
[51.0, 10000.0, 0.7],  # Sample 6
[25.0, 10000.0, 0.7],  # Sample 7
[98.0, 12000.0, 0.7],  # Sample 8
[90.0, 18000.0, 0.7],  # Sample 9
[12.0, 11000.0, 0.7],  # Sample 10
]

# Ground truth labels (0, 1, or 2)
y_true: List[int] = [0, 1, 2, 0, 1, 0, 1, 2, 2, 1]

probabilities = model.predict(sample_inputs)
print(probabilities)

# Validate
validator = ValidationModel()
y_pred = validator.predict_classes(probabilities)

print(f"\nTrue labels:      {y_true}")
print(f"Predicted labels: {y_pred}")

print("\nPer-class (precision, recall):")
for i, (p, r) in enumerate(validator.precision_recall_per_class(y_true, y_pred)):
    print(f"  Class {i}: precision={p:.2f}, recall={r:.2f}")

acc, macro_p, macro_r = validator.overall_metrics(y_true, y_pred)
print(f"\nOverall: accuracy={acc:.2f}, macro_precision={macro_p:.2f}, macro_recall={macro_r:.2f}")

loss = validator.log_loss(y_true, probabilities)
print(f"Log loss: {loss:.3f}")