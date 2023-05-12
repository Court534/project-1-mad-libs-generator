def madlibs():

    # Print welcome message
    print("Welcome to my Mad Libs Generagtor!")

    # Get user input
    noun = input("Please enter a Noun: ")
    adjective = input("Please enter a Adjective: ")
    verb = input("Please enter a Verb: ")
    adverb = input("Please enter a Adverb: ")
    interjection = input("Please enter a Interjection: ")

    # Print the final Mad Lib with the users input
    print(f"""
          Once upon a time, in a faraway land, there lived a brave {noun}. This {adjective} hero had the power to 
          {verb} {adverb} and protect the innocent. One day, while wandering through the enchanted forest, the hero 
          suddenly heard a rustling sound. "Oh {interjection}!" exclaimed the hero, ready to face any danger that 
          lay ahead. With {adverb} speed, the hero dashed towards the noise, holding their {noun} tightly. Little 
          did they know, a thrilling adventure awaited them!
          """)

madlibs()

