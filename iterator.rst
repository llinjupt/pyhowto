生成器和迭代器
================

生成器
---------------

列表作为一个容器，其所占内存大小和元素个数成正比，也即每增加一个元素，那么内存中就要分配一块区域来存储它。我们看一个例子：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  import sys
  
  list0 = [1] * 100
  list1 = [1] * 1000000
  
  print(sys.getsizeof(list0))
  print(sys.getsizeof(list1))
  
  >>>
  864
  8000064

list1 列表元素个数是 list0 元素个数的 10000 倍，所占内存也大约大 10000 倍。

如果我们要处理更多元素，那么所占内存就呈线性增大，所以受到内存限制，列表容量是有限的。通常我们并不会一次处理所有元素，而只是集中在其中的某些相邻的元素上。所以如果列表元素可以用某种算法用已知量推导出来，就不必一次创建所有的元素。这种边循环边计算的机制，称为生成器（generator），生成器是用时间换空间的典型实例。

生成器通常由两种方式生成，用小括号()表示的生成器表达式（generator expression）和生成器函数（generator function）。

生成器表达式
~~~~~~~~~~~~~~~~

在生成列表和字典时，可以通过推导表达式完成。只要把推导表达式中的中括号换成小括号就成了生成器表达式。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [x * x for x in range(5)]
  print(list0)

  list_generator0 = (x * x for x in range(5))
  print(list_generator0)
  
  list_generator1 = (x * x for x in range(5000000))
  print(sys.getsizeof(list_generator0))
  print(sys.getsizeof(list_generator1))

  >>>
  [0, 1, 4, 9, 16]
  <generator object <genexpr> at 0x000002C7B9955B48>
  88
  88

显然生成器对象的大小不会因为生成元素的上限个数而增大，此外不能够像列表被打印出来，那么如何获取通过生成器获取每一个元素呢？ 借助 Python 内建方法 next()：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list_generator0 = (x * x for x in range(3))
  print(next(list_generator0))
  print(next(list_generator0))
  print(next(list_generator0))
  print(next(list_generator0)) # 触发 StopIteration 异常

  >>>
  0
  1
  4
  StopIteration

每次调用 next() 方法时，总是根据最后的值和生成器给出的生成方法来计算下一个值。直到最后一个元素，抛出 StopIteration 异常。generator 也是可迭代对象，通常不会使用 next() 来逐个获取元素，而是使用 for in，它自动在遇到 StopIteration 异常时结束循环。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list_generator0 = (x * x for x in range(3))
  print(isinstance(list_generator0, Iterable))
  for i in list_generator0:
      print(i)

  >>>
  True
  0
  1
  4

生成器函数
~~~~~~~~~~~~~~~~

通过生成器表达式来生成 generator 是有局限的，比如斐波那契数列用表达式写不出来，复杂的处理需要生成器函数完成。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def fibonacci(n):
      i, j = 0, 1
      
      while(i < n):
          print(i, end=' ')
          i, j = j, i + j
  
  fibonacci(5)
  print(type(fibonacci))
  >>>
  0 1 1 2 3 <class 'function'>
  
  
很容易写出打印斐波那契数列的函数，参数表示生成的元素个数。有时候我们不需要打结果一个个打印出来，而是要把这种推导算法封装起来，把 fibonacci() 函数变成一个生成器函数。只需要把 print 这一行替换为 ``yielb i`` 即可。

如果一个函数定义中包含 yield 表达式，那么这个函数就不再是一个普通函数，而是一个生成器函数。yield 语句类似 return 会返回一个值，但它会记住这个返回的位置，下次 next() 迭代就从这个位置下一行继续执行。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def fib_generator(n):
      i, j = 0, 1
      
      while(i < n):
          yield i
          i, j = j, i + j
  
  print(type(fib_generator))
  print(type(fib_generator(5)))
  
  >>>
  <class 'function'>
  <class 'generator'>

生成器函数并不是生成器，它运行返回后的结果才是生成器。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  generator = fib_generator(5)
  for i in generator:
      print(i, end=' ')
  
  >>>
  0 1 1 2 3 

生成器的本质
~~~~~~~~~~~~~~~~

任何一个生成器都会定义一个名为 __next__ 的方法，这个方法要在最后一个元素之后需抛出 StopIteration 异常。next() 函数的本质就是调用对象的 __next__()。这个方法要么返回迭代的下一项，要么引起结束迭代的异常 StopIteration，下面的示例揭示了生成器的本质。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  class FibGenerator():
      def __init__(self, n):
          self.__n = n
      
          self.__s0 = 0
          self.__s1 = 1
          self.__count = 0
      
      def __next__(self):  # 用于内建函数 next()
         if self.__count < self.__n:           
             ret = self.__s0    
             self.__s0, self.__s1 = self.__s1, (self.__s0 + self.__s1)
             self.__count += 1
  
             return ret
         else:
             raise StopIteration

      def __iter__(self):  # 用于 for 循环语句
         return self

  fg = FibGenerator(5)
  print(type(fg))
  print(isinstance(fg, Iterable))
  
  for i in fg:
      print(i, end=' ')
  
  >>>
  <class '__main__.FibGenerator'>
  True
  0 1 1 2 3 

示例中如果没有定义 __iter__() 方法则只能使用 next() 函数进行迭代，当它定义后，就可以使用 for 和 in 语句访问了，同时定义了这两种方法的对象称为迭代器（Iterator）。

迭代和迭代对象
---------------

