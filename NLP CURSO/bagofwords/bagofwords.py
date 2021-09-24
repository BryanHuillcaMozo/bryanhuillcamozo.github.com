import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

dataset = open("topic.txt","r").read()

def create_word_cloud(string):
    cloud = WordCloud(background_color ="white",max_words =200, stopowords= set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("WordCloud.png")
dataset = dataset.lower()
create_word_cloud(dataset)
