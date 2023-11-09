函数和装饰器
================

函数特性
---------------

函数是大部分高级编程语言的构成基础，本小结主要总结在 Python 中函数的一些特性和高阶函数。

定义和调用顺序
~~~~~~~~~~~~~~~

由于 Python 是一种解释执行的脚本语言，解释器在执行到某行语句时，当遇到一个符号调用时，比如一个函数，会根据函数名去对应的作用域去回溯查找，直至内建函数，如果找不到，则报错未定义，所以如果函数定义在执行语句之后，是不允许的。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  a()
  
  def a():
      print("function a")
  
  >>>  
  NameError: name 'a' is not defined

但是如果是在定义一个对象时，比如一个函数 a ，引用另一个未定义函数 b，而在执行语句调用 a 函数之前，b 已经定义了，则不会报错，因为解释器遇到 b 的定义时会加入到当前的作用域，然后再执行到该语句时，作用域中已经存在 b 的定义了。


.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def a():
      b()
  
  def b():
      print("function b")
  
  a()
  
  >>>
  function b

匿名函数
~~~~~~~~~~~

如果一个函数使用简单的表达式就可以实现所需功能，那么就无需显式定义一个函数，lamdba 表达式可以返回一个没有名字的函数，也即匿名函数。

比如一些函数需要函数作为参数，那么直接使用 lambda 就很简便。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  homo_add = lambda x, y : x + y  # 定义匿名函数
  print(type(homo_add))
  print(homo_add(1, 2))
  
  >>>
  <class 'function'>
  3

上面的匿名函数定义等价于：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  def homo_add(x, y):
      return x + y

把匿名函数赋值给变量 homo，所以它的类型是 function。通常在需要定义匿名函数的地方，直接使用 lambda 表达式即可，无需再给它一个名字：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(list(map(lambda x: x * x * x, [1, 2, 3, 4])))
  
  >>>
  [1, 8, 27, 64]
  
函数参数类型
~~~~~~~~~~~~~

Python 中的函数参数类型一共有五种，参考 `inspect 模块 <https://docs.python.org/3/library/inspect.html>`_ ，分别是：

- POSITIONAL_ONLY 位置参数，内置函数或模块使用，用户无法自定义一个只支持位置参数的函数。
- POSITIONAL_OR_KEYWORD 位置或关键字参数，参数同时支持位置或者关键字传递给函数。
- VAR_POSITIONAL 可变长参数，任意多个位置参数通过元组传递给函数。
- KEYWORD_ONLY 关键字参数，也被称为命名参数，通过指定的键值对传递给函数。
- VAR_KEYWORD 可变关键字参数，任意多个键值对参数通过字典传递给函数。

位置或关键字参数
`````````````````

首先看一下只（ONLY）支持通过参数位置来传递给函数的位置参数。它们没有名字，不能通过键值对传递。只有内置函数或者模块使用，用户无法自定义一个只支持位置参数的函数。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def foo(n):
      print(n)
  
  foo(1)
  foo(n = 2)
  
  >>>
  1
  2

我们看到自定义的函数 foo()，不仅可以通过第一个参数位置来传递实参 1，还可以通过名称 n 来传递参数 2。这里的 n 就是一个位置或关键字参数。它是最常用的参数传递方式。

而有一些内置函数，无法通过名称来传递，否则会报不支持关键参数的错误，比如内置函数 oct(x)，ord(c)，divmod(x, y)等等。它们的函数手册里一般就使用一个字母来表示一个参数，常用的比如 x，y，c。

::

  ord(c, /)
      Return the Unicode code point for a one-character string.

.. code-block:: python
  :linenos:
  :lineno-start: 0

  ord(c='1')
  
  >>>
      ord(c='1')

  TypeError: ord() takes no keyword arguments

可变参数
`````````````

可变参数用一个 * 号来声明，它把所有接收到的，未被位置或关键字参数处理的参数放入一个元组。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def variable_args(name="default", *args):
      print("name: %s" % name)
      print(args)
  
  variable_args("John", "Teacher", {"Level": 1})
  
  >>>
  name: john
  ('Teacher', {'Level': 1})

可以看到，"John" 均通过参数位置传递给了形参 name，后边多余的参数全部传递给了 ``*args``，它是一个元组。注意键值对参数不能被它处理。

