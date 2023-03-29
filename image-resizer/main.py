import cv2
source="img.png"
destination= "new_img.jpeg"
src = cv2.imread(source)
sp=int(input("Enter scale percentage: "))
new_width=int(src.shape[1]*sp/100)
new_height=int(src.shape[0]*sp/100)
output=cv2.resize(src,(new_width,new_height))
cv2.imwrite(destination,output)


