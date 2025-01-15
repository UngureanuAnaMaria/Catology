import openai

openai.api_key = "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"


def compare_breeds_openai(breed1, breed2):
    prompt = (
        f"""Provide a detailed, side-by-side comparison of the {breed1} cat breed and the {breed2} cat breed.
            Discuss their physical traits in detail, such as coat color, body size, shape, and facial features.
            Describe their personalities, including their interaction with humans, behavior around other animals, and their temperament.
            Include their origins, history, and any unique traits that distinguish these two breeds from one another.
        """
        )

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in cat breeds."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000,
            top_p=0.9,
            frequency_penalty=0.0,
            presence_penalty=0.6
        )

    return response.choices[0].message['content']
