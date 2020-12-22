from tensorflow import keras
import pickle

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = keras.models.load_model('path/to/location')

def writelyrics(numwords,initial_sent):
    seed_text = initial_sent
    next_words = numwords
  
    for _ in range(next_words):
	    token_list = tokenizer.texts_to_sequences([seed_text])[0]
	    token_list = pad_sequences([token_list], maxlen = 15, padding='pre')
	    predicted = model.predict_classes(token_list, verbose=0)
	    output_word = ""
	    for word, index in tokenizer.word_index.items():
		    if index == predicted:
			    output_word = word
			    break
	    seed_text += " " + output_word
    return seed_text
