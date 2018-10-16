# Small-tools

### 利用爬虫实现的翻译小工具(translation.py)
  - 对接有道翻译
  - 可以中英混输
  - 自动识别语言，如果输入中文，则翻译为英文，反之相同
  - 仅支持中英互译

### 利用爬虫实现的查询天气小工具(weather.py)
  - 仅支持查询中国国内县级及以上城市
  - 使用汉语拼音全拼查询，如北京，则需输入beijing，若有重复尝试在末尾处加上数字1重试，如qixian1
  - 支持直接点击回车查询，默认查询本地天气
  - 若输入的内容没有对应的城市，会显示本地天气
  
### 利用爬虫做的其他历法查询(calendar.py)
  - 运行会显示当前公元日期的其他历法的日期
  - 支持:中国传统历法、中国阴历、佛历、中华民国年号、日本年号等
  - [示图](http://ww1.sinaimg.cn/large/005WOYz1ly1ftpsnf48yvj30a603ht8n.jpg)

### 表盘(watch_plate.py)
![](http://ww1.sinaimg.cn/large/007fldCely1fw90pqbxc3j30bo0d5aa3.jpg)

### 随机数(random_number.py)
  - 忽略数值大小顺序
  - +-int

### request(requests_get.py)
  - 可自定义重试次数
  - 适用于爬虫
