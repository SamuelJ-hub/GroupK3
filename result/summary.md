# Projects in Data Science (2025)
We were given a dataset of 100 images of skin lesions to process and clean. First step of processing was manually annotating each image by multiple annotators based on the clarity of image. In this case, it was numbering the images from 0-2, depending on the amount of hair in the image. Later we implemented a function for hair removal, that we looped through our whole dataset, which would give us the processed images without any hair. That could be later used for tasks such as detecting cancerous lesions with an algorithm. As per hair removal, we got better and worse results, which you can see in the example images here.

<img src="bad.png" alt="Description" width="300">

text

<img src="good.png" alt="Description" width="300">

text

Thinking about this problem, if we wanted to improve our algorithm and make it faster, we could implement a function that would iterate through our csv file of annotated images and output only the images that were labeled as 1 or 2, ignoring the images that were not containing any hair in the first place.

In this mandatory assignment, we learned about image processing and cv2 library, as well as collaboration on GitHub.