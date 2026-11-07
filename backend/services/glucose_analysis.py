def glucose_summary(values):
    if not values:
        return {
            "average": None,
            "minimum": None,
            "maximum": None,
            "count": 0
        }

    return {
        "average": round(sum(values) / len(values), 2),
        "minimum": min(values),
        "maximum": max(values),
        "count": len(values)
    }
