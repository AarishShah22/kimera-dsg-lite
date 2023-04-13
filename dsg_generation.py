# load required libraries
# added comment
import numpy as np
from numpy import genfromtxt

class DSG_Generation():

    def __init__(self, voxel_map, room_constraints): 

        # TODO: 
        # Add correlations as input

        self.voxel_map = voxel_map
        self.room_constraints = room_constraints # dictionary
        self.semantic_labels = genfromtxt('semantic_segmentation_labels.csv',delimiter=',')
        self.dsg = {}
        self.n_buildings = 1
        self.n_rooms = len(room_constraints)

    # def in_room(self, constraints, voxel_coords):

    #     isInRoom = False
    #     x = constraints["x"]
    #     y = constraints["y"]
    #     xlim = constraints["xlim"]
    #     ylim = constraints["ylim"]

    #     if x<voxel_coords[0]<x+xlim and y<voxel_coords[1]<y+ylim:
            
    #         isInRoom = True

    #     return isInRoom

    def rgb_to_id(self):

        voxel_map_ = self.voxel_map

        self.voxel_map = np.zeros((voxel_map_.shape[0],4))
        for i in range(voxel_map_.shape[0]):

            self.voxel_map[i,0:3] = voxel_map_[i,0:3]
            rgb = voxel_map_[i,3:6]

            for j in range(self.semantic_labels.shape[0]):

                if np.array_equal(rgb, self.semantic_labels[j,1:4]):
                    self.voxel_map[i,3] = self.semantic_labels[j,4]

    def initialize_dsg(self):

        for i in range(self.n_buildings):

            building = {}
            building["walls"] = []
            building["correlations"] = []

            for j in range(self.n_rooms):

                room = {}
                
                room["objects"] = []
                room["floors and ceilings"] = []

                building["R"+str(j+1)] = room

            self.dsg["B"+str(i+1)] = building

    def populate_dsg(self):

        for voxel in self.voxel_map:

            semantic_id = voxel[3]

            if semantic_id == 19:

                self.dsg["B1"]["walls"].append(voxel)

            else:

                isInRoom = False

                for i in range(self.n_rooms):
                    constraints = self.room_constraints["R"+str(i+1)]
                    #check in each room (using search alg) and assign to room

                    voxel_array_xy = np.asarray([voxel[0], voxel[1]])
                    isInRoom = np.any(np.all(constraints == voxel_array_xy, axis=1))    

                    if isInRoom:
                        
                        #check semantic label
                        
                        if semantic_id == 3 or semantic_id == 4:
                            self.dsg["B1"]["R"+str(i+1)]["floors and ceilings"].append(voxel)
                        else:
                            self.dsg["B1"]["R"+str(i+1)]["objects"].append(voxel)
                        break

    def print_dsg(self):

        print(self.dsg)

voxel_map = np.ones((100,6))
room_constraints = {"R1":np.ones((100,2)), "R2":np.zeros((100,2))}
uhumans_dsg = DSG_Generation(voxel_map, room_constraints)
uhumans_dsg.rgb_to_id()
uhumans_dsg.initialize_dsg()
uhumans_dsg.populate_dsg()
uhumans_dsg.print_dsg()