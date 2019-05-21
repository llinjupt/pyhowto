打印输出和格式化
==================

直接打印输出
-----------------

::

 print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

print()内建函数用于打印输出，默认打印到标准输出 sys.stdout。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  print("Hello %s: %d" % ("World", 100))
  print("end")
  
  >>>
  Hello World: 100
  end

print()函数会自动在输出行后添加换行符。

不换行打印输出
-----------------

.. code-block:: python
  :linenos:
  :lineno-start: 0

  strs = "123"
  for i in strs:
      print(i),
  print("end")
  
  >>>
  1 2 3 end
  
通过在print()语句后添加"," 可以不换行，但会自动在输出后添加一个空格。

print()函数支持end参数，默认为换行符，如果句尾有逗号，则默认为空格，可以指定end参数为空字符，来避免输出空格

.. code-block:: python
  :linenos:
  :lineno-start: 0

  str0 = "123"
  print(str0, end='')
  print("end")
  >>>
  
  123end

使用 sys.stdout 模块中的 write() 函数可以实现直接输出。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  import sys
  strs = "123"
  for i in strs:
      sys.stdout.write(i)
  print("end")

  >>>
  123end

分隔符打印多个字符串
--------------------

print()函数支持一次输入多个打印字符串，默认以空格分割，可以通过sep参数指定分割符号。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  str0 = "123"
  str1 = "456%s" # 字符串中的%s不会被解释为格式化字符串
  
  # 含有%s的格式化字符串只能有一个，且位于最后
  print(str0,str1,"%s%s" %("end", "!")) 
  print(str0,str1,"%s%s" %("end", "!"), sep='*') 
  
  print("%s*%s*end!" % (str0, str1)) # 手动指定分隔符
  
  >>>
  123 456%s end!
  123*456%s*end!
  123*456%s*end!

格式化输出到变量
-----------------

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  tmpstr = ("Number is: %d" % 100)
  print(tmpstr)
  hexlist = [("%02x" % ord(x) )for x in tmpstr]
  print(' '.join(hexlist))
  print("end")

  >>>
  Number is: 100
  4e 75 6d 62 65 72 20 69 73 3a 20 31 30 30
  end

通过打印字符串的 ascii 码，可以看到换行符是 print()函数在打印时追加的，而并没有格式化到变量中。

长行打印输出
--------------

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  def print_long_line():
      print("The door bursts open. A MAN and WOMAN enter, drunk and giggling,\
  horny as hell.No sooner is the door shut than they're all over each other,\
  ripping at clothes,pawing at flesh, mouths locked together.")

  print_long_line()
  
  >>>
  The door bursts open. A MAN and WOMAN enter, drunk and giggling,horny as 
  hell.No sooner is the door shut than they're all over each other, ripping 
  at clothes,pawing at flesh, mouths locked together.

如果 print() 函数要打印很长的数据，则可使用右斜杠将一行的语句分为多行进行编辑，编译器在执行时，
将它们作为一行解释，注意右斜杠后不可有空格，且其后的行必须顶格，否则头部空格将被打印。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def print_long_line():
      print("""The door bursts open. A MAN and WOMAN enter, drunk and giggling,
  horny as hell.No sooner is the door shut than they're all over each other,
  ripping at clothes,pawing at flesh, mouths locked together.""")

使用一对三引号和上述代码是等价的，以上写法每行字符必须顶格，否则对齐空格将作为字符串内容被打印，这影响了代码的美观。可以为每行添加引号来解决这个问题。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  def print_long_line():
      print("The door bursts open. A MAN and WOMAN enter, drunk and giggling,"
            "horny as hell.No sooner is the door shut than they're all over each other,"
            "ripping at clothes,pawing at flesh, mouths locked together.")
  
  print_long_line()
  
  >>>
  The door bursts open. A MAN and WOMAN enter, drunk and giggling,horny as 
  hell.No sooner is the door shut than they're all over each other, ripping 
  at clothes,pawing at flesh, mouths locked together.

打印含有引号的字符串
-----------------------

Python 使用单引号或者双引号来表示字符，那么当打印含有单双引号的行时如何处理呢？

