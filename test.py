from utils import *

url = "https://t.bilibili.com/579885164093097529"  # 动态地址
Dynamic_id = GetDynamicID(url)                     # 获取动态ID
print("获取动态成功，ID为：" + Dynamic_id)
print("正在获取转发数据中......\n")
total = GetTotalRepost(Dynamic_id)                 # 获取转发数
print("转发数总数: ", total)

data = GetUsers(Dynamic_id)                        # 获取评论用户
print("抽奖用户总数：", len(data))
for elem in data:
    print(elem)

lucky_num = input("\n---请粘贴随机数种子：---\n")
lucky_num = hashlib.sha256(lucky_num.encode("utf-8")).hexdigest()  # 用lucky_num生成hash值
print("开奖号码为：", lucky_num)

lucky_num = int(lucky_num, 16)
users = sorted(data, key=lambda i: abs(int(i['hash'], 16) - lucky_num))  # 按照随机数种子，再次打乱数据

n = input("\n---请输入奖品数量(1~{})：---\n".format(len(data)))
n = int(n)
print("\n【获奖用户为：】")
for index, user in enumerate(users[0:n]):  # 取前n个用户，格式化输出
    print("[{}] uid: {} name: {} Hash({})\n评论:{}".format(index, user["uid"], user["name"], user["hash"], user["comment"]))
