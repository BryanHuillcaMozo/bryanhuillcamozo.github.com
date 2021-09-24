# -*- coding: utf-8 -*-
"""PosTagging-NER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f_4dcDpZNAM_qeahBV6Et1Fb2pt2Pgz0

# POS-TAGGING y NER

## Librerías

"es_core_news_md" Modelo optimizado con gpu para postagging en español
"""

!python -m spacy download es_core_news_md
!python -m spacy link es_core_news_md es

!pip install stylecloud

from collections import Counter
from nltk import word_tokenize
from spacy import displacy
from nltk.tag.stanford import StanfordPOSTagger
import es_core_news_md
import nltk
import spacy
import os
import json
import pandas as pd
import random
import matplotlib.pyplot as plt
from PIL import Image
# LIBRERIA PARA REALIZAR NUBES DE PALABRAS
from wordcloud import WordCloud
import stylecloud as sc

"""*** Requisito adicional ***

Instalación de java
"""

def install_java():
  !apt update
  !apt-get install -y openjdk-8-jdk-headless -qq > /dev/null      #install openjdk
  os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"     #set environment variable
  !java -version       #check java version
install_java()

"""## Módulos"""

def PosTagging(rows):
  nlp = spacy.load("es")
  titulos = dict()
  objetos = dict()
  for row in rows:
    pt_titulo = []
    pt_objeto = []
    for i in range(len(row)):
      if i == 0:
        doc = nlp(row[i])
        for token in doc:
          arreglo_tokens_titulo = [token.text, token.pos_, token.dep_]
          pt_titulo.append(arreglo_tokens_titulo)
        titulos[doc.text] = pt_titulo
      if i == 1:
        doc = nlp(row[i])
        for token in doc:
          arreglo_tokens_objeto = [token.text, token.pos_, token.dep_]
          pt_objeto.append(arreglo_tokens_objeto)
        objetos[doc.text] = pt_objeto
  return titulos,objetos

def NER(rows):
  nlp = es_core_news_md.load()
  for row in rows:
    for i in range(len(row)):
      if i == 0:
        titulo = row[i]
        print("Título: ", titulo)
        print("NER Título: ")
        displacy.render(nlp(titulo), jupyter=True, style='ent')
      if i == 1:
        objeto = row[i]
        print("Objeto: ", objeto)
        print("NER Objeto: ")
        displacy.render(nlp(objeto), jupyter=True, style='ent')

def PosTagging_NER_Titulo(rows, nro_fila):
  nlp = es_core_news_md.load()

  titulo = rows[nro_fila][0]

  doc = nlp(titulo)
  print([(w.text, w.pos_) for w in doc])
  print()
  print([(X.text, X.label_) for X in doc.ents])
  print([(X, X.ent_iob_, X.ent_type_) for X in doc])
  return doc,titulo

def PosTagging_NER_Objeto(rows, nro_fila):
  objeto = rows[nro_fila][1]

  doc = nlp(objeto)
  print([(w.text, w.pos_) for w in doc])
  print()
  print([(X.text, X.label_) for X in doc.ents])
  print([(X, X.ent_iob_, X.ent_type_) for X in doc])
  return doc,objeto

def diccionarios_para_nubes(diccionario):
  sustantivos = []
  verbos = []
  adjetivos = []
  dic_sust = dict()
  dic_verb = dict()
  dic_adj = dict()
  for key in diccionario.keys():
    for i in diccionario[key]:
      if (i[1] == "NOUN" or i[1] == "PROPN"):
        sustantivos.append(i[0])
      elif (i[1] == "VERB"):
        verbos.append(i[0])
      elif (i[1] == "ADJ"):
        adjetivos.append(i[0])
  sust_sin_repeticiones = list(set(sustantivos))
  verb_sin_repeticiones = list(set(verbos))
  adj_sin_repeticiones = list(set(adjetivos))
  for sust in sust_sin_repeticiones:
    dic_sust[sust] = sustantivos.count(sust)
  for verb in verb_sin_repeticiones:
    dic_verb[verb] = verbos.count(verb)
  for adj in adj_sin_repeticiones:
    dic_adj[adj] = adjetivos.count(adj)
  return (dic_sust,dic_verb,dic_adj)

