## BilibiliLottery

使用哈希映射实现的抽奖方法，dist里面有Windows下的预编译程序，可以直接使用。

## 修改内容
添加的注释和一个测试文件，微改了一些源代码
代码思路：
1. 爬取动态的评论区中已转发和评论的用户
2. 根据用户的uid生成hash值
3. 再根据hash值排序
4. 获取输入的随机种子数，根据种子数生成一个hash值
5. 用户的hash减去种子的hash，再取绝对值，把绝对值转成16进制，根据这个值升序排序
6. 更加用户输入的奖品数n，输出前n个用户的信息

## 注意
main.exe的使用，要在命令行里打开，要不然看不到最后的结果  
先在命令行去到dist的文件夹下，然后./main.exe

## 修复的bug
- 可能出现抽到一个用户多次，解决的方法在test.py

## hash
- 哈希算法不可逆，即不能从输出得到输入
- 对于用一个输入，哈希算法得到同一个输出
- 哈希算法常用于保存密码，即网页服务器保存密码的hash值，防止密码泄露。