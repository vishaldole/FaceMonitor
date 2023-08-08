#if not os.path.exists('photos/' + name):
#        os.makedirs('photos/' + name)

import cv2
import os
import time

name = input("Enter the person's name: ")
folder_path = os.path.join('photos', name)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

cap = cv2.VideoCapture(0)

i = 1
start_time = time.time()
while i <= 20:
    ret, frame = cap.read()
    if not ret:
        print("failed to grab frame, try again")
        break

    cv2.putText(frame, f"Image {i}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(60) == ord('q'):
        break
        
    
    img_name = os.path.join(folder_path, f"{i}.jpg")
    cv2.imwrite(img_name, frame)
    print(f"Image {i} saved.")
        
    i += 1

    time.sleep(0.3) # wait for 0.3 seconds before capturing the next image

end_time = time.time()
duration = end_time - start_time
print(f"{i-1} images captured in {duration:.2f} seconds.")
    
cap.release()
cv2.destroyAllWindows()
