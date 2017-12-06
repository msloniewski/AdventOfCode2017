#include <iostream>
#include <fstream>
#include <vector>

using namespace std; 
//0 if the same 1 if different
int compare (const vector<int> &a, const vector<int> &b)
{
	for (int i=0; i < a.size(); i++)
	{
		if (a[i] != b[i])
			return 1;
	}
	return 0;
}

int findBiggest (const vector<int> &a)
{
	int comp =0;
	int index =0;
	for (int i=0; i< a.size(); i++)
	{
		if (a[i]> comp)
		{
			comp = a[i];
			index =i;
		}
	}
	return index;
}
int haveISeenItBefore(const vector<int> &a, const vector<vector<int>> &b)
{
	for (int i=0 ; i< b.size();i++)
	{
		if ( !compare(a,b[i]) )
			return 1;
	}
	return 0;
}
int main()
{
	ifstream input("input.txt");

	vector<int> current {10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6};
	vector<vector<int>> previous;

	
	int no = 0;
	while ( !haveISeenItBefore(current, previous) )
	{	
		previous.push_back(current);
		int index = findBiggest( current );
		int toDo = current[index];
		current[index] = 0;
		while(toDo > 0)
		{
			index = (index +1)% current.size();
			current[index] ++;
			toDo--;
		}
		no++;
	}
	cout<<"numb:"<<no<<endl;
	
	
}
