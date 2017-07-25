# -*- coding: utf-8 -*-
__author__ = "ALEX-CHUN-YU (P76064538@mail.ncku.edu.tw)"
import warnings
warnings.filterwarnings(action = 'ignore', category = UserWarning, module = 'gensim')
from gensim.models import word2vec

# 主要透過 gensim 訓練成 model 並供使用
class Train(object):

	def __init__(self):
		pass

	# 可參考 https://radimrehurek.com/gensim/models/word2vec.html 更多運用
	def train(self):
		print("訓練中...(喝個咖啡吧^0^)")
		# Load file
		sentence = word2vec.Text8Corpus("segmentation.txt")
		# Setting degree and Produce Model(Train)
		model = word2vec.Word2Vec(sentence, size = 300, window = 10, min_count = 5, workers = 4, sg = 1)
		# Save model 
		model.wv.save_word2vec_format(u"wiki300.model.bin", binary = True)
		print("model 已儲存完畢")

if __name__ == "__main__":
	t = Train()
	# 訓練(shallow semantic space)
	t.train()
