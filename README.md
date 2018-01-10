# Word2Vec
Word2vec 是基於非監督式學習，訓練集建議越大越好，語料涵蓋的越全面，訓練出來的結果相對比較好，當然也有可能 garbage input 進而得到 garbage output ，由於檔案所使用的資料集較大，所以每個過程中都請耐心等候。(ps: word2vec 如果把每種字當成一個維度，假設總共有 4000 個總字，那麼向量就會有 4000 維度。故可透過它來降低維度)</br></br>
此網址可以讓你更了解它(http://cpmarkchang.logdown.com/posts/773062-neural-network-word2vec-part-1-overview)

![demo](https://github.com/Alex-CHUN-YU/Word2vec/blob/master/image/demo.png)</br></br>
WiKi簡介:</br>
Word2vec is a group of related models that are used to produce word embeddings. These models are shallow, two-layer neural networks that are trained to reconstruct linguistic contexts of words. Word2vec takes as its input a large corpus of text and produces a vector space, typically of several hundred dimensions, with each unique word in the corpus being assigned a corresponding vector in the space. Word vectors are positioned in the vector space such that words that share common contexts in the corpus are located in close proximity to one another in the space. By the way, Skip-Gram 是給定 input word 來預測上下文。而 CBOW 是給定上下文，來預測 input word.</br>
by the way :</br>
Skip-gram: works well with small amount of the training data, represents well even rare words or phrases.</br>

CBOW: several times faster to train than the skip-gram, slightly better accuracy for the frequent words.

## 使用方式
Input:</br>
```
1.download wiki data(請參考資料集)
2.進入 Word2Vec 資料夾
3.執行 python wiki_to_txt.py zhwiki-latest-pages-articles.xml.bz2(wiki xml 轉換成 wiki text)
4.執行 python segmentation.py(簡體轉繁體，在進行斷詞並同步過濾停用詞，由於檔案較大故斷詞較久)
5.執行 python train.py(訓練並產生 model ，時間上也會比較久)
5.執行 python main.py(使用 Model，輸入詞彙)
註:如果在 Windows cmd 下執行 python 時有編碼問題請下以下指令:chcp 65001(使用utf-8)
```
Output:</br>
```
1.輸入一個詞彙會找出前5名相似
2.輸入兩個詞彙會算出兩者之間相似度
3.輸入三個詞彙爸爸之於老公,如媽媽之於老婆

輸入格式( Ex: 爸爸,媽媽,....註:最多三個詞彙)
老師
詞彙相似詞前 5 排序
班導,0.6360481977462769
班導師,0.6360464096069336
代課,0.6358826160430908
級任,0.6271134614944458
班主任,0.6270170211791992

輸入格式( Ex: 爸爸,媽媽,....註:最多三個詞彙)
爸爸,媽媽
計算兩個詞彙間 Cosine 相似度
0.780765200371

輸入格式( Ex: 爸爸,媽媽,....註:最多三個詞彙)
爸爸,老公,媽媽
爸爸之於老公，如媽媽之於
老婆,0.5401346683502197
蠢萌,0.5245970487594604
夠秤,0.5059393048286438
駁命,0.4888317286968231
孔爵,0.4857243597507477
```

## 資料集(wiki data)
```
主要以 pages-articles.xml.bz2 結尾之檔案類型，這邊使用 zhwiki-latest-pages-articles.xml.bz2。
```
* 維基資料集:</br>
https://zh.wikipedia.org/wiki/Wikipedia:%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8B%E8%BD%BD</br>
* zhwiki-latest-pages-articles.xml.bz2 下載網址:</br>
https://drive.google.com/file/d/0B4rlWa2S_JMBUmlMSG5IRVRMbnc/view?usp=sharing </br>
* 程式參考網址:</br>
https://radimrehurek.com/gensim/corpora/wikicorpus.html</br>
https://radimrehurek.com/gensim/models/word2vec.html</br>
## 開發環境
Python 3.5.2</br>
pip install gensim</br>
pip install jieba</br>
pip install hanziconv</br>