.. code-block:: php
  :linenos:
  :lineno-start: 0

  print("It's a dog!")
  print('It is a "Gentleman" dog!')
  print('''It's a "Gentleman" dog!''')

  >>>
  It's a dog!
  It is a "Gentleman" dog!
  It's a "Gentleman" dog!

.. _my-reference-label0:

打印输出到文件
-----------------

print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

print() 函数支持 file 参数来指定输出文件的描述符。默认值是标准输出sys.stdout，与此对应，
标准的错误输出是 sys.stderr，当然也可以指定普通文件描述符。

输出到磁盘文件时，为了保证实时性，根据实际情况可能需要把 flush 参数设置为 True。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  logf = open("logfile.log", "a+")
  print("123", file=logf, flush=True)

对齐输出（左中右对齐）
----------------------

通过print()函数可以直接实现左对齐输出。print() 函数不能动态指定对齐的字符数，
也不能指定其他填充字符，只能使用默认的空格进行填充。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  man = [["Name", "John"], ["Age", "25"], ["Address", "BeiJing China"]]
  for i in man:
      print("%-10s: %s" % (i[0], i[1]))
  
  >>>
  Name      : John
  Age       : 25
  Address   : BeiJing China

Python中字符串处理函数 ljust(), rjust() 和 center() 提供了更强大的对齐输出功能。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  print("123".ljust(5) == "123  ")
  print("123".rjust(5) == "  123")
  print("123".center(5) == " 123 ")

  print("123".ljust(5, '~'))
  print("123".rjust(5, '~'))
  print("123".center(5, '~'))
  
  >>>
  True
  True
  True
  123~~
  ~~123
  ~123~

左对齐 ljust() 示例，计算特征量的长度，决定动态偏移的字符数。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  len_list=[len(x[0]) for x in man]
  offset = max(len_list) + 5        # 增加5个空白符号
  for i in man:
      print("%s: %s" % (i[0].ljust(offset), i[1]))

  >>>
  Name        : John
  Age         : 25
  Address     : BeiJing China

左对齐 rjust() 示例:

.. code-block:: python
  :linenos:
  :lineno-start: 0

  len_list=[len(x[0]) for x in man]
  offset = max(len_list) + 5        # 增加5个空白符号
  for i in man:
      print("%s: %s" % (i[0].ljust(offset), i[1]))

  >>>
  Name        : John
  Age         : 25
  Address     : BeiJing China

居中对齐示例，这里以字符‘~’填充。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  lines = ["GNU GENERAL PUBLIC LICENSE", "Version 3, 29 June 2007"]
  len_list=[len(x) for x in lines]
  center_num = max(len_list) + 30
  for i in lines:
      print(i.center(center_num, "~"))

  >>>
  ~~~~~~~~~~~~~~~GNU GENERAL PUBLIC LICENSE~~~~~~~~~~~~~~~
  ~~~~~~~~~~~~~~~~Version 3, 29 June 2007~~~~~~~~~~~~~~~~~

.. _output_format:

格式化输出
----------------

更多格式化输出请参考 :ref:`str_format` 。

百分号格式化
~~~~~~~~~~~~~

与 C 语言类似，python 支持百分号格式化，并且基本保持了一致。

数值格式化
``````````````

整数格式化符号可以指定不同进制：

- %o —— oct 八进制
- %d —— dec 十进制
- %x —— hex 十六进制
- %X —— hex 十六进制大写

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print('%o %d %x %X' % (10, 10, 10, 10))
  
  >>>
  12 10 a A

浮点数可以指定保留的小数位数或使用科学计数法：

- %f —— 保留小数点后面 6 位有效数字，%.2f，保留 2 位小数位。
- %e —— 保留小数点后面 6 位有效数字，指数形式输出，%.2e，保留 2 位小数位，使用科学计数法。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print('%f' % 1.23)  # 默认保留6位小数
  
  >>> 
  1.230000
  
  print('%0.2f' % 1.23456) # 保留 2 位小数
  
  >>>
  1.23

  print('%e' % 1.23)  # 默认6位小数，用科学计数法
  
  >>>
  1.230000e+00
  
  print('%0.2e' % 1.23)  # 保留 2 位小数，用科学计数法
  
  >>>
  1.23e+00

