class SQLScorer:

    def score(
        self,
        validation_result
    ):

        score = 100

        issues = validation_result[
            "issues"
        ]

        score -= (
            len(issues) * 10
        )

        if score < 0:
            score = 0

        if score >= 90:
            grade = "A"

        elif score >= 80:
            grade = "B"

        elif score >= 70:
            grade = "C"

        else:
            grade = "F"

        return {
            "score": score,
            "grade": grade,
            "issues": issues
        }
