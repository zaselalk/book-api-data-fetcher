import random


def generate_description(times=1):
    adjectives = ["captivating", "entertaining", "thought-provoking", "fascinating",
                  "compelling", "intriguing", "gripping", "mesmerizing", "unputdownable", "spellbinding"]
    nouns = ["story", "tale", "narrative", "book",
             "novel", "fiction", "work", "prose", "literature"]
    verbs = ["will keep you", "will leave you", "will take you", "will transport you",
             "will captivate you", "will mesmerize you", "will leave a lasting impression on you"]

    sentences = []
    for _ in range(times):
        sentence = f"This {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}."
        sentences.append(sentence)

    description = "".join(sentences)
    return description
