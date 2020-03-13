import os 
 
def main(): 
    i = 0
    
    for filename in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/Images/thumbs_up_–_Google_Sök"): 
        dst ="0000" + str(i) + ".JPEG"
        src ='C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/Images/thumbs_up_–_Google_Sök/'+ filename 
        dst ="C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/Images/thumbs_up_–_Google_Sök/"+ dst 
        
        os.rename(src, dst) 
        i += 1
 
main()