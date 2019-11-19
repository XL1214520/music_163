# music_163
爬取网易云所有的歌词

该程序流程

一：输入歌手的ID


二、解析歌手页的源代码，获取所有的歌曲和歌词

使用zip返回歌曲、歌词


三、循环 zip 返回来的歌曲、歌词


四、获取的歌词使用json.loads()转换成json格式

  将时间段[00:00] 和 歌词 分开 
  
  json['lrc']['lyric']
  
  使用正则表达式去掉时间段 r'\[.*\]' 和首尾的空格
  
  
五、写入text

with open("{}.text".format(song_name),'a',encoding='utf-8') as f:

  f.write()