在 Python 中通过 for in 对对象进行遍历的操作被称为迭代(Iteration)，可以进行迭代操作的对象被称为可迭代 （Iterable） 对象，例如字符串，列表和元组。如何判断一个对象是否可迭代呢？

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  from collections import Iterable
  
  print(isinstance(1, Iterable))
  print(isinstance('abc', Iterable))
  print(isinstance([1, 2, 3], Iterable))
  print(isinstance({'name': 'val'}, Iterable))

  print(isinstance(range(10), Iterable))
  print(type(range(10)))
  
  >>>
  False
  True
  True
  True
  True
  <class 'range'>

除了常见的基本数据类型是可迭代对象外，文件对象，管道对象以及更复杂的生成器等也是可迭代对象。

迭代器
-----------

可迭代对象和迭代器
~~~~~~~~~~~~~~~~~~~~

如 list、tuple、dict、set、str、range、enumerate 等这些可以直接用于 for 循环的对象称为可迭代（Iterable）对象，也即它们是可迭代的。但是生成器不但可以作用于 for 和 in 语句，还可以被 next() 函数不断调用并返回下一个值，直到最后抛出 StopIteration 错误，它是一个迭代器（Iterator）。

- 可迭代对象，需要提供 __iter__()方法，否则不能被 for 语句处理。
- 迭代器必须同时实现 __iter__() 和 __next__()方法，__next__() 方法包含了用户自定义的推导算法，这是迭代器对象的本质。生成器表达式和生成器函数产生生成器时，会自动生成名为 __iter__ 和 __next__ 的方法。参考 `Python 迭代对象 <https://docs.python.org/3/library/stdtypes.html#iterator-types>`_。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list_generator0 = (x * x for x in range(3))
  print('__iter__' in dir(list_generator0))
  print('__next__' in dir(list_generator0))
  
  fg = fib_generator(5)
  print('__iter__' in dir(fg))
  print('__next__' in dir(fg))
  
  >>>
  True
  True
  True
  True

如同判断对象是否可迭代一样，可以使用isinstance()判断一个对象是否是 Iterator 对象：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list_generator0 = (x * x for x in range(3))
  isinstance(list_generator0, Iterator)
  isinstance(list_generator0, Iterable)
  
  >>>
  True
  True

迭代对象类型判断
~~~~~~~~~~~~~~~~~~~~

另外一种方式是通过 iter() 函数来判断，这种方法是最准确的（可迭代对象并不一定是 Iterable 或者 Iterator 类的实例），后面会详解 iter()内建函数的作用。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # 判断可迭代对象
  def is_iterable(obj):
      status = True
      try:
        iter(obj)
      except TypeError: 
        status = False
  
    return status

  # 判断迭代器对象
  def is_iterator(obj):
    return is_iterable(obj) and obj is iter(obj)

由上述分析可知，只要一个对象是迭代器，那么它一定是可迭代对象，反过来不成立。

生成迭代器
~~~~~~~~~~~~~~~

iter() 内建方法可以把list、dict、str等可迭代对象转换成迭代器。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  list0 = [0, 1, 2]
  iter0 = iter(list0)
  
  print(type(iter0))

  >>>
  <class 'list_iterator'>

除字典外，一个对象只要实现了 __getitem__() 方法，就认为它是序列类型，序列类型总是可迭代的，循环作用在序列类型上的本质参考 :ref:`index_loop_access`。

对于序列类型，字典，还有更复杂的可迭代类型如 range，Python 内建了对应的迭代器对它们进行迭代操作，它们无需实现 __next__() 方法，iter() 函数会返回对应的内建迭代器。

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  print(type(iter("")))
  print(type(iter([])))
  
  print(type(iter({})))
  print(type(iter({}.values())))
  
  print(type(iter(range(5))))

  >>>
  <class 'str_iterator'>
  <class 'list_iterator'>
  <class 'dict_keyiterator'>
  <class 'dict_valueiterator'>
  <class 'range_iterator'>

需要强调，可迭代对象并不一定是 Iterable 或者 Iterator 类的实例，可以参考 :ref:`index_loop_access`。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  ......
  
  print(isinstance(rwstr, Iterator))
  print(isinstance(rwstr, Iterable))
  
  print(is_iterable(rwstr))
  print(is_iterator(rwstr))

  >>>
  False
  False
  True
  False
  
而对于迭代器类型来说，iter() 函数直接执行对象中的 __iter__()函数并返回，循环操作的实质如下所示：

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  for element in iterable:
      # do something with element

  # 等价于如下操作
  # create an iterator object from that iterable
  iter_obj = iter(iterable)
  
  # infinite loop
  while True:
      try:
          # get the next item
          element = next(iter_obj)
          # do something with element
      except StopIteration:
          # if StopIteration is raised, break from loop
          break

::
  
  iter(iterable) -> iterator
  iter(callable, sentinel) -> iterator

查看 iter() 函数定义，它的第二种用法比较特殊，如果提供了第二个参数 sentinel，那么第一个参数必须是一个可调用对象，比如函数。下面示例用于实现读取到指定的行：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # 读取到 SystemExit\n 的前一行
  with open('test.txt', 'r', encoding="utf-8") as fp:
      for line in iter(fp.readline, 'SystemExit\n'):
          print(line)          

  # 只处理 1 和 2
  list0 = [1, 2, 3]
  for i in iter(list0.pop, 3):
    print(i)

无限迭代器
~~~~~~~~~~~~~~

所谓无限迭代器，也即是没有限制，永不抛出 StopIteration 异常。下面是一个奇数生成器，可以无限制地生成奇数。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class OddIter:

      def __iter__(self):
          self.num = 1
          return self
  
      def __next__(self):
          num = self.num
          self.num += 2
          return num
  
  for i in OddIter():
      if i > 5:       # 处理无限生成器需要退出分支
          break
      print(i, end=' ')
  
  >>>
  1 3 5 
