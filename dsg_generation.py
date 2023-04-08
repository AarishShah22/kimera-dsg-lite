# load required libraries
import numpy as np
from numpy import genfromtxt

class DSG_Generation():

    def __init__(self, voxel_map):

        self.voxel_map = voxel_map
        self.semantic_labels = genfromtxt('semantic_segmentation_labels.csv',delimiter=',')
        self.dsg = {}
        self.n_buildings = 1
        self.n_rooms = 5

    def in_room(self, constraints, voxel_coords):

        isInRoom = False
        x = constraints["x"]
        y = constraints["y"]
        xlim = constraints["xlim"]
        ylim = constraints["ylim"]

        if x<voxel_coords[0]<x+xlim and y<voxel_coords[1]<y+ylim:
            
            isInRoom = True

        return isInRoom

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

            for j in range(self.n_rooms):

                room = {}
                room["constraints"] = {}
                room["objects"] = []
                room["floors and walls"] = []
                room["correlation"] = []

                building["R"+str(j)] = room

            self.dsg["B"+str(i)] = building

    def populate_dsg(self):

        pass
        #TODO

    def print_dsg(self):

        print(self.dsg)

    # print(dsg)

        # for k in range(voxel_map.shape[0]):

        #     if inRoom(constraints,voxel_map[0:3]) == True:
voxel_map = np.zeros((100,6))
uhumans_dsg = DSG_Generation(voxel_map)
uhumans_dsg.initialize_dsg()
uhumans_dsg.print_dsg()