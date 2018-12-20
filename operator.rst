operator
-----------------

Python 内建了 operator 和 functools 模块来支持函数式编程。

operator 将大部分的运算操作符（算术运算，逻辑运算，比较运算，in 关系等等）都定义了等价函数。例如加法运算：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  def add(a, b):
      "Same as a + b."
      return a + b

operator 模块提供的这类函数可以取代很多 lambda 匿名函数，让代码更简洁和易懂，下面是一个求阶乘的函数示例：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  def factorial(n):
      from functools import reduce
      return reduce(lambda x, y: x * y, range(1, n + 1))
  
  def factorial(n):
      from functools import reduce
      import operator
      return reduce(operator.mul, range(1, n + 1))

operator 除了定义了运算符等价函数，最重要的是它还定义了一组对象元素和属性的操作函数，它把属性访问转化成一个可调用（Callable）对象。

attrgetter
~~~~~~~~~~~~~

::

  attrgetter(attr, ...) --> attrgetter object
      Return a callable object that fetches the given attribute(s) from its operand.
 
attrgetter() 可以把对象属性转换为一个可调用对象，作为参数传递给其他函数，以实现批量处理。它等价于如下匿名函数：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  lambda obj, n='attrname': getattr(obj, n):

下面的示例批量获取一个类实例的 arg 属性值：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
    
  import operator
  class AttrObj():
     def __init__(self, arg):
          self.arg = arg
  
  objs = [AttrObj(i) for i in range(5)]
  ga = operator.attrgetter('arg')
  
  # 等价于 [getattr(i, 'arg') for i in objs] 
  vals = [ga(i) for i in objs] 
  print(vals) 

  >>>
  [0, 1, 2, 3, 4]

排序函数 :ref:`sorted_func` 参数 key 接受一个可调用对象，使用它的返回值作为排序关键字，示例中使用学生年龄排序：

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
          Student('John', 'A', 15),
          Student('Jane', 'B', 12),
          Student('Davie', 'B', 10),
      ]
  
  print(sorted(student_objects, key=operator.attrgetter('age')))
 
  >>>
  [('Davie', 'B', 10), ('Jane', 'B', 12), ('John', 'A', 15)]

attrgetter() 还可以传入多个属性，返回一个包含各个属性值的元组：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  ga = operator.attrgetter('age', 'name', 'grade')
  print([ga(i) for i in student_objects])
  
  >>>
  [(15, 'John', 'A'), (12, 'Jane', 'B'), (10, 'Davie', 'B')]

itemgetter
~~~~~~~~~~~~~~~~~

itemgetter() 把字典的键值访问转换为一个可调用对象。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  list0 = [dict(val = -1 * i) for i in range(4)]
  print(list0)
  
  ga = operator.itemgetter('val')
  print(ga(list0[0]))
  
  >>>
  [{'val': 0}, {'val': -1}, {'val': -2}, {'val': -3}]
  0

可以指定字典中的特定键值来对字典进行排序：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  print(sorted(list0, key=ga))
  
  >>>
  [{'val': -3}, {'val': -2}, {'val': -1}, {'val': 0}]

itemgetter() 也支持多个参数，同时传入多个键，返回一个元组：

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  list0 = [{'name':'John', 'age': 15, 'grade' : 'A'}, 
           {'name':'Jane', 'age': 18, 'grade': 'B'}]
  print(sorted(list0, key=operator.itemgetter('name', 'age')))
  
  >>>
  [{'name': 'Jane', 'age': 18, 'grade': 'B'}, {'name': 'John', 'age': 15, 'grade': 'A'}]

sorted() 根据元组进行排序，首先按名字排序，对于名字无法区分顺序的再按年龄排序。

methodcaller
~~~~~~~~~~~~~~~~~~

methodcaller() 将实例的方法转换为可调用对象，可以把实例作为参数。尽管使用 attrgetter() 也可以间接实现调用，但是没有 methodcaller() 直接和简单。例如：

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
      def print_name(self):
          print(self.name)
  
  # 采用 attrgetter 方式
  student = Student('John', 'A', 15)
  ga = operator.attrgetter('print_name')
  ga(student)()
  
  # 采用 methodcaller 方式
  mh = operator.methodcaller('print_name')
  mh(student)

  >>>
  John
  John

