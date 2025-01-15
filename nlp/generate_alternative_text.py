import nltk
from nltk.corpus import wordnet as wn
import random
import re
import math
import rowordnet as rwn
from nlp.detect_language import detect_language
from nlp.find_abbreviation import find_abbreviation
from nlp.find_language import find_language


def get_synonyms(word, language):
    synonyms = set()
    for syn in wn.synsets(word, lang=language):
        for lemma in syn.lemmas(lang=language):
            synonyms.add(lemma.name())
    return list(synonyms)


def get_antonyms(word, language):
    antonyms = set()
    for syn in wn.synsets(word, lang=language):
        for lemma in syn.lemmas(lang=language):
            for antonym in lemma.antonyms():
                antonyms.add(antonym.name())
    return list(antonyms)


def get_hypernyms(word, language):
    hypernyms = set()
    for syn in wn.synsets(word, lang=language):
        for hypernym in syn.hypernyms():
            for lemma in hypernym.lemmas(lang=language):
                hypernyms.add(lemma.name())
    return list(hypernyms)


def get_synonyms_ro(word):
    wnn = rwn.RoWordNet()

    synonyms = set()

    synset_ids = wnn.synsets(literal=word)

    for synset_id in synset_ids:
        synset_object = wnn.synset(synset_id)

        synonyms_from_literals = synset_object.literals

        for synonym in synonyms_from_literals:
            synonyms.add(synonym)
    print(list(synonyms))
    return list(synonyms)


def get_antonyms_ro(word):
    antonyms = set()

    wn = rwn.RoWordNet()
    synsets_id = wn.synsets(literal=word)

    for synset_id in synsets_id:
        synset = wn(synset_id)

        synset_outbound_id = wn.outbound_relations(synset.id)
        synset_antonyms_id = [synset_tuple[0] for synset_tuple in synset_outbound_id
                              if synset_tuple[1] == 'near_antonym']

        for synset_antonym_id in synset_antonyms_id:
            synset_object = wn(synset_antonym_id)

            antonyms_from_literals = synset_object.literals

            for antonym in antonyms_from_literals:
                antonyms.add(antonym)

    return list(antonyms)


def get_hypernyms_ro(word):
    hypernyms = set()

    wn = rwn.RoWordNet()
    synsets_id = wn.synsets(word)

    for synset_id in synsets_id:
        synset = wn.synset(synset_id)

        synset_outbound_id = wn.outbound_relations(synset.id)
        hypernyms_id = [synset_tuple[0] for synset_tuple in synset_outbound_id
                        if synset_tuple[1] == 'hypernym']

        for hypernym_id in hypernyms_id:
            hypernym_object = wn.synset(hypernym_id)

            for hypernym in hypernym_object.literals:
                hypernyms.add(hypernym)

    return list(hypernyms)


def replace_word(word, language):
    """
    if language == "ron":
         synonyms = get_synonyms_ro(word)
         antonyms = get_antonyms_ro(word)
         hypernyms = get_hypernyms_ro(word)
         print(synonyms)
         print(antonyms)
         print(hypernyms)
    else:
         synonyms = get_synonyms(word, language)
         antonyms = get_antonyms(word, language)
         hypernyms = get_hypernyms(word, language)
    """
    synonyms = get_synonyms(word, language)
    antonyms = get_antonyms(word, language)
    hypernyms = get_hypernyms(word, language)

    if synonyms:
        return random.choice(synonyms), True
    elif antonyms:
        return random.choice(antonyms), True
    elif hypernyms:
        return random.choice(hypernyms), True

    return word, False


def generate_alternative_text(text):
    lines = text.split("\n")
    modified_lines = []

    abbreviation, probability = detect_language(text)
    language = find_language(abbreviation)

    stopwords = set(nltk.corpus.stopwords.words(language))

    abbreviations = find_abbreviation(abbreviation)
    # print(abbreviations)

    if len(abbreviations) > 1 and (isinstance(abbreviations[len(abbreviations) - 1], str)
                                   or math.isnan(abbreviations[len(abbreviations) - 1]) == False):
        lang = abbreviations[len(abbreviations) - 1]
    else:
        lang = abbreviations[0]

    # print(lang)

    for line in lines:
        words = nltk.word_tokenize(line)
        filtered_words = [word for word in words if word not in stopwords]

        # print(words)
        total_words = len(words)
        modified_count = 0
        modified_words = []
        # print(total_words)

        required_modified_count = int(total_words * 0.2)
        # print(required_modified_count)

        for word in words:
            if re.match(r"^[a-zA-Z'-]+$", word) and word in filtered_words:
                replaced_word, was_modified = replace_word(word, lang)
                if was_modified:
                    modified_count += 1
                    modified_words.append(replaced_word)
                else:
                    modified_words.append(replaced_word)
            else:
                modified_words.append(word)

        # print(modified_count)

        if modified_count < required_modified_count:
            modified_count = 0
            modified_words = []
            for word in words:
                if re.match(r"^[a-zA-Z'-]+$", word):
                    replaced_word, was_modified = replace_word(word, lang)
                    if was_modified:
                        modified_count += 1
                        modified_words.append(replaced_word)
                    else:
                        modified_words.append(replaced_word)
                else:
                    modified_words.append(word)

        # print(modified_count)

        modified_lines.append(" ".join(modified_words))

    modified_text = "\n".join(modified_lines)
    return modified_text
