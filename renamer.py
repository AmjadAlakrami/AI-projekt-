import os 
 
def main(): 
    i = 0
    
    for filename in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/IMPORTENT/annotationsXML_2"):
        f = filename.split(".") 
        s = f[0]+".JPEG"

        #dst ="0000" + str(i) + ".JPEG"
        #src ='C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/IMPORTENT/Images/thumbs_up_–_Google_Sök/'+ s 
        #dst ="C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/Images/thumbs_up_–_Google_Sök/"+ dst 
        if s in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/IMPORTENT/Images/thumbs_up_–_Google_Sök"):
            print ("finded")
        else:
            os.remove("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/IMPORTENT/annotationsXML_2/"+filename)
        #os.rename(src, dst) 
        i += 1
 
main()