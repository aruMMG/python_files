import glob
import cv2
import random
import os


for img_path in glob.glob("/home/aru/phd/objective1/thesis/chapter5/dataset2/central/good/*.jpg"):
    fname = os.path.basename(img_path).split(".")[0]
    img = cv2.imread(img_path)
    if img.shape==(130,195,3):
        tile_size = 87
    elif img.shape==(190,245,3):
        tile_size = 109
    elif img.shape==(250,320,3):
        tile_size = 142

    for i in range(10,20):
        start0 = random.randint(0,img.shape[0]-tile_size-1)
        start1 = random.randint(0,img.shape[1]-tile_size-1)
        tile = img[start0:start0+tile_size,start1:start1+tile_size]
        assert tile.shape==(tile_size,tile_size,3)
        cv2.imwrite(f"/home/aru/phd/objective1/thesis/chapter5/dataset2/tiles/good/{fname}_{i}.jpg", tile)


# image_list = ["4"]

# for img_num in image_list:
#     img = cv2.imread(os.path.join("/home/aru/phd/objective1/thesis/chapter5/dataset2/central/defect", f"img{img_num}.jpg"))
#     img = cv2.rotate(img, cv2.ROTATE_180)
#     fname = f"img{img_num}"
#     if img.shape==(130,195,3):
#         tile_size = 87
#     elif img.shape==(190,245,3):
#         tile_size = 109
#     elif img.shape==(250,320,3):
#         tile_size = 142

#     for i in range(40,50):
#         start0 = random.randint(0,img.shape[0]-tile_size-1)
#         start1 = random.randint(0,img.shape[1]-tile_size-1)
#         tile = img[start0:start0+tile_size,start1:start1+tile_size]
#         assert tile.shape==(tile_size,tile_size,3)
#         tile = cv2.rotate(tile, cv2.ROTATE_180)
#         cv2.imwrite(f"/home/aru/phd/objective1/thesis/chapter5/dataset2/tiles/defects/2/{fname}_{i}.jpg", tile)