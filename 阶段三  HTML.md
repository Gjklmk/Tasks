
# 一、什么是HTML
用来描述网页的一种超文本标记语言。

第一次接触HTML使用下来感觉跟Markdown语法很像。
![[Pasted image 20221110105119.png]]
HTML是一种标记语言，我的理解是它与Markdown只是使用的标签不同。比如在Markdown中用#加空格将一段文字标记为一级标题，而在HTML中这是由`<h1></h1>`来标记的。

- XHTML与HTML 
	XHTML 是**更严谨更纯净**的 HTML 版本。




# 二、基础语法
1. 标签
	HTML标记是由"<"和">"所括住的指令标记，用于向浏览器发送标记指令。
	
	单标签
		无属性<标签名/>
		有属性<标签名 属性名=“属性值”/>   注意标签的属性之间要以空格隔开
	双标签
		无属性<标签名></标签名>
		有属性<标签名 属性名=“属性值“></标签名>

2. 整体结构
	-   `<html> 与 </html>` 之间的文本描述网页
	-   `<head></head>` 头部信息
	-   `<body> 与 </body>` 之间的文本是可见的页面内容
	-   `<doctype.html>`html5的版本声明，要在第一行
	每一个网页都要包含以上基本结构，之间可以加入一些其他的标签
	如：
```
//以下是网页区域
<doctype.html> //版本声明
<html>
	<head>
		//头部区域，不会在浏览器中被看到
		<meta charset="utf-8">  //编码格式
		<title></title>          //页面标题
		<link rel="stylesheet"href="l入的css文件的路径"/>  //引入CSS
		<script src="l入的js文件的路径"type="text/javascript"charset:="utf-8"></script> 
			//引入JS
	</head>
	<body>
		//内容区域，浏览器中的可见内容
		hello world
	</body>
</html>
```
以上结构一般编辑器都会自动生成，如在VScode中，在英文输入下输入！再按tab键便可以自动生成一个HTML结构。


# 三、常用的HTML标签
1. 结构标签
-   `<html> 与 </html>` 之间的文本描述网页
- `<head></head>` 头部信息
-   `<body> 与 </body>` 之间的文本是可见的页面内容
	属性：eg. `<body bgcolor="pink" text="blue">`——背景粉色字体蓝色
	bgcolor   背景颜色    颜色名
	text           字体颜色   颜色名
-   `<doctype.html>`版本声明

2. 文本标签
- 注释
	`<!--这是一个注释，注释在浏览器中不会显示-->`
- 标题
	`<h1></h1>~<h6></h6>` 依次从大到小
- 水平线标签
	`<hr>`
	属性：eg.`<hr width="50%" align="left" size="5"/>`
	width  宽度          1.百分比    2.px
	align   对齐方式   left right center（默认）
	size     水平线粗细
- 段落
	`<p></p>` 段落会自动换行
- 换行
	`<br>或<br/>`
- 列表
	无序
		```<ul>
			<li></li>
			<li></li>
		</ul>```
	有序
		```<ol>  
			<li></li>  
			<li></li>  
		</ol>```
- 图片
	`<img>`
		`<img src="_url_" alt="_some_text_">`
		src——源属性。src 指 "source"。源属性的值是图像的 URL 地址。URL 指存储图像的位置。



3. 块级标签
- `<div></div>`
	层，块级元素，标签会自动换行。用于布局。可以把文档分割为独立的、不同的部分。
	属性：
	align    div中内容的对齐方式
- `<span>`标签
	块，行内元素，标签不会自动换行




4. `<a>`
	定义超链接，用于从一张页面链接到另一张页面。
	- 属性
		href属性，它指示要链接的目标位置，同时没有href属性a标签内的内容与普通文本没有区别，也就失去了超链接的功能。
		`<a href-"http:/www.baidu.com">百度</a>`



5. `<input>`
	用于搜集用户信息。
	根据不同的type属性值，输入字段拥有很多种形式。输入字段可以是文本字段、复选框、单选按钮、按钮等等。
	- 属性
		type ——	button color submit——type 属性规定要显示的 `<input>` 元素的类型。


5. `<button>`
	`<button>按钮</button>`
	- 属性
		disabled——disabled——禁用该按钮。
		type——button、submit（默认）、reset——规定按钮的类型。
		value——text——规定按钮的初始值。
		name——button_name——规定按钮的名称。
	- 好处
		双标签，标签之间可以添加内容（文本或标签等）


- `<style> `
	定义 HTML 文档的样式信息。在 `<style>` 元素中，您可以规定在浏览器中如何呈现 HTML 文档。
	HTML 的 style 属性 : **提供了一种改变所有 HTML 元素的样式的通用方法。**






