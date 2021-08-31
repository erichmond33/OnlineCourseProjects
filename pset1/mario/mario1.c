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
for(int i = 0; i < h; i++)
{
    for(int b = 0; b <=  h - 1; b++)
    {
        if(i % 2 == 0)
        {
            printf("#");

            if((i != b - 1) && (h % 2 != 1))
            {
                printf(" ");
            }
        }
        else if((i != b - 1) && (h % 2 != 1))
        {
            printf(" ");
            if(i != b - 1)
            {
                printf("#");
            }
        }

    }
    printf("\n");




}




}
