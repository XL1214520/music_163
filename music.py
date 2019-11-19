import requests,json,re
from bs4 import BeautifulSoup


# 获取歌手页的源代码
def get_html(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Refer":"http://music.163.com/",
        "Host":"music.163.com"
    }
    try:
        response = requests.get(url,headers=headers)
        html = response.text
        return html
    except:
        print("request error")
        pass

# 解析歌手页的源代码，获取所有歌词和歌名
def get_singer_info(html):
    soup = BeautifulSoup(html,"lxml")
    links = soup.find("ul",class_='f-hide').find_all("a")
    song_IDs = []
    song_names = []
    for link in links:
        # 获取每一首歌的歌词页面
        song_ID = link.get("href").split("=")[-1]
        # 获取歌曲名称
        song_name = link.get_text()
        song_IDs.append(song_ID)
        song_names.append(song_name)
    return zip(song_names,song_IDs)

def get_lyric(song_id):
    url = 'http://music.163.com/api/song/lyric?'+'id='+str(song_id)+"&lv=1&kv=1&tv=1"
    html = get_html(url)
    json_obj = json.loads(html)
    # 将获取的歌词分为 时间段 和 歌词
    initial_lyric = json_obj['lrc']["lyric"]

    # 用正则表达式，去掉不需要的部分 时间段
    regex = re.compile(r'\[.*\]')
    # 去掉首尾的 空格
    final_lyric = re.sub(regex,'',initial_lyric).strip()
    return final_lyric

def write_text(song_name,lyric):
    print('G:/text/正在写入歌曲：{}'.format(song_name))
    with open("{}.text".format(song_name),'a',encoding='utf-8')as f:
        f.write(lyric)

def main():
    singer_id = input('请输入歌手ID：')
    start_url = "http://music.163.com/artist?id={}".format(singer_id)
    html = get_html(start_url)
    singer_infos = get_singer_info(html)
    for singer_info in singer_infos:
        lyric = get_lyric(singer_info[1])
        # 将歌名，和歌词
        write_text(singer_info[0],lyric)

if __name__ == '__main__':
    main()
