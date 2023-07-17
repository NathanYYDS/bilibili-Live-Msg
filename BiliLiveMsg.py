import requests

# 直播间ID
roomID = '22884968'

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


# 发送一条弹幕
def post_msg(content:str):
    # 先判一下内容是否非空
    if content == '':
        print('请指定发送弹幕内容')
        return False
    # 初始化cookie
    cookies = {
        'buvid3': 'D2B57090-1F01-F8CB-8BCE-435D21361B3820473infoc',
        'b_nut': '1689299220',
        '_uuid': 'EB10764D6-C46F-451B-15110-610376C38C6F120682infoc',
        'buvid4': '6172BA89-0611-05D6-0DF5-C01130BF306921236-023071409-FpRurigT5QQ9c7yecMklWA%3D%3D',
        'rpdid': "|(J|YkJmm|JY0J'uY)mkmmkkR",
        'header_theme_version': 'CLOSE',
        'SESSDATA': '7f671553%2C1704855077%2C61f5b%2A72ckmwNfqzsRCOevRKzJyjh3xVJ9siUs1NW7gSG5R_K3_E_hDE8LyuuOucrANVn2bjXv3PcgAAAgA',
        'bili_jct': '993436a7912b537cef424b331429ff9f',
        'DedeUserID': '472975402',
        'DedeUserID__ckMd5': '54709fd6c6cd4162',
        'sid': '54srw0e6',
        'FEED_LIVE_VERSION': 'V_LIVE_2',
        'CURRENT_QUALITY': '80',
        'fingerprint': '5c5915367ce67775efa9a9e2ac0bfd85',
        'buvid_fp_plain': 'undefined',
        'bsource': 'search_baidu',
        'home_feed_column': '5',
        'bp_t_offset_472975402': '818897366815866979',
        'CURRENT_FNVAL': '4048',
        'LIVE_BUVID': 'AUTO8916895366686212',
        'b_lsid': 'C3FF8EDD_18962433F58',
        'browser_resolution': '1707-809',
        'buvid_fp': 'f56061f596cce5dc9f7ae2105acf280c',
        '_dfcaptcha': 'ca51c788bd5c8fcef34e2208f6fa3d78',
        'PVID': '25',
    }
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
