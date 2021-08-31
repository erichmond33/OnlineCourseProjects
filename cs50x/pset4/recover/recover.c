#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    //Ensuring the user uses the program properly
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    //Number of files created so far
    int nof_files = 0;
    //An unsigned intger defined as BYTE
    typedef uint8_t BYTE;
    //Opening the file
    FILE *card = fopen(argv[1], "r");
    //Making sure it opens correctly?
    if (card == NULL)
    {
        return 1;
    }
    //Creating an array of 512 BYTES
    BYTE buffer[512];
    //Vairble that will change names with each file
    char *file_name = malloc(7);

    //Looping through the entire file
    while (fread(buffer, sizeof(BYTE), 512, card) == 512)
    {
        //Checking for a jpg
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
        {
            //Changing file_name to ###.jpg
            sprintf(file_name, "%03i.jpg", nof_files);
            //Opening that file
            FILE *file_block = fopen(file_name, "w");
            //Writing a 512 byte chuck to it
            fwrite(buffer, sizeof(BYTE), 512, file_block);
            //Closing the file
            fclose(file_block);
            //Adding one to nof_files
            nof_files++;
        }
        //If a file has already been created but the header isn't the start of a new jpg
        else if (nof_files != 0)
        {
            //Open file
            FILE *file_block = fopen(file_name, "a");
            //Append the new 512 byte chunk
            fwrite(buffer, sizeof(BYTE), 512, file_block);
            //close file
            fclose(file_block);
        }
    }

    //close card
    fclose(card);
    //free the malloc memory
    free(file_name);


}