#include <stdio.h>
#include <cs50.h>

void mario(int h);



int main(void)
{
//Gets the desired height
int height =0;
do
{
    height = get_int("Height: ");
}
while (height > 8 || height < 1);

//calls the fuction
mario(height);
}



void mario(int h)
{
    for(int i = 0; i < h; i++) // Creates a loop the length of height and returns a new line at the end
    {
        int d = h - i; // Creates a vairible that gets smaller rather than bigger
        for(int j = i; j < h - 1; j++) //Prints spaces for as many times as height minus one
        {
            printf(" ");
        }
        for(int w = d; w <= h; w++) //Prints # using the d vairble that gets smaller; therefore increasing the gap between d and height so it prints more #s
        {
            printf("#");
        }
        for(int e = 0; e < 2; e++) //Prints two spaces one every line
        {
            printf(" ");
        }
        for(int r = d; r <= h; r++) //Prints # using the same d vairable as line 30
        {
            printf("#");
        }
        printf("\n");
    }
}