关键字参数
`````````````````

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def keyword_only_args(name="default", *args, age):
      print("name: %s, age: %d" % (name, age))
      print(args)
  
  keyword_only_args("John", "Teacher", {"Level": 1}, age=30)    
  
  >>>      
  name: John, age: 30
  ('Teacher', {'Level': 1})

由于 age 形参位于可变参数之后，那么它的位置是不明确的，此时只能指定关键字 age，以键值对的方式传递它，被称为关键字参数。此时 args 元组中不会处理它。

可变关键字参数
````````````````

可变关键字参数通过前缀 ** 来声明，这种参数类型可以接收 0 个或多个键值对参数，并存入一个字典。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  def keyword_variable_args(name="default", *args, age, **kwargs):
      print("name: %s, age: %d" % (name, age))
      print(args)
      print(kwargs)
   
  keyword_variable_args("John", "Teacher", {"Level": 1}, id="332211", 
                      city="New York", age=30)

  >>>
  name: John, age: 30
  ('Teacher', {'Level': 1})
  {'id': '332211', 'city': 'New York'}

通过以上的示例，我们看到参数处理是有优先级的，首先通过位置匹配，然后进行关键字匹配，最后剩下的所有参数按照是否提供参数名来对应到可变参数或可变关键字参数。

.. _var_parameters_fun:

可变参数函数
~~~~~~~~~~~~~~~~

在了解了 Python 参数类型之后，我们可以定义一个可以处理任意类型任意参数数目的函数。 

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def test_args(*args, **kwargs):
      print(args)
      print(kwargs)
      
  test_args(1, 2, {"key0": "val0"}, name="name", age=18)

  >>>
  (1, 2, {'key0': 'val0'})
  {'name': 'name', 'age': 18}

test_args() 是一个可以接受任意多个参数的函数。由于参数处理是有优先级的，kwargs 和 args 顺序不可颠倒。

.. _var_pass_methods:

函数参数传递形式
~~~~~~~~~~~~~~~~~~

在介绍了 Python 参数类型后，我们可以通过两种形式为形参提供实参。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def test_input_args(list0, num0, name="Tom"):
      print("list:%s, num:%d, name:%s" % (str(list0), num0, name))
  
  test_input_args([1], 2, name="John")
  test_input_args(*([1], 2), **{"name": "John"}) 

  >>>
  list:[1], num:2, name:John
  list:[1], num:2, name:John

可以通过常用位置和关键字传递，也可以使用可变参数和可变关键字参数传递，它们是等价的。有了第二种参数传递形式，就可以在一个函数中调用不同的函数了，这一特性对于实现装饰器函数非常重要。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def func0(n):
      print("from %s, %d" %(func0.__name__, n))
  
  def func1(m, n):
      print("from %s, %d" %(func0.__name__, m + n))
  
  def test_call_func(func, *args, **kwargs):
      func(*args, **kwargs)

  test_call_func(func0, 1)
  test_call_func(func1, 1, 2)

  >>>
  from func0, 1
  from func0, 3

高阶函数
--------------------

functools 模块提供了一系列的重量级函数，这些函数有一个特点，函数调用其他函数完成复杂功能，或把一个函数作为返回值，这类函数被称为高阶（Higher-order）函数。
由于历史原因，多数高阶函数从内置函数中封装进 functools 模块，有些函数还没有，比如 map()。

Python3.x 中对这些函数进行了功能扩展，它们可以处理可迭代对象，并返回可迭代对象，具有惰性计算的特点，参考 :ref:`lazy_evaluation` 。

map
~~~~~~~~~~~~~~

::

  map(func, *iterables) --> map object
    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.  

map() 根据传入的函数对指定迭代对象做迭代处理，这一行为很像数学概念中的映射。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  mapobj = map(str, [1, 2, 3])
  print(type(mapobj))
  print(mapobj is iter(mapobj))

  print(list(mapobj))
  
  >>>
  <class 'map'>
  True
  ['1', '2', '3']

Python2.x 返回列表，Python3.x 则返回 map 对象，它是一个迭代器。这个改进具有重大的意义，可以用来处理无限序列。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def uint_creater():
      i = 0
      while(True):
          yield i
          i += 1
  
  cube = map(lambda x: x * x * x, uint_creater())
  for i in cube:
      if i < 10000000000:
          continue
      if i > 10099999999:
          break
      print(i)

  >>>
  10007873875
  10021812416
  10035763893

上面的示例用于查看特定范围内可以用来表示立方数的数，在范围是上百亿级别也和普通小数一样处理。可以应用在数论研究领域，比如进行质数的稀疏度分析。
由于第二个参数可以是多个迭代对象，我们还可以对数据进行并行操作：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  funcs = [lambda x: x * x, lambda x: x * x * x]
  map_func = lambda f: f(i)
  for i in range(4):
      print(list(map(map_func, funcs)))

  >>>
  [0, 0]
  [1, 1]
  [4, 8]

如果的函数列表中的函数具有多个参数如何处理呢？ 只要改写传入函数的参数个数即可，这里计算列表中每个成对的元素的差与和：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  funcs = [lambda x, y: abs(x - y), lambda x, y: y + x]
  map_func = lambda f: f(i[0], i[1])
  
  for i in [[1, 2], [3, 4]]:
      value = map(map_func, funcs)
      print(list(value))
  
  >>>
  [1, 3]
  [1, 7]

如果传入的函数有多个参数，如何处理呢？根据函数参数个数，来传递多个参数序列。例如依次求 pow(2, 2)，pow(3, 3) 和 pow(4, 4) 的值：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(list(map(pow, [2, 3, 4], [2, 3, 4])))
  
  >>>
  [4, 27, 256]

map() 函数的本质等同于如下函数：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def homo_map(func, seq):
  	  result = []
    	for x in seq: 
    	    result.append(func(x))
    	
    	return result

.. _reduce:

reduce
~~~~~~~~~~~~~~

reduce() 函数有两个参数，它把 function 计算结果结果继续和序列的下一个元素做累积计算。

::

  reduce(function, sequence[, initial]) -> value
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.

reduce() 的行为等价于： 

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def homo_reduce(func, seq):
      result = seq[0]
      for next in seq[1:]:
        result = func(result, next)
      return result

以下示例计算列表中所有数值的乘积。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  from functools import reduce
  total = reduce((lambda x, y: x * y), [1, 2, 3, 4])
  print(total)  
  
  >>>
  24

filter
~~~~~~~~~~~~~

::

  filter(function or None, iterable) --> filter object
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.

filter() 方法与 map() 类似，和 map()不同的是，filter() 把传入的函数依次作用于每个元素，然后根据返回值的真假决定保留还是过滤掉该元素。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  def homo_filter(func, seq):
  	  result = []
    	for x in seq:
          if func(x)
          	result.append(x)
      return result

下面的示例用于过滤空字符串：

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  strs = ['hello', ' ', 'world']
  ret = filter(lambda x : not x.isspace(), strs)
  print(type(ret))
  print(ret == iter(ret))
  print(list(ret))

  >>>
  <class 'filter'>
  True
  ['hello', 'world']

filter() 返回值是一个 filter 对象，它也是一个迭代器。filter() 还可以用于求交集：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  a = [4, 0, 3, 5, 7]
  b = [1, 5, 6, 7, 8]
  print(list(filter(lambda x: x in a, b)))
  
  >>>
  [5, 7]

.. _sorted_func:

sorted
~~~~~~~~~~~~~~

::

  sorted(iterable, *, key=None, reverse=False) --> new sorted list
    Return a new list containing all items from the iterable in ascending order.

sorted() 相对于列表自带的排序函数 L.sort() 具有以下特点：

- 将功能扩展到所有的可迭代对象。
- L.sort 直接作用在列表上，无返回，sortd() 则返回新的排序列表。
- sortd() 是稳定排序，且经过优化，排序速度更快。

排序的本质在于对两个需要排序的元素进行大小的比较，来决定位置的先后，对于数字和字符串类型比较好判断。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(sorted([5, 2, 3, 1, 4]))
  print(sorted((5, 2, 3, 1, 4)))
  print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})) # 字典默认使用键名排序
  
  # sorted() 返回列表类型，用它对字符串排序，注意类型转换
  print(''.join(sorted("hello")))
  >>>
  [1, 2, 3, 4, 5]
  [1, 2, 3, 4, 5]
  [1, 2, 3, 4, 5]
  ehllo

为 key 指定函数参数，该函数只能接受一个参数，它的返回值作为比较的关键字，比如忽略大小写排序：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  sorted_list = sorted("This is a test string from Andrew".split(), key=str.lower)
  print(sorted_list)
  
  >>>
  ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

对于复杂对象，我们可以把元素中的部分成员作为排序关键字：
  
.. code-block:: python
  :linenos:
  :lineno-start: 0

  scores = {'John': 15, 'Bill': 18, 'Kent': 12}
  new_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)
  print(new_scores)
  
  >>>
  [('Bill', 18), ('John', 15), ('Kent', 12)]

由于字典默认以 key 来迭代，对字典进行排序时，第一个参数要使用 dict.items() 来转化为 dict_items 对象。

如果要对自定义的类对象排序，可以选择某个对象成员，下面的示例使用年龄对学生进行排序：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  class Student():
      def __init__(self, name, grade, age):
          self.name = name
          self.grade = grade
          self.age = age
      def __repr__(self):
          return repr((self.name, self.grade, self.age))
  
  student_objects = [
          Student('john', 'A', 15),
          Student('jane', 'B', 12),
          Student('dave', 'B', 10),
      ]
  
  print(sorted(student_objects, key=lambda student: student.age))

  >>>
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]  

key 参数还可以指定 operator 模块提供的 itemgetter 和 attrgetter 方法。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  student_tuples = [ ('john', 'A', 15),
                     ('jane', 'B', 12),
                     ('dave', 'B', 10),]
  print(sorted(student_tuples, key=lambda student: student[2])) # age 排序
  
  from operator import itemgetter, attrgetter
  print(sorted(student_tuples, key=itemgetter(2))) # age 排序
  print(sorted(student_objects, key=attrgetter('age'))) 
  
  print(sorted(student_tuples, key=itemgetter(1,2))) # 先以 grade 排序，再以 age 排序
  print(sorted(student_objects, key=attrgetter('grade', 'age')))
  
  >>>
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
  [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

reverse 参数默认以升序排序，如果为 True 则以降序排序。更详细的介绍参考 `Python howto sorting <https://docs.python.org/3/howto/sorting.html>`_ 。