def show_wordcloud(Dic, save=False, img_name=None):
  wordcloud = WordCloud(
    background_color = 'white',
    max_words = 100,
    relative_scaling = 1,
    scale = 2,
    random_state=1,
    collocations=False,
    max_font_size=200
  ).generate_from_frequencies(Dic)
  fig = plt.figure(1, figsize=(12, 12))
  plt.axis('off')
  plt.imshow(wordcloud)
  if save: plt.savefig(img_name)
  plt.show()

"""## Lectura de datos"""



Accesibilidad = read_data('LeyesAccesibilidad.csv', 'Titulo', 'Objeto')

Auditabilidad = read_data('LeyesAuditabilidad.csv', 'Titulo', 'Objeto')

Informatividad = read_data('LeyesInformatividad.csv', 'Titulo', 'Objeto')

Usabilidad = read_data('LeyesUsabilidad.csv', 'Titulo', 'Objeto')

Comprensibilidad = read_data('LeyesComprensibilidad.csv', 'Titulo', 'Objeto')

"""## TOPICO 1: ACCESIBILIDAD

### 1. POS-Tagging usando spacy
"""

TitulosAccesibilidad, ObjetosAccesibilidad = PosTagging(Accesibilidad)

TitulosAccesibilidad

ObjetosAccesibilidad

"""### 2. NER usando spacy"""

NER(Accesibilidad)

"""### 3. Ejemplo específico: Pos tagging y NER"""

# Nro de fila aleatorio para mostrar un ejemplo específico
Nro_fila = random.randrange(0,len(Accesibilidad)-1)
nlp = es_core_news_md.load()

"""#### Título"""

DocAccesibilidad,TitleAccesibilidad = PosTagging_NER_Titulo(Accesibilidad, Nro_fila)

displacy.render(DocAccesibilidad, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(TitleAccesibilidad), jupyter=True, style='ent')

"""#### Objeto"""

DocAccesibilidad2,ObjetoAccesibilidad = PosTagging_NER_Objeto(Accesibilidad, Nro_fila)

displacy.render(DocAccesibilidad2, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(ObjetoAccesibilidad), jupyter=True, style='ent')

"""### 4. Nube de palabras"""

Sus_Tit_Acces, Verb_Tit_Acces, Adj_Tit_Acces = diccionarios_para_nubes(TitulosAccesibilidad)
Sus_Obj_Acces, Verb_Obj_Acces, Adj_Obj_Acces = diccionarios_para_nubes(ObjetosAccesibilidad)

"""#### Sustantivos del título"""

show_wordcloud(Sus_Tit_Acces, save=True, img_name="WC_Sust_Titulo_Accesibilidad")

"""#### Verbos del título"""

show_wordcloud(Verb_Tit_Acces, save=True, img_name="WC_Verb_Titulo_Accesibilidad")

"""#### Adjetivos del título"""

show_wordcloud(Adj_Tit_Acces, save=True, img_name="WC_Adj_Titulo_Accesibilidad")

"""#### Sustantivos del Objeto"""

show_wordcloud(Sus_Obj_Acces, save=True, img_name="WC_Sust_Objeto_Accesibilidad")

"""#### Verbos del Objeto"""

show_wordcloud(Verb_Obj_Acces, save=True, img_name="WC_Verb_Objeto_Accesibilidad")

"""#### Adjetivos del Objeto"""

show_wordcloud(Adj_Obj_Acces, save=True, img_name="WC_Adj_Objeto_Accesibilidad")

"""## TOPICO 2: AUDITABILIDAD

### 1. POS-Tagging usando spacy
"""

