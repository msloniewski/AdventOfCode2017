data = dlmread('input.txt');

maxIndex = rows(data)

current = 1;
steps = 0;
while ( current >= 1 & current <= maxIndex )
	curr_back = current;

	if ( data(current) >= 3  )
		inc = -1;
	else
		inc = 1;
	endif

	current += data(current);
	data(curr_back) += inc;
	++steps;
endwhile 

steps