partial
~~~~~~~~

::

  partial(func, *args, **keywords) - new function with partial application
          of the given arguments and keywords.


一些函数提供多种参数，有时我们只需要改变其中的一些参数，而另一些参数只需要固定的值，那么每次都要把所有参数都补全是件繁琐的事情。
partial() 方法可以将一个函数的参数固定，并返回一个新的函数。

int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换，其中有一个 base 参数可以指定转换的进制。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(int('123'))
  print(int('123', base=8))
  print(int('a', base=16))
  print(int('101', base=2))

如果要转换大量的十六进制字符串，每次都传入 base = 16 就很繁琐，为了简便可以想到定义一个 hexstr2int() 的函数，默认把 base = 16 传进去：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def hexstr2int(x):
      return int(x, base=16)
  
  print(hexstr2int('a'))
  
  >>>
  10

functools.partial() 方法可以直接创建一个这样的函数，而不需要自己定义 hexstr2int():

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  from functools import partial
  hexstr2int = partial(int, base=16)
  print(hexstr2int('a'))
  
  print(type(hexstr2int))
  >>>
  10
  <class 'functools.partial'>

注意到它返回的是一个 functools.partial 类型，而不是一个普通的函数，它等价于定义了一个如下的函数：

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  def hexstr2int(x):
      args = (x)
      kwargs = {'base': 16}
      
      return int(*args, **kwargs)

如果我们不使用关键字参数，而是直接使用值，那么将作为位置参数传递给 int()，例如：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  hexstr2int = partial(int, 'a')

  #等价于
  def hexstr2int(x):
      args = ('a')
      kwargs = {'base': x}
      
      return int(*args, **kwargs)

如果一个函数有多个参数，那么就要区分这种参数的传递关系，我们看一个示例：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def func(a, b, c, d):
      print("a %d, b:%d c:%d, d:%d" %(a, b, c, d))
      return a * 4 + b * 3 + c * 2 + d

  part_func = partial(func, 1, d=4)
  part_func(2, 3)
  
  part_func = partial(func, b=1, d=4)
  part_func(2, c=3)
  
  part_func0 = partial(part_func, c=3) # 嵌套
  part_func0(2)
  
  >>>
  a 1, b:2 c:3, d:4
  a 2, b:1 c:3, d:4
  a 2, b:1 c:3, d:4