字符串格式化
`````````````

- %s     —— 格式化字符串
- %10s   —— 右对齐，空格占位符 10 位
- %-10s  —— 左对齐，空格占位符 10 位
- %.2s   —— 截取 2 个字符串
- %10.2s —— 10 位占位符，截取两个字符

.. code-block:: python
  :linenos:
  :lineno-start: 0
 
  print('%s' % 'hello world')  # 字符串输出

  >>>
  hello world

  print('%20s' % 'hello world')  # 右对齐，取 20 个字符，不够则空格补位
  
  >>>
           hello world
  print('%-20s' % 'hello world')  # 左对齐，取 20 个字符，不够则空格补位
  
  >>>
  hello world         
  
  print('%.2s' % 'hello world')  # 取 2 个字符，默认左对齐
  
  >>>
  he
  
  print('%10.2s' % 'hello world')  # 右对齐，取 2 个字符
  
  >>>
          he
          
  print('%-10.2s' % 'hello world')  # 左对齐，取 2 个字符
  
  >>>
  he

format 格式化
~~~~~~~~~~~~~~~~~

format() 是字符串对象的内置函数，它提供了比百分号格式化更强大的功能，例如调整参数顺序，支持字典关键字等。它该函数把字符串当成一个模板，通过传入的参数进行格式化，并且使用大括号 ‘{}’ 作为特殊字符代替 ‘%’。

位置匹配
````````````

位置匹配有以下几种方式：

- 不带编号，即“{}”，此时按顺序匹配
- 带数字编号，可调换顺序，即 “{1}”、“{2}”，按编号匹配
- 带关键字，即“{name}”、“{name1}”，按字典键匹配
- 通过对象属性匹配，例如 obj.x
- 通过下标索引匹配，例如 a[0]，a[1]

.. code-block:: python
  :linenos:
  :lineno-start: 0

  >>> print('{} {}'.format('hello','world'))  # 默认从左到右匹配
  hello world
  
  >>> print('{0} {1}'.format('hello','world'))  # 按数字编号匹配
  hello world
  >>> print('{0} {1} {0}'.format('hello','world'))  # 打乱顺序
  hello world hello
  >>> print('{1} {1} {0}'.format('hello','world'))
  world world hello
  
  >>> print('{wd} {ho}'.format(ho='hello',wd='world'))  # 关键字匹配
  world hello  

通过对象属性匹配，可以方便地实现对象的 str 方法：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  class Point:
      def __init__(self, x, y):
          self.x, self.y = x, y
      
      # 通过对象属性匹配
      def __str__(self):
          return 'Point({self.x}, {self.y})'.format(self=self)
  
  >>>str(Point(5, 6))
  'Point(4, 2)'

对于元组，列表，字典等支持索引的对象，支持使用索引匹配位置：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  >>> point = (0, 1)
  >>> 'X: {0[0]};  Y: {0[1]}'.format(point)
  'X: 0;  Y: 1'
  >>> a = {'a': 'val_a', 'b': 'val_b'}
  
  # 注意这里的数字 0 代表引用的是 format 中的第一个对象
  >>> b = a
  >>> 'X: {0[a]};  Y: {1[b]}'.format(a, b)
  'X: val_a;  Y: val_b'

数值格式转换
``````````````

- 'b' - 二进制。将数字以2为基数进行输出。
- 'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
- 'd' - 十进制整数。将数字以10为基数进行输出。
- 'o' - 八进制。将数字以8为基数进行输出。
- 'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
- 'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
- 'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
- 'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
- '%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # 整数格式化
  >>> print('{0:b}'.format(3))
  11
  >>> print('{:c}'.format(97))
  a
  >>> print('{:d}'.format(20))
  20
  >>> print('{:o}'.format(20))
  24
  >>> print('{:x},{:X}'.format(0xab, 0xab))
  ab,AB
  
  # 浮点数格式化
  >>> print('{:e}'.format(20))
  2.000000e+01
  >>> print('{:g}'.format(20.1))
  20.1
  >>> print('{:f}'.format(20))
  20.000000
  >>> print('{:n}'.format(20))
  20
  >>> print('{:%}'.format(20))
  2000.000000%  

各种进制转换：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  >>> # format also supports binary numbers
  >>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
  'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
  >>> # with 0x, 0o, or 0b as prefix:
  
  # 在前面加“#”，自动添加进制前缀
  >>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)  
  'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
  
位数对齐和补全
```````````````

