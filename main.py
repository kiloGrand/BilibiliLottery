from utils import *

if __name__ == "__main__":
    Dynamic_id = str(GetDynamicID())
    print("获取动态成功，ID为：" + Dynamic_id)
    print("正在获取转发数据中......\n")
    users = GetUsers(Dynamic_id)

    for index, user in enumerate(users):
        print("[{}] {}({}) Hash({})\n评论:{}".format(index, user["uid"], user["name"], user["hash"], user["comment"]))

    lucky_num = input("\n---请粘贴随机数种子：---\n")
    lucky_num = hashlib.sha256(lucky_num.encode("utf-8")).hexdigest()

    print("\n【开奖号码为：{}】".format(lucky_num))
    n = input("\n---请输入奖品数量(1~{})：---\n".format(len(users)))

    lucky_num = int(lucky_num, 16)
    users = sorted(users, key=lambda i: abs(int(i['hash'], 16) - lucky_num))
    # 按照随机数种子，再次打乱数据

    print("\n【获奖用户为：】")
    for i in range(int(n)):
        print(users[i])
        print("\n")
