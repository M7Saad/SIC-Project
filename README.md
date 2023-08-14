# Fire and Smoke Detection
This project aims to detect and monitor fire incidents by training a deep learning model to classify fire and smoke images. 
## Installation 
if you are interested in running the project on your device, make sure to install all the dependencies.
You can write the command below to install it all:
```
pip install -r requirements.txt
```
## Data
This project used [Fire-Smoke-Dataset](https://github.com/DeepQuestAI/Fire-Smoke-Dataset/tree/master) which contains 3 classes (i.e., Fire, Smoke, Neutral) with the same proportion of each class (balanced dataset.)

## Experiement set-up
### Data Preparation
 - Data Partitioning: splits the dataset into train/val/test folders in the `Data Preparation.ipynb` notebook.
 - Data Preprocessing: resize, rescale, and augment the dataset in the 'code.ipynb' notebook.
### Methodology
The models used in this experiment were:
- CNN model from scratch.
- EfficientNetv2 model.
### Results 
#### 1. CNN Model
###### Classification Report:
|       | Precision | Recall | F1-Score | Overall Accuracy |
|:------|:---------|:------|:--------|:----------------|
| Fire   |	0.88    |	0.83 |	0.86   |	0.74           |
| Neutral|	0.59    |	0.87	| 0.70	  |       -        |
| Smoke	 | 0.88	   | 0.52	 | 0.65	  |       -        | 
###### Confusion Matrix:
![Confusion_Matrix_FromScratchModel](https://github.com/M7Saad/SIC-Project/assets/141254648/3d311fc8-fbfb-45c9-b1e9-aad1c5474ca2)

#### 2. EfficicentNetv2
###### Classification Report:
|       | Precision | Recall | F1-Score | Overall Accuracy |
|:------|:---------|:------|:--------|:----------------|
| Fire   |	0.97    |	0.92 |	0.94   |	0.9633           |
| Neutral|	0.99    |	0.99	| 0.99	  |       -        |
| Smoke	 | 0.93	   | 0.98	 | 0.96	  |       -        | 
###### Confusion Matrix:
![Confusion_Matrix_EfficientNetModel](https://github.com/M7Saad/SIC-Project/assets/141254648/28a87a71-4cca-42f6-9a5e-422a43978e7b)


## Deployment
To deploy our model, we used Gradio library to build an interface. \
You can check the website [here](https://4f19cf68b86ba94583.gradio.live) \
![Website-Interface](https://github.com/M7Saad/SIC-Project/assets/141254648/2a2f28e9-2103-4433-9cdf-3092eeb66ce1)
