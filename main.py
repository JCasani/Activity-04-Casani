import cv2

filepath = "jackie.jpg"

input2 = int(input("\n1 - Color \n2 - Grayscale \n3 - Unchanged \n CHOOSE MY COLOR : "))
if input2 == 1:
            image = cv2.imread(filepath, 1)
            cv2.imshow("Malinaw na AKO", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
elif input2 == 2:
           image = cv2.imread(filepath, 0)
           cv2.imshow("Malabo parang kami", image) 
           cv2.waitKey(0)
           cv2.destroyAllWindows()
else:
           image = cv2.imread(filepath, -1)
           cv2.imshow("Ako parin pero Maganda", image)
           cv2.waitKey(0)
           cv2.destroyAllWindows()
      
