import requests

# 直播间ID
#-------------------------此处需修改---------------------------#
roomID = ''
#-------------------------此处需修改---------------------------#

# 获取弹幕API
url_get='http://api.live.bilibili.com/ajax/msg?roomid='

# 发送弹幕API
url_post='https://api.live.bilibili.com/msg/send'


# 获取最新弹幕，返回最后一条弹幕信息
def get_msg():
    # 保存GET到的内容，以json格式存于res中
    res = requests.get(url_get+roomID).json()

    #从res中提取最新弹幕内容
    # res = res['data']['room'][-1]
    text = res.get('data').get('room')[-1].get('text')
    
    return text


# 发送一条弹幕，返回bool值，成功为 1，反之为 0 
def post_msg(content:str):
    # 先判一下内容是否非空
    if content == '':
        print('请指定发送弹幕内容')
        return False
        
    # 初始化cookie
    #-------------------------此处需修改---------------------------#
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
    #-------------------------此处需修改---------------------------#
    
    # 初始化data
    data = {
        'bubble': '0',
        'msg': content,
        'color': '16777215',
        'mode': '1',
        'room_type': '0',
        'jumpfrom': '77002',
        'fontsize': '25',
        'rnd': '1689571593',
        'roomid': roomID,
        'csrf': '993436a7912b537cef424b331429ff9f',
        'csrf_token': '993436a7912b537cef424b331429ff9f'
    }
    res = requests.post(url_post,cookies=cookies,data=data).text

    # 以下语句在弹幕刷新太快时可能会出点小问题，测试代码这里我就将就了
    if content == get_msg():
        print('弹幕发送成功，内容：'+content)
        return True

# 主函数

if roomID == '':
    print('Warning: 请修改roomID变量以指定直播间')
    exit()
print('1.获取弹幕\n2.发送弹幕')
cmd= input()

if cmd == '1':
    msg=''
    #不间断的运作，我这里就直接写死循环了，反正是测试代码
    while True:
        # 重复：无操作
        # 不重复：输出最新弹幕
        latest = get_msg()
        if msg != latest :
            msg = latest
            print(msg)
        else:
            pass
elif cmd=='2':
    print('请输入弹幕内容')
    post_msg(input())
