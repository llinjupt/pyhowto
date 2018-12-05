附录
================

参考书目
-----------

| [1] Eric Matthes，袁国忠(译).Python编程从入门到实践[M].北京:人民邮电出版社，2016
| [2] Micha Gorelick，Ian Ozsvald，胡世杰，徐旭彬(译).Python高性能编程[M].北京:人民邮电出版社，2017
| [3] Jake VanderPlas，陈俊杰，陈小莉(译).Python数据科学手册[M].北京:人民邮电出版社，2017
| [4] Mark Lutz. Learning Python(5th Edtion) [M] O’reilly Media Inc Gravenstein Highway North，2013

参考网站
-----------
- `Python官方文档 <https://docs.python.org>`_ 
- `机器学习 <https://thepythonguru.com/top-5-machine-learning-libraries-in-python/#more-1948>`_
- `2to3版本代码转换工具 <https://bitbucket.org/python_mirrors/2to3>`_
- `Python公开课 <https://python123.io>`_
- `tutorialspoint代码示例 <http://www.tutorialspoint.com/python>`_
- `Python 代码编写规范 <https://pep8.org/>`_
- `Unix教程 <https://www.unixtutorial.org/>`_
- `Python快速入门LearnXinYminutes <https://learnxinyminutes.com/docs/python/>`_
- `迭代和迭代器关系  <https://nvie.com/posts/iterators-vs-generators/>`_
- `Python课程和测验 <https://www.programiz.com/>`_

RST语法参考
------------

| .. _my-reference-label0:
|  :ref:`my-reference-label0`。
| .. _nopara_decorator_class:

.. admonition:: 注意

  任何对文件的读取和写入动作，都会自动改变文件的指针偏移位置。
  
*重点(emphasis)通常显示为斜体*

**重点强调(strong emphasis)通常显示为粗体**

`解释文字(interpreted text)通常显示为斜体`

:时间: 2016年06月21日

1. 枚举列表1
#. 枚举列表2
#. 枚举列表3

(I) 枚举列表1
(#) 枚举列表2
(#) 枚举列表3

A) 枚举列表1
#) 枚举列表2
#) 枚举列表3

下面是引用的内容：

    “真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血。”

    --- 鲁迅

..

      “人生的意志和劳动将创造奇迹般的奇迹。”

      — 涅克拉索

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def AAAA(a,b,c):
      for num in nums:
          print(Num)

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            | DOS/VMS-style options toofdsfds
              | fdsafdsafdsafsafdsafsa
              | fdsafdsafsd

John Doe wrote::

>> Great idea!
>
> Why didn't I think of that?

You just did!  ;-)

    | A one, two, a one two three four
    |
    | Half a bee, philosophically,
    |     must, *ipso facto*, half not be.
    | But half the bee has got to be,
    |     *vis a vis* its entity.  D'you see?
    |
    | But can a bee be said to be
    |     or not to be an entire bee,
    |         when half the bee is not a bee,
    |             due to some ancient injury?
    |
    | Singing...
    
| 第四个段落，段内的换行。
| 用竖线和空格开头，之后的每一行
| 在渲染时都会单独成行。
| 这功能不常用，因为用列表会更美观。

=====  =====
col 1  col 2
=====  =====
1      Second column of row 1.
2      Second column of row 2.
       Second line of paragraph.
3      - Second column of row 3.

       - Second item in bullet
         list (row 3, column 2).
\      Row 4; column 1 will be empty.
=====  =====

- 功能      

  - 你好 list item.  The blank line above the
    first list item is required; blank lines between list items
    (such as below this paragraph) are optional.

- 函数

  - 你好 is the first paragraph in the second item in the list.
  
    This is the second paragraph in the second item in the list.
    The blank line above this paragraph is required.  The left edge
    of this paragraph lines up with the paragraph above, both
    indented relative to the bullet.
  
    - This is a sublist.  The bullet lines up with the left edge of
      the text blocks above.  A sublist is a new list so requires a
      blank line above and below.

::

    原始文本块内的任何标记都不会被转换，随便写。

    `Bary.com <http://www.bary.com/>`_

    这还会显示在原始文本块中。

        缩进都会原样显示出来。

        只要最后有空行，缩进退回到 :: 的位置，就表示退出了\ `原始文本块`_。

会自动把网址转成超链接，像这样 http://www.bary.com/ ，注意结束的地方要跟空格。

如果你希望网址和文本之间没有空格，可以用转义符号反斜杠 \\ 把空格消掉，由于反斜\
杠是转义符号，所以如果你想在文中显示它，需要打两个反斜杠，也就是用反斜杠转义一\
个反斜杠。

渲染后紧挨文本和句号的超链接\ http://www.bary.com/\ 。

其实遇到紧跟常用的标点的情况时，不需要用空格，只是统一使用空格记忆负担小。\
你看\ http://www.bary.com/，这样也行。

.. note::

  写完本文我发现我用的渲染器对中文自动消除了空格，行尾不加反斜杠也行，但我不\
  保证其他渲染器也这么智能，所以原样保留了文内的反斜杠。

如果希望硬断行且不自动添加空格（例如中文文章），在行尾添加一个反斜杠。\
折上去的部分就不会有空格。注意所有的硬换行都要对齐缩进。

+-------------+----+-----+----+-----+----+-----+
+打开模式     +r   +r+   +w   +w+   +a   +a+   +
+=============+====+=====+====+=====+====+=====+
+可读         ++   ++    +    ++    +    ++    +
+-------------+----+-----+----+-----+----+-----+
+可写         +    ++    ++   ++    ++   ++    +
+-------------+----+-----+----+-----+----+-----+
+创建         +    +     ++   ++    +    +     +
+-------------+----+-----+----+-----+----+-----+
+覆盖         +    +     ++   ++    +    +     +
+-------------+----+-----+----+-----+----+-----+
+指针在开始   ++   ++    ++   ++    +    +     +
+-------------+----+-----+----+-----+----+-----+
+指针在结尾   +    +     +    +     ++   ++    +
+-------------+----+-----+----+-----+----+-----+ 

以空格作分隔符，间距均匀。决定了这个表格最多可以有5列,下划线的长度应不小于字符长度。
每一行的下划线，决定了相应列是否合并，如果不打算合并列，可以取消表内分隔线

===== ===== ===== ===== =====   
11    12    13    14    15
----------- -----------------   
21    22    23    24    25
----- ----- ----- ----- -----   
31    32    33    34    35
----- ----------- -----------   
41    42    42    44    45
============================= 

:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer
