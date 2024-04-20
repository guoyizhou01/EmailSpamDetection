# EmailSpamDetection

## Dependancy

- Python 3.10 (Does not support Python 3.11 due to Tensorflow restriant)
- Tensorflow 2.10
- Keras 2.10.0
- Numpy 1.26.4
- Pandas 2.2.1

## Data Sets

Currently, the model is trained and tested with Enron1 dataset. However, the program does accomodate different ones. To use a different dataset, load the folder to current folder, and use '''python3 fileIO.py FolderName''' to load the dataset. Then, change the name in learning.ipynb file to "data/FolderName_data.csv".

Enron-Spam: http://nlp.cs.aueb.gr/software_and_datasets/Enron-Spam/index.html

## Wordslist

Model performance relies on using proper word list. The one currently using is 5000_words. To use a different wordlist, modification to fileIO.py is required.

3000_words: https://gist.github.com/hyper-neutrino/561f120125ae0e7c1d22777eebf083c8

5000_words: https://github.com/mahsu/IndexingExercise/blob/master/5000-words.txt

## Results

## Reference

Spam Filtering with Naive Bayes – Which Naive Bayes?: https://www2.aueb.gr/users/ion/docs/ceas2006_paper.pdf

Machine learning for email spam filtering: review, approaches and open research problems: https://www.sciencedirect.com/science/article/pii/S2405844018353404?ref=pdf_download&fr=RR-2&rr=8773bdb96f7e53ea