TitulosAuditabilidad,ObjetosAuditabilidad = PosTagging(Auditabilidad)

"""### 2. NER usando spacy"""

NER(Auditabilidad)

"""### 3. Ejemplo especifico: Pos tagging y NER"""

# Nro de fila aleatorio para mostrar un ejemplo específico
Nro_fila = random.randrange(0,len(Auditabilidad)-1)

"""#### Título"""

DocAuditabilidad,TitleAuditabilidad = PosTagging_NER_Titulo(Auditabilidad,Nro_fila)

displacy.render(DocAuditabilidad, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(TitleAuditabilidad), jupyter=True, style='ent')

"""#### Objeto"""

DocAuditabilidad2,ObjetoAuditabilidad = PosTagging_NER_Objeto(Auditabilidad, Nro_fila)

displacy.render(DocAuditabilidad2, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(ObjetoAuditabilidad), jupyter=True, style='ent')

"""### 4. Nube de palabras"""

Sus_Tit_Audi, Verb_Tit_Audi, Adj_Tit_Audi = diccionarios_para_nubes(TitulosAuditabilidad)
Sus_Obj_Audi, Verb_Obj_Audi, Adj_Obj_Audi = diccionarios_para_nubes(ObjetosAuditabilidad)

"""#### Sustantivos del título"""

show_wordcloud(Sus_Tit_Audi, save=True, img_name="WC_Sust_Titulo_Auditabilidad")

"""#### Verbos del título"""

show_wordcloud(Verb_Tit_Audi, save=True, img_name="WC_Verb_Titulo_Auditabilidad")

"""#### Adjetivos del título"""

show_wordcloud(Adj_Tit_Audi, save=True, img_name="WC_Adj_Titulo_Auditabilidad")

"""#### Sustantivos del Objeto"""

show_wordcloud(Sus_Obj_Audi, save=True, img_name="WC_Sust_Objeto_Auditabilidad")

"""#### Verbos del Objeto"""

show_wordcloud(Verb_Obj_Audi, save=True, img_name="WC_Verb_Objeto_Auditabilidad")

"""#### Adjetivos del Objeto"""

show_wordcloud(Adj_Obj_Audi, save=True, img_name="WC_Adj_Objeto_Auditabilidad")

"""## TOPICO 3: INFORMATIVIDAD

### 1. POS-Tagging usando spacy
"""

TitulosInformatividad,ObjetosInformatividad = PosTagging(Informatividad)

"""### 2. NER usando spacy"""

NER(Informatividad)

"""### 3. Ejemplo específico: Pos tagging y NER"""

# Nro de fila aleatorio para mostrar un ejemplo específico
Nro_fila = random.randrange(0,len(Informatividad)-1)

"""#### Título"""

DocInformatividad,TitleInformatividad = PosTagging_NER_Titulo(Informatividad,Nro_fila)

displacy.render(DocInformatividad, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(TitleInformatividad), jupyter=True, style='ent')

"""#### Objeto"""

DocInformatividad2,ObjetoInformatividad = PosTagging_NER_Objeto(Informatividad, Nro_fila)

displacy.render(DocInformatividad2, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(ObjetoInformatividad), jupyter=True, style='ent')

"""### 4. Nube de palabras"""

Sus_Tit_Infor, Verb_Tit_Infor, Adj_Tit_Infor = diccionarios_para_nubes(TitulosInformatividad)
Sus_Obj_Infor, Verb_Obj_Infor, Adj_Obj_Infor = diccionarios_para_nubes(ObjetosInformatividad)

"""#### Sustantivos del título"""

show_wordcloud(Sus_Tit_Infor, save=True, img_name="WC_Sust_Titulo_Informatividad")

"""#### Verbos del título"""

show_wordcloud(Verb_Tit_Infor, save=True, img_name="WC_Verb_Titulo_Informatividad")

"""#### Adjetivos del título"""

