import requests
import re

a = requests.get(url="https://movie.douban.com/chart",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"})
print("结果",a.text)


print(re.findall(r'<a.*?"nbg".*?title="(.*?)">',a.text))