有些内置函数只有位置参数，没有关键字参数，如何实现定制函数呢？以 divmod() 为例，如果我们固定第一个参数，这很容易。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  tendivmode = partial(divmod, 10)
  
如果要固定第二个参数，就需要把 divmod() 内置方法的位置参数重定义为支持关键字传入的参数。例如：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def homo_divmod(a, b):
    return divmod(a, b)
  
  divmod10 = partial(homo_divmod, b=10)

使用 partial() 的目的是为简化代码，让代码简洁清晰，但也要注意到它的副作用，由于它返回 functools.partial 类型，隐藏了某些逻辑，比如新函数没有函数名，让跟踪更困难。

作用域和闭包
---------------

在程序设计中变量所能作用的范围被称为作用域（scope），在作用域内，该变量是有效的，可以被访问和使用。

在介绍 Python 的作用域之前，先看一个名为 globals() 的内建函数。它返回当前运行程序的所有全局变量，类型为字典。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  print(type(globals()))
  print(globals())

  >>>
  <class 'dict'>
  {'__loader__': <_frozen_importlib.SourceFileLoader object at 0xb72acbac>, 
   '__name__': '__main__', '__package__': None, '__builtins__': <module 'builtins' (built-in)>, 
   '__file__': './scope.py', '__spec__': None, 'dict0': {...}, '__doc__': None, '__cached__': None}

块作用域
~~~~~~~~~~~~~

在代码块中定义的变量，它的作用域通常只在代码块中，这里测试下 Python 是否支持块作用域。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  dict0 = globals()
  print(len(dict0))
  print(dict0.keys())
  
  while True:  # 在代码块中定义 block_para
      block_var = "012345"
      break
  
  print(block_var)
  dict0 = globals()
  print(len(dict0))
  print(dict0.keys())
  
  >>>
  012345
  9
  dict_keys(['__file__', '__spec__', '__builtins__', '__package__', 
            '__cached__', 'dict0', '__name__', '__loader__', '__doc__'])
  10
  dict_keys(['__file__', '__spec__', '__builtins__', '__package__', '__cached__', 
            'dict0', 'block_var', '__name__', '__loader__', '__doc__'])

从示例中，可以看出在 Python 中，在代码块结束后依然可以访问块中定义的变量，块作用域是不存在。代码块中的定义的变量的作用域就是代码块所在的作用域。默认就是全局作用域。在 globals() 的返回值中可以看到在代码块执行后，全局变量中出现了 block_var，为简便起见，这里只打印了全部变量名。

局部作用域
~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def foo():
      local_var = 0
  
  foo()
  print('local_var' in globals())  
  print(local_var)
  
  >>>
  False
  NameError: name 'local_var' is not defined

即便执行了函数 foo()，local_var 实际上也分配过内存，执行依然报错，所以 local_var 的作用域也只是在函数内部，函数结束时，局部变量所占的资源就被释放了，外部无法再访问。

实际上，Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）不会引入新的作用域。

作用域链
~~~~~~~~~~~~~

是否可以在函数中定义新的子函数，并调用子函数中呢？事实上，在 Python 中函数作为对象存在，函数可以作为另一个函数的参数或返回值，也可以在函数中嵌套定义函数。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def outer():
      var0, var1 = "ABC", "DEF"
      
      def inner():
          var0 = "abc"
          local_var = "123"
          
          print(var0)
          print(var1)
          print(local_var)
      
      print(var0)
      inner()
      
  outer()
  # inner() 这里调用 inner()将报未定义错误
  >>>
  ABC
  abc
  DEF
  123

内部函数只可以在包含它的外部函数中使用，也即它是局部的，相对于外部函数来说，内部函数是嵌入进来的，所以又被称为内嵌函数。从运行结果，可以得知：

- 内嵌函数中定义的变量只可在内嵌函数内使用
- 内嵌函数中可以访问外部函数定义的变量，如果内嵌函数中定义的变量与外部函数中变量重名，那么内嵌函数的作用域优先级最高。

变量的查找过程就像一条单向链一样，逐层向上，要么找到变量的定义，要么报错未定义。这种作用域机制称为作用域链。

.. _func_as_return:

函数作为返回值
~~~~~~~~~~~~~~~~~~~~

函数名实际上就是一个变量，它指向了一个函数对象，所以可以有多个变量指向一个函数对象，并引用它。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def foo():
      return abs
  
  myabs = foo()
  print(myabs(-1))

  >>>
  1

以上示例直接把系统内建函数 abs() 作为返回值赋值给 myabs 变量，所以 myabs() 等价于 abs()。为了深入理解 Python 是如何处理函数作为返回值的，再看一个更复杂的例子。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  flist = [] 
  for i in range(3): 
      def foo(x): 
          print(x + i) 
      flist.append(foo)
  
  for f in flist: 
      f(1)
      
  >>>
  3
  3
  3

按照预期，程序应该输出 1 2 3，然而却得到 3 3 3，这是因为以下两点：

- Python 中没有块作用域，当循环结束以后，循环体中的临时变量 i 作为全局变量不会销毁，它的值是 2。
- Python 在把函数作为返回值时，并不会把函数体中的全局变量替换为实际的值，而是原封不动的保留该变量。

flist 列表中的函数等价于如下的函数实现：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def flist_foo(x):
      global i
      print(x + i)

