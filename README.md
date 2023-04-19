# kimera-dsg-lite

The purpose of this github is to provide base code for users of Kimera-Semantics to have an elementary implementation of a Dynamic Scenes Graph. After running Kimera-Semantics, a voxel based file is generated that our code categorizes by semantic labels and then visualizes. Additionally, a demonstration is provided about how this DSG can be augmented with the usage of a Generative Preditive Text model for tasks such as a categorizing rooms based on detected features. 


![image](https://user-images.githubusercontent.com/109474044/232984442-1ce64e10-89a8-4acf-b571-0fd71ded1626.png)


## Structure

<img width="418" alt="Screenshot 2023-04-19 at 1 13 41 AM" src="https://user-images.githubusercontent.com/109474044/232973069-c3e183e4-eb5f-429e-a563-effe56b9b28a.png">


## Description

An in-depth paragraph about your project and overview of use.

## Getting Started


### Dependencies

* Ubuntu 18.04.6 LTS
* [Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics)
* [opencv-python](https://pypi.org/project/opencv-python/)
* [Open3D](http://www.open3d.org/)


### Download [uHumans 2](https://web.mit.edu/sparklab/datasets/uHumans2/) dataset
```
cd uhuman_data
```
```
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=**1rtuRm7Ej83Dwm6azRR_qhjnRq6fAVjaR**' -O retimestamped_humans_24_long.bag
```
### Kimera-Semantics Point Cloud Quick Launch

#### 1. Install the Kimera Semantics library from official repository: [Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics).

#### 2. Replace the launch file under kimera_semantics_ros/launch with the file provided in this repository, modify the location of dataset in launch file.

#### 3. Launch Kimera-Semantics with following commands:

- In one terminal, run 

  ```
  roscore
  ```

- Open a new terminal, source Kimera-Semantics and run:

  ```
  roslaunch kimera_semantics_ros kimera_semantics.launch
  ```

- Open a new terminal, source Kimera-Semantics and run:

  ```
  rviz -d $(rospack find kimera_semantics_ros)/rviz/kimera_semantics_gt.rviz
  ```

- After map is generated, run following to save .ply file:

  ```
  rosservice call /kimera_semantics_node/generate_mesh
  ```

### Adjacency Matrix Computation

#### 1. Download the room_adjacency_mat.py and labels.np files.

- In desired python environment run

  ```
  df1 =np.load('labels.npy')
  distance_tolerance = 30
  hold_mat=adj_matrix(df1, distance_tolerance)
  ```

### Running DSG Lite

#### 1. Download the room_adjacency_mat.py and labels.np files.

- In Terminal run

  ```

  ```
  

## Authors

Contributors names and contact info

Yipei Ge yipeige@umich.edu
Misael Ortiz misaelo@umich.edu
Aditya Paranjape adityaap@umich.edu
Aarish Shah aarishs@umich.edu
Zhouyi Yang zyyangzy@umich.edu


## Acknowledgments

Inspiration, code snippets, etc.
* [MIT-SPARK Kimera-Semantics]https://github.com/MIT-SPARK/Kimera-Semantics
* [OpenCV Development Partnership {Old)] https://opencv.org/opencv-development-partnership-old/
* [OpenAi] https://openai.com/blog/chatgpt
