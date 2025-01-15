import spacy
import rowordnet
from colorama import Fore, Style
from rowordnet import Synset
import random

nlp = spacy.load("ro_core_news_sm")
rown = rowordnet.RoWordNet()


def str_to_synset_pos(pos_str: str):
    synset_pos_map = {
        "NOUN": Synset.Pos.NOUN,
        "VERB": Synset.Pos.VERB,
        "ADV": Synset.Pos.ADVERB,
        "ADJ": Synset.Pos.ADJECTIVE,
    }
    if pos_str in synset_pos_map:
        return synset_pos_map[pos_str]
    return None


def generate_replaced_text(text: str):
    """
    This function takes a text as input and returns the text with words replaced
    based on synonyms, hypernyms, and antonyms using WordNet and the Lesk algorithm.

    Parameters:
        text (str): The input text to process.

    Returns:
        str: The processed text with replaced words.
    """
    doc = nlp(text)
    replaced_words: list[str] = []

    def append_word_with_space(arr, word, pos=None):
        if pos != "PUNCT" and len(arr) > 0 and word[0] != "-" and arr[-1][-1] != "-":
            replaced_words.append(" ")
        replaced_words.append(word)

    for token in doc:
        synsets = rown.synsets(token.lemma_, pos=str_to_synset_pos(token.pos_), strict=True)
        if not synsets:
            append_word_with_space(replaced_words, token.text, token.pos_)
            continue

        synonyms = [
            literal for ss in synsets for literal in rown.synset(ss).literals if literal.strip() != token.text.strip()
        ]

        outbound_relations = [x for ss in synsets for x in rown.outbound_relations(ss)]
        hypernym_synsets = [ss for ss, relation in outbound_relations if relation == "hypernym"]
        antonym_synsets = [ss for ss, relation in outbound_relations if relation in {"antonym", "near_antonym"}]
        hypernyms = [literal for ss in hypernym_synsets for literal in rown.synset(ss).literals]
        not_antonyms = ["nu " + literal for ss in antonym_synsets for literal in rown.synset(ss).literals]

        possible_words = [*synonyms, *hypernyms, *not_antonyms]
        if not possible_words or random.randint(0, 4) != 0:
            append_word_with_space(replaced_words, token.text, token.pos_)
            continue

        final_word = (
            possible_words[random.randint(0, len(possible_words) - 1) if len(possible_words) > 1 else 0]
            .replace("_", " ")
            .replace("[", "")
            .replace("]", "")
            .replace("|", "")
        )
        append_word_with_space(replaced_words, final_word, token.pos_)

    replaced_words_result = "".join(replaced_words)
    print(f"\n{Fore.BLUE}Modified text:{Style.RESET_ALL}")
    print(replaced_words_result)
    print('\n')
    return replaced_words_result
