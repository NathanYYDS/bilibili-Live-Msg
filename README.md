# bilibili-Live-Msg
基于python的bilibili直播间弹幕获取，注释详细，简单易懂，是个小白都能上手

需要requests包,此处用清华源
```python
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

注意！！python代码中第5、37~61行需要修改！！

1、roomID可以在直播间链接中找到
比如我的直播间链接是这个 https://live.bilibili.com/24507335 ， roomID就是24507335

2、以下是cookie获取流程
先打开直播间网页控制台开始监听网络流，发送一条弹幕，会出现一个名叫send的请求包

![image](https://github.com/NanthanYYDS/bilibili-Live-Msg/assets/49605891/b8924a09-bf7a-484c-b80e-84b76867c719)

在请求标头中我选中的部分就是cookie啦

![image](https://github.com/NanthanYYDS/bilibili-Live-Msg/assets/49605891/f0c89774-90d4-4b42-aba2-432c1484af5d)

然后用下面的形式填到代码中去就OK了
```
cookies = {
        'buvid3': '',
        'b_nut': '',
        '_uuid': '',
        'buvid4': '',
        'rpdid': "",
        'header_theme_version': '',
        'SESSDATA': '',
        'bili_jct': '',
        'DedeUserID': '',
        'DedeUserID__ckMd5': '',
        'sid': '',
        'FEED_LIVE_VERSION': '',
        'CURRENT_QUALITY': '',
        'fingerprint': '',
        'buvid_fp_plain': '',
        'bsource': '',
        'home_feed_column': '',
        'bp_t_offset_472975402': '',
        'CURRENT_FNVAL': '',
        'LIVE_BUVID': '',
        'b_lsid': '',
        'browser_resolution': '',
        'buvid_fp': '',
        '_dfcaptcha': '',
        'PVID': '',
    }
```
