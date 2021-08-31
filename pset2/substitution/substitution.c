#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

bool check_alpha(string key);
bool check_repitition(string key);
void translate(string key, string sentence);

int main(int argc, string argv[])
{
    if (argc == 1)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }
    else if (check_alpha(argv[1]) == false)
    {
        printf("Only letters\n");
        return 1;
    }
    else if (check_repitition(argv[1]) == false)
    {
        printf("No repeating letters\n");
        return 1;
    }



    string plaintext = get_string("plaintext:  ");
    printf("ciphertext: ");
    translate(argv[1], plaintext);

    return 0;
}



bool check_alpha(string key)
{
    int text_length = strlen(key);
    bool check = true;
    for (int i = 0; i < text_length; i++)
    {
        if (isalpha(key[i]))
        {
            check = true;
        }
        else
        {
            check = false;
            i = text_length;
        }
    }
    return check;
}



bool check_repitition(string key)
{
    int text_length = strlen(key);
    bool check = true;
    for (int i = 0; i < text_length; i++)
    {
        for (int x = 0; x < i; x++)
        {
            if (((int) key[i] == (int) key[x]) || ((int) key[i] == (int) key[x] + 32) || ((int) key[i] == (int) key[x] - 32))
            {
                x = i;
                check = false;
            }
            else
            {
                check = true;
            }
        }

        if (check == false)
        {
            i = text_length;
        }
    }
    return check;
}



void translate(string key, string sentence)
{
    int text_length = strlen(sentence);
    char ciphertext[text_length];
    string abc = "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < text_length; i++)
    {
        if (isalpha(sentence[i]) == 0)
        {
            ciphertext[i] = sentence[i];
            printf("%c", ciphertext[i]);
        }
        for (int x = 0; x < 26; x++)
        {
            bool uppercase = isupper(sentence[i]);
            if ((int) tolower(sentence[i]) == (int) abc[x])
            {
                if (uppercase == false)
                {
                    ciphertext[i] = tolower(key[x]);
                    printf("%c", ciphertext[i]);
                    x = 26;
                }
                else if (uppercase == true)
                {
                    ciphertext[i] = toupper(key[x]);
                    printf("%c", ciphertext[i]);
                    x = 26;
                }
            }
        }
    }
    printf("\n");
}
