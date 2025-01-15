import langid


def detect_language(text):
    """
    Detects the language of the given text.
    """

    try:
        language = langid.classify(text)
        return language
    except Exception as e:
        print(f"Error detecting language: {e}")
        raise
