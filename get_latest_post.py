import feedparser

blog_rss_url = "https://takeknowledge.tistory.com/rss"
rss_feed = feedparser.parse(blog_rss_url)

latest_blog_post_list = ""

MAX_POST_NUM = 5

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=Take%20Knowledge&fontSize=90&fontAlign=50)
<div align="center">

---

<h3 align="center"> 주로 개발을 하고 가끔 글을 쓰며 어쩌다 랩을 합니다 </h3>

---

<p align="center">
  <a href="https://takeknowledge.tistory.com/">
      <img src="https://img.shields.io/badge/tistory-000000?style=flat-square&logo=tistory&logoColor=white"/>
  </a>
  <a href="https://www.melon.com/artist/timeline.htm?artistId=3233569">
      <img alt="Melon" src="https://img.shields.io/badge/-Melon-00CD3C" />
  </a> 
    <a href="https://www.melon.com/artist/timeline.htm?artistId=3233569">
      <img alt="Brunch" src="https://img.shields.io/badge/-Brunch-1E191A" />
  </a> 
  <a href="https://www.instagram.com/takeknowledge/">
      <img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white"/>
  </a>
</p>

  
[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=nomelancholy)](https://solved.ac/nomelancholy)
</div>

---

### 🚀 Latest Posting

---

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
