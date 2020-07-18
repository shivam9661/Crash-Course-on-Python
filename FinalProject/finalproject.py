# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys



# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()




def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is","in","one","not", "it", "of", "and", "or", "an","on", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just","for"]

    # LEARNER CODE START HERE
    wordDictionary = {}
    wordList = file_contents.split()
    for word in wordList:
        wor = ""
        for c in word:
            if c not in punctuations:
                wor = wor + c
        if wor.lower() not in uninteresting_words and len(wor)>3:
            if wor not in wordDictionary.keys():
                wordDictionary[wor] = 1
            else:
                wordDictionary[wor] += 1
    # wordcloud
    import wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(wordDictionary)
    return cloud.to_array()



# Display your wordcloud image
from matplotlib import pyplot as plt

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()