如果我们想要得到预期的效果，那么就要让全部变量变成函数内部的局部变量，把 i 作为参数传递给函数可以完成这一转换。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  flist = [] 
  for i in range(3): 
      def foo(x, y = i):
          print(x + y) 
      flist.append(foo)
  
  for f in flist: 
      f(1)

  >>>
  1
  2
  3

闭包函数
~~~~~~~~~~

闭包（closure）在 Python 中可以这样解释：如果在一个内部函数中，对定义它的外部函数的作用域中的变量（甚至是外层之外，只要不是全局变量，也即内嵌函数中还可以嵌套定义内嵌函数）进行了引用，那么这个子函数就被认为是闭包。所以我们上面例子中的 inner() 函数就是一个闭包函数，简称为闭包。

闭包具有以下两个显著特点，可以认为闭包 = 内嵌函数 + 内嵌函数引用的变量环境：

- 它是函数内部定义的内嵌函数。
- 它引用了它作用域之外的变量，但非全局变量。

如果我们将闭包作为外部函数的返回值，然后在外部调用这个闭包函数会怎样呢？

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def offset(n):
      base = n

      def step(i):
          return base + i
      
      return step

  offset0 = offset(0)
  offset100 = offset(100)
  
  print(offset0(1))
  print(offset100(1))

  >>>
  1
  101

按照常规分析，第一次调用 offset(0) 时，base 的值是 0，第二次调用 offset(100)后，base 的值应该变为 100，但是执行结束后，base 作为局部变量应该被释放了，也即不能再被访问了，然而结果却并非如此。

实际上在 Python 中，当内嵌函数作为返回值传递给外部变量时，将会把定义它时涉及到的引用环境和函数体自身复制后打包成一个整体返回，这个整体就像一个封闭的包裹，不能再被打开修改，所以称为闭包很形象。

对于上例中的 offset0 来说，它的引用环境就是变量 ``base = 0`` ，以及建立在引用环境上函数体 `` base + i `` 。 引用 offset0() 和执行下面的函数是等价的。 

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def offset0(i):
      base = 0

      return base + i

四种作用域
~~~~~~~~~~~~~

Python 的作用域一共有4种，分别是：

- L （Locals）局部作用域，或作当前作用域。
- E （Enclosing）闭包函数外的函数中
- G （Globals）全局作用域
- B （Built-ins）内建作用域

Python 解释器查找变量时按照 L –> E –> G –>B 作用域顺序查找，如果在局部作用域中找不到该变量，就会去局部的上一层的局部找（例如在闭包函数中），还找不到就会去全局找，再者去内建作用域中查找。

上面的示例已经涉及到前三种作用域，下面的示例对内建作用域进行验证。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def globals():
      return "from local globals()"
  
  print(globals())
  
  >>>
  from local globals()

系统内建的函数 globals() 被我们自定义的同名函数“拦截”，显然如果我们没有在全局作用域中定义此处的 globals()，则会去内建作用域中查找。

作用域同名互斥性
~~~~~~~~~~~~~~~~~~~

所谓作用域的同名互斥性，是指在不同的两个作用域中，若定义了同名变量，那么高优先级的作用域中不能同时访问这两个变量，只能访问其中之一。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  var = 0
  def foo():
      var = 1     # 定义了局部变量 var
      print(var)
      
      global var
      print(var)
  
  >>>
      global var
      ^
  SyntaxError: name 'var' is used prior to global declaration

global 声明 var 是全局变量，也即 global 可以修改作用域链，当访问 var 变量时而直接跳转到全局作用域查找, 错误提示在本语句前变量名 var 已经被占用了。所以函数体内的局部作用域内，要么只使用局部变量 var，要么在使用 var 前就声明是全局变量 var。

与以上示例类似，在内嵌函数中，也具有同样的特性，以下代码是在 Python 中使用闭包时一段经典的错误代码。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  def foo(): 
      a = 0
      def bar():
          a = a + 1  # 或 a += 1
          return a
      
      return bar
  
  c = foo()
  print(c())

  >>>
      a = a + 1
  UnboundLocalError: local variable 'a' referenced before assignment

以上代码并未如预期打印出来数字 1。根据闭包函数的机制进行分析，c 变量对应的闭包包含两部分，变量环境 ``a = 0`` 和函数体 ``a = a + 1``。
问题出在，函数体中的变量 a 和变量环境中的 a 不是同一个。

Python 语言规则指定，所有在赋值语句左边的变量名如果是第一次出现在当前作用域中，都将被定义为当前作用域的变量。由于在闭包 bar() 中，变量 a 在赋值符号 "=" 的左边，被 Python 认为是 bar() 中的局部变量。再接下来执行 c() 时，程序运行至 a = a + 1 时，因为先前已经把 a 定义为 bar() 中的局部变量，由于作用域同名互斥性，右边 a + 1 中的 a 只能是局部变量 a，但是它并没有定义，所以会报错。

引用 c() 和执行下面的函数是等价的。 

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def c():
      a = 0
      
      local_a = local_a + 1 
      return local_a

nonlocal 声明
~~~~~~~~~~~~~~~~~

与 global 声明类似，nonlocal 声明可以在闭包中声明使用上一级作用域中的变量。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def foo(): 
      a = 0
      def bar():
          nonlocal a
          a += 1  
          return a  
      
      return bar
  c = foo()
  print(c())
  print(c())
  
  >>>
  1
  2

使用 nonlocal 声明 a 为上一级作用域中的变量 a，就解决了该问题，可以实现累加了。注意 nonlocal 关键字只能用于内嵌函数中，并且外层函数中定义了相应的局部变量，否则报错。

由闭包到装饰器
----------------

闭包和变量
~~~~~~~~~~~~~

尽管闭包函数可以引用外层函数中的变量，但是这个变量不能被动态改变。

