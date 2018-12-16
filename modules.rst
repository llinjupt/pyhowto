内建模块
================

inspect
---------------

inspect 模块用于收集 Python 对象的信息，可以获取类或函数的参数的信息，源码，解析堆栈，对对象进行类型检查等。

我们使用 sample.py 作为测试模块，源码如下：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  # -*- coding: utf-8 -*-
  """
  Created on Wed Dec 12 17:16:47 2017
  @author: Red
  """

  sample_str = "sample module"  
  sample_list = [1, 2, 3]

  # This is a function of sample
  def sample_func(arg0, args1="name", *args, **kwargs):
      """This is a sample module function."""
      f_var = arg0 + 1
      return f_var
  
  class A():
      """Definition for A class."""
  
      def __init__(self, name):
          self.name = name
  
      def get_name(self):
          "Returns the name of the instance."
          return self.name
  
  obj_a = A('A Class instance')
  
  class B(A):
      """B class, inherit A class. """
  
      # This method is not part of A class.
      def cls_func(self):
          """Anything can be done here."""
  
      def get_name(self):
          "Overrides method from X"
          return 'B(' + self.name + ')'
  
  obj_b = B('B Class instance')

获取模块信息
~~~~~~~~~~~~~~~~~

getmodulename(path) 方法获取文件名，ismodule(obj) 判断对象是否为模块。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  import sample
  print(inspect.getmodulename("./sample.py"))
  print(inspect.ismodule(sample))
  print(inspect.ismodule(1))
  
  >>>
  sample
  True
  False

