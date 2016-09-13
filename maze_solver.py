import numpy as np 


#################################################################################################
###################   navigation requirements                         ###########################
#################################################################################################
start_pixel =[ 280,34]
stop_pixel = [599,494]


#############################################################################################
####           for movement of the object along the maze         ############################
#############################################################################################

###### functions for movement ######
####################################
def surrounding_pixels(current_pixel=[]):
	surrounding_pixels_array =[]
	for a in range(0,3):
		for b in range(0,3):
			if(a==1 and b==1):
				None
			else:	
				surrounding_pixels_array.append([current_pixel[0]-1+a,current_pixel[1]-1+b])

    
	return surrounding_pixels_array                     

def junction_order(current_pixel,previous_pixel):
	order =0
	for a in surrounding_pixels(current_pixel):
		if(a != previous_pixel):
			if(img[a[0],a[1]]==255):                                        # img being the matrix of the processed image
				order++
	return order 			

def junction (current_pixel,previous_pixel) :
	
	return





current_pixel = start_pixel
while current_pixel != stop_pixel:
	for a in surrounding_pixels(start_pixel):
		print(a)
	break
