def predict_sentiment(text: str) -> str:
    if not text:
        return "neutral"

    lowered = text.lower()
    if "happy" in lowered or "good" in lowered:
        return "positive"
    if "sad" in lowered or "bad" in lowered:
        return "negative"
    return "neutral"


# Compat: certains énoncés/tests attendent `predict(...)`
def predict(text: str) -> str:
    return predict_sentiment(text)