show_wordcloud(Adj_Tit_Infor, save=True, img_name="WC_Adj_Titulo_Informatividad")

"""#### Sustantivos del Objeto"""

show_wordcloud(Sus_Obj_Infor, save=True, img_name="WC_Sust_Objeto_Informatividad")

"""#### Verbos del Objeto"""

show_wordcloud(Verb_Obj_Infor, save=True, img_name="WC_Verb_Objeto_Informatividad")

"""#### Adjetivos del Objeto"""

show_wordcloud(Adj_Obj_Infor, save=True, img_name="WC_Adj_Objeto_Informatividad")

"""## TOPICO 4: USABILIDAD

### 1. POS-Tagging usando spacy
"""

TitulosUsabilidad,ObjetosUsabilidad = PosTagging(Usabilidad)

"""### 2. NER usando spacy"""

NER(Usabilidad)

"""### 3. Ejemplo específico: Pos tagging y NER"""

# Nro de fila aleatorio para mostrar un ejemplo específico
Nro_fila = random.randrange(0,len(Usabilidad)-1)

"""#### Título"""

DocUsabilidad,TitleUsabilidad = PosTagging_NER_Titulo(Usabilidad,Nro_fila)

displacy.render(DocUsabilidad, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(TitleUsabilidad), jupyter=True, style='ent')

"""#### Objeto"""

DocUsabilidad2,ObjetoUsabilidad = PosTagging_NER_Objeto(Usabilidad, Nro_fila)

displacy.render(DocUsabilidad2, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(ObjetoUsabilidad), jupyter=True, style='ent')

"""### 4. Nube de palabras"""

Sus_Tit_Usa, Verb_Tit_Usa, Adj_Tit_Usa = diccionarios_para_nubes(TitulosUsabilidad)
Sus_Obj_Usa, Verb_Obj_Usa, Adj_Obj_Usa = diccionarios_para_nubes(ObjetosUsabilidad)

"""#### Sustantivos del título"""

show_wordcloud(Sus_Tit_Usa, save=True, img_name="WC_Sust_Titulo_Usabilidad")

"""#### Verbos del título"""

show_wordcloud(Verb_Tit_Usa, save=True, img_name="WC_Verb_Titulo_Usabilidad")

"""#### Adjetivos del título"""

show_wordcloud(Adj_Tit_Usa, save=True, img_name="WC_Adj_Titulo_Usabilidad")

"""#### Sustantivos del Objeto"""

show_wordcloud(Sus_Obj_Usa, save=True, img_name="WC_Sust_Objeto_Usabilidad")

"""#### Verbos del Objeto"""

show_wordcloud(Verb_Obj_Usa, save=True, img_name="WC_Verb_Objeto_Usabilidad")

"""#### Adjetivos del Objeto"""

show_wordcloud(Adj_Obj_Usa, save=True, img_name="WC_Adj_Objeto_Usabilidad")

"""## TOPICO 5: COMPRENSIBILIDAD

### 1. POS-Tagging usando spacy
"""

TitulosComprensibilidad,ObjetosComprensibilidad = PosTagging(Comprensibilidad)

"""### 2. NER usando spacy"""

NER(Comprensibilidad)

"""### 3. Ejemplo específico: Pos tagging y NER"""

# Nro de fila aleatorio para mostrar un ejemplo específico
Nro_fila = random.randrange(0,len(Comprensibilidad)-1)

"""#### Título"""

DocComprensibilidad,TitleComprensibilidad = PosTagging_NER_Titulo(Comprensibilidad,Nro_fila)

displacy.render(DocComprensibilidad, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(TitleComprensibilidad), jupyter=True, style='ent')

"""#### Objeto"""

DocComprensibilidad2,ObjetoComprensibilidad = PosTagging_NER_Objeto(Comprensibilidad, Nro_fila)

displacy.render(DocComprensibilidad2, style='dep', jupyter=True, options={'distance': 120})

