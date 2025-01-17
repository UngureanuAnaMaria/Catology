import spacy
import re

nlp = spacy.load("en_core_web_sm")

attribute_mapping = {
    "Shy": ["shy"],
    "Calm": ["calm", "quiet"],
    "Fearful": ["fearful", "scared", "afraid"],
    "Intelligent": ["intelligent", "smart", "clever"],
    "Vigilant": ["vigilant", "alert"],
    "Perseverant": ["perseverant", "determined"],
    "Affectionate": ["affectionate", "loving"],
    "Friendly": ["friendly", "sociable"],
    "Solitary": ["solitary", "independent"],
    "Brutal": ["brutal", "rough"],
    "Dominant": ["dominant", "alpha"],
    "Aggressive": ["aggressive", "hostile"],
    "Impulsive": ["impulsive", "reckless"],
    "Predictable": ["predictable", "consistent"],
    "Distracted": ["distracted", "unfocused"]
}

negations = [
    "not", "isn't", "is not", "isn't very", "doesn't", "never", "no", "don't", "can't", "won't",
    "not very", "not really", "not quite", "not at all", "not so",
    "barely", "hardly", "scarcely", "neither", "nor", "not much",
    "not really", "not entirely", "not exactly"
]


def detect_negations(description):
    description = description.lower()
    negation_phrases = []
    for negation in negations:
        if re.search(r'\b' + re.escape(negation) + r'\b', description):
            negation_phrases.append(negation)
    # print(negation_phrases)
    return negation_phrases


def extract_adjectives_after_negation(description, negation_phrases):
    doc = nlp(description.lower())
    negation_adjective_dict = {}

    for negation in negation_phrases:
        negation_word = negation.split()[-1]
        for token in doc:
            if token.text == negation_word:
                next_token = token.nbor()
                if next_token.pos_ == "ADJ":
                    negation_adjective_dict[negation] = next_token.text

    # print(negation_adjective_dict)
    return negation_adjective_dict


def extract_character_attributes(description):
    doc = nlp(description)
    attributes = {key: "Unknown" for key in attribute_mapping.keys()}

    negation_phrases = detect_negations(description)

    negation_adjective_dict = extract_adjectives_after_negation(description, negation_phrases)

    for i, token in enumerate(doc):
        for attr, keywords in attribute_mapping.items():
            if token.text.lower() in keywords:
                if any(negation in negation_adjective_dict and negation_adjective_dict[negation] == token.text.lower()
                       for negation in negation_phrases):
                    attributes[attr] = "No"
                else:
                    attributes[attr] = "Yes"

    return attributes


"""
# text = "This cat is not calm but is quite intelligent and loving."
text =  "This is a calm, not brutal."
traits = extract_character_attributes(text)
print(traits)
"""