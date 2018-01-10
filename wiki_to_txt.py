# -*- coding: utf-8 -*-
__author__ = "ALEX-CHUN-YU (P76064538@mail.ncku.edu.tw)"
import logging
import sys
import warnings
warnings.filterwarnings(action ='ignore', category = UserWarning, module = 'gensim')
from gensim.corpora import WikiCorpus

# 將 wiki 資料集載下後進行 xml convert to txt 
class Wiki_to_txt(object):

	def __init__(self):
		# 用默認 Formatter 為日誌系統建立一個 StreamHandler ，設置基礎配置並加到 root logger 中
		logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)

	# 使用方法 https://radimrehurek.com/gensim/corpora/wikicorpus.html
	def set_wiki_to_txt(self, wiki_data_path = None):
		if wiki_data_path == None:
			# 系統下參數
			if len(sys.argv) != 2:
				print("Please Usage: python3 " + sys.argv[0] + " wiki_data_path")
				exit()
			else:
				wiki_corpus = WikiCorpus(sys.argv[1], dictionary = {})
		else:
			wiki_corpus = WikiCorpus(wiki_data_path, dictionary = {})
		# wiki.xml convert to wiki.txt
		with open("wiki_text.txt", 'w', encoding = 'utf-8') as output:
			text_count = 0
			for text in wiki_corpus.get_texts():
				# save use string(gensim)
				output.write(' '.join(text) + '\n')
				text_count += 1
				if text_count % 10000 == 0:
					logging.info("目前已處理 %d 篇文章" % text_count)
			print("轉檔完畢!")
			
if __name__ == "__main__":
	wiki_to_txt = Wiki_to_txt()
	# 將 wiki xml 轉換成 wiki txt
	wiki_to_txt.set_wiki_to_txt()
