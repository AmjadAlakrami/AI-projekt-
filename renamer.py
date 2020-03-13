import os 
 
def main(): 
    i = 47
    
    for filename in os.listdir("C:/Users/s8amjala/Desktop/IMPORTENT/annotationsXML"): 
        dst ="000" + str(i) + ".xml"
        src ='C:/Users/s8amjala/Desktop/IMPORTENT/annotationsXML/'+ filename 
        dst ="C:/Users/s8amjala/Desktop/IMPORTENT/annotationsXML/"+ dst 
        
        os.rename(src, dst) 
        i += 1
 
main()