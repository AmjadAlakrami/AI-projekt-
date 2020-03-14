import os 
 
def main(): 
    i = 0
    
    for filename in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w"):
        dst ="000" + str(i) + ".JPEG"
        src ='C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w/'+ filename
        dst ="C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w/"+ dst 
        os.rename(src, dst)
        i += 1

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