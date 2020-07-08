#include <cs50.h>
#include <stdio.h>
#include <string.h>
#define MAX 9               // Max number of candidates
typedef struct              // Candidates have name and vote count
{
    string name;
    int votes;
}
candidate;
candidate candidates[MAX];      // Array of candidates
int candidate_count;             // Number of candidates
bool vote(string name);          // Function prototypes
void print_winner(void);
int main(int argc, string argv[])
s
    if (argc < 2)                   // Check for invalid usage
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }
// Populate array of candidates
    candidate_count = argc - 1;     //Candidadte count = no of CLAs - 1
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }
    int voter_count = get_int("Number of voters: ");
    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");
        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }
    // Display winner of election
    print_winner();
}
// Update vote totals given a new vote
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    if (strcmp(candidates[i].name, name) == true)
    {
        candidates[i].votes++;
        return true;
    }
    return false;
} // TO DO
// Print the winner (or winners) of the election
void print_winner(void)
{
    int most_votes = 0;
    int i = 0;
    for (i = 0; i < candidate_count; i++) // TODO
        if (candidates[i].votes > most_votes)
        {
            most_votes = candidates[i].votes;
        }
    printf("Winner(s): %s",candidates[i].name);
    return;
}
