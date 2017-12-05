#!/usr/bin/lua5.1

threshold = 265149
n = 0
val = 1

while (val < threshold)
then 
	rad = 0
	while ( ( 2 * rad + 1  )^2 < n)
	do
		rad = rad +1
	end
	side = 2 * rad 
	offset = n - ( rad * 2 - 1 )^2 - 1
	offset2 = offset % side  
	
	side_num = floor (offset / side)

	if side_num == 0 
		then asd
	elseif	side_num == 1
		then asdasd
	elseif side_num == 2
		then asdasd
	elseif  side_num == 3
		then asdasd
	end
	
	if offset == 0 
	then
		asdasd
	end 
	if offset == side -1
	then 
		asdasdasd
	end
	
	if offset == side -2 
	then 
		asdasdasdasd
	end


	else 


--	val = tab[n-1]
	
	n += 1 --lets gooo
end


io.write( n  , "n\n")
io.write( side  , "side\n")
io.write( offset , "offset\n")
io.write( offset2 , "offset2\n")
io.write( distance , "distance\n")

--      36  35  34  33  32  
-- 17   16  15  14  13  30 
-- 18    5   4   3  12  29
-- 19    6   1   2  11  28
-- 20    7   8   9  10  27
-- 21   22  23  24  25  26
--
--
