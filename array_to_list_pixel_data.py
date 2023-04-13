import numpy as np
labels = np.load('labels_0.005.npy')

label_id = np.array([3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15])

label_dict = {}
room_no = 0

for id in label_id:

    room_no += 1
    label_dict["R"+str(room_no)] = np.argwhere(labels == id)