在 :ref:`func_as_return` 一节中，已经看到 Python 在把函数作为返回值时，并不会把函数体中的全局变量替换为实际的值，而是原封不动的保留该变量。那么当这种情况出现在闭包中会怎样呢？

.. code-block:: python
  :linenos:
  :lineno-start: 0

  def fun():
      flist = []
      for i in range(3):
          def foo(x):
              print(x + i, end=' ')
              
          flist.append(foo)
      return flist
  
  flist = fun()
  for f in flist: 
      f(1)

  >>>
  3 3 3

结果是一样的，如果一个变量已被闭包函数引用，那么就要保证这个变量不会再被改变，否则闭包函数的行为将难以预知。除了 for 循环以外，while 循环也会导致相同问题，改进方法也一样，不再赘述。

装饰器的引入
~~~~~~~~~~~~~

在 Python 中，闭包函数最多的应用就是装饰器（Decorator）。 一个简单的日志生成的例子：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def func(n):
      print("from func(), n is %d!" % (n), flush=True)

已经存在了函数 func()，现在有一个新的需求，希望可以记录下函数的执行日志，我们可以在函数中添加一行记录日志的代码，但是如果有很多函数，这样做会费时费力，且代码重复冗长。一个容易想到的办法是重新定义一个日志函数，在调用完函数后，记录日志。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def log(func):
      func(0)
      logging.debug('%s is called' % func.__name__)
  
  log(func)
  
  >>>
  from func(), n is 0!
  DEBUG:root:func is called

然而这样并不能彻底解决问题，对需要记录日志的函数的每一处调用都要调用新函数 log()，如果要取消日记记录，就要重新做一遍代码撤销的工作。这里就引入了装饰器。

装饰器
----------

从装饰的实现方式上可以分为装饰器函数和装饰器类，也即分别使用函数或者类对其他对象（通常是函数或者类）进行封装（装饰）。

装饰器函数
~~~~~~~~~~~~

无参装饰器
``````````````

使用函数作为装饰器的方法如下：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def log(func):
      def wrapper(*args, **kwargs):
          ret = func(*args, **kwargs)
          logging.debug('%s is called' % func.__name__)
          return ret
      return wrapper
  
  func = log(func)
  func(0)
  
  >>>
  from func(), n is 0!
  DEBUG:root:func is called
  
上面代码中的 wrapper() 是一个闭包，它的接受一个函数作为参数，并返回一个新的闭包函数，这个函数对传入的函数进行了封装，也即起到了装饰的作用，所以包含了闭包的函数 log() 被称为装饰器。运用装饰器可以在函数进入和退出时，执行特定的操作，比如插入日志，性能测试，缓存，权限校验等场景。有了装饰器，就可以抽离出大量与函数功能无关的重复代码。

上面的写法还是不够简便，Python 为装饰器专门提供了语法糖 @ 符号。无需在调用处修改函数时候，只需要在定义前一行加上装饰器。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  @log   # 添加装饰器 log()        
  def func2(n):
      print("from func2(), n is %d!" % (n), flush=True)
  
  func2(0)
  
  >>>
  from func2(), n is 0!
  DEBUG:root:func2 is called

以上语句相当于执行了如下操作：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  func2 = log(func2)
  func2(0)

关于装饰器是如何把参数传递给不同函数的，请参考 :ref:`var_pass_methods` 小结。

含参装饰器
``````````````

为了让装饰器可以带参数，需要在原装饰器外部再封装一层，最外层出入装饰器参数，内存传入函数的引用。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def log(level='debug'):
      def decorator(func):
          def wrapper(*args, **kwargs):
              ret = func(*args, **kwargs)
              if level == 'warning':
                  logging.warning("{} is called".format(func.__name__))
              else:
                  logging.debug("{} is called".format(func.__name__))
              return ret
          return wrapper
      return decorator
  
  @log(level="warning") # 添加带参数的装饰器 log()
  def func(n):
      print("from func(), n is %d!" % (n), flush=True)
  
  func(0)
  
  >>>
  from func(), n is 0!
  WARNING:root:func is called

以上语句相当于执行了如下操作：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  func = log('warning')(func)
  func()
  
由于装饰器 log() 已经设置了默认参数，所以如果不需要传递参数给装饰器，那么直接使用 ``@log`` 即可。

类方法装饰器
``````````````

类方法的函数装饰器和函数的函数装饰器类似。对于类方法来说，都有一个默认的形数 self，所以在装饰器的内部函数 wrapper 中也要传入该参数，其他的用法和函数装饰器相同。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  import time
  def decorator(func):
      def wrapper(self, *args, **kwargs):
          start_time = time.time()
          ret = func(self, *args, **kwargs)
          end_time = time.time()
          print("%s.%s() cost %f second!" % (self.__class__, 
                func.__name__, end_time - start_time))
          return ret
      return wrapper
  
  class TestDecorator():
      @decorator 
      def mysleep(self, n):
          time.sleep(n)
  
  obj = TestDecorator()
  obj.mysleep(1)

  >>>
  <class '__main__.TestDecorator'>.mysleep() cost 1.000091 second!

类方法装饰如要需要传入参数，请参考含参装饰器，只要再封装一层即可。

.. _decorator_class:

装饰器类
~~~~~~~~~

.. _nopara_decorator_class:

无参装饰器类
``````````````

以上介绍了函数作为装饰器去装饰其他的函数或者类方法，那么可不可以让一个类发挥装饰器的作用呢？答案是肯定的。
而且，相比装饰器函数，装饰器类具有更大灵活性，高内聚，封装性特点。

