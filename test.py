from utils import *
import pandas as pd

# pycharm控制台输出显示pandas设置
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

url = "https://t.bilibili.com/579885164093097529"  # 动态地址
Dynamic_id = GetDynamicID(url)                     # 获取动态ID
print("获取动态成功，ID为：", Dynamic_id)

print("正在获取转发数据中......\n")
total = GetTotalRepost(Dynamic_id)                 # 获取转发数
print("转发数总数: ", total)

print("正在获取评论中......\n")
data = GetUsers(Dynamic_id)                        # 获取评论用户
print("获取到的评论总数：", len(data))

lucky_num = input("\n---请粘贴随机数种子：---\n")
lucky_num = hashlib.sha256(lucky_num.encode("utf-8")).hexdigest()  # 用lucky_num生成hash值
print("开奖号码为：", lucky_num)

lucky_num = int(lucky_num, 16)
users = sorted(data, key=lambda i: abs(int(i['hash'], 16) - lucky_num))  # 按照随机数种子，再次打乱数据

# 发现会出现同一个用户评论多次，会出现再users，所以要去除重复出现的uid
users = pd.DataFrame(users)
users.drop_duplicates(subset=['uid'], inplace=True, keep='last')  # 去除重复出现的uid，保留最后一个出现的

n = input("\n---请输入奖品数量(1~{})：---\n".format(len(data)))
n = int(n)
if n < 1:
    n = 1
print("\n【抽奖用户总数：】", users.shape[0])
print(users)

print("\n【获奖用户为：】")
print(users[0:n])
users[0:n].to_csv("lucky_peoples.csv", encoding='gbk')
