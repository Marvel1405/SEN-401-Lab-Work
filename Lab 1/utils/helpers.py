"""
Helper utilities for calculating student grade statistics.
Includes error handling for empty lists and median calculation (Perfective/Preventive maintenance).
"""

from typing import List, Dict, Union

def get_highest_score(students: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[str, float]]:
    """Returns the student dictionary with the highest score. Safe against empty lists."""
    if not students:
        return {"name": "N/A", "score": 0.0}
    return max(students, key=lambda s: s["score"])

def get_lowest_score(students: List[Dict[str, Union[str, float]]]) -> Dict[str, Union[str, float]]:
    """Returns the student dictionary with the lowest score. Safe against empty lists."""
    if not students:
        return {"name": "N/A", "score": 0.0}
    return min(students, key=lambda s: s["score"])

def get_median_score(students: List[Dict[str, Union[str, float]]]) -> float:
    """Calculates the median score of the student cohort."""
    if not students:
        return 0.0
    scores = sorted([float(s["score"]) for s in students])
    n = len(scores)
    mid = n // 2
    if n % 2 == 0:
        return (scores[mid - 1] + scores[mid]) / 2.0
    return scores[mid]