data = dlmread('input.txt');

maxIndex = rows(data)

current = 1;
steps = 0;
while ( current >= 1 & current <= maxIndex )
	curr_back = current;
	current += data(current);
	++data(curr_back);
	++steps;
	
endwhile 

steps
