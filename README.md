# Real-Time-Food-Detection-using-YOLOV3

The objective of this work package is to detect and classify food items from streaming video
frames acquired by the egocentric camera. Specifically, we are interested in any type of
food item which could be captured in the camera’s field-of-view. Food items have different
priority on a scene: (1) the less relevant belong to the background, in case of food shopping
or cooking activity; (2) the relevant food items belong to the foreground, in case of food
placed on a dish during a meal; (3) the most relevant food items are handled by the user, in
case of an intake. With the term food item, we intend also any type of drink container. We
will apply a state-of-the-art approach among the many networks available. The idea is to use
an on-the-shelf network pre-trained on a generic dataset, e.g., ImageNET. Subsequently,
we will transfer learning using Epic Kitchen’s and our dataset’s food instances.
