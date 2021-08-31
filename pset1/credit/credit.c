#include <stdio.h>
#include <cs50.h>

int check_length(long integer);
bool iterate(long integer);
void check_visa13(long integer13);
int check_visa16(long integer16);
void check_mastercard(long integer16);
void check_Amex(long integer15);


int main(void)
{
    long card_number = get_long("Number: ");
    int length = check_length(card_number);
    bool key = iterate(card_number);
    if (key == true)
    {
        if (length == 16)
        {
            int zero_or_one = check_visa16(card_number);
            if (zero_or_one == 1)
            {
                check_mastercard(card_number);
            }
        }
        else if (length == 15)
        {
            check_Amex(card_number);
        }
        else if (length == 13)
        {
            check_visa13(card_number);
        }
        else
        {
            printf("INVALID\n");
        }
    }

}


//CHECKS THE LENGTH OF AN INTEGER 13 - 16

int check_length(long integer)
{
    int length;
    for (long i = 1000000000000; i <= 1000000000000000; i = i * 10)
    {
        long x = integer / i;
        if (0 < x && x < 10 && i == 1000000000000)
        {
            length = 13;
        }
        else if (0 < x && x < 10 && i == 10000000000000)
        {
            length = 14;
        }
        else if (0 < x && x < 10 && i == 100000000000000)
        {
            length = 15;
        }
        else if (0 < x && x < 10 && i == 1000000000000000)
        {
            length = 16;
        }
    }
    return length;
}


/*FUNCTION FOR CHECKING 16 DIGIT VISA*/

int check_visa16(long integer16)
{
    int result = 0;
    long y = 0;
    for (long i = 10000000000000000; i <= 10000000000000000; i = i * 10)
    {
        long x = integer16 % i;
        x = x - y;
        x = x / (i / 10);
        y = x;
        if (x == 4)
        {
            printf("VISA\n");
        }
        else
        {
            result = 1;
        }
    }
    return result;
}


/*FUCNTION FOR CHECKING 13 DIGIT VISA*/

void check_visa13(long integer13)
{
    long y = 0;
    for (long i = 10000000000000; i <= 10000000000000; i = i * 10)
    {
        long x = integer13 % i;
        x = x - y;
        x = x / (i / 10);
        y = x;

        if (x == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
}


/*FUNCTION FOR CHECKING MASTERCARD*/

void check_mastercard(long integer16)
{
    int n1 = 0;
    long y = 0;
    for (long i = 1000000000000000; i < 100000000000000000; i = i * 10)
    {
        long x = integer16 % i;
        x = x - y;
        x = x / (i / 10);
        y = x;


        if (x > 0 && x < 6 && i == 1000000000000000)
        {
            n1 = 1;
        }
        else if (x == 5 && n1 == 1 && i == 10000000000000000)
        {
            printf("MASTERCARD\n");
        }
        else if (i == 10000000000000000)
        {
            printf("INVALID\n");
        }
    }
}


/*FUNCTION FOR CHECKING AMEX*/

void check_Amex(long integer15)
{
    long y = 0;
    int n1 = 0;
    for (long i = 100000000000000; i < 10000000000000000; i = i * 10)
    {
        long x = integer15 % i;
        x = x - y;
        x = x / (i / 10);
        y = x;

        if ((x == 4 || x == 7) && i == 100000000000000)
        {
            n1 = 1;
        }
        else if (x == 3 && n1 == 1 && i == 1000000000000000)
        {
            printf("AMEX\n");
        }
        else if (i == 1000000000000000)
        {
            printf("INVALID\n");
        }
    }
}


/*LUNS ALGO*/

bool iterate(long integer)
{
    //This loops through the number starting at the second to last number and multiplies those numbers by 2
    long number = 0;
    long number3 = 0;
    for (long iter = 100; iter < 100000000000000000; iter = iter * 100)
    {
        long number2 = integer % iter;
        number2 = number2 - number;
        number2 = number2 / (iter / 10);
        number = number2;
        number2 = number2 * 2;

        //This takes any numbers that are larger than 9 and breaks them up so their individual digets can be added
        if (number2 > 9)
        {
            long number4 = 0;
            for (long iteration = 10; iteration <= 100; iteration = iteration * 10)
            {
                long numberi = number2 % iteration;
                numberi = numberi - number4;
                numberi = numberi / (iteration/ 10);
                number4 = numberi;
                number3 = number3 + numberi;
                //printf("Ni - 1  %li\n", numberi);
            }
        }
        else
        {
            number3 = number3 + number2;
        }

        //printf("N2 %li\n", number2);
        //printf("N3 %li\n", number3);

    }


    //this loops through to get the other numbers
    long numbery = 0;
    for (long iterate3 = 10; iterate3 < 100000000000000000; iterate3 = iterate3 * 100)
    {
        long numberx = integer % iterate3;
        numberx = numberx - numbery;
        numberx = numberx / (iterate3 / 10);
        numbery = numberx;
        number3 = number3 + numberx;
        //printf("%li\n", numberx);
        //printf("n3 -- %li\n", number3);
    }
    int valid = number3 % 10;
    if (valid == 0)
    {
        return true;
    }
    else
    {
        printf("INVALID\n");
        return false;
    }
}
