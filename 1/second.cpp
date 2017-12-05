#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream input("input.txt");

	char inp_parse;
	vector<int> input_vec;
	int current;
	long sum = 0;


	while (!input.eof())
	{
		input>>inp_parse;
		current = inp_parse - '0';
		if (!input.eof())
		{
			input_vec.push_back(current);
		}
	}

	int half_way = input_vec.size()/2;

	for (int i=0; i < input_vec.size(); i++)
	{
		if(input_vec[i] == input_vec[(i+half_way)%input_vec.size()])
		{
			sum += input_vec[i];
		}
	}
	cout<<"sum"<<sum<<endl;
	return 0;
}
