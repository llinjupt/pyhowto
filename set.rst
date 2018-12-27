.. _set:

集合
================

可散列对象
----------------

如果一个对象实现了 __hash__ 方法和 __eq__ 方法，那么这个对象就是可散列的（Hashable），参考 :ref:`hashable` 。 

Python 提供的基本数据类型都是可散列的，比如数值型，str 和 bytes 。当元组包含的所有元素都是可散列类型时，元组也是可散列的。
对于列表和字典，由于它们的值是可以动态改变的，所以无法提供一个唯一的散列值来代表这个对象，所以是不可散列的。

可散列对象要求对象在整个生命周期，调用 __hash__() 方法都必须返回一致的散列值，散列值可以通过内置函数  hash(obj) 获取。

可散列特性让一个对象可以作为字典的 key（字典实际使用一个键的散列值作为 key），或者一个集合（set）的成员。

.. admonition:: 注意

  如果一个类型没有定义 __eq__()，那么它也不应该定义__hash__()，集合操作对成员进行重复比较时，首先查看 __hash_() 值是否相等，然后再分别使用两个对象的 __eq__() 比较，只有全部为真时，才认为是重复元素，如果没有实现对应方法则报错。

以下示例可已看出由于 a 和 b 的散列值都是 1，最终键 a 的值被键 b 的值覆盖。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  class HashableCls():
      def __eq__(self, b):
          return True
      
      def __hash__(self):
          return 1
  
  a = HashableCls()
  b = HashableCls()
  print(hash(a), hash(b))
  
  dict0 = {a : 1, b : 2}
  print(dict0[a], dict0[hash(a)])
  
  >>>
  1 1
  2 2

为了方便，我们那可以定义以下函数来判断一个对象是否为可散列的：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  def ishashable(obj):
      try:
          if obj.__hash__ and obj.__eq__:
              return True
      except:
          return False

集合特性
----------------------

集合（set）是一个无序且不重复的可散列的元素集合。具有以下特性：

- 集合成员可以做字典中的键。
- 和列表，元组，字典类型一样，集合支持用 in 和 not in 操作符检查成员。
- 由 len() 内建函数得到集合的基数（大小）。
- 支持 for 循环迭代集合的成员。但因集合本身是无序的，不可以进行索引或执行切片操作，也没有键（key）可用来获取集合中元素的值。

set 非常类似 dict，只是没有 value，相当于 dict 的 key 集合。

集合操作
----------------------

创建集合
~~~~~~~~~~~~~~~~~

::
  
  set() -> new empty set object
     set(iterable) -> new set object  

注意在创建空集合的时候只能使用 `s = set()`，s = {} 将创建空字典。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  s0 = set()        # 创建空集合
  s1 = {1, 2, 3, 4} # 创建非空集合  
  print(type(s0).__name__)
  print(s0, s1)
  
  >>>
  set
  set() {1, 2, 3, 4}

可以看到，打印集合输出的形式和打印字典一致的。空集合用 set() 表示，以防和空字典冲突。set() 方法可以接受一个可迭代对象，会自动去除重复元素：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  set0 = set('abbc')
  set1 = set([1, 2, 2, 3])
  set2 = set((1, 2, 3))
  set3 = set({"key0":'val0','key1':'val1'})
  
  print(set0, set1)
  print(set2, set3)

  >>>
  {'b', 'a', 'c'} {1, 2, 3}
  {1, 2, 3} {'key0', 'key1'}

添加和移除元素
~~~~~~~~~~~~~~~

添加指定元素
`````````````

add(obj) 方法用于添加新元素，一次只能添加一个，如果该元素已存在，则忽略。

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  set0 = set()
  set0.add('abc')
  set0.add('abc') # 忽略，不会报错
  
  print(set0)
  
  >>>
  {'abc'}

删除指定元素
`````````````

remove(obj) 删除一个指定元素，如果不存在报错。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  set0 = {'a', 'b'}
  print(set0.remove(1))

  >>>
  KeyError: 1

discard(obj) 删除一个指定元素，如果不存在，则忽略。

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  set0 = {'a'}
  set0.discard('a')
  set0.discard('a') # 忽略，不会报错
  
  print(set0)
  
  >>>
  set()

