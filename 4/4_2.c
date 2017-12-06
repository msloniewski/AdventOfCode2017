#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUM_WORDS 20

int compare(char* a, char*b)
{
	if ( strlen(a) != strlen(b) )
		return 1;

	int alphabet_a[26];
	int alphabet_b[26];
	int i = 0;
	for (i = 0; i< 26 ; i++)
	{
		alphabet_a[i] = 0;
		alphabet_b[i] = 0;
	}
	
	i =0;
	while (a[i] != 0)
	{
		alphabet_a[a[i]-97]++;
		i++;
	}
	i=0;
	while (b[i] != 0)
	{
		alphabet_b[b[i]-97]++;
		i++;
	}
	int flag = 0;
	for (i=0;i<26; i++)
	{
		if (alphabet_a[i] != alphabet_b[i])
		{

			flag = 1;
			return flag;
		}
	}
	return flag;
}
int main()
{
	FILE *file = fopen("input.txt", "r");
	char line[256];
	
	char *words[MAX_NUM_WORDS];
	char *currentWord = NULL;
	int noOfWords = 0;
	int i=0;
	int j=0;
	int Passphrases = 0;
	int flag = 0;
	int all =0;
	for (i=0; i< MAX_NUM_WORDS; i++)
	{
		words[i] = malloc(sizeof(char)*90);
	}

	while (fgets(line, sizeof(line), file))
	{

		noOfWords = 1;

		currentWord = strtok(line," ");
		while (currentWord != NULL  )
		{
			strcpy(words[noOfWords],currentWord);
			noOfWords++;
			currentWord = strtok(NULL," ");
		}
		//strcpy(words[noOfWords],line);

		int len = strlen(words[noOfWords-1]);
		if ( words[noOfWords-1][len-1] == 10 ) //Line feed
		{
			words[noOfWords-1][len-1] =0;
		}

		flag = 0;
		for (i=1; i< noOfWords-1 ; i++)
		{
			for (j=i+1; j< noOfWords; j++)
			{
				if ( !compare( words[i], words[j]) )
				{
					flag = 1;
				}
				
			}

		}
		if ( !flag)  
			Passphrases++;
		all++;
		
	}

	printf("ans %d\n",Passphrases);
	printf("all %d\n",all);

	fclose(file);
	while (i=0, i< MAX_NUM_WORDS, i++)
	{
		free (words[i]);
	}

}
