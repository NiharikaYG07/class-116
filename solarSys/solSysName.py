import cv2
image=cv2.imread("Solar-system.webp")


cv2.putText(image,"Sun",(20,100),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(image,"Mercury",(100,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(image,"Venus",(180,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(image,"Earth",(280,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(image,"Mars",(330,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(image,"Jupiter",(430,400),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(image,"Saturn",(600,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(image,"Uranus",(750,400),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(image,"Neptune",(850,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))

cv2.imshow("Solar-system",image)
cv2.waitKey(0)
