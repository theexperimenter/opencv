# import the necessary packages
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
#change 'cascade.xml' to the name of your classifier
ap.add_argument("-c", "--cascade",
                default="cascade.xml",
                help="path to cat detector haar cascade")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the car detector Haar cascade, then detect car faces
# in the input image
detector = cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
                                  minNeighbors=10, minSize=(75, 75))

# loop over the car faces and draw a rectangle surrounding each
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #break;

# show the detected cars
cv2.imshow("Cars", image)
cv2.waitKey(0)
cv2.destroyAllWindows()