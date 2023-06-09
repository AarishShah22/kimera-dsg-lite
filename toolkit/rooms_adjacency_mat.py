#Code to generate adjacency matrix for rooms classification
#Inputs:
#Numpy array with 0s for walls, 1s for whitespace, and additional numbers
#denoting different rooms

#Outputs:
#Adjacency matrix (np.array)
#denotes rooms that are adjacent to eachother

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from scipy.io import loadmat

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def adj_matrix(df2, distance_tolerance):
    num_rooms = len(np.unique(df2)) - 2
  
    hold_mat = np.zeros([num_rooms,num_rooms])
    iterate_list = list(range(num_rooms)) + 2*np.ones(num_rooms)
    iterate_list = [int(item) for item in iterate_list]
    
    for val1 in iterate_list:
        for val2 in iterate_list:
        
            ind_3 = np.where(df2 == val1)
            ind_4 = np.where(df2 == val2)

            for i in range(len(ind_4[0])):
                check_x = find_nearest(ind_3[0], value=ind_4[0][i])
                dif_x = abs(check_x -  ind_4[0][i])
        
                check_y = find_nearest(ind_3[1], value=ind_4[1][i])
                dif_y = abs(check_y -  ind_4[1][i])
    
                distance =(dif_y**2 + dif_x**2)**(1/2)

                if distance < distance_tolerance:
                    #print("yes")
                    hold_mat[val1-3,val2-3] = 1
                    break
                
    hold_mat = hold_mat - np.eye(num_rooms)
    return (hold_mat)

#Example usage of function
#df1 =np.load('labels.npy')
#distance_tolerance = 30
#hold_mat=adj_matrix(df1, distance_tolerance)