# kimera-dsg-lite

The purpose of this github is to provide base code for users of Kimera-Semantics to have an elementary implementation of a Dynamic Scenes Graph. After running Kimera-Semantics, a voxel based file is generated that our code categorizes by semantic labels and then visualizes. Additionally, a demonstration is provided about how this DSG can be augmented with the usage of a Generative Preditive Text model for tasks such as a categorizing rooms based on detected features. 

## Structure
* |____Kimera_Semantic_launch
* | |____README.md
* | |____kimera_semantics.launch
* |____utils
* | |____text_toolkit.py
* |______pycache__
* | |____dsg_generation.cpython-310.pyc
* | |____array_to_list_pixel_data.cpython-310.pyc
* |____DSG
* | |____Visualization.py
* | |____voxel_color_map_uhuman_complete_0.05_txt.txt
* | |____labels_0.05_latest.npy
* | |____dsg_generation.py
* | |____array_to_list_pixel_data.py
* |____README.md
* |____configs
* | |____semantic_segmentation_labels.csv
* | |____tesse_multiscene_office1_segmentation_mapping.csv
* |____uhuman_data
* | |____voxel_color_map_uhuman_complete.ply
* | |____voxel_color_map_uhuman_complete_0.05_txt.txt
* |____toolkit
* | |____room_area_assignment.ipynb
* | |____rooms_adjacency_mat.py
* | |____get_room_label.py


## Description

An in-depth paragraph about your project and overview of use.

## Getting Started






### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
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
