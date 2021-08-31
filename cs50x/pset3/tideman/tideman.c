#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool check_cycle(int locked_pairs, int original_pair, int current_pair, int locked_winners_index[]);
bool is_circle(int winner, int loser);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
            //printf("Ranks: %i\n", ranks[j]); //JUST TO ENSURE RANKS IS RECORDING PROPERLY
        }
        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    //check that name exists
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcasecmp(name, candidates[i]) == 0)
        {
            //add the name to ranks[i]
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // Updating the 2d array
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]] += 1;
        }
    }
    // Visulizing the array
    /*for( int i=0; i<candidate_count; i++) {
      for(int j=0;j<candidate_count;j++) {
         printf("%d ", preferences[i][j]);
         if(j==candidate_count - 1){
            printf("\n");
         }
      }
    }*/
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    //Looping over each candidate (i), then each voters preference (j)
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            //Checking which was more preferred
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
            else if (preferences[i][j] < preferences[j][i])
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count++;
            }
            //printf("winner: %i loser: %i\n", pairs[pair_count - 1].winner, pairs[pair_count - 1].loser);
        }
    }

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        //resetting the linear search vairbles
        int largest_index = i;
        int largest_number_winner = pairs[i].winner;
        int largest_number_loser = pairs[i].loser;
        //Checking that it is sorted
        for (int h = 0; h < pair_count; h++)
        {
            printf("%i ---> ", pairs[h].winner);
            printf("%i ||| ", pairs[h].loser);
        }
        //Linear search
        for (int j = i; j < pair_count; j++)
        {
            if (preferences[pairs[largest_index].winner][pairs[largest_index].loser] < preferences[pairs[j].winner][pairs[j].loser])
            {
                largest_index = j;
                largest_number_winner = pairs[j].winner;
                largest_number_loser = pairs[j].loser;
            }
        }
        //Swapping the first and largest number
        //printf("largest number: %i\n", largest_number);
        pairs[largest_index].winner = pairs[i].winner;
        pairs[largest_index].loser = pairs[i].loser;
        pairs[i].winner = largest_number_winner;
        pairs[i].loser = largest_number_loser;
        printf("\n");
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    int locked_pairs = 0;

    int locked_winners_index[locked_pairs];

    for (int i = 0; i < pair_count; i++)
    {
        /*if (is_circle(pairs[i].winner, pairs[i].loser) == false)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
        */

        if (check_cycle(locked_pairs, i, i, locked_winners_index) == true)
        {
            locked_winners_index[locked_pairs] = pairs[i].winner;
            locked[pairs[i].winner][pairs[i].loser] = true;
            locked_pairs++;
        }
    }






    // Visulizing the array
    printf("Locked Array\n");
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            printf("%d ", locked[i][j]);
            if (j == candidate_count - 1)
            {
                printf("\n");
            }
        }
    }

    return;
}

// Print the winner of the election
void print_winner(void)
{
    // Vairible to count how many wins are on each y axis
    bool locked_y[candidate_count];
    // Vairble for counting each x axis
    int x_count = 0;
    // Vairble for election winner
    int election_winner;
    //looping over the locked array
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            //if a vertical column is all false then that is the winner
            if (locked[j][i] == false)
            {
                x_count++;
            }
        }
        if (x_count == candidate_count)
        {
            election_winner = i;
        }
        x_count = 0;
    }
    printf("%s\n", candidates[election_winner]);

    return;
}





bool check_cycle(int locked_pairs, int original_pair, int current_pair, int locked_winners_index[])
{

    if (locked_pairs == 0)
    {
        return true;
    }


    for (int i = 0; i <= locked_pairs; i++)
    {

        if (pairs[current_pair].loser == locked_winners_index[i])
        {
            if (pairs[i].loser == pairs[original_pair].winner)
            {
                return false;
            }
            else if (check_cycle(locked_pairs - 1, original_pair, i, locked_winners_index) == false)
            {
                return false;
            }

        }

    }

    //locked_winners_index[locked_pairs] = pairs[original_pair].winner;
    return true;
}


bool is_circle(int winner, int loser)
{

    while (winner != -1 && winner != loser)
    {
        bool found = false;

        for (int i = 0; i < candidate_count; i++)
        {
            if (locked[i][winner])
            {
                found = true;
                winner = i;
            }
        }

        if (!found)
        {
            winner = -1;
        }

    }

    if (winner == loser)
    {
        return true;
    }

    return false;
}

