#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream input("input.txt");

	char inp_parse;
	int  current,  first, previous;

	long sum = 0;

	input >> inp_parse;
	first = inp_parse - '0';
	previous = first;

	while (!input.eof())
	{
		input>>inp_parse;
		current = inp_parse - '0';
		if (!input.eof())
		{
			if(current == previous)
			{
				sum += current;
			}
			previous = current;
			cout << "prev" << previous << "curr" << current;
		}
	}
	if (current == first)
	{
		sum += current;
	}
	cout << "suma:" <<sum << endl;
	return 0;
}
