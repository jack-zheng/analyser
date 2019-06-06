# Issue Track

1. 使用 moment js 的时候，不能显示， 查看页面元素时间标签显示： style: display:none
    * 使用 jinjia {% blick script %} 引入 moment 和 jQuery
1. base.html 中加入一些 block 不起做用，比如 footer 和 flash。再继承了base 的页面上都不起作用，但是再单独的页面上却可以正常工作，比如到login.html里面
    * 导致以上问题的原因是对flask-bootstrap的机制不熟悉，在bootstrap的base.html中并没有预留出来footer block，如果要使用的话就需要每个子模版中分别添加或者用super()语法，不是很方便，最后我决定参照书上的做法结合bootstrap的例子，自建了一个base.html
1. 在使用了Flask-WTF扩展之后，如果你要用Ajax来发送post请求，需要在Ajax中添加CSRF token或者创建form页面元素并将之序列化传到Ajax中,当然form中需要到CSRF token.
1. 有什么比较优雅的在子模块中取配置的方式，类似取默认分页数什么的
    * 最后直接用 os.getenv 啦
1. 网站上线后，自定义的js没有加载，真是扯淡, 应该是由于docker 的 nginx config 导致的, 但是按照docker提供者的信息来看，应该都是默认就设置好了才对，擦
    * 应该是权限问题，[favicon](http://10.129.126.245:4000/static/favicon.ico)这个不能访问，原权限是 600 但是改了权限到 644 后就可以了。MAC上面倒是没什么问题，真是日狗了。不过mac和linux上docker image 的版本也不一样
    * linux: 4.4.0-109-generic; mac: 4.9.125-linuxkit; windows: 4.9.125-linuxkit
    * on windows when build image all file and directory got permission '-rwxr-xr-x'
    * resolve this issue by manually run command 'chmod 655 -R static templates', add it to Dockerfile as tmp workaround. but this still not make sense, let's test it on other linux machine to see if it's an environment issue.

permission of MAC:  
drwxr-xr-x 5 root root   4096 Jun  3 11:42 static  
drwxr-xr-x 8 root root   4096 Jun  4 11:39 templates

permission of server:  
drwx------+  5 root root   4096 Jun  4 11:29 static  
drwx------+  8 root root   4096 Jun  4 11:29 templates

permission of Windows:  
drwxr-xr-x 5 root root   4096 Jun  3 12:44 static  
drwxr-xr-x 8 root root   4096 Jun  5 14:59 templates

``` bash
PS C:\Users\Jack\gitStore\analyser> docker version
Client: Docker Engine - Community
 Version:           18.09.2
 API version:       1.39
 Go version:        go1.10.8
 Git commit:        6247962
 Built:             Sun Feb 10 04:12:31 2019
 OS/Arch:           windows/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          18.09.2
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.6
  Git commit:       6247962
  Built:            Sun Feb 10 04:13:06 2019
  OS/Arch:          linux/amd64
  Experimental:     false
```
