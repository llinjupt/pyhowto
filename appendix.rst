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
- `廖雪峰 Python 教程 <https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000>`_
- `机器学习 <https://thepythonguru.com/top-5-machine-learning-libraries-in-python/#more-1948>`_
- `2to3版本代码转换工具 <https://bitbucket.org/python_mirrors/2to3>`_
- `Python公开课 <https://python123.io>`_
- `tutorialspoint代码示例 <http://www.tutorialspoint.com/python>`_
- `Python 代码编写规范 <https://pep8.org/>`_
- `Unix教程 <https://www.unixtutorial.org/>`_
- `Python快速入门LearnXinYminutes <https://learnxinyminutes.com/docs/python/>`_
- `迭代和迭代器关系  <https://nvie.com/posts/iterators-vs-generators/>`_
- `Python课程和测验 <https://www.programiz.com/>`_
- `Python Coding Samples <https://www.bogotobogo.com/python/pytut.php>`_
- `Python 面试题 <https://www.bogotobogo.com/python/python_interview_questions.php>`_
- `Python 内部实现 <https://eli.thegreenplace.net/tag/python-internals>`_
- `graphviz 官方文档 <https://graphviz.org/documentation/>`_
- `Python 进阶 <https://docs.pythontab.com/interpy/>`_
- `Python 函数模块实例 <https://www.journaldev.com/python>`_
- `Python3.0 简史 <https://www.cnblogs.com/animalize/p/5633215.html>`_
- `Module of the Week <https://pymotw.com/3/>`_

数据编码
--------------
- `JSON 格式 <http://www.json.org/json-zh.html>`_

数据库相关
--------------
- `Python 数据库操作实例 <http://www.cnblogs.com/idbeta/p/5209522.html>`_
- `Sqlite数据库操作 <http://www.runoob.com/sqlite/sqlite-data-types.html>`_

图像相关
-----------
- `Graphviz 官网 <http://www.graphviz.org>`_
- `Graphviz 示例1 <https://graphs.grevian.org/example>`_
- `Graphviz 示例2 <https://renenyffenegger.ch/notes/tools/Graphviz/examples/index>`_
- `Graphviz 示例3 <http://www.tonyballantyne.com/graphs.html>`_
- `Matplotlib 教程 <https://liam.page/2014/09/11/matplotlib-tutorial-zh-cn/>`_
- `matplotlib 进阶和入门 <https://blog.csdn.net/qq_34337272/article/details/79555544>`_
- `Pillow 图像处理 <https://pillow.readthedocs.io/en/5.3.x/>`_
- `Turtle 绘图示例 <https://www.zhihu.com/question/271643290/answer/525019532>`_
- `Matplotlib 用户指南 <https://wizardforcel.gitbooks.io/matplotlib-user-guide/>`_

符号和表达式
--------------
- `正则表达式 <http://deerchao.net/>`_
- `常用数学符号的 LaTeX 表示方法 <http://www.mohu.org/info/symbols/symbols.htm>`_
- `Math in reStructuredText <https://yuyuan.org/MathInreStructuredText/#use-mathjax-in-restructuredtext>`_

RST语法参考
------------

LaTeX数学表达式
~~~~~~~~~~~~~~~~

.. math::
  
  c^{2}=a^{2}+b^{2}
  
.. math::
  
  \ P(X=a|Y=b)=\frac{P(X=a,Y=b)}{P(Y=b)}
 
.. role:: raw-latex(raw)
    :format: latex html

This: :raw-latex:`\((x+a)^3\)`

this: :raw-latex:`\(W \approx \sum{f(x_k) \Delta x}\)`

this: :raw-latex:`\(W = \int_{a}^{b}{f(x) dx}\)`

:raw-latex:`\(\sqrt{x}\)`，不好处理

and this:

.. raw:: latex html

   \[ \frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} =
   1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}
   {1+\frac{e^{-8\pi}} {1+\ldots} } } } \]

When :raw-latex:`\(a \ne 0\)`, there are two solutions to :raw-latex:`\(ax^2 + bx + c = 0\)` and they are
:raw-latex:`\(x = {-b \pm \sqrt{b^2-4ac} \over 2a}.\)`

其他语法
~~~~~~~~~~~~

| .. _my-reference-label0:
| .. _nopara_decorator_class:
| :ref:`nopara_decorator_class` 

.. parsed-literal::

     驱动器 C 中的卷是 系统专区
     卷的序列号是 78E7-2220

.. figure:: imgs/obj.png
  :scale: 100%
  :align: center
  :alt: DAG

  object 和 type 关系图 （实线表继承关系，虚线表实例关系 Shalabh Chaturvedi）
 
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
