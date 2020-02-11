# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 

# Function to rename multiple files 
def main(): 
	i = 0
	
	for filename in os.listdir("C:/Users/s8amjala/Downloads/hand_open_palm_with_five_fingers_isolated_–_Google_Sök"): 
		dst ="000" + str(i) + ".jpg"
		src ='C:/Users/s8amjala/Downloads/hand_open_palm_with_five_fingers_isolated_–_Google_Sök/'+ filename 
		dst ='C:/Users/s8amjala/Downloads/hand_open_palm_with_five_fingers_isolated_–_Google_Sök/'+ dst 
		
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 
		i += 1

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
