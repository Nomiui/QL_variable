#### 根据变量运行自动运行对应任务
## 爬虫源码仓库 https://github.com/XgzK/TGreptile
爬虫端项目不再维护融合完成将保留此项目
本项目主要为国内没外网环境的人准备的公益项目
本项目因为一些问题暂时需要外网环境的东西
如果没有请等下次项目支持后再使用
## 特别声明

```text
版本BUG消除后会出详细使用教程，版本暂时内测中，不对外开发线报拉群服务，请稍等一段时间
因新技术不稳定暂时封群清净几天
有问题可以 https://t.me/InteIJ 群组联系
需要其他功能的可以反馈添加，或者反馈脚本BUG问题
有如果有其他获取参数的可以反馈给我添加
本项目所有活动来自TG各大频道,本项目偷免单助力介意勿用
害怕偷CK的勿用,不接受任何形式甩锅,不对任何行为负责
本脚本优先适配船长和M系列脚本,如果有其他相同脚本参数不同将以优先适配船长和M系列为准
```

### 容器构建命令
```shell
docker run -dit \
  -p 5008:5008 \
  -e TZ=Asia/Shanghai \
  --name qlva \
  --restart unless-stopped \
  xgzk/qlvariable:latest
```
```http request
http://IP:5008/ 提交青龙参数和更新程序
http://IP:5008/log 日志页面
```
需要定时任务配置文件权限
容器里面没有代码需要等待1-4分钟让程序跑起来
```text
机器人指令
群里发送 /id 机器人会返回群组ID
频道消息转发给机器人会返回 频道信息
私聊机器人发送 /forward ID 会把东西转发到这个频道或者群组 暂时只能使用一个ID
找 https://t.me/BotFather 发送 /setprivacy 选择自己使用的机器人名称
怎么申请机器人自己百度
```

### 非adm64系统的问题
```text
因为不能测试adm64外的版本不清楚其他版本是否正常
如果拉取三次容器都显示相同错误的
请手动构架
第一步 下载docker目录下的UpdateAll.sh detect.sh dockerfile
上传到Linux系统进入这三个文件的目录,如果你是arm64直接执行
docker build -t xgzk/qlvariable:latest: .
就行,然后重新执行容器构建命令
如果你不是arm64和adm64再反馈吧
```

## 更新说明

```text
版本1.1 
 > 修复不同版本数据库差异问题
 > 添加去重功能
 > BUG未知，请遇到反馈
版本1.1.1
    > 修复重复提示不清楚问题
    > 增加请求次数，由原来一次请求失败，现在可以最多请求三次，只要成功一次，就不再请求了
    > 优化活动参数重复提醒
版本1.1.2
    > 适配了特别10.2版本，把10.2之前包括10.2定义为9版本
版本1.2
    > 更新可以保留conn.yml文件
    > 对一些获取进行不去重处理
    > 建议之前版本拉取最新脚本
版本1.3
    > 添加了配置文件检测
    > 修补了缺少的文件
    > 添加了10版本以上数据库表的检测
版本2
    > 正式启用容器版本
    > 取消了复杂的配置,改用程序自动适配
    > 有了自动更新省去了更新繁琐的步骤
版本2.1
    > 添加了库优先级,可以指定所有活动脚本走特定库,当库没有才走ID前面的脚本
    > 添加禁用活动脚本
    > 添加对相同活动去重复功能,只要其他脚本执行过将不再执行
版本2.2
    > 对页面进行美化
版本3.0
    > 使用tg官方机器人监控进行监控群组
    > 因机器人不能监听机器人消息活动粗暴于爬虫端核心代码合并
    > 缺陷对多参数活动支持不精确
    > 支持使用反代域名
    > 完美与爬虫端融合
    > 修改了对比去重复的标记物问题
    > 优化了对比数据执行时间缓慢问题
    > 不需要科学环境的正在开发还不支持使用(因公益服务器被攻击暂停开发这个部分)
    > 2022-11-1 修复当前版本出现BUG问题
    > 取消了官方的额TG库改成统一长连接请求
    > 2022-11-6 添加转发消息功能正式版本即将开始发布使用
    > 频道消息转发给机器人返回频道ID 群组发送 /id 机器人发给用户频道ID
```
### 待开发记录
```text
3.0版本缓慢开发中
抛弃原来主动获取参数的方法，改用TG官方机器人进入特殊处理参数的监控群
格式 脚本名称\n活动参数
对没国外环境的将使用 websocket 方法进行广播推送
    添加黑名单脚本,不执行在黑名单的脚本
因公益服务器被攻击 websocket 不再开发
```
