# Face Recognizer System for ML Term Project

## 1. The ML technology you used in the recognizer:  
我們使用Convolution nerual network的方式進行訓練。  
![Alt text](https://github.com/NdhuCarrey/ML2018-FinalProject_154622/blob/master/2.png)  
## 2. The modules enclosed in your recognizer and their functions:  
使用keras套件來實作。GUI的部分使用Python中的tkinter來實作，利用GUI的方式讀取檔案，顯示程式結果。 
![Alt text](https://github.com/NdhuCarrey/ML2018-FinalProject_154622/blob/master/3.png)  
## 3. How you test your recognizer to evaluate its recognition rate:  
我們將training data 切割出20%當作 Validation Set，用來測試神經網路的正確率。
![Alt text](https://github.com/NdhuCarrey/ML2018-FinalProject_154622/blob/master/1.png)
## 4. The problems suffered in your development:  
撰寫測試程式時，訓練時因為training data正確率非常高，但Validation set正確率卻不高，懷疑是overfitting，所以加入dropout來解決這個問題。
在撰寫GUI時，因為第一次接觸Tkinter，在最後要輸出測試結果的圖片到視窗時，無法呈現在GUI上。
## 5. The task allocation of each member and how you integrate the task outputs from all members:  
### 工作分配
| 賴威廷 | 鄭詠儒 | 黃建銘 |
| :--- | :----: | ----:|
|data training| GUI整合 | 部分data training+GUI功能|
### 整合


## 6. How you feel about doing this project:  

