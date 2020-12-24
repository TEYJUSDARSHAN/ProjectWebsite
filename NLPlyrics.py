import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np 

import pickle
with open('tokenizer (1).pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = keras.models.load_model('sheeran_npl_model.h5')




def writelyrics(number,intial_sent):

	seed_text = intial_sent
	next_words = number
  
	for _ in range(next_words):
		token_list = tokenizer.texts_to_sequences([seed_text])[0]
		#print(token_list)
		token_list = pad_sequences([token_list], maxlen=16-1, padding='pre')
		#print(token_list)
		predicted = model.predict_classes(token_list, verbose=0)
		output_word = ""
		for word, index in tokenizer.word_index.items():
			if index == predicted:
				output_word = word
				break
		seed_text += " " + output_word
	return seed_text




