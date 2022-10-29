import requests

def get_meaning(word):
    w = word.lower()
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{w}"

    response = requests.get(api_url)
    response.encoding = 'utf-8'
    content = response.json()
    
    try:
        report = content[0]['meanings']
        print(f"\nDefinitions for {word} ---->>>>\n")

        for r in range(len(report)):

            part_of_speech = report[r]['partOfSpeech']
            word_meanings = report[r]['definitions']
            print(f"\nPART OF SPEECH : ||{part_of_speech}||")

            for wm in word_meanings:
                try:
                    definition = wm['definition']
                    example = wm['example']
                    synonyms = wm['synonyms']
                    antonyms = wm['antonyms']

                    print(f"\nMEANING : {definition}")
                    print(f"EXAMPLE : {example}")

                    if len(synonyms) > 0:
                        print(f"SYNONYMS : {synonyms}")

                    if len(antonyms) > 0:
                        print(f"ANTONYMS : {antonyms}")

                except KeyError:
                    pass

    except KeyError:
        print("!! Please check the spellings.")

