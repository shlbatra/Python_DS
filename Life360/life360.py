# 2 classes

# Train model random scorer -> provide probabilities as tuple (a, b, c) -> using predict return list of tuples (,,)
# tgt classes 3 -> [a, b, c]

# validation model
# predict -> predict model scores
# provide metrics
# how calculate precision / recall for 3 class problem
# overall system vs each class.

# learn to explain log loss -> you still struggle.


import random
from typing import List, Tuple


class TrainModel:
    """A model that takes inputs and outputs probability tuples for 3 classes."""

    def __init__(self, seed: int = 42):
        if seed is not None:
            random.seed(seed)

    def predict(self, inputs: List[List[float]]) -> List[Tuple[float, float, float]]:
        """
        Takes a list of input samples and returns probability tuples.

        Args:
            inputs: A list of samples (each sample is a list of features)

        Returns:
            A list of tuples, each containing three floats that sum to 1.0
        """
        results = []
        for _ in inputs:
            # Generate 3 random values and normalize to sum to 1
            raw = [random.random() for _ in range(3)]
            total = sum(raw)
            normalized = tuple(v / total for v in raw)
            results.append(normalized)
        return results


class ValidationModel:
    """Evaluates model predictions and provides metrics for 3-class classification."""

    def __init__(self):
        self.num_classes = 3

    def predict_classes(self, probabilities: List[Tuple[float, float, float]]) -> List[int]:
        """Convert probability tuples to predicted class labels (0, 1, or 2)."""
        return [probs.index(max(probs)) for probs in probabilities]

    def confusion_matrix(self, y_true: List[int], y_pred: List[int]) -> List[List[int]]:
        """Build a 3x3 confusion matrix."""
        matrix = [[0] * self.num_classes for _ in range(self.num_classes)]
        for true, pred in zip(y_true, y_pred):
            matrix[true][pred] += 1
        return matrix

    def precision_recall_per_class(
        self, y_true: List[int], y_pred: List[int]
    ) -> List[Tuple[float, float]]:
        """
        Calculate precision and recall for each class.

        Returns:
            List of (precision, recall) tuples for classes 0, 1, 2
        """
        cm = self.confusion_matrix(y_true, y_pred)
        results = []

        for c in range(self.num_classes):
            tp = cm[c][c]
            fp = sum(cm[i][c] for i in range(self.num_classes)) - tp
            fn = sum(cm[c]) - tp

            precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            results.append((precision, recall))

        return results

    def overall_metrics(
        self, y_true: List[int], y_pred: List[int]
    ) -> Tuple[float, float, float]:
        """
        Calculate overall accuracy, macro precision, and macro recall.

        Returns:
            (accuracy, macro_precision, macro_recall)
        """
        per_class = self.precision_recall_per_class(y_true, y_pred)

        accuracy = sum(1 for t, p in zip(y_true, y_pred) if t == p) / len(y_true)
        macro_precision = sum(p for p, _ in per_class) / self.num_classes
        macro_recall = sum(r for _, r in per_class) / self.num_classes

        return (accuracy, macro_precision, macro_recall)

    def log_loss(
        self, y_true: List[int], probabilities: List[Tuple[float, float, float]]
    ) -> float:
        """
        Calculate log loss (cross-entropy loss) for multi-class classification.

        Log loss measures how well probability predictions match actual classes.
        Formula: -1/N * sum(log(p_true_class)) for each sample

        Lower is better. Perfect predictions = 0, random = ~1.1 for 3 classes.
        For a random model with 3 classes, each class gets probability 1/3 ≈ 0.333
        log_loss = -log(1/3) = -log(0.333) = 1.099 ≈ 1.1
        """
        import math

        epsilon = 1e-15  # Prevent log(0)
        n = len(y_true)
        total_loss = 0.0

        for true_class, probs in zip(y_true, probabilities):
            # probs[true_class] -> predicted probability for the correct class
            # min(probs[true_class], 1 - epsilon) -> - Caps the value at 0.999999999999999 (just under 1)
            # max(..., epsilon) -> Ensures the value is at least 0.000000000000001
            # probability is clamped to range [epsilon, 1-epsilon]
            # Because log loss uses log(probability)
            # | Probability | log(prob) | Problem               |
            # |-------------|-----------|-----------------------|
            # | 0.5         | -0.69     | Fine                  |
            # | 0.01        | -4.6      | Fine                  |
            # | 0.0         | -infinity | Crashes!              |
            # | 1.0         | 0         | Fine, but unrealistic |

            prob_true = max(min(probs[true_class], 1 - epsilon), epsilon) 
            # | prob_true | log(prob_true) | -log(prob_true) | Meaning                             |
            # |-----------|----------------|-----------------|-------------------------------------|
            # | 0.9       | -0.105         | 0.105           | Confident & correct → small penalty |
            # | 0.5       | -0.693         | 0.693           | Uncertain → medium penalty          |
            # | 0.1       | -2.303         | 2.303           | Confident & wrong → big penalty     |
            # | 0.01      | -4.605         | 4.605           | Very wrong → huge penalty           |
            total_loss = total_loss - math.log(prob_true)

        return total_loss / n
