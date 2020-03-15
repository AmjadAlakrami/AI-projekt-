import os 
 
def main(): 
    i = 0
    
    for filename in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w"):
        dst ="0000" + str(i) + ".jpg"
        src ='C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w/'+ filename
        dst ="C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w/"+ dst 
        os.rename(src, dst)
        i += 1

main()


# import xml.etree.ElementTree as ET
# import os

# for filename in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/annotationsXML_3"):

#     tree = ET.parse("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/annotationsXML_3/"+filename)
#     root = tree.getroot()

#     for child in root.iter("name"):
#         # print(child.text)
#         if child.text == "openhand":
#             for i in root.iter("filename"):
#                 if i.text in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w"):
#                     print(1)
#                     os.rename('C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w/'+i.text, "C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w3/"+i.text )
#     #     r = filename.split(".")
#     #     x = r[0]+".JPEG"
#     #     child.text=x

    # tree.write("C:/Users/amjad/OneDrive/Desktop/IMPORTENT/annotationsXML_2/"+filename)