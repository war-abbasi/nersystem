import spacy
from spacy import displacy
import json

nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str):
    """
    Extract people, organizations, and locations from raw text.
    Returns a dict with entities grouped by type.
    """
    doc = nlp(text)
    entities = {"PERSON": [], "ORG": [], "GPE": []}  # GPE = Geopolitical Entity (countries, cities)

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities

def main():
    print("📌 Named Entity Recognition (NER) System")
    print("Type or paste text, and I'll extract People, Orgs, and Locations.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter text: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        results = extract_entities(user_input)

        print("\nExtracted Entities:")
        print(json.dumps(results, indent=2))
        print()

        # Optional: visualize entities in the sentence
        # Uncomment to see colored HTML output
        # displacy.serve(nlp(user_input), style="ent")

if __name__ == "__main__":
    main()