随机删除
`````````````

pop() 方法随机删除一个元素并返回，更新原集合。

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  s0 = {'a', 'b'}
  print(set0.pop())
  print(set0)
  
  >>>
  b
  {'a'}

清空集合
``````````````

clear() 方法清空集合中所有元素，清空后为空集合。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  set0 = {'a', 'b'}
  set0.clear()
  print(set0)
  
  >>>
  set()

浅拷贝
~~~~~~~~~

copy(set0) 浅拷贝 set0，返回新集合。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  s0 = {'a', 'b'}
  s1 = s0.copy()
  print(s1)
  
  >>>
  {'b', 'a'}

取差集
~~~~~~~~~~~~~~~

差集表示 set0 中存在，set1 中不存在的集合。

::

  difference(...)
      Return the difference of two or more sets as a new set.

set0.difference(set1) 可以对两个或多个集合取差集，不影响原集合，返回一个新集合。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
    
  set0 = {1, 2, 3}
  set1 = {3, 4, 5}
  diff = set0.difference(set1, {1})
  print(diff)
 
  >>>
  {2}

difference_update() 与 difference() 唯一不同在于取差集后，更新原集合，无返回。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  set0 = {1, 2, 3}
  set1 = {3, 4, 5}
  set0.difference_update(set1, {1})        
  print(set0)

  >>>
  {2}

合并不同项
~~~~~~~~~~~~

合并不同项又称为对称差集，指两个集合中不重复的元素集合，会移除两个集合中都存在的元素。

set0.symmetric_difference(set1) 合并 set0 和 set1 中的不同元素，返回新集合。

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  set0 = {'a', 'b'}
  set1 = set0.symmetric_difference({'b', 'c'})
  print(set1)
  
  >>>
  {'a', 'c'}

symmetric_difference_update() 更新原集合，无返回。

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  set0 = {'a', 'b'}
  set0.symmetric_difference_update({'b', 'c'})
  print(set0)

  >>>
  {'a', 'c'}


取并集
~~~~~~~~~~

set0.union(set1,set2...) 取两个或多个集合的并集，返回新集合，不更新原集合。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  set0 = {'a', 'b'}
  set1 = set0.union({1}, {2})
  print(set1)
   
  >>>
  {2, 1, 'b', 'a'}

set0.update(set1,set2...) 取并集，更新原集合，无返回。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  set0 = {'a', 'b'}
  set0.update({1}, {2})
  print(set0)

  >>>
  {2, 1, 'b', 'a'}

取交集
~~~~~~~~~~~

::

  intersection(...)
    Return the intersection of two sets as a new set.

intersection() 方法取两个或多个集合的交集，返回一个新的集合，不影响原集合。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  set0 = {1, 2, 3}
  set1 = {1, 4, 5}
  sect = set0.intersection(set1, {1})        
  print(sect)
  
  >>>
  {1}

intersection_update() 取交集，更新原集合，无返回。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  set0 = {1, 2, 3}
  set1 = {1, 4, 5}
  set0.intersection_update(set1, {1})        
  print(set0)
  
  >>>
  {1}

交集判定
~~~~~~~~~~

set0.isdisjoint(set1) 判定两个集合是否有交集，有返回 Flase，无则返回 True。

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  set0 = {1, 2, 3}
  set1 = {1, 4, 5}
  print(set0.isdisjoint(set1))
  print(set0.isdisjoint({0}))
  
  >>>
  False
  True

子集父集判定
~~~~~~~~~~~~~~~~

子集判定
```````````````

set0.issubset(set1)，判定 set0 是否为 set1 的子集，是返回 True，否则返回 False。

任何集合都是自身的子集，空集是任何集合的子集。

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  set0 = {1}
  print(set0.issubset({1, 2}))
  print(set().issubset({})) # 空集是任何集合的子集
  
  >>>
  True
  True

set0.issuperset(set1)，判定 set0 是否为 set1 的父集，是返回 True，否则返回 False。

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  set0 = {1}
  print(set0.issuperset({1, 2}))
  print(set().issuperset({}))
  
  >>>
  False
  True

frozenset
----------------

frozenset 是指冻结的集合，它的值是不可变的，一旦创建便不能更改，没有 add，remove 方法，支持集合的其他不更新自身的交并集操作。

普通集合是可变的，不是可散列的，冻结集合是可散列的，它可以作为字典的 key，也可以作为其它集合的元素。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  fset = frozenset('abc')
  print(type(fset).__name__)
  print(fset)
  
  >>>
  frozenset
  frozenset({'b', 'a', 'c'})

集合操作符
----------------

集合类型提供了一系列函数方法用于集合运算，它同时借用了一些操作符，比如位操作符来简化集合操作：

  ================== ========================= ================
  操作符             示例                      说明  
  ================== ========================= ================
  len(s)             len({1, 2}) =>2           集合元素数
  x in s             1 in {1,2} =>True         成员判定
  x not in s         1 not in {1,2} =>False    成员判定
  set <= other       {1,2} <= {1,2} => True    子集判定，等价于 {1,2}.issubset({1,2})  
  set < other        {1,2} < {1,2}  => False   真子集判定
  set >= other       {1,2} >= {1,2} => True    父集判定，等价于 {1,2}.issuperset({1,2})
  set > other        {1,2} > {1,2} => False    真父集判定
  set \| other \|... {1,2} \| {2,3} => {1,2,3}  并集，等价于 {1,2}.union({2,3})
  set \|= other\|... set \|= {2,3} => {1,2,3}   并集，等价于 {1,2}.update({2,3})
  set & other &...   {1,2} & {2,3} => {2}      交集，等价于 {1,2}.intersection({2,3})
  set &= other &...  set &= {2,3}              交集，等价于 {1,2}.intersection_update({2,3})
  set - other -...   {1,2} - {2,3} => {1}      差集，等价于 {1,2}.difference({2,3})
  set -= other\|...  set -= {2,3}              差集，等价于 {1,2}.difference_update({2,3})
  set ^ other        {1,2} ^ {2,3}    {1,3}    合并不同项，等价于 {1,2}.symmetric_difference({2,3})
  set ^= other       set ^= {2,3}              等价于 {1,2}.symmetric_difference_update({2,3})
  ================== ========================= ================

含有等于号 = 的表达式表示将结果更新到集合中，无返回。