#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int count_letters(string sentence);
int count_words(string sentence);
int count_sentences(string sentence);



int main(void)
{
    string text = get_string("Text: ");

    float L = ((float) count_letters(text) * 100) / (float) count_words(text);
    float S = ((float) count_sentences(text) * 100) / (float) count_words(text);
    float index = (0.0588 * L) - (0.296 * S) - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if ((1 < index) && (index < 16))
    {
        printf("Grade %.0f\n", index);
    }
    else
    {
        printf("Grade 16+\n");
    }
}



int count_letters(string sentence)
{
    int text_length = strlen(sentence);
    int number_of_letters = 0;
    for (int i = 0; i <= text_length; i++)
    {
        if (isalpha(sentence[i]))
        {
            number_of_letters++;
        }
    }
    return number_of_letters;
}



int count_words(string sentence)
{
    int text_length = strlen(sentence);
    int number_of_words = 0;
    for (int i = 0; i <= text_length; i++)
    {
        if (isspace(sentence[i]))
        {
            number_of_words++;
        }
    }
    return number_of_words + 1;
}



int count_sentences(string sentence)
{
    int text_length = strlen(sentence);
    int number_of_sentences = 0;
    for (int i = 0; i <= text_length; i++)
    {
        if ((int) sentence[i] == 33 || (int) sentence[i] == 46 || (int) sentence[i] == 63)
        {
            number_of_sentences++;
        }
    }
    return number_of_sentences;
}



