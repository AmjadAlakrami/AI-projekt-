# import os 
 
# def main(): 
#     i = 0
    
#     # for filename in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/IMPORTENT/annotationsXML_2"):

#     xml = open("C:/Users/amjad/OneDrive/Desktop/IMPORTENT/annotationsXML_2/000205.xml", "r")
#     lines_of_file = xml.readlines()
#     print(lines_of_file)
#         #dst ="0000" + str(i) + ".JPEG"
#         #src ='C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/IMPORTENT/Images/thumbs_up_–_Google_Sök/'+ s 
#         #dst ="C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/Images/thumbs_up_–_Google_Sök/"+ dst 
#         #os.rename(src, dst) 

# main()


import xml.etree.ElementTree as ET
import os

for filename in os.listdir("C:/Users/amjad/OneDrive/Desktop/IMPORTENT/annotationsXML_2"):

    tree = ET.parse('C:/Users/amjad/OneDrive/Desktop/IMPORTENT/annotationsXML_2/'+filename)
    root = tree.getroot()

    for child in root.iter("filename"):
        print(child.text)
        r = filename.split(".")
        x = r[0]+".JPEG"
        child.text=x

    tree.write("C:/Users/amjad/OneDrive/Desktop/IMPORTENT/annotationsXML_2/"+filename)