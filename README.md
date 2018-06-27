## Face Recognizer System for ML Term Project

   Team members: 410323022 賴威廷 41032115 鄭詠儒 410321146 黃健銘

## The ML technology we used in the recognizer:  
我們使用Convolution nerual network的方式進行訓練。  

![Alt text](https://github.com/NdhuCarrey/ML2018-FinalProject_154622/blob/master/2.png) 


## The modules enclosed in our recognizer and their functions:  
我們使用keras套件來實作。GUI的部分使用Python中的tkinter來實作，利用GUI的方式讀取檔案，顯示程式結果。   

![Alt text](https://github.com/NdhuCarrey/ML2018-FinalProject_154622/blob/master/3.png)  


## How we test our recognizer to evaluate its recognition rate:  
我們將training data 切割出20%當作 Validation Set，用來測試神經網路的正確率。  

![Alt text](https://github.com/NdhuCarrey/ML2018-FinalProject_154622/blob/master/1.png)  


## The problems suffered in our development:  
撰寫測試程式時，訓練時因為training data正確率非常高，但Validation set正確率卻不高，懷疑是overfitting，所以加入dropout來解決這個問題。
在撰寫GUI時，因為第一次接觸Tkinter，在最後要輸出測試結果的圖片到視窗時，因為變數宣告的方式錯誤導致無法呈現在GUI上。  


## The task allocation of each member and how we integrate the task outputs from all members:  

### 工作分配
| 賴威廷 | 鄭詠儒 | 黃建銘 |
| :---: | :----: | :----:|
|data training| GUI整合 | 部分data training+GUI功能|  

### 整合  
一開始寫了訓練data的演算法，第二個同學加入GUI的按鈕功能，最後一位同學將所有測試結果加入GUI讓所有執行結果在UI視窗上出現。

## How we feel about doing this project:  

我們沒有使用老師建議的演算法而是用了CNN，自己找方法其實並沒有想像中的困難，再來我們把訓練數據的功能完成後加入GUI，而第一次接觸tkinter碰了一些困難，幸好最後有一起將問題解決，順利了完成期末專案。
對於這個專案有點可惜的地方是沒有用一開始同學們的人臉當測試資料，或許按照原本的方式會測試結果對準確率更有感。
