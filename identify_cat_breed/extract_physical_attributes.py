import spacy
import re

nlp = spacy.load("en_core_web_sm")

unique_physical_attribute_mapping = {
    "Coat Color": ["white", "cream", "snow", "silver", "cream and seal", "cream and chocolate",
                   "cream and blue", "cream and lilac", "blue", "blue-gray", "red", "tabby",
                   "brown tabby", "brown", "black", "tortoiseshell", "skin-toned"],
    "Coat Pattern": ["rosetted", "spotted", "mitted", "color-point", "bicolor", "solid", "tabby",
                     "harlequin", "tortie", "no pattern"],
    # "Coat Length": ["short", "medium", "long", "hairless"],
    "Coat Length": ["hairless"],
    "Coat Texture": ["sleek", "silky", "plush", "dense and plush", "dense and woolly", "slightly coarse",
                     "luxurious", "smooth"],
    # "Size": ["small", "medium", "big", "very big"],
    "Size": [],
    "Body Type": ["muscular and athletic", "long and lean", "cobby"],
    # "Leg Length": ["short", "medium", "long"],
    "Leg Length": [],
    # "Face Shape": ["flat", "wedge-shaped", "rounded", "round", "square"],
    "Face Shape": ["flat", "wedge-shaped", "round", "square"],
    "Eye Shape": ["almond-shaped", "oval", "round"],
    "Eye Color": ["blue", "green", "blue-green", "gold", "yellow", "copper",
                  "orange", "odd-eyed", "hazel", "amber"],
    # "Ear Size": ["small", "medium", "big", "very big"],
    "Ear Size": [],
    # "Ear Shape": ["rounded", "pointed", "triangular", "tufted"],
    "Ear Shape": ["pointed", "triangular", "tufted"],
    "Tail Shape": ["plume and straight", "straight and whip-like", "tapered and whip-like",
                   "straight and slightly curved", "straight and tapered"],
    # "Tail Length": ["short", "medium", "long"]
    "Tail Length": []
}

# "small", "medium", "big", "very big", "short", "long", "rounded"
context_map = {
    "short": {"fur": "Coat Length", "coat": "Coat Length", "hair": "Coat Length",
              "legs": "Leg Length", "limbs": "Leg Length", "feet": "Leg Length",
              "tail": "Tail Length"},
    "medium": {"fur": "Coat Length", "coat": "Coat Length", "hair": "Coat Length",
               "legs": "Leg Length", "limbs": "Leg Length", "feet": "Leg Length",
               "ears": "Ear Size", "ear": "Ear Size",
               "tail": "Tail Length",
               "size": "Size"},
    "long": {"fur": "Coat Length", "coat": "Coat Length", "hair": "Coat Length",
             "legs": "Leg Length", "limbs": "Leg Length", "feet": "Leg Length",
             "tail": "Tail Length"},
    "small": {"ears": "Ear Size", "ear": "Ear Size",
              "size": "Size"},
    "big": {"ears": "Ear Size", "ear": "Ear Size",
            "size": "Size"},
    "very big": {"ears": "Ear Size", "ear": "Ear Size",
                 "size": "Size"},
    "rounded": {"face": "Face Shape", "head": "Face Shape",
                "ears": "Ear Shape", "ear": "Ear Shape"}
}

negations = [
    "not", "isn't", "isn't very", "doesn't have", "never", "no", "don't", "can't", "won't",
    "not very", "not really", "not quite", "not at all", "not so",
    "barely", "hardly", "scarcely", "neither", "nor", "not much",
    "not really", "not entirely", "not exactly"
]


def detect_negations(description):
    description = description.lower()
    negation_phrases = [neg for neg in negations if re.search(r'\b' + re.escape(neg) + r'\b', description)]
    return negation_phrases


def extract_adjectives_after_negation(description, negation_phrases):
    doc = nlp(description.lower())
    negation_adjective_dict = {}
    for negation in negation_phrases:
        negation_position = description.lower().find(negation)
        if negation_position != -1:
            negation_end_position = negation_position + len(negation)
            for token in doc:
                if token.idx > negation_end_position and token.pos_ == "ADJ":
                    negation_adjective_dict[negation] = token.text
                    break
    return negation_adjective_dict


def extract_simple_attributes(description):
    attributes = {key: "Unknown" for key in unique_physical_attribute_mapping.keys()}

    description_lower = description.lower()
    for attr, values in unique_physical_attribute_mapping.items():
        for value in values:
            if value in description_lower:
                attributes[attr] = value.capitalize()

    return attributes


def extract_attributes_with_context(description):
    attributes = {key: "Unknown" for key in unique_physical_attribute_mapping.keys()}

    description_lower = description.lower()
    for descriptor, context_words in context_map.items():
        matches = re.finditer(rf"\b{descriptor}\b (\w+)", description_lower)
        for match in matches:
            next_word = match.group(1)
            if next_word in context_words:
                attribute = context_words[next_word]
                attributes[attribute] = descriptor.capitalize()

    return attributes


def extract_physical_attributes(description):
    simple_attributes = extract_simple_attributes(description)
    context_attributes = extract_attributes_with_context(description)

    negation_phrases = detect_negations(description)
    negation_adjectives = extract_adjectives_after_negation(description, negation_phrases)

    final_attributes = {key: simple_attributes[key] if simple_attributes[key] != "Unknown" else context_attributes[key]
                        for key in simple_attributes}

    for negation, adjective in negation_adjectives.items():
        for attr in final_attributes:
            if adjective.lower() in final_attributes[attr].lower():
                final_attributes[attr] = "Unknown"

    return final_attributes
