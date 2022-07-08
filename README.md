# 根据变量运行对应任务

本脚本存在风险，使用此脚本默认接受下列风险

```text
1. 此脚本可能会导致您的账户被盗，请谨慎使用，在conn.yml中需要配置你的青龙IP:port + Client ID + Client Secret,如果我在脚本添加可以发送这些内容的信息，那么偷盗你们的ck什么都将不是问题
2. 只要我在获取数据那个网址添加我想运行的青龙脚本，那么只要是使用这个脚本的用户使用的青龙上有脚本与之匹配，那么就会运行这个脚本
3. 可能会添加一些对我个人有益的变量让你们跑，而你们没有收益，所以请谨慎使用
4. 可能还有其他的风险，请自行考虑
5. 使用此脚本产生的任何后果将与本人无关，请承担考虑
6. 变量来自 https://t.me/KingRan521 频道 京东脚本仓库地址 https://github.com/KingRan/KR，应该有人用过这个仓库，我看反馈有如下
    A: 发现东东萌宠提现到非本人账号
    B: 领现金被其他人提了
    C: 锦鲤每天都被用掉了，非本人使用
    D: 赚京豆脚本偷助力
    E: 被偷CK
    F: 等等问题
不放心变量或者脚本的可以不使用，暂时用的库只有KR
7. 如果后期所有东西丢失或者其他问题请勿找本人负责
```

<details>
  <summary>废话内容</summary>
  <pre><code> 
> 变量来自 https://t.me/KingRan521 频道 京东脚本仓库地址 https://github.com/KingRan/KR
> 如果用过之前写的青龙代理脚本的，应该没有发生过脚本偷你们东西的情况吧
> 不过使用此脚本有可能真的会帮我助力一些任务，或者可能发起组队任务，不过和本人有关的不会损害你们京东利益问题，或者无关紧要的东西，不会让你们运行推一推和挖宝助力这种分你们肉吃的脚本，不过我懒的搞，这个github号虽然只是存放一些垃圾脚本的，不过我也不会想看到有人反馈本人偷你们ck之类的反馈
> 写此脚本只是因为我需要用这个和青龙代理那个不同，
> 后端获取TG值放在了docker容器上了，懒得研究京东这一套，可能一直不会有你们被白嫖的一天
> 因为TG机器人没办法向普通用户一样关注频道只能我专门写个获取TG网页版的爬虫，很多是国内服务器就是给你们大部分也不能爬TG，等那个脚本写的差不多完善了，会开源出来给你们，很多只有在自己手里才完全安全，我这样艰信
> CK我去年被偷了，但是使用了抓CK的APP和KR的加密脚本，并不知道是什么原因导致被偷，所以我非常理解自己白嫖京东被别人白嫖的感受
> 日志里面添加了运行的脚本和日志，你们可以在东西丢失后对比日志，就是我也不能跳过日志偷你们东西
> 脚本只有get请求和put请求，不懂的可以百度这两个请求作用
  </code></pre>
</details>

### 运行脚本

#### 安装需要的库

```text
pip3 install -r requirements.txt
```

#### 启动脚本

如果运行没有问题就执行下面的命令

```pycon
python3 main.py
```

#### 添加守护进程

如果你想要守护进程，可以执行下面的命令

```pycon
python3 ql_cs.py
```

### conn.yml配置详情

```txt
第2行 登录青龙面板-->系统设置-->应用设置-->新建应用，选择定时任务的权限就行，复制Client ID
第3行 登录青龙面板-->系统设置-->应用设置-->新建应用，选择定时任务的权限就行，复制Client Secret
第5行不用管1，但是不能删这一行或者移动
第7行 换成自己的青龙面板的域名:端口
第9行 是我搭建获取TG中KR信息的网址，九月会域名到期，可能不定期更换
第11行 是青龙任务列表，你们可以去地址查看你们青龙的脚本
第13行 是青龙配置文件的路径 默认/root/ql/config/config.sh
第15行 不修改，此行不能移动或者更改，否则会删除错误你们青龙配置文件
第17行 日志输出路径
```

## 活动相关

```text
活动抓取的是KR的频道，如果有其他地方也有活动参数和链接也可以反馈我添加进去
活动链接类似如下
    > ## CJ组队瓜分-jd_cjzdgf.js
    > export jd_cjhy_activityId="bede6cabc9e74240998d25baf0a6fc10"
    > https://cjhy-isv.isvjcloud.com/wxDrawActivity/activity/367921?activityId=420206514a03469490639d99c206a73f
```

## 关于参数和获取参数网址

参数网址

```text
http://xr.xgz.buzz:5000 测试页面，确定网址是否正常运行
http://xr.xgz.buzz:5000/qlcs TG上一些活动参数
http://xr.xgz.buzz:5000/qljs 里面脚本名称
http://xr.xgz.buzz:5000/qlurl 一些参数
http://xr.xgz.buzz:5000/qlrz 脚本运行的日志很乱
```