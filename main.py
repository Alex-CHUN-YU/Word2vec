# -*- coding: utf-8 -*-
__author__ = "ALEX-CHUN-YU (P76064538@mail.ncku.edu.tw)"
import warnings
warnings.filterwarnings(action = 'ignore', category = UserWarning, module = 'gensim')
from gensim.models.keyedvectors import KeyedVectors
'''# 一次處理完畢
from wiki_to_txt import Wiki_to_txt
from segmentation import Segmentation
from train import Train
'''

# 載入 model 並去運用
def main():
	
	'''# 一次處理完畢
	wiki_to_txt = Wiki_to_txt()
	# 將 wiki xml 轉換成 wiki txt
	wiki_to_txt.set_wiki_to_txt("zhwiki-latest-pages-articles.xml.bz2")
	segmentation = Segmentation()
	# 讀取停用詞辭典
	segmentation.set_stopword()
	# data 進行簡體轉繁體
	segmentation.simplified_to_traditional()
	# 進行 jieba 斷詞同步過濾停用詞，並產生辭典
	segmentation.segmentation()
	t = Train()
	# 訓練(shallow semantic space)
	t.train()
	'''
	# 可參考 https://radimrehurek.com/gensim/models/word2vec.html 更多運用
	# How to use bin(model)?
	word_vectors = KeyedVectors.load_word2vec_format("wiki300.model.bin", binary = True)
	print("\n1.輸入一個詞彙會找出前5名相似")
	print("2.輸入兩個詞彙會算出兩者之間相似度")
	print("3.輸入三個詞彙爸爸之於老公,如媽媽之於老婆")
	while True:
		try:
			query = input("\n輸入格式( Ex: 爸爸,媽媽,....註:最多三個詞彙)\n")
			query_list = query.split(",")
			if len(query_list) == 1:
				print("詞彙相似詞前 5 排序")
				res = word_vectors.most_similar(query_list[0], topn = 5)
				for item in res:
					print(item[0] + "," + str(item[1]))
			elif len(query_list) == 2:
				print("計算兩個詞彙間 Cosine 相似度")
				res = word_vectors.similarity(query_list[0], query_list[1])
				print(res)
			else:
				print("%s之於%s，如%s之於" % (query_list[0], query_list[1], query_list[2]))
				res = word_vectors.most_similar(positive = [query_list[0], query_list[1]], negative = [query_list[2]], topn = 5)
				for item in res:
					print(item[0] + "," + str(item[1]))
		except Exception as e:
			print("Error:" + repr(e))

if __name__ == "__main__":
    main()