装饰器类必须定义 __call__() 方法，它将一个类实例变成一个用于装饰器的方法。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class Tracer():
      def __init__(self, func):
          self.func = func
          self.calls = 0
      def __call__(self, *args, **kwargs):
          self.calls += 1
          print("call %s() %d times" % (self.func.__name__, self.calls))
          return self.func(*args, **kwargs)
  
  @Tracer
  def test_tracer(val, name="default"):
      print("func() name:%s, val: %d" % (name, val))
  
  for i in range(2):
      test_tracer(i, name=("name" + str(i)))
    
  >>>
  call test_tracer() 1 times
  func() name:name0, val: 0
  call test_tracer() 2 times
  func() name:name1, val: 1

装饰器类不能用于装饰类的方法，因为 __call__() 的第一个参数必须传递装饰器类 Tracer 的实例。

.. _para_decorator_class:

带参数装饰器类
``````````````

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class Tracer():
      def __init__(self, arg0): # 可支持任意参数
          self.arg0 = arg0
          self.calls = 0
      def __call__(self, func):
          def wrapper(*args, **kwargs):
              self.calls += 1
              print("arg0:%d call %s() %d times" % (self.arg0, func.__name__, self.calls))
              return func(*args, **kwargs)
          return wrapper
      
  @Tracer(arg0=0)
  def test_tracer(val, name="default"):
      print("func() name:%s, val: %d" % (name, val))
  
  for i in range(2):
      test_tracer(i, name=("name" + str(i)))
  
  >>>
  arg0:0 call test_tracer() 1 times
  func() name:name0, val: 0
  arg0:0 call test_tracer() 2 times
  func() name:name1, val: 1

装饰器类的参数需要通过类方法 __init__() 传递，所以被装饰的函数就只能在 __call__() 方法中传入，为了把函数的参数传入，必须在 __call__() 方法中再封装一层。

类装饰器
~~~~~~~~~~~

所谓类装饰器，就是对类进行装饰的函数或者类。从装饰器的本质，我们知道，一个对函数进行装饰的装饰器函数，它的语法糖被解释的时候，默认转换为如下形式：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  @decorator
  def func():
      ......
   
  func = decorator(func)
  func()

如果使用装饰器类，则进行如下转换：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class decorator():
      .....
      
  @decorator
  def func():
      ......
  
  instance = decorator(func)
  func = instance.__call_()
  func()
  
所以装饰一个函数，就是对函数进行封装，就要把被装饰的函数传递给装饰器，如果要装饰一个类，那么就要把类传递给装饰器。

使用函数装饰类
````````````````

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class DotClass():
          pass
  
  def class_add_method(Class):
      Class.x, Class.y = 0, 0
      def move(self, a, b):
          self.x += a
          self.y += b
          print("Dot moves to (%d, %d)" % (self.x, self.y))
      
      Class.move = move
      return Class
  
  DotClass = class_add_method(DotClass)
  dot = DotClass()
  dot.move(1, 2)

  >>>
  Dot moves to (1, 2)

DotClass 类原本是一个空类，既没有成员变量也没有方法，我们使用函数动态的为它添加类成员 x 和 y，以及类方法 move()，唯一要注意的是 move() 方法第一个参数一定是 self，在类对象调用它时，它对应实例自身。

可以看到上面的行为很像装饰器的过程，我们使用语法糖 @ 来测试下，是否如预期一样：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  @class_add_method
  class DotClass():
          pass
  
  dot = DotClass()
  dot.move(1, 2)
  
  >>>
  Dot moves to (1, 2)

以上示例我们只是为类安装了参数和方法，返回原来的类，我们也可以定义一个新类，并返回它。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def class_add_method_new(Class):        # @语句处调用
      class Wrapper():
          def __init__(self, *args):      # 创建实例时调用
              self.wrapped = Class(*args) # 调用 DotClass.__init__
  
          def move(self, a, b):
              self.wrapped.x += a
              self.wrapped.y += b
              print("Dot moves to (%d, %d)" % (self.wrapped.x, self.wrapped.y))
          
          def __getattr__(self, name):    # 对象获取属性时调用
              return getattr(self.wrapped, name)
  
      return Wrapper
  
  @class_add_method_new
  class DotClass():           # DotClass = class_add_method_new(DotClass)
      def __init__(self):     # 在 Wrapper.__init__ 中调用
          self.x, self.y = 0, 0
  
  dot = DotClass()            # dot = Wrapper()
  dot.move(1, 2)              
  print(dot.x)                # 调用 Wrapper.__getattr__ 

  >>>
  Dot moves to (1, 2)
  1

示例中，我们返回了一个新的类，要注意的是，新的初始化函数封装了对原来类的实例化调用，并在新增的方法中引用原来类中成员，此外由于新类并不感知被装饰类的成员，所以必须实现 __getattr__() 方法。

使用带参函数装饰类
````````````````````

原理与带参数的函数装饰器装饰函数一样，只需要再封装一层即可，不再赘述。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  def decorator(arg0=0):
      def class_add_method_new(Class):
          class Wrapper():
              ......
          return Wrapper
      
      return class_add_method_new
  
  @decorator(arg0=2)
  class DotClass():
  
  # @语句等价于
  decorator = decorator(2)
  DotClass = decorator(DotClass)

使用类装饰类
````````````````

参考 :ref:`nopara_decorator_class` 和 :ref:`para_decorator_class` 的实现，原理是一样的，这里不再赘述。无参类装饰器：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class Tracer():
      def __init__(self, Class):  # @语句处调用
          self.Class = Class
      
      def __call__(self, *args, **kwargs): # 创建实例时调用
          self.wrapped = self.Class(*args, **kwargs)
          return self
      
      def __getattr__(self, name): # 获取属性时调用
          return getattr(self.wrapped, name)

  @Tracer()
  class C():
    ......
  
支持参数的类装饰器：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class TracerP():
      def __init__(self, arg0):  # @语句处调用
          self.arg0 = arg0
      
      def __call__(self, Class):
          self.Class = Class
          def wrapper(*args, **kwargs): # 创建实例时调用
              self.wrapped = self.Class(*args, **kwargs)
              return self
          return wrapper
      
      def __getattr__(self, name): # 获取属性时调用
          return getattr(self.wrapped, name)

  @TracerP(arg0=1)
  class C():
    ......

注意使用装饰器的前提是为了更简便的实现功能，而不要为用而用，装饰器和被装饰的函数或类应该是各自功能内聚，没有耦合关系。否则应该考虑其他方式，比如类继承。
在选择装饰器时，也应遵循先易后繁的原则，在装饰器函数不能满足需求时，才使用装饰器类。

装饰器嵌套
~~~~~~~~~~~~

如果我们需要对一个函数既要统计运行时间，又要记录运行日志，如何使用装饰器呢？Python 函数或类也可以被多个装饰器修饰，也即装饰器嵌套（Decorator Nesting）。要是有多个装饰器时，这些装饰器的执行顺序是怎么样的呢？

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def markbold(f):
      return lambda: '<b>' + f() + '</b>'
  
  def markitalic(f):
      return lambda: '<i>' + f() + '</i>'
  
  @markbold
  @markitalic
  def markstr():
      return "Python"
  
  >>>
  <b><i>Python</i></b> 

可以看到按照 ``markbold(markitalic(markstr()))`` 的顺序执行，多个装饰器按照靠近被修饰函数或者类的距离，由近及远依次执行的。

装饰器副作用
~~~~~~~~~~~~~~

装饰器极大地复用了代码，但是一个缺点就是原函数的元信息不见了，比如函数的 docstring，__name__，参数列表。
这是一个严重的问题，当进行函数跟踪，调试时，或者根据函数名进行判断的代码就不能正确执行，这些信息非常重要。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def markitalic(f):
      return lambda: '<i>' + f() + '</i>'
  
  @markitalic
  def markstr():
      return "Python"
  
  print(markstr.__name__)
  
  >>>
  <lambda>

functools 模块中的 wraps 可以帮助保留这些信息。functools.wraps 本身也是一个装饰器，它把被修饰的函数元信息复制到装饰器函数中，这就保留了原函数的信息。

.. code-block:: python
  :linenos:
  :lineno-start: 0
   
  from functools import wraps
  def markitalic(f):
      @wraps(f)
      def wrapper():
          return '<i>' + f() + '</i>'
      return wrapper
  
  @markitalic
  def markstr():
      return "Python"
  
  print(markstr.__name__)
  
  >>>
  markstr

其实 functools.wraps 并没有彻底恢复所有函数信息，具体请参考第三方模块 wrapt。

.. _buildin_decorator:

内置装饰器
~~~~~~~~~~~~~

定义类静态方法
````````````````

``@staticmethod`` 装饰器将类中的方法装饰为静态方法，不需要创建类的实例，可以通过类名直接引用。实现函数功能与实例解绑。

静态方法不会隐式传入参数，不需要传入 self ，类似一个普通函数，只是可以通过类名或者类对象来调用。

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  class C():
      @staticmethod
      def static_method():
          print("This is a static method!")

  C.static_method()     # 类名直接调用

  c = C()        
  c.static_method()     # 类对象调用
  
  >>>
  This is a static method!
  This is a static method!

定义类方法
``````````````````````

``@classmethod`` 装饰器用于定义类方法，类方法和类的静态方法非常相似，只是会隐式传入一个类参数
。类方法被哪个类调用，就传入哪个类作为第一个参数进行操作。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  class C():
      @classmethod
      def class_method(cls):
          print("This is ", cls)
  
  class B(C):
    pass
  
  C.class_method()  # 类名直接调用
  c = C()
  c.class_method()  # 类对象调用
  
  B.class_method()  # 继承类调用
  
  >>>
  This is  <class '__main__.C'>
  This is  <class '__main__.C'>
  This is  <class '__main__.B'>

.. _property_decorator:

实例方法属性化
```````````````````

::

  property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

内置方法 property() 可以将类中定义的实例方法（对象方法）属性化，可以直接为成员赋值和读取，也可以定义只读属性。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class C():
      def __init__(self):
          self.__arg = 0
   
      def getarg(self):
          return self.__arg
   
      def setarg(self, value):
          self.__arg = value
   
      def delarg(self):
          del self.__arg
   
      arg = property(fget=getarg, fset=setarg, fdel=delarg, doc="'arg' property.")
  
  c = C()
  c.arg = 10        # 调用 setarg
  print(c.arg)      # 调用 getarg
  
  c.setarg(20)      # 调用 setarg
  print(c.getarg()) # 调用 getarg
  del c.arg         # 调用 delarg
  
如果不提供 fset 参数，则属性就变成只读的了。``@property`` 装饰器以更简单的方式实现了相同功能。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class C():
      def __init__(self):
          self.__arg = 0
      
      @property
      def arg(self):
          return self.__arg
      
      @arg.setter
      def arg(self, value):
          self.__arg = value
      
      @arg.deleter
      def arg(self):
          del self.__arg
  
  c = C()
  c.arg = 10
  print(c.arg)
  del c.arg

注意三个方法的命名必须相同，getter（prorperty() 中名为 fget）对应的方法总是用 "@property" 修饰，其他两个为方法名加上 ".setter" 和 ".deleter"，如果定义只读属性，不定义 setter 方法即可。
