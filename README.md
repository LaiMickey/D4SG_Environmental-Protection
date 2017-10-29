# [D4SG_新竹縣環保局-便利資訊看板](https://laimickey.github.io/D4SG_Environmental-Protection/)

## 當天簡報(https://www.slideshare.net/MickeyLai2/d4sg-81315677)
<iframe src="//www.slideshare.net/slideshow/embed_code/key/yzTbIGpzWkByHP" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/MickeyLai2/d4sg-81315677" title="【D4SG】新竹縣環保局-便利資訊看板(雛形)" target="_blank">【D4SG】新竹縣環保局-便利資訊看板(雛形)</a> </strong> from <strong><a href="https://www.slideshare.net/MickeyLai2" target="_blank">Mickey Lai</a></strong> </div>

## Power BI(https://goo.gl/81wqnm)
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

<pre class="r"><code class="r"><span class="keyword">library</span><span class="paren">(</span><span class="identifier">RODBC</span><span class="paren">)</span>
<span class="keyword">library</span><span class="paren">(</span><span class="identifier">httr</span><span class="paren">)</span>

<span class="identifier">regexp</span> <span class="operator">&lt;-</span> <span class="keyword">function</span><span class="paren">(</span><span class="identifier">pattern</span>, <span class="identifier">data</span>, <span class="identifier">idx</span><span class="operator">=</span><span class="number">1L</span>, <span class="identifier">is.split</span><span class="operator">=</span><span class="literal">FALSE</span>, <span class="identifier">spt</span><span class="operator">=</span><span class="literal">NULL</span><span class="paren">)</span> <span class="paren">{</span>
  <span class="identifier">text</span> <span class="operator">&lt;-</span> <span class="identifier">data</span><span class="paren">[</span><span class="identifier">idx</span><span class="paren">]</span>
  <span class="identifier">v</span> <span class="operator">&lt;-</span> <span class="identifier">regexpr</span><span class="paren">(</span><span class="identifier">pattern</span>, <span class="identifier">text</span><span class="paren">)</span>
  <span class="identifier">n</span> <span class="operator">&lt;-</span> <span class="identifier">unlist</span><span class="paren">(</span><span class="identifier">lapply</span><span class="paren">(</span><span class="identifier">strsplit</span><span class="paren">(</span><span class="identifier">pattern</span>, <span class="string">"\\.\\+"</span><span class="paren">)</span>, <span class="identifier">nchar</span><span class="paren">)</span><span class="paren">)</span>
  <span class="identifier">out</span> <span class="operator">&lt;-</span> <span class="identifier">substr</span><span class="paren">(</span><span class="identifier">text</span>, <span class="identifier">v</span> <span class="operator">+</span> <span class="identifier">n</span><span class="paren">[</span><span class="number">1</span><span class="paren">]</span>, <span class="identifier">v</span> <span class="operator">+</span> <span class="identifier">attr</span><span class="paren">(</span><span class="identifier">v</span>,<span class="string">"match.length"</span><span class="paren">)</span> <span class="operator">-</span> <span class="paren">(</span><span class="identifier">n</span><span class="paren">[</span><span class="number">2</span><span class="paren">]</span><span class="operator">+</span><span class="number">1</span><span class="paren">)</span><span class="paren">)</span>
  <span class="keyword">if</span> <span class="paren">(</span><span class="identifier">is.split</span><span class="paren">)</span> <span class="identifier">unlist</span><span class="paren">(</span><span class="identifier">strsplit</span><span class="paren">(</span><span class="identifier">out</span>, <span class="identifier">spt</span><span class="paren">)</span><span class="paren">)</span> <span class="keyword">else</span> <span class="identifier">out</span>
<span class="paren">}</span> <span class="comment"># end regexp()</span>


