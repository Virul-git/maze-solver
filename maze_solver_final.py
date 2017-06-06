import numpy as np 

img =[  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
	    [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
	    [0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
	    [0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
	    [0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,9,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
		[0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],\
		[0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]]
#               1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1	

cor =[  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],\
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],\
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]]	
#################################################################################################
####   the start pixel is mentioned and the end pixel is given the value 9            #######
start_pixel=[1,4]
#############################################################################################
####           for movement of the object along the maze         ############################
#############################################################################################

###### functions for movement ###### 
####################################



def keep_moving(x,y):
	global img
	global cor
	if(cor[y][x]==4):
		return False
	if(img[y][x]==0 or cor[y][x]==3):
		cor[y][x]==4
		return False
	if(img[y][x]==9):
		img[y][x]=4
		return True
	cor[y][x]=3
	if x !=0:
		if keep_moving(x-1,y):
			cor[y][x]=4
			return True
	if x !=0 and y !=0:
		if keep_moving(x-1,y-1):
			cor[y][x]=4
			return True
	if y !=0:
		if keep_moving(x,y-1):
			cor[y][x]=4
			return True		
	if x !=len(img[1])-1 and y!=0:
		if keep_moving(x+1,y-1):
			cor[y][x]=4
			return True								
	if x !=len(img[1])-1:
		if keep_moving(x+1,y):
			cor[y][x]=4
			return True		
	if y !=len(img)-1 and x != len(img[1])-1:
		if keep_moving(x+1,y+1):
			cor[y][x]=4
			return True					
	if y !=len(img)-1:
		if keep_moving(x,y+1):
			cor[y][x]=4
			return True	
	if y !=len(img) -1 and x!=0:
		if keep_moving(x-1,y+1):
			cor[y][x]=4
			return True		
	
	
	
	return False

	


keep_moving(start_pixel[1],start_pixel[0])

for a in cor:
	for b in a :
		print(b),
	print(' ',)		

input()
