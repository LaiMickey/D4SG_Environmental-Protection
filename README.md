# [D4SG_新竹縣環保局-便利資訊看板](https://laimickey.github.io/D4SG_Environmental-Protection/)

## 當天簡報
<iframe width="1024" height="768" src="https://www.slideshare.net/MickeyLai2/d4sg-81315677" frameborder="0" allowfullscreen></iframe>

## Power BI
<iframe width="1024" height="768" src="https://goo.gl/81wqnm" frameborder="0" allowfullscreen></iframe>

## 資料來源
* 行政院環境保護署 環境資源資料開放平台(https://opendata.epa.gov.tw/)
* 透明足跡(https://thaubing.gcaa.org.tw)
* 全國商工行政服務入口網(http://gcis.nat.gov.tw)
* 公司名稱&股票代號對照表(D4SG_Environmental-Protection/公司名稱&股票代號對照表.txt)
* 股票網站

## 資料處理步驟
<img src="./資料處理流程圖.jpg" width="100%" />
### Step1. 處理好環保署開放資料後，取出公司名稱，至透明足跡爬取相關資訊(Use R)

<pre><code>
url_front <- "https://thaubing.gcaa.org.tw/envmap?facility_name=&corp_id=&industry_name=All&poltype=All&factory_fine=1&id_2=All&page=0&qt-front_content=1&facility_name="
url_end <- "&corp_id=&industry_name=All&poltype=All&factory_fine=1&id_2=All"
get_url <- paste0(url_front, "公司名稱", url_end)
</code></pre>
