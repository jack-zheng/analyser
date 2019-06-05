# Issue Track

1. 使用 moment js 的时候，不能显示， 查看页面元素时间标签显示： style: display:none
    * 使用 jinjia {% blick script %} 引入 moment 和 jQuery
1. base.html 中加入一些 block 不起做用，比如 footer 和 flash。再继承了base 的页面上都不起作用，但是再单独的页面上却可以正常工作，比如到login.html里面
    * 导致以上问题的原因是对flask-bootstrap的机制不熟悉，在bootstrap的base.html中并没有预留出来footer block，如果要使用的话就需要每个子模版中分别添加或者用super()语法，不是很方便，最后我决定参照书上的做法结合bootstrap的例子，自建了一个base.html
1. 在使用了Flask-WTF扩展之后，如果你要用Ajax来发送post请求，需要在Ajax中添加CSRF token或者创建form页面元素并将之序列化传到Ajax中,当然form中需要到CSRF token.
1. 有什么比较优雅的在子模块中取配置的方式，类似取默认分页数什么的
    * 最后直接用 os.getenv 啦
1. 网站上线后，自定义的js没有加载，真是扯淡, 应该是由于docker 的 nginx config 导致的, 但是按照docker提供者的信息来看，应该都是默认就设置好了才对，擦