displacy.render(nlp(ObjetoComprensibilidad), jupyter=True, style='ent')

"""### 4. Nube de palabras"""

Sus_Tit_Comp, Verb_Tit_Comp, Adj_Tit_Comp = diccionarios_para_nubes(TitulosComprensibilidad)
Sus_Obj_Comp, Verb_Obj_Comp, Adj_Obj_Comp = diccionarios_para_nubes(ObjetosComprensibilidad)

"""#### Sustantivos del título"""

show_wordcloud(Sus_Tit_Comp, save=True, img_name="WC_Sust_Titulo_Comprensibilidad")

"""#### Verbos del título"""

show_wordcloud(Verb_Tit_Comp, save=True, img_name="WC_Verb_Titulo_Comprensibilidad")

"""#### Adjetivos del título"""

show_wordcloud(Adj_Tit_Comp, save=True, img_name="WC_Adj_Titulo_Comprensibilidad")

"""#### Sustantivos del Objeto"""

show_wordcloud(Sus_Obj_Comp, save=True, img_name="WC_Sust_Objeto_Comprensibilidad")

"""#### Verbos del Objeto"""

show_wordcloud(Verb_Obj_Comp, save=True, img_name="WC_Verb_Objeto_Comprensibilidad")

"""#### Adjetivos del Objeto"""

show_wordcloud(Adj_Obj_Comp, save=True, img_name="WC_Adj_Objeto_Comprensibilidad")

"""# Otros"""

# CREAMOS LA NUBE DE PALABRAS Y LA GUARDAMOS
def draw_wordcloud(Dic, img_name=None):
  url_save_png = img_name + ".png"

  sc.gen_stylecloud(
      text= Dic,
      colors=['#ecf0f1', '#3498db', '#e74c3c'],
      icon_name='fas fa-cloud',
      background_color='#1A1A1A',
      output_name = url_save_png,
      size = 2048,
      max_words = 300,
      max_font_size = 450
       )
  img = Image.open(img_name + ".png",'r')
  img.show()

def show_wordcloud(Dic, save=False, img_name=None):
  wordcloud = WordCloud(
    background_color = 'white',
    max_words = 1000,
    relative_scaling = 1,
    scale = 3,
    random_state=1,
    collocations=False
  ).generate_from_frequencies(Dic)
  fig = plt.figure(1, figsize=(12, 12))
  plt.axis('off')
  plt.imshow(wordcloud)
  if save: plt.savefig(img_name)
  plt.show()

dictionary= {'asielzoekers': 0.0034861170591325486,
 'belastingverlaging': 0.0018551991553514675,
 'buma': 0.0020712555982839408,
 'islam': 0.0029519544163739155,
 'moslims': 25,
 'ouderen': 4,
 'pechtold': 10,
 'president': 16,
 'rutte': 5,
 'samsom': 4} 

show_wordcloud(dictionary, save=True, img_name="nn")

draw_wordcloud(dictionary, img_name="nuu")

"""### 2. Pos Tagging usando la librería nltk"""

java_path = "/usr/lib/jvm/java-11-openjdk-amd64/bin"
os.environ['JAVAHOME'] = java_path
spanish_postagger = StanfordPOSTagger('spanish.tagger', 
                                      'stanford-postagger.jar')

with open("spanish-tags.json", "r") as r:
    spanish_tags = json.load(r)

for row in rows:
  pt_titulo = []
  for i in range(len(row)):
    if i == 0:
      print(row[i])
      tags = spanish_postagger.tag(row[i].split())
      for token, tag in tags:
        print(f"{token:15} -> {spanish_tags[tag]['description']}")
    if i == 1:
      print(row[i])
      tags = spanish_postagger.tag(row[i].split())
      for token, tag in tags:
        if (tag in spanish_tags):
          print(f"{token:15} -> {spanish_tags[tag]['description']}")
        else:
          print(f"{token:15} -> {tag}")
  print(" ")