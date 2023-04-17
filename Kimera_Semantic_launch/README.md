# Kimera-Semantics Point Cloud Quick Launch

### 1. Install the Kimera Semantics library from official repository: [Kimera-Semantics](https://github.com/MIT-SPARK/Kimera-Semantics).

### 2. Download dataset from [uHumans 2](https://web.mit.edu/sparklab/datasets/uHumans2/) dataset.

### 3. Replace the launch file under kimera_semantics_ros/launch with the file provided in this repository, modify the location of dataset in launch file.

### 4. Launch Kimera-Semantics with following commands:

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

  





