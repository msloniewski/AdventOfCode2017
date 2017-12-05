#!/usr/bin/lua5.1

element = 11
element = 265149
n = 0

while ( ( 2 * n + 1  )^2 < element)
do
	n = n+1
end

side = 2*n 

offset = element - ( n * 2 - 1 )^2 - 1
if offset > side
then 
	offset2 = offset % side  
else 
	offset2 = offset 
end

if offset2 <= side / 2 -1
then
	distance = n + ( n - 1 ) - offset2
else
	distance = n + (  offset2 -side/2 +1) 
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