我们也可以使用 getmembers() 获取更多的模块信息，关于 getmembers() 方法的详细使用请参考下一小节：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  for name, data in inspect.getmembers(sample):
      if name == '__builtins__':
          continue
      if name.startswith('__'):
          print(name, repr(data))
  
  >>>
  __cached__ 'Z:\\sdc\\lbooks\\ml\\__pycache__\\sample.cpython-36.pyc'
  __doc__ '\nCreated on Wed Dec 12 17:16:47 2017\n@author: Red\n'
  __file__ 'Z:\\sdc\\lbooks\\ml\\sample.py'
  __loader__ <_frozen_importlib_external.SourceFileLoader object .....>
  __name__ 'sample'
  __package__ ''
  __spec__ ModuleSpec(name='sample', loader=......

getmembers
~~~~~~~~~~~~~~~~~

::
  
  getmembers(object, predicate=None)
      Return all members of an object as (name, value) pairs sorted by name.
      Optionally, only return members that satisfy a given predicate.

getmembers() 方法非常强大，它可以获取模块，对象成员属性。predicate 用于过滤特定属性的成员。
它返回一个列表，列表中的每个元素是一个形如 (name, value) 的元组。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  print(inspect.getmembers(sample))
  
  >>>
  [('A', <class 'sample.A'>), ('B', <class 'sample.B'>), ('__builtins__',
  ......

由于模块默认继承很多内建属性，它会打印很多信息，内建属性通常以 __ 开头，我们可以进行如下过滤：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  for name,type in inspect.getmembers(sample):
      if name.startswith('__'):
          continue
      print(name, type)
  
  >>>
  A <class 'sample.A'>
  B <class 'sample.B'>
  obj_a <sample.A object at 0x000002B5960E9128>
  obj_b <sample.B object at 0x000002B5960E99E8>
  sample_func <function sample_func at 0x000002B5960732F0>
  sample_list [1, 2, 3]
  sample_str sample module

通过 predicate 参数指定 inspect 自带的判定函数，可以获取类，函数等任何特定的信息。

查看模块中的类
`````````````````

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  for name,type in inspect.getmembers(sample, inspect.isclass):
      print(name, type)

  >>>
  A <class 'sample.A'>
  B <class 'sample.B'>

查看模块中函数
`````````````````

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  for name,type in inspect.getmembers(sample, inspect.isfunction):
      print(name, type)

  >>>
  sample_func <function sample_func at 0x000002B5961F8840>

查看类属性
`````````````

查看类函数：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  for name, type in inspect.getmembers(sample.A, inspect.isfunction):
      print(name, type)
  
  >>>
  __init__ <function A.__init__ at 0x000002B5961F8D08>
  get_name <function A.get_name at 0x000002B5961F80D0>

查看对象属性
`````````````

查看对象方法：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  for name, type in inspect.getmembers(sample.obj_a, inspect.ismethod):
      print(name, type)
  print()
  for name, type in inspect.getmembers(sample.obj_b, inspect.ismethod):
      print(name, type)
  
  >>>
  __init__ <bound method A.__init__ of <sample.A object at 0x000002B5961BAA90>>
  get_name <bound method A.get_name of <sample.A object at 0x000002B5961BAA90>>
  
  __init__ <bound method A.__init__ of <sample.B object at 0x000002B596117278>>
  cls_func <bound method B.cls_func of <sample.B object at 0x000002B596117278>>
  get_name <bound method B.get_name of <sample.B object at 0x000002B596117278>>

getdoc 和 getcomments
~~~~~~~~~~~~~~~~~~~~~~~~

getdoc(object) 可以获取任一对象的 __doc__ 属性。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print('A.__doc__:')
  print(sample.A.__doc__)
  print()
  print('getdoc(A):')
  print(inspect.getdoc(sample.A))
  
  >>>
  A.__doc__:
  Definition for A class.
  
  getdoc(A):
  Definition for A class.

getcomments() 方法获取模块，函数或者类定义前的注释行，注释必须以 # 开头。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(inspect.getcomments(sample))
  print(inspect.getcomments(sample.sample_func))

  >>>
  # -*- coding: utf-8 -*-

  # This is a function of sample

getsource
~~~~~~~~~~~~~~~~~~~~

getsource(object) 可以获模块，函数或者类，类方法的源代码。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  print(inspect.getsource(sample.sample_func))  
  print(inspect.getsource(sample.B.get_name))
  
  >>>
  def sample_func(arg0, arg1="name", *args, **kwargs):
      """This is a sample module function."""
      f_var = arg0 + 1
      return f_var
      
    def get_name(self):
        "Overrides method from X"
        return 'B(' + self.name + ')'

getsourcelines(object) 返回一个元组，元组第一项为对象源代码行的列表，第二项是第一行源代码的行号。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(inspect.getsourcelines(sample.sample_func))
  
  >>>
  (['def sample_func(arg0, *args, **kwargs):\n',...... return f_var\n'], 10)

函数参数相关
~~~~~~~~~~~~

signature() 返回函数的参数列表，常被 IDE 用来做代码提示：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(inspect.signature(sample.sample_func))
  print(inspect.signature(sample.B.get_name))
  
  >>>
  (arg0, *args, **kwargs)
  (self)

getfullargspec() 将函数参数按不同类型返回。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  arg_spec = inspect.getfullargspec(sample.sample_func)
  print('namedkey:', arg_spec[0])
  print('*       :', arg_spec[1])
  print('**      :', arg_spec[2])
  print('defaults:', arg_spec[3])
  
  >>>
  namedkey: ['arg0', 'args1']
  *       : args
  **      : kwargs
  defaults: ('name',)

getcallargs() 方法将函数形参与实参绑定，返回一个字典：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  def f(a, b=1, *pos, **named):
    pass
  
  print(getcallargs(f, 1, 2, 3) == {'a': 1, 'named': {}, 'b': 2, 'pos': (3,)})
  print(getcallargs(f, a=2, x=4) == {'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()})  
  
  >>> 
  True
  True

getmro
~~~~~~~~~~~~

获取继承序列，与类对象的 __mro__ 属性对应：

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  print(B.__mro__)
  print(inspect.getmro(B))

  >>>
  (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
  (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

获取调用栈
~~~~~~~~~~~~~~

获取调用栈信息的系列方法均支持 context 参数，默认值为1，可以传入整数值 n 来获取调用栈的上线文的 n 行源码。

stack 和 getframeinfo
````````````````````````````

类似于 C 语言，Python 解释器也使用栈帧（Stack frame）机制来管理函数调用。

stack() 方法获取当前的所有栈帧信息，它是一个 list。getframeinfo() 打印栈帧信息。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def dump_stack(stack):
      for i in stack:
          frame,filename,lineno,funcname,lines,index = i
          print(inspect.getframeinfo(frame))
          print(filename,lineno,funcname,lines,index)    
  
  dump_stack(inspect.stack())
  
  >>>
  Traceback(filename='tmp.py', lineno=29, function='<module>', 
  code_context=['dump_stack(inspect.stack())\n'], index=0)
  ('tmp.py', 29, '<module>', ['dump_stack(inspect.stack())\n'], 0)

可以看到一个栈帧是一个元组，包含文件名，行号，函数名（如果是在函数外调用，则显示模块名），调用 stack() 处的代码和上下文索引 6 个元素。

所谓上下文索引，即调用 stack() 所在语句在源码上下文的编号。如果要获取栈帧信息的更多源码，可以给传入 context 参数，默认为 1。

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  # before line 2
  # before line 1
  dump_stack(inspect.stack(3))
  # after line 1

  >>>

  Traceback(filename='tmp.py', lineno=29, function='<module>', 
  code_context=['dump_stack(inspect.stack(3))\n'], index=0)
  ('tmp.py', 29, '<module>', ['# before line 1\n', 'dump_stack(inspect.stack(3))\n', 
   '# after line 1\n'], 1)

trace
````````````````````

trace() 返回异常时的栈帧信息，如果没有异常发生，trace() 返回空列表。

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  def call():
      try:
          1/0
      except:
          dump_stack(inspect.trace())
  
  call()

  >>>

  Traceback(filename='tmp.py', lineno=31, function='call', 
  code_context=['        dump_stack(inspect.trace())\n'], index=0)
  ('tmp.py', 29, 'call', ['        1/0\n'], 0) # lines 返回触发异常时的代码

这里与 stack() 做一对比，显然 stack() 返回所有栈帧信息，顶层栈帧记录的不是触发异常的代码行，而是调用 stack() 的代码行。

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  def call():
      try:
          1/0
      except:
          dump_stack(inspect.stack())
  
  call()
  
  >>>  
  Traceback(filename='tmp.py', lineno=31, function='call', 
  code_context=['        dump_stack(inspect.stack())\n'], index=0)
  ('tmp.py', 31, 'call', ['        dump_stack(inspect.stack())\n'], 0)
  Traceback(filename='tmp.py', lineno=33, function='<module>', 
  code_context=['call()\n'], index=0)
  ('tmp.py', 33, '<module>', ['call()\n'], 0)

currentframe
`````````````````````

获取当前正在运行的代码行所在的栈帧，也即当前栈帧。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def dump_frame(frame):
      print(getframeinfo(frame))
  
  dump_frame(inspect.currentframe())
  
  >>>
  Traceback(filename='tmp.py', lineno=31, function='<module>', 
  code_context=['dump_frame(inspect.current)\n'], index=0)

getouterframes
````````````````````

getouterframes(frame) 返回从 frame 到栈底的所有栈帧，对于 frame 来说，从它到栈底的帧都被称为外部帧。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def current_frame():
      return inspect.currentframe()
  
  stack = inspect.getouterframes(current_frame())

上述代码返回含当前栈帧的所有帧，等同于 stack()。

getinnerframes
```````````````````````

getinnerframes(traceback) 用于获取一个 traceback 对象中的栈帧。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  import sys
  try:
      1/0
  except:
      prev_cls, prev, tb = sys.exc_info()
      frames = inspect.getinnerframes(tb)
      dump_stack(frames)
  
  >>>
  Traceback(filename='tmp.py', lineno=42, function='<module>', 
  code_context=['    dump_stack(frames)\n'], index=0)
  tmp.py 38 <module> ['    1/0\n'] 0

re
---------------

我们常常需要判断一个给定字符串的合法性，比如一串数字是否是电话号码；一串字符是否是合法的 URL，Email 地址；用户输入的密码是否满足复杂度要求等等。

如果我们为每一种格式都定义一个判定函数，首先这种定义可能很复杂，比如时间可以用 “1970 年 1 月 1 日” 表示，也可以表示为 “1970-01-01” 或者 “1970-1-1”。这样代码的逻辑复杂度就线性增加。其次我们定义的函数功能很难重用，匹配 A 的不能匹配 B。能否有一个万能的函数，只要我们传入特定的参数就能实现我们特定的字符匹配需求呢？答案是肯定的。

在 :ref:`strs_map_replace` 中我们曾经使用过 re.sub 函数来替换多个字符串。这个问题看似简单，直接可以想到使用多次 replace 替换，但是会带来副作用，因为前一次被替换的字符串可能被再次替换掉，比如后面的替换字符串是前一个的子串，或者已经替换的字符串和前后字符正好形成了后来要替换的字符串。

一个可行的解决方案是使用第一个被替换字符串把字符串分割成多个子串，然后用第二个被替换字符串再次分割每一子串，依次类推，直至最后一个被替换字符分割完毕，再依次使用被替换字符进行合并逆操作。这种方案实现起来比较复杂，使用 re.sub 就简单多了。

正则表达式（Regular Expression）描述了一种字符串匹配的模式（Pattern），re 模块名就是正则表达式的缩写，它提供强大的字符匹配替换统计等操作，且适用于 Unicode 字符串。

正则表达式语法
~~~~~~~~~~~~~~~

