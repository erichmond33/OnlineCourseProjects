from cs50 import get_string


def main():
    # User Input
    text = get_string("Text: ")
    
    # Vairble to store letters
    nof_letters = 0
    # Vairble to store words
    nof_words = 1
    # Vairble to store sentences
    nof_sentences = 0
    
    # Determining the number of words, letters, and sentences
    for c in text:
        if (c.isalpha()):
            nof_letters += 1
        elif (c.isspace()):
            nof_words += 1
        elif ((c == ".") or (c == "!") or (c == "?")):
            nof_sentences += 1

    # Claculating L
    L = (nof_letters * 100) / nof_words
    # Calculating S
    S = (nof_sentences * 100) / nof_words
    # Getting the index
    Liau_Index = 0.0588 * L - 0.296 * S - 15.8
    
    # determining what the Liau Index is and giving the correct responses
    if (round(Liau_Index) < 1):
        print("Before Grade 1")
    elif ((round(Liau_Index) >= 1) and (round(Liau_Index) < 16)):
        print(f"Grade {round(Liau_Index)}")
    else:
        print("Grade 16+")

  
main()