# glados自动签到

环境变量：`GLADOS_COOKIE`（必要） 和 `PUSHPLUS_TOKEN`（非必要）

如果使用多个账号，则多个`GLADOS_COOKIE`需使用 '&' 隔开
  示例：cookie&cookie&cookie

 `PUSHPLUS_Token`则是用于推送签到信息


# 食用方法 （基于github_actions）
## 1.点亮右上角的星星 **star** 激活本项目 

很显然，这是我在骗star

## 2.点击右上角 **fork** 按钮 

将本项目fork至自己的仓库，如果没有别的需求，可以直接默认选项，直接fork即可
 
## 3.在自己仓库中打开此项目

fork后在自己的仓库中打开此项目
  
## 4.配置环境变量

点击自己上面一栏中的Settings进入设置，再选择左边中二级选项Actions

<img width="244" alt="image" src="https://github.com/Alter-Liu/glados_auto/assets/91472748/b6d64c40-aeb1-40ee-a468-3d67e695f7b3">

再点击绿色按钮新建环境变量，名字如图：

<img width="513" alt="image" src="https://github.com/Alter-Liu/glados_auto/assets/91472748/afad468b-d1a0-4581-90a5-a0def29a2906">

#### 第一个参数获取于glodas的官网，按F12检查代码，点击网络，此时点击官网的签到按钮，即会向服务器发送一个cookie，此时我们的浏览器可以在报头中截获该cookie，使用该cookie即可实现免登陆签到（PS：cookie位于checkin—>标头—>cookie）

#### 第二个参数需要自己从Pushplus获取（非必须）

点击<https://www.pushplus.plus/>申请一个秘钥,放到环境变量里就可以了

<img width="228" alt="image" src="https://github.com/Alter-Liu/glados_auto/assets/91472748/596c0e72-35e4-4eea-927a-4d4d2a056fb7">



## 5.然后点击 Actions 标签查看运行的详细状况
 
Tips:不要修改系统变量的名字，如果你会自行修改工作流文件就当我放屁
