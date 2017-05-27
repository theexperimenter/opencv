# opencv

Train your own classifier using this guide:
http://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html

This classifier is used to detect cars in images and videos. 

This is first Iteration of Classifier 

Ran the classifier with LBP flag on opencv_traincascade 

Works well but there are still inaccuracies in detection 

Will need to train again with better images and for longer to get better results 

Enter following command in terminal to test classifier

python opencv.py --image test_image.jpg


RESULTS SO FAR:

http://imgur.com/yxDj4Tn --- Worked well in this instance

http://imgur.com/JZPaZOP --- Some errors with the edges of detection. Will be trying to solve such errors with tuning training parameters

http://imgur.com/IRooDC1 --- Seems that in this case its quite off from the desired area. Might be because of pick up truck or the angle
 
http://imgur.com/PWjvfCU --- A little outside the desired range 

http://imgur.com/uOegeGb --- A little outside the range as well 


Demo I created to show the stage I plan to reach:

https://www.youtube.com/watch?v=SogW4c2BqT0

