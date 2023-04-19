# kimera-dsg-lite

The purpose of this github is to provide base code for users of Kimera-Semantics to have an elementary implementation of a Dynamic Scenes Graph. After running Kimera-Semantics, a voxel based file is generated that our code categorizes by semantic labels and then visualizes. Additionally, a demonstration is provided about how this DSG can be augmented with the usage of a Generative Preditive Text model for tasks such as a categorizing rooms based on detected features. 



![image](https://user-images.githubusercontent.com/109474044/232984442-1ce64e10-89a8-4acf-b571-0fd71ded1626.png)


## Structure

<img width="659" alt="Screenshot 2023-04-19 at 4 10 50 PM" src="https://user-images.githubusercontent.com/109474044/233188900-9fe78395-a939-489a-bf55-7286dd38d1b5.png">

### Description
This github



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

- In desired python environment run the following lines to generate the adjacency matrix. Can also substitute dataset.

  ```
  df1 =np.load('labels.npy')
  distance_tolerance = 30
  hold_mat=adj_matrix(df1, distance_tolerance)
  ```
 ![image](https://github.com/AarishShah22/kimera-dsg-lite/blob/orgnized/DSG/combined_adj_plot.png)

### Running DSG Lite
- Inside DSG folder

#### 1. Converting Mesh to Voxel Map

  - This will convert the mesh grid into a .ply file containing voxels. This file needs to be fed in to the OpenCV algorithm
  ```
  python ply_to_voxel.py
  ```
#### 2. Building room constraints
  - Coverting the output of the OpenCV algorithm to room constraints to be used in 'dsg_generation.py'
  ```
  python array_to_list_pixel_data.py
  ```
#### 3. Running DSG
  - Run the DSG generation algorithm. First create the .txt file of the Voxel Map from (1). The make sure to have semantic_segmentation_labels.csv in the running folder.
  ```
  python dsg_generation.py
  ```
  
  ![image](https://github.com/AarishShah22/kimera-dsg-lite/blob/orgnized/DSG/Floors%20and%20Ceilings.png) ![image](https://github.com/AarishShah22/kimera-dsg-lite/blob/orgnized/DSG/Objects.png) ![image](https://github.com/AarishShah22/kimera-dsg-lite/blob/orgnized/DSG/Walls.png)


### Get Room label using language model

There is a useful tool in the folder

  ```
  /toolkit/get_room_label.py
  ```
 There is also a notebook demo to show how to use it
  ```
  /toolkit/get_room_label_demo.ipynb
  ```
 To use it, you should apply for a OpenAI API key. To set up OpenAI key, you should add a line in the code
   ```
  openai_api_key = "your openai key"
  ```
 Or set the OpenAI key in your environment
  ```
  echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc
  source ~/.zshrc
  ```
 
 The default API we use is "gpt-3.5-turbo", you can also change the language model for better performance like "gpt-4-0314" with same interface “openai.ChatCompletion.create“.
 But if you want to you the model below, you should change the interface to "openai.Completion.create". For more information, please follow the instrcution from [OpenAI](https://platform.openai.com/docs/api-reference/completions/create).
 ```
 ["text-davinci-001", "text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001"](gpt-3)
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
