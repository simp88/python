# 字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
# 创建字符串很简单，只要为变量分配一个值即可。例如：
var1 = "Holle Word!"
var2 = "Python"
# Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法格式如下
print(var1[1])
print(var2[0:4])
# 字符串更新
print(var2[:6] + " good！")

var2 = var2 + " good!"
print(var2)

# 替换字符串中的某些字符或子字符串，可以使用replace()方法
var2 = var2.replace("Python", "good")
print(var2)