<span class="comment">## 組出爬網URL</span>
<span class="identifier">url_front</span> <span class="operator">&lt;-</span> <span class="string">"https://thaubing.gcaa.org.tw/envmap?facility_name=&amp;corp_id=&amp;industry_name=All&amp;poltype=All&amp;factory_fine=1&amp;id_2=All&amp;page=0&amp;qt-front_content=1&amp;facility_name="</span>
<span class="identifier">url_end</span> <span class="operator">&lt;-</span> <span class="string">"&amp;corp_id=&amp;industry_name=All&amp;poltype=All&amp;factory_fine=1&amp;id_2=All"</span>
<span class="identifier">get_url</span> <span class="operator">&lt;-</span> <span class="identifier">paste0</span><span class="paren">(</span><span class="identifier">url_front</span>, <span class="string">"峻源股份有限公司"</span>, <span class="identifier">url_end</span><span class="paren">)</span>


<span class="comment">## 至透明足跡爬取資料=&gt;先取得該公司在透明足跡網址</span>
<span class="identifier">html</span> <span class="operator">&lt;-</span> <span class="identifier">GET</span><span class="paren">(</span><span class="identifier">get_url</span><span class="paren">)</span>
<span class="identifier">web_content</span> <span class="operator">&lt;-</span> <span class="identifier">content</span><span class="paren">(</span><span class="identifier">html</span>, <span class="string">"text"</span>, <span class="identifier">encoding</span> <span class="operator">=</span> <span class="string">"UTF-8"</span><span class="paren">)</span>

<span class="identifier">target_path</span> <span class="operator">&lt;-</span> <span class="identifier">regexp</span><span class="paren">(</span><span class="identifier">paste0</span><span class="paren">(</span><span class="string">'&lt;div class=\"views-field views-field-facility-name factory-name\"&gt;&lt;span class=\"field-content\"&gt;&lt;a href=\".+\"&gt;'</span>, <span class="string">"峻源股份有限公司"</span>, <span class="string">'&lt;/a&gt;'</span><span class="paren">)</span>, <span class="identifier">web_content</span><span class="paren">)</span>

<span class="identifier">print</span><span class="paren">(</span><span class="identifier">target_path</span><span class="paren">)</span></code></pre>

<pre><code>## [1] "/facility/J5604458"</code></pre>

<pre class="r"><code>dns &lt;- &quot;https://thaubing.gcaa.org.tw&quot;
target_url &lt;- paste0(dns, target_path)

## 開始針對目標公司爬取資料
tmp &lt;- read_html(target_url, encoding = &quot;UTF-8&quot;)
  
web_content &lt;- tmp %&gt;% html_nodes('.views-field-corp-id')
corp_id &lt;- web_content %&gt;% html_nodes('a') %&gt;% html_text()
  
web_content &lt;- tmp %&gt;% html_nodes('.views-field-facility-name')
corp_name &lt;- web_content %&gt;% html_nodes('.field-content') %&gt;% html_text()
  
web_content &lt;- tmp %&gt;% html_nodes('.views-field-facility-address')
address &lt;- web_content %&gt;% html_nodes('.field-content') %&gt;% html_text()

web_content &lt;- tmp %&gt;% html_nodes('.views-field-industry-area-name')
industry_area &lt;- web_content %&gt;% html_nodes('.field-content') %&gt;% html_text()
  
web_content &lt;- tmp %&gt;% html_nodes('.views-field-industry-name')
industry &lt;- web_content %&gt;% html_nodes('.field-content') %&gt;% html_text()
  
web_content &lt;- tmp %&gt;% html_nodes('.views-field-poltype')
apply_type &lt;- web_content %&gt;% html_nodes('.field-content') %&gt;% html_text()
  
web_content &lt;- tmp %&gt;% html_nodes('.views-field-updatetime')
snap_date &lt;- web_content %&gt;% html_nodes('.field-content') %&gt;% html_text()

print(paste0('公司統編:', corp_id, ';公司名稱:', corp_name, ';公司地址:', address))</code></pre>
<pre><code>## [1] &quot;公司統編:27873415;公司名稱:峻源股份有限公司;公司地址:新竹縣關西鎮南新里新城１之１、１之７號&quot;</code></pre>

