# 一、什么是CSS
CSS(Cascading Style Sheets)层叠样式表，是一种用来表现HTML或XML等文件样式的计算机语言。

CSS是用来美化网页用的，设有网页则CSS毫无用处，所以CSS需要依赖HTML展示其功能。

HTML也可以设置一些元素的样式，但不够简洁，能设置的细节也不够丰富。CSS可以很好地解决这些问题。



# 二、CSS的基本语法
- 格式
	CSS样式由选择器和一条或多条以**分号**隔开的样式声明组成。每条声明的样式包含着一个CSS
	属性和属性值。
	选择器名 {
			属性：属性值；
			……
			}
	![[Pasted image 20221112150914.png]]
	**注意**
	1.css声明要以分号结尾，声明要用{}括起来
	2.建议一行写一个声明
	3.如果属性值由多个单词红成，要给值加上引号


- 注释
	`/*注释内容*/`


# 三、CSS的基本使用
1.行内式
	行内样式将样式定义在具体html元素的style属性中。
	以行内式写的CSS耦合度高，只适用于当前元素，在设定某个元素的样式时比较常用。
	`<p style="color:red;font-size:50px;">这是一段文本</p>`


2.嵌入式
	嵌入式通过在html页面内容开辟一段属于css的代码区域，通常做法为在`<head>`标签中嵌套`<style>`标签，在`<style>`中通过**选择器**的方式调用指定的元素并设置相关CSS.
	`<style type="text/css">p {color:blue;font-size:40px;}</style>`


3.引入外联样式文件
	通过link标签引入外部的css文件
	在实际开发当中，很多时候都使用引入外联样式文件，这种形式可以使html页面更加清晰，而且可以达到更好的重用效果。
	`<link rel="stylesheet"type="text/css"href="css/style.css"/>`
		rel :     当前文件与引入的文件之间的关系
		type :  类型，css类型
		href :  引入的资源的路径

**CSS的优先级：就近原则**


# 四、CSS选择器

1. 通用选择器
	选择所有元素——只要在页面中都被选中
	```
	*{
		属性名：属性值
	}
	```

2. 元素选择器
	选择指定元素(标签)
	```
	标签名{
		属性名：属性值
	}
	```

3. ID选择器
	选译指定id属性值的元素#
	```
	#id属性值{
	属性名：属性值
	}
	```
	**注意**
	- id值最好保持唯一
	- id定义规则：以字母、数字、下划线、中划线组成，不要以数字开头

4. class类选择器
	选译设置指定class属性值的元素
	```
	.class属性值{
		属性名：属性值
	}
	```


5. 分组选择器
	选择指定选择器选中的元点
	```
	选择器1，选择器2，选择器3,..{
		属性名：属性值
		}
	```


- 选择器的优先级：(权重值)
	id选择器(100) > 类选择器(10) > 元素选择器 (1) > 通用选择器
	行内样式style属性——权重是188C




# 五、CSS常用属性

- 背景
	-   background-color  背景颜色
	-   background-image  背景图片
	-   background-repeat   设置背景图像是否及如何重复。
		no-repeat:表示不重复；repeat-x:横向重复；repeat-y:纵向重复；repeat:横向横向重复
	-   background-attachment 背景图像是否固定或者随着页面的其余部分滚动。
	-   background-position  设置背景图像的起始位置。
	eg. 
	```
	body{
		background-image:url('paper.gif');
		}
	```

- 文本
	- color	设置文本颜色
	- direction	设置文本方向。
	- letter-spacing	设置字符间距
	- line-height	设置行高
	- text-align	对齐元素中的文本
	- text-decoration	向文本添加修饰
	- text-indent	缩进元素中文本的首行
	- text-shadow	设置文本阴影
	- text-transform	控制元素中的字母
	- unicode-bidi	    设置或返回文本是否被重写 
	- vertical-align	    设置元素的垂直对齐
	- white-space	     设置元素中空白的处理方式
	- word-spacing	设置字间距

- 字体
	- font	在一个声明中设置所有的字体属性
	- font-family	指定文本的字体系列
	- font-size	指定文本的字体大小
	- font-style	指定文本的字体样式
	- font-variant	以小型大写字体或者正常字体显示文本。
	- font-weight	指定字体的粗细。

- 伪类
	伪类用于定义元素的特殊状态。
	例如，它可以用于：
	-   设置鼠标悬停在元素上时的样式
	-   为已访问和未访问链接设置不同的样式
	-   设置元素获得焦点时的样式。
	如：
	-   a:link - 正常，未访问过的链接
	-   a:visited - 用户已访问过的链接
	-   a:hover - 当用户鼠标放在链接上时
	-   a:active - 链接被点击的那一刻



- CSS的盒模型 
	![[Pasted image 20221113014911.png]]
	- 蓝框——内容
	- 绿框——内边距
	- 黄框——边框
	- 橙框——外边距
	eg. `div { width: 300px; border: 25px solid green; padding: 25px; margin: 25px; }`
	

-   定位 
	position
	eg: `h2 { position:absolute; left:100px; top:150px; }`
	- 属性
		- absolute	生成绝对定位的元素， "left", "top", "right" ，"bottom" 。
		- fixed	    生成固定定位的元素，相对于浏览器窗口进行定位。 "left", "top", "right"， "bottom" 。
		- relative	生成相对定位的元素，相对于其正常位置进行定位。因此，"left:20" 会向元素的 LEFT 位置添加 20 像素。
		- static	默认值。没有定位，元素出现在正常的流中（忽略 top, bottom, left, right 或者 z-index 声明）。
		- sticky	粘性定位，该定位基于用户滚动的位置。它的行为就像 position:relative; 而当页面滚动超出目标区域时，它的表现就像 position:fixed;，它会固定在目标位置。


-   布局
	一般分为：**头部区域、菜单导航区域、内容区域、底部区域**
	常用边框来区隔各区域


- display
	规定元素生成框的类型
	- 属性
		- block  元素会被显示,且元素会变成块级元奏，元素前后会有换行符
		- none   元素会被隐藏
		- inline   元素会显示为行内元素，元素前后没有换行符
		- inline-block       行内块级元素

