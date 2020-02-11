from PIL import Image
import os 
for filename in os.listdir("C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami"):
    # im = Image.open("C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami/"+filename)
    # im.save("C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami/"+filename.replace("jpg","JPEG"))
    if "jpg" in "C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami/"+filename:
        os.remove("C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami/"+filename)
    #print("C:/Users/s8amjala/Desktop/AI-projekt-/Images/hand_open_palm_with_five_fingers_isolated_–_Google_Sök/"+filename)

# import os 
 
# def main(): 
#     i = 0
    
#     for filename in os.listdir("C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami"): 
#         dst ="000" + str(i) + ".jpg"
#         src ="C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami/"+ filename 
#         dst ="C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami/"+ dst 
        
#         os.rename(src, dst) 
#         i += 1
 
# main()
# from PIL import Image
# import os
# # open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
# for filename in os.listdir("C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami"):
#     imageFile = "C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami/"+filename
#     im1 = Image.open(imageFile)
# # adjust width and height to your needs
#     width = 500
#     height = 420
#     # use one of these filter options to resize the image
#     im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
#    # best down-sizing filter
#     im2.save( "C:/Users/s8amjala/Desktop/AI-projekt-/Images/iCloud Photos from Amjad Al akrami/"+filename)
