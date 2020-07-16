# Book-Genre-Prediction
A Natural Language Processing (NLP) Project for predicting genres of a book using its summary as a feature.

The web app was hosted in a VM on Azure Cloud.

### Description of File Structure:

#### Datasets:
This folder has all the datasets used for different experiments.
* test.xml and train.xml are used for Multi Label Genre Prediction.
* booksummaries.txt is used for Single Label Genre Prediction.
* ds_beforeduplication.csv has the data before augmentation.
* augmented_data.csv has the data after augmentation.

#### book_genre_prediction.ipynb:
This file has the final code containing implementation details of the most accurate models.

#### Flask:
This folder has the code for web app built using Flask.

#### Experiments:
This folder has notebook files related to the experiments conducted to evaluate impact of different techniques of classification.

#### Docs:
This folder has log files of info collected all through the development.

#### own implementation of models:
This folder has our own implementation of models, created whilst learning. They are not used in implementation.

#### trial at summary:
This folder has a file where we tried generating summary of a doc. It uses extractive summarization. It is not used in the project.

### Links to Drive: 
* [Pickle Files](https://drive.google.com/drive/folders/1LDFT-sCyCNOtSd7KsPkNzrxy4QrpQI9d?usp=sharing)
: All pickle files of trained models

* [Multi Label Genre Prediction](https://drive.google.com/open?id=1xIyTuyQrV0vOUFWQv39sISeBxgwUFKKD)
: Augmented data, code and trained model for Multi Label Genre Prediction.
