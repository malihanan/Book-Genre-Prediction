# Book-Genre-Prediction
A Natural Language Processing (NLP) Project for predicting genre of a book using its summary as a feature.

### Web app that uses prediction model created earlier

To run the application on Azure VM, use the following command from the current folder:

	set FLASK_APP=main
	flask run --port=80 --host=0.0.0.0 >> serverlog.txt 2>&1

#### Requirements:
* [Pickle Files](https://drive.google.com/drive/folders/1LDFT-sCyCNOtSd7KsPkNzrxy4QrpQI9d?usp=sharing)
: All pickle files of trained models. This will be reuired by the web application to predict genres.
Download them in the current folder.

