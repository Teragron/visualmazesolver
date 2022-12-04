import cv2
import os

image_folder = 'frames'
video_name = 'video.avi'

# Get a list of all the .jpg files in the frames directory
# and sort them numerically
# Get a list of all the .jpg files in the frames directory
# and sort them numerically
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images = sorted(images, key=lambda x: int(x.split("_")[1].split(".")[0]))


frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 4, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
