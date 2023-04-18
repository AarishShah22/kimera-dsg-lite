import numpy as np
from numpy import genfromtxt
from sklearn.neighbors import NearestNeighbors
import numpy as np
from array_to_list_pixel_data import label_dict
import matplotlib.pyplot as plt
import pickle
import time
import tqdm

class DSG_Generation():

    def __init__(self, voxel_map, room_constraints): 

        self.voxel_map = voxel_map
        self.room_constraints = room_constraints 
        self.semantic_labels = genfromtxt('semantic_segmentation_labels.csv',delimiter=',')
        self.dsg = {}
        self.n_buildings = 1
        self.n_rooms = len(room_constraints)

    #### Converting RBG to a specific Semantic id ####
    def rgb_to_id(self):

        voxel_map_ = self.voxel_map

        self.voxel_map = np.zeros((voxel_map_.shape[0],4))
        for i in range(voxel_map_.shape[0]):

            self.voxel_map[i,0:3] = voxel_map_[i,0:3]
            rgb = voxel_map_[i,3:6]

            for j in range(self.semantic_labels.shape[0]):

                if np.array_equal(rgb, self.semantic_labels[j,1:4]):
                    self.voxel_map[i,3] = self.semantic_labels[j,4]

    #### DSG as a nested dictionary with List of Voxels for every Classification ####
    def initialize_dsg(self):

        for i in range(self.n_buildings):

            building = {}
            building["walls"] = []

            for j in range(self.n_rooms):

                room = {}
                
                room["objects"] = []
                room["floors and ceilings"] = []

                building["R"+str(j+1)] = room

            self.dsg["B"+str(i+1)] = building

    def populate_dsg(self):
        c=0
        from tqdm import tqdm
        for voxel in tqdm(self.voxel_map):
            
            semantic_id = voxel[3]

            if semantic_id == 19:

                self.dsg["B1"]["walls"].append(voxel)

            else:

                isInRoom = False

                for i in range(self.n_rooms):
                    constraints = np.array(self.room_constraints["R"+str(i+1)])

                    voxel_array_xy = np.asarray([voxel[0], voxel[1]]).reshape(1,-1)
                    #isInRoom = np.any(np.all(constraints == voxel_array_xy, axis=1))

                    if(isInRoom != True):
                       X = constraints
                       #### Spatial Constraints ####
                       nbrs = NearestNeighbors(n_neighbors=1, algorithm='kd_tree').fit(X) #check in each room (using search alg) and assign to room
                       query_point = voxel_array_xy
                       distances, indices = nbrs.kneighbors(query_point)
                       if(distances < 1):
                        isInRoom = True
                           

                    if isInRoom:
                        #### check semantic label and assign the class ####
                        
                        if semantic_id == 3 or semantic_id == 4:
                            self.dsg["B1"]["R"+str(i+1)]["floors and ceilings"].append(voxel)
                        else:
                            self.dsg["B1"]["R"+str(i+1)]["objects"].append(voxel)
                        break
        print("For Completed")


    def print_dsg(self):

        print(self.dsg)

    def save_dict(self):
        dsg = self.dsg
        with open('dsg.pickle', 'wb') as f:
        # use pickle to serialize and save the dictionary to the file
            pickle.dump(dsg, f)

    def load_dict(self):
        with open('dsg.pickle', 'rb') as f:
        # use pickle to deserialize and load the dictionary from the file
            dsg = pickle.load(f)
        return dsg
        



#### FUNCTION CALLS ####

start_time = time.time()
voxel_map = np.loadtxt('voxel_color_map_uhuman_complete_0.05_txt.txt')
#### Voxel Map for Trial Run ####
# voxel_map = voxel_map[:20000,:]

room_constraints = label_dict
uhumans_dsg = DSG_Generation(voxel_map, room_constraints)
uhumans_dsg.rgb_to_id()
uhumans_dsg.initialize_dsg()
uhumans_dsg.populate_dsg()
#uhumans_dsg.print_dsg()
uhumans_dsg.Visualization()
uhumans_dsg.save_dict()
dsg_pickle = uhumans_dsg.load_dict()
print("#########################################################################################")

end_time = time.time()

total_time = end_time - start_time

#Print the total execution time
print(f"Execution time: {total_time} seconds")



