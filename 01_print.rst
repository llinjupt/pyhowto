打印输出和格式化
==================

直接打印输出
-----------------

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

不换行打印输出(1)
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

不换行打印输出(2)
-----------------

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

长行打印输出(1)
-----------------

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

使用一对三引号和上述代码是等价的，以上写法每行字符必须顶格，否则对齐空格将作为字符串内容被打印，这影响了代码的美观。
  

长行打印输出(2)
-----------------

上面的输出方式有一个缺点，代码必须顶格，否则作为代码对齐的空格将被打印输出。可以为每行加引号来解决这个问题。

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
--------------------------

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
---------------------

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

