# -*- coding: utf-8 -*-
__author__ = "ALEX-CHUN-YU (P76064538@mail.ncku.edu.tw)"
import jieba
import logging
from hanziconv import HanziConv

# 進行斷詞並過濾 stopword
class Segmentation(object):

	def __init__(self):
		# 用默認 Formatter 為日誌系統建立一個 StreamHandler ，設置基礎配置並加到 root logger 中
		logging.basicConfig(format = "%(asctime)s : %(levelname)s : %(message)s", level = logging.INFO)
		self.stopwordset = set()
		
	# 讀取 stopword 辭典，並存到 stopwordset
	def set_stopword(self):
		with open("stopwords.txt", "r", encoding = "utf-8") as stopwords:
			for stopword in stopwords:
				self.stopwordset.add(stopword.strip('\n'))
		#print(self.stopwordset)
		print("StopWord Set 已儲存!")
	
	# 簡 to 繁
	def simplified_to_traditional(self):
		logging.info("等待中..(簡 to 繁)")
		traditional = open("traditional.txt", "w", encoding = "utf-8")
		with open("wiki_text.txt", "r", encoding = "utf-8") as simplified:
			for s in simplified:
				traditional.write(HanziConv.toTraditional(s))
		print("成功簡體轉繁體!")
		traditional.close()
	
	# 斷詞(Segmentation)並過濾掉停用詞(Stop Word)
	def segmentation(self):
		logging.info("等待中..(jieba 斷詞，並過濾停用詞)")
		segmentation = open("segmentation.txt", "w", encoding = "utf-8")
		with open("traditional.txt", "r", encoding = "utf-8") as Corpus:
			for sentence in Corpus:
				sentence = sentence.strip("\n")
				pos = jieba.cut(sentence, cut_all = False)
				for term in pos:
					if term not in self.stopwordset:
						segmentation.write(term + " ")
		print("jieba 斷詞完畢，並已完成過濾停用詞!")
		segmentation.close()

if __name__ == "__main__":
	segmentation = Segmentation()
	# 讀取停用詞辭典
	segmentation.set_stopword()
	# data 進行簡體轉繁體
	segmentation.simplified_to_traditional()
	# 進行 jieba 斷詞同步過濾停用詞，並產生辭典
	segmentation.segmentation()