- < （默认）左对齐、> 右对齐、^ 中间对齐、= （只用于数字）在小数点后进行补齐
- 取字符数或者位数“{:4s}”、"{:.2f}"等

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  >>> print('{} and {}'.format('hello','world'))  # 默认左对齐
  hello and world
  >>> print('{:10s} and {:>10s}'.format('hello','world'))  # 取10位左对齐，取10位右对齐
  hello      and      world
  >>> print('{:^10s} and {:^10s}'.format('hello','world'))  # 取10位中间对齐
    hello    and   world   
  >>> print('{} is {:.2f}'.format(1.123,1.123))  # 取2位小数
  1.123 is 1.12
  >>> print('{0} is {0:>10.2f}'.format(1.123))  # 取2位小数，右对齐，取10位
  1.123 is       1.12
  
  >>> '{:<30}'.format('left aligned')  # 左对齐
  'left aligned                  '
  >>> '{:>30}'.format('right aligned')  # 右对齐
  '                 right aligned'
  >>> '{:^30}'.format('centered')  # 中间对齐
  '           centered           '
  >>> '{:*^30}'.format('centered')  # 使用“*”填充
  '***********centered***********'
  >>>'{:0=30}'.format(11)  # 还有“=”只能应用于数字，这种方法可用“>”代替
  '000000000000000000000000000011'

正负号和百分显示
`````````````````

正负符号显示通过 %+f, %-f, 和 % f 实现：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  >>> '{:+f}; {:+f}'.format(3.14, -3.14)  # 总是显示符号
  '+3.140000; -3.140000'
  >>> '{: f}; {: f}'.format(3.14, -3.14)  # 若是+数，则在前面留空格
  ' 3.140000; -3.140000'
  >>> '{:-f}; {:-f}'.format(3.14, -3.14)  # -数时显示-，与'{:f}; {:f}'一致
  '3.140000; -3.140000'

打印百分号，注意会自动计算百分数：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  >>> 'Correct answers: {:.2%}'.format(1/2.1)
  'Correct answers: 47.62%'
  
  # 以上代码等价于
  >>> 'Correct answers: {:.2f}%'.format(1/2.1 * 100)

千位分割数字
`````````````

用 “,” 分隔数字，每一千进位：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  >>> '{:,}'.format(1234567890)
  '1,234,567,890'

时间格式化
````````````````

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  >>> import datetime
  >>> d = datetime.datetime(2018, 5, 4, 11, 15, 38)
  >>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
  '2018-05-04 11:15:38'

占位符嵌套
```````````

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  >>> for align, text in zip('<^>', ['left', 'center', 'right']):
          '{0:{fill}{align}16}'.format(text, fill=align, align=align)
  
  'left<<<<<<<<<<<<'
  '^^^^^center^^^^^'
  '>>>>>>>>>>>right'

  >>> width = 5
  >>> for num in range(5,12):
          for base in 'dXob':
              print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
          print()
  
      5     5   101
      6     6   110
      7     7   111
      8    10  1000
      9    11  1001
      A    12  1010
      B    13  1011

repr 和 str 占位符
```````````````````

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  """
  replacement_field ::= "{" [field_name] ["!" conversion] [":" format_spec] "}"
  conversion ::= "r" | "s" | "a"
  这里只有三个转换符号，用"!"开头。
  "!r"对应 repr()；"!s"对应 str(); "!a"对应ascii()。
  """
  
  >>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
  "repr() shows quotes: 'test1'; str() doesn't: test2"  # 输出结果是一个带引号，一个不带

format 缩写形式
````````````````

可在格式化字符串前加 f 以达到格式化的目的，在 {} 里加入对象，这是 format 的缩写形式：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # a.format(b)
  >>> "{0} {1}".format("hello","world")
  'hello world'
  
  >>> a = "hello"
  >>> b = "world"
  >>> f"{a} {b}"
  'hello world'
  
  name = 'Tom'
  age = 18
  sex = 'man'
  job = "IT"
  salary = 5000
  
  print(f'My name is {name.capitalize()}.')
  print(f'I am {age:*^10} years old.')
  print(f'I am a {sex}')
  print(f'My salary is {salary:10.2f}')
  
  # 结果
  My name is Tom.
  I am ****18**** years old.
  I am a man
  My salary is 5000.00
