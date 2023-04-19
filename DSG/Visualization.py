import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from array_to_list_pixel_data import label_dict
import numpy as np
import pickle

def load_dict():
        with open('dsg_all_900k.pickle', 'rb') as f:
        # use pickle to deserialize and load the dictionary from the file
            dsg = pickle.load(f)
        return dsg

class Visualization():

    def __init__(self, voxel_map, dsg_pickle, label_dict):
        self.voxel_map = voxel_map
        self.dsg = dsg_pickle
        self.label_dict = label_dict

    def len_(self):
        length = 0
        length += len(self.dsg['B1']['walls'])
        for i in range(16):
            length += len(self.dsg['B1'][f'R{i+1}']['objects'])
            length += len(self.dsg['B1'][f'R{i+1}']['floors and ceilings'])
            
        print("Total voxels in DSG",length)


    def viz_test(self):
        object_arrays = []
        for i in range(16):
            object_arrays += self.dsg['B1'][f'R{i+1}']['objects']
            object_arrays += self.dsg['B1'][f'R{i+1}']['floors and ceilings']
       
        x_values = [arr[0] for arr in object_arrays]
        y_values = [arr[1] for arr in object_arrays]
        
        plt.xlim([0,1000])
        plt.ylim([0,1000])
        plt.scatter(x_values, y_values,s=3)

        


    def visualization_walls(self):
        
        walls_arrays = self.dsg['B1']['walls']
        x_values = [arr[0] for arr in walls_arrays]
        y_values = [arr[1] for arr in walls_arrays]
        
        plt.scatter(x_values, y_values,s=3)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Walls')

    def visualize_objects(self):
         
         #### Room ids to be plotted ####
        rooms = [1,7,12, 13, 16]
        colors = ['blue','green','yellow','red','orange']
        color_id = 0

        fig2 = plt.figure()
        ax = fig2.add_subplot(projection='3d')

        for room_no in rooms:

            object_arrays = self.dsg['B1'][f'R{room_no}']['objects']
            x_values = []
            y_values = []
            z_values = []

            for arr in object_arrays:
                
                if arr[3] != 0:
                    x_values.append(arr[0])
                    y_values.append(arr[1])
                    z_values.append(arr[2])
            
            ax.scatter(x_values, y_values,z_values,c=colors[color_id],s=1)
            color_id+=1

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            plt.title('Objects color-coded according to rooms')
            
    def visualize_fnc(self):

        rooms = [1,7,12, 13,16]
        colors = ['blue','green','yellow','red','orange']
        color_id = 0

        fig3 = plt.figure()
        ax = fig3.add_subplot(projection='3d')

        for room_no in rooms:

            fnc_arrays = self.dsg['B1'][f'R{room_no}']['objects']
            fnc_arrays_2 = self.dsg['B1'][f'R{room_no}']['floors and ceilings']
            fnc_arrays += fnc_arrays_2
            x_values = []
            y_values = []
            z_values = []

            for arr in fnc_arrays:
                
                if arr[3] == 0 or arr[3] == 3 or arr[3] == 4:
                    x_values.append(arr[0])
                    y_values.append(arr[1])
                    z_values.append(arr[2])
            
            ax.scatter(x_values, y_values,z_values,c=colors[color_id])
            color_id+=1

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title('Floors and ceilings color-coded according to rooms')

voxel_map = np.loadtxt('voxel_color_map_uhuman_complete_0.05_txt.txt')
dsg_pickle = load_dict()


viz = Visualization(voxel_map, dsg_pickle, label_dict)
viz.visualize_objects()
viz.visualization_walls()
viz.visualize_fnc()
#viz.viz_test()
#viz.len_()
plt.show()

