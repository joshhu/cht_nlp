# 20200615-20200617中華電信NLP課程

## 投影片說明

本投影片大部分來自台大電機系教授李宏毅老師的youtube影片，特此聲明。講義內容如下：

* 00 - NLP介紹.pptx
* 01 - NLP Tasks介紹.pptx
* 02 - Word Embeddings.pptx
* 03 - 神經網路語言模型(optional).pptx
* 04 - RNN & LSTM.pptx
* 05 - Seq2Seq.pptx
* 06 - Transformers.pptx
* 07 - Elmo, Bert and family.pptx

## 程式碼說明

* Amazon_Reviews - 用lstm做出amazon商品的情境分析
* Chinese_Poem - 中文做詩系統，使用lstm
* Jokes - 用gpt2訓練一個會產生笑話的系統
* MNIST - 用lstm跑 mnist 手寫辨識系統
* Tranformer - 用bert做google play的商品評價分析
* Word2vec - 用gensim做維基百科中文版的word embedding

## 參考資料

大部分投影片最後都有參考的網頁資料。主要參考李宏毅老師的影片

李宏毅老師影片 - https://www.youtube.com/channel/UC2ggjtuuWvxrHHHiaDH1dlQ

史丹佛大學cs224n-2019 - https://www.bilibili.com/video/BV19b411n7K1/?spm_id_from=333.788.videocard.0

## 聯絡方式

如果有任何問題，請寫信給我
joshhu.usa@gmail.com

## 同學問題

1. Amazon Review中`vocab_size = len(word2idx) + 1`是錯誤的，因為已經放入`_PAD`和`_UNK`，因此更正為`vocab_size = len(word2idx)`即可。


