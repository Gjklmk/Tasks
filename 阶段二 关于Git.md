
# 一、Git是什么？

Git是一个分散式版本控制软件。

参考：
[Git教程 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/896043488029600)
[猴子都能懂的GIT入门 | 贝格乐（Backlog）](https://backlog.com/git-tutorial/cn/)


# 二、Git可以做什么

1. 自动记录每次文件的改动
2. 多人协作编辑
3. 将本地的文件推送到远程


# 二、Git怎么用？
刚开始官网下载Git应用并打开之后我还挺懵的，Git打开跟电脑系统的命令行窗口一样，跟我熟知的软件很不同。我还一度怀疑是不是下错了。
后来我才知道Git本身就是一款命令行工具，其本身的操作就是用命令行完成的。

发现了一个很有意思的Git教程网站：[Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN) 是以游戏的形式来教授Git原理的。

在学习Git的过程中，遇到了很多问题。真正意义上的零基础教程很少，很多教程教完初始步骤之后用词便开始专业了起来，我也就开始懵了。还有一些教程只给了一些步骤，但是不说某个步骤的意义是什么，某个命令是什么意思。导致我某些步骤要是没弄对的话就进行不下去。在操作中也遇到了很多小问题，比如：输入git init后默认存放在c盘中，如何改变库的根目录？

通过Google和[这个视频](https://www.bilibili.com/video/BV1Cr4y1J7iQ?vd_source=89a17076aba9767938ed80fb80f82e45)我的问题基本得到了解决。以下是一些过程及现阶段得到的答案。


## 基本操作

1. 初始设置
  安装好Git后打开Git Bash，用以下命令配置用户名与邮箱。
- 配置用户名
```
$ git config --global user.name "Your Name"
```
- 配置邮箱
```
$ git config --global user.email "email@example.com"
```

2. 新建库
（在任意位置建立库的方法）
- 在想要新建库的任意位置右键，选择Git Bash here
	在这里遇到个问题，点了之后打不开。我推测是之前已经新建了一个，所以不能再新建了。为此产生了一个疑问：Git只能建立一个库吗？Google后未果，于是尝试删除原来建的库，后再操作一次。然而还是不行，实在没办法了就卸载重装了。搜索得是注册表的问题（[GitBash: 右键添加 Git Bash Here 菜单 - osc_lv07cfd1的个人空间 - OSCHINA - 中文开源技术交流社区](https://my.oschina.net/u/4410888/blog/3798576)）。
	- 删除库：删除.git文件即可（注意.git是隐藏文件，如果在对应目录找不到这个文件，那么需要点查看 然后显示隐藏文件。也可用工具everything进行搜索。）
- 输入命令
git clone 写GitHub上的地址—— 在GitHub上下载源码 
	这里克隆不成功就多换用几次网址（注意用SSh的网址）
git init —— 建立本地库



## 提交文件
添加文件
```
$ git add .加文件名称
```
加 . 表示当前文件夹

提交
```
$ git commit -m "在此写备注"
```

查看提交的历史记录
```
$ git log
```



## 远程推送

如果地址格式为SSH，那么需要以下操作：[远程仓库 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/896043488029600/896954117292416)
		其中遇到两个问题：
		1. 用户主目录在哪？   一般默认在**C:\Users\用户名**
		2. .SSH文件中只有`id_rsa`而没有`id_rsa.pub` —— 文件中找不到，但命令行里有，用everything也可以搜得到。最后我的解决方式就是用everything直接搜索打开。后来我找了一下，我发现文件中的`id_rsa`其实就是`id_rsa.pub` ，只不过隐藏了 文件扩展名。这里直接双击是打不开的，要用记事本。

比较详细通俗的步骤：[配置github 配置git 使用git - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/48209762)

完成了上述步骤，在后续步骤中我遇到了无数的问题，是真的搞不下去了。




完成了这些之后，我才知道图形化客户端是什么









##  Git常用命令汇总

- 配置用户名
```
$ git config --global user.name "Your Name"
```
- 配置邮箱
```
$ git config --global user.email "email@example.com"
```
以上两步要在初始时完成设置















