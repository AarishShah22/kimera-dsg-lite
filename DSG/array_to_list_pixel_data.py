#### Segregating Pixels from Room constraints into a Dictionary ####
import numpy as np
labels = np.load('labels_0.05_latest.npy') # Pixels array for each room constraint
y_max = 867

label_id = np.array([3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16,17, 18, 19]) 

label_dict = {}
room_no = 0

for id in label_id:

    room_no += 1

    arr = np.argwhere(labels == id)
    
    #### Check for correct allotment ####
    for element in arr:

        if element[0]>867:
            print("0:"+str(element[0]))
        if element[1]>966:
            print("1:"+str(element[1]))


    label_dict["R"+str(room_no)] = np.argwhere(labels == id)

print("###################################")
#### Converting from Image frame to Environment frame ####

for room in label_dict:
    
    room_array = label_dict[room]
    room_array[:,0] = 867 - room_array[:,0]
    if np.any(room_array[:,0] < 0):
        print("Wrong Allotment")

    label_dict[room] = room_array ## Stored as [y,x] in original Frame