# 前言及目的  
PowerBI是一個相對便宜好用的報表及資料視覺化的工具，這篇文章討論到
1. 以此資料集讀入資料時，需要在哪裡調整格式  
2. 簡單常用的圖表  
3. PowerBI限制及缺點  

## 資料格式調整處

讀入資料後，若需要
* 清理資料  
* 合併資料 
* 調整資料格式 
需要到Edit Queires
你做的任何步驟 都會在操作介面最右側呈現

![調整處](https://www.evernote.com/l/ANxhsmSScrJKC6yY8-1eiq63nNp9jxWhTXcB/image.png)

![操作介面](https://www.evernote.com/l/ANzvGHxJsotEy578ps2KpHHsNMOWCp1TMQsB/image.png)  

目前微軟提供的操作選項有以下，綠框為此次專案有使用到的

![工作選項](https://www.evernote.com/l/ANwwxuEAF8RCLoriwHGEanc3edW17oxfvscB/image.png)
![工作選項](https://www.evernote.com/l/ANzlOmYoBMlEr6pl-Jxirj1WIVWD4BmKqVIB/image.png)  


重要!重要!重要!
資料操作完後，請記得按下"Close & Apply"
(目前使用PowerBI心得，在資料格式整理 應該是獨立的模組_Edit Queires_ 執行，所以，需要另外按下Close&Apply才會儲存完畢回到PowerBI)


## 簡單常用的圖表  

### 直方圖  
先選取右上角直方圖的圖例，在資料集中對應Axis,Legend,Value做對應選擇

![直方圖](https://www.evernote.com/l/ANw7Dtobw35DfpoThUe9vReEohqaxAUjNAUB/image.png)  

參考線需要選取，此次報告的參考線是固定形式，在Value部分加入值。
![參考線](https://www.evernote.com/l/ANyLLu8js8xO9Li1VDp_y0WHUIburA3r0rIB/image.png)


### Filter  

可增加Filter,此Filter控制整個頁面
![filter](https://www.evernote.com/l/ANzTVymnEARJ57OvSH7_iSJxgPK2GlwtayoB/image.png)



## PowerBI優點、限制及缺點、建議

### 優點  
相對於Excel、ggplot2等軟體，PowerBI在製作互動式報表快速跟簡便，如果都在同一個組織群組(email domain為相同學校或公司)可共編。

### 限制及缺點  
* 目前只開放組織申請，私人的email帳號無法使用，需要組織的email帳號  
* 以此次是黑客松形式，組員都不在同一個組織下，在共編使用不同步的方式，以A做完存成pbix檔，轉給下一個人，但，資料集的路徑需要另外設定不能指向私人的路徑 
* PowerBI只能在WindowsOS使用  
* PowerBI豐富性及方便度略遜於tableau

## 建議  
* 若是可公開資料，建議可使用tableau  
* 建議資料集另外存在db中，方便大家共同使用  



