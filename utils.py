import urllib.request
import json
import re
import urllib.request
import hashlib


def GetDynamicID(s=None):  # 获取动态ID
    if s is None:
        s = input("---请粘贴Bilibili动态的网址：---\n（形如 https://t.bilibili.com/xxxxxxx）\n")
    nums = re.findall(r'\d+', s)  # 正则表达式： \d指代数字0-9 +匹配前面字符1次及以上，字符串前加r表示忽略转义字符
    return nums[0]  # 列表中的第一个字符串


def GetTotalRepost(Dynamic_id):  # 获取评论总数
    global UP_UID
    DynamicAPI = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?dynamic_id=" + Dynamic_id
    try:
        response = urllib.request.urlopen(DynamicAPI)  # 使用GET方式对DynamicAPI发起请求
        BiliJson = json.loads(response.read())  # 使用read获取网页内容，将json格式数据转换为字典
        Total_count = BiliJson['data']['card']['desc']['repost']  # view观看数 repose转发数 comment评论数 is_liked三连数
        UP_UID = BiliJson['data']['card']['desc']['user_profile']['info']['uid']
    except:
        print("GetTotalRepost ERROR!!!")
        Total_count = None
    return Total_count


def GetMiddleStr(content, startStr, endStr):  # 获取这一页的评论信息
    startIndex = content.index(startStr)  # index：如果包含子字符串返回开始的索引值，否则抛出异常。
    if startIndex >= 0:
        startIndex += len(startStr)
    endIndex = content.index(endStr)
    return content[startIndex:endIndex]  # 切片


def GetUsers(Dynamic_id):  # 获取评论用户的数据 ['uid', 'name', 'hash', 'comment']
    total = GetTotalRepost(Dynamic_id)  # 获取评论总数
    if total is None:
        exit(0)
    DynamicAPI = "https://api.live.bilibili.com/dynamic_repost/v1/dynamic_repost/view_repost?dynamic_id=" + Dynamic_id + "&offset="
    index = 0
    users = []
    while index < total:
        Tmp_DynamicAPI = DynamicAPI + str(index)  # 评论区第i页API，一页20个评论，offset：偏移量，maybe每次读取20个评论
        try:
            BiliJson = json.loads(
                GetMiddleStr(urllib.request.urlopen(Tmp_DynamicAPI).read(),
                             b"comments\":", b",\"total")  # 字符串前加b代表该它是bytes类型
            )

            for BiliJson_dict in BiliJson:
                Bilibili_UID = str(BiliJson_dict['uid'])
                Bilibili_Uname = BiliJson_dict['uname']
                Bilibili_Comment = BiliJson_dict['comment']
                Bilibili_Hash = hashlib.sha256(Bilibili_UID.encode("utf-8")).hexdigest()  # 根据uid生成hash，同一个uid的hash一样

                user = {"uid": Bilibili_UID, "name": Bilibili_Uname, "hash": Bilibili_Hash, "comment": Bilibili_Comment}
                users.append(user)
        except:
            break

        index += 20

    users = sorted(users, key=lambda i: int(i['hash'], 16))  # 按照hash值16进制大小，升序排序
    # lambda i: int(i['hash'], 16)：将将字符串i['hash']转化成16进制
    # 相当于使用哈希映射打乱数据
    return users


def binarySearch(arr, l, r, x):  # 二分查找，arr: 数组，l: 左边界下标，r: 右边界下标，x: 目标值
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return l
