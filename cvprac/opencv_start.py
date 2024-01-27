import cv2
import os

PATH = os.getcwd()
cur_dir = os. path.join(PATH,'cvprac')
image_path = os.path.join(cur_dir, "sample.jpg")
image = cv2.imread(image_path)

if image is not None :
    print("이미지 읽어오기 성공")
else:
    print("이미지 읽어오기 실패")

cv2.imshow("방금 읽어온 이미지", image)
cv2.imwrite(os.path.join(cur_dir,'new_sample.jpg'),image)
cv2.waitKey(0)
cv2.destroyAllWindows()