import os, re, csv

SPECIAL_CHAR = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def has_alphabet(word):
	return re.search('[a-zA-Z]', word)

def remove_non_alphabet(word):
	english_chars = re.findall('[a-zA-Z]', word)
	return ''.join(english_chars)

def read_dict(filename):
	with open(filename,'r') as file:
		content = file.read()
		words = content.split()
		for i in range(len(words)):
			words[i] = remove_non_alphabet(words[i].lower())
		return words




def pre_process(ham_folder,spam_folder,out_file,words_list,dictionary_file):
	# data = []
	words_list += ['un_recog','re_recog','special_char','total_word','label']
	with open(out_file, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(words_list)
		for filename in os.listdir(ham_folder):
			file_path = os.path.join(ham_folder,filename)
			if os.path.isfile(file_path):
				try:
					with open(file_path,'r', encoding='utf-8', errors='strict') as file:
						content = file.read()
						words = content.split()
						file_data = []
						# words list plus non-recognized words and total words
						for _ in range(len(words_list)+5):
							file_data.append(0)
						for word in words:
							for char in word:
								if char in SPECIAL_CHAR:
									file_data[-3] +=1
							# count wordlist words
							if word in words_list:
								file_data[words_list.index(word)] += 1
							# count non-recognized words
							if has_alphabet(word) and not (word.lower() in dictionary_file):
								file_data[-5] += 1
								# count misspelled words
								if remove_non_alphabet(word.lower()) in dictionary_file:
									file_data[-4] += 1

							file_data[-2] += 1
							file_data[-1] = 1 # spam
						writer.writerow(file_data)
				except UnicodeDecodeError:
					pass

		for filename in os.listdir(spam_folder):
			file_path = os.path.join(spam_folder,filename)
			if os.path.isfile(file_path):
				try:
					with open(file_path,'r', encoding='utf-8', errors='strict') as file:
						content = file.read()
						words = content.split()
						file_data = []
						# words list plus non-recognized words and total words
						for _ in range(len(words_list)+5):
							file_data.append(0)
						for word in words:
							for char in word:
								if char in SPECIAL_CHAR:
									file_data[-3] +=1
							# count wordlist words
							if word in words_list:
								file_data[words_list.index(word)] += 1
							# count non-recognized words
							if has_alphabet(word) and not (word.lower() in dictionary_file):
								file_data[-5] += 1
								# count misspelled words
								if remove_non_alphabet(word.lower()) in dictionary_file:
									file_data[-4] += 1

							file_data[-2] += 1
							file_data[-1] = 0 # spam
						writer.writerow(file_data)
				except UnicodeDecodeError:
					pass
			




def main():
	# folders = ['enron1']
	folders = ['enron1','enron2','enron3','enron4','enron5','enron6']
	dictionary_file = '3000_words.txt'
	dictionary = read_dict(dictionary_file)
	

	for f in folders:
		words_list = ['money','send','chance','you','call']
		ham_folder = '../data/'+f+'/ham'
		spam_folder = '../data/'f+'/spam'
		out_file = '../data/'f+'_data.csv'
		pre_process(ham_folder,spam_folder,out_file,words_list,dictionary)

if __name__ == '__main__':
	main()