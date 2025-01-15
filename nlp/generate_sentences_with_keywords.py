import spacy
import re
import openai

nlp = spacy.load("ro_core_news_sm")

openai.api_key = "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"

def extract_keywords(text):
    doc = nlp(text)
    keywords = set([token.text for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ"] and not token.is_stop])
    print(f"Keywords: {keywords}")
    return keywords


def generate_sentences(keywords):
    for keyword in keywords:
        prompt = f'O propoziție conținând cuvântul "{keyword}" este:'

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Ești un asistent care creează propoziții concise în limba română."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=50,
                temperature=0.7
            )

            generated_text = response['choices'][0]['message']['content'].strip()
            print(f'\nPropoziție generată pentru cuvântul "{keyword}":')
            sentence_match = re.match(r'(\"([^"]+)\")|([^.?!]*[.?!])', generated_text)
            if sentence_match:
                sentence = sentence_match.group(0).strip('"')
                if sentence[-1] not in {".", "?", "!"}:
                    sentence += "."
                print(sentence)
            else:
                print(generated_text)
        except Exception as e:
            print(f"Eroare la generarea propoziției pentru cuvântul '{keyword}': {e}")


input_text = "Pisica mea este foarte independentă, agilă și are o blană scurtă."


keywords = extract_keywords(input_text)
generate_sentences(keywords)

