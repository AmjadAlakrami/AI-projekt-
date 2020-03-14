import os 
 
def main(): 
    i = 0
    
    for filename in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/annotationsXML_2"):
        # dst ="0000" + str(i) + ".JPEG"
        x = filename.split(".")
        y = x[0]
        z = y+".JPEG"
        if z not in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/Images/thumbs_up_–_Google_Sök"):
        # src ='C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/IMPORTENT/Images/thumbs_up_–_Google_Sök/'+ s 
        # dst ="C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/Images/thumbs_up_–_Google_Sök/"+ dst 
            os.remove("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/annotationsXML_2/"+filename) 

main()


# import xml.etree.ElementTree as ET
# import os

# for filename in os.listdir("C:/Users/amjad/OneDrive/Desktop/IMPORTENT/annotationsXML_2"):

#     tree = ET.parse('C:/Users/amjad/OneDrive/Desktop/IMPORTENT/annotationsXML_2/'+filename)
#     root = tree.getroot()

#     for child in root.iter("filename"):
#         print(child.text)
#         r = filename.split(".")
#         x = r[0]+".JPEG"
#         child.text=x

#     tree.write("C:/Users/amjad/OneDrive/Desktop/IMPORTENT/annotationsXML_2/"+filename)