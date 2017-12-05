#!/usr/bin/lua5.1


function add(x,y)
	sum=0
	for i_l = -1,1,1 do
		for j_l = -1,1 do
			if ( mat[x+i_l][y+j_l] ~= nil ) then
				in_x = x+i_l
				in_y= y+j_l
				sum = sum + mat[in_x][in_y]
			end
		end
	end
	mat[x][y]=sum
	last_val =sum
	io.write( x, " ", y, " " , sum,"\n")
end

threshold = 265149
--threshold = 2
n = 2

side = 2

last_val=1 
	
mat={}
for i=-1000,1000 do
	mat[i] = {}
end

curr_x = 0
curr_y = 0
mat[0][0] = 1

while (last_val < threshold) do
	curr_x=curr_x + 1
	curr_y=curr_y - 1

	mult_x = -1
	mult_y = 1
	for h=1,2 do

			for k=1,side do
				curr_y = curr_y + mult_y 
				add(curr_x,curr_y)
				n=n+1
				if last_val > threshold then break end
			end
			if last_val > threshold then break end


			for k=1,side do
				curr_x =curr_x + mult_x  
				add(curr_x,curr_y)
				n=n+1
				if last_val > threshold then break end
			end
			if last_val > threshold then break end

		mult_x = 1
		mult_y = -1
		if last_val > threshold then break end
	end

	side =side+2
end


io.write( n, "index\n")
io.write( last_val, "val bigger\n")
