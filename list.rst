列表处理
================

序列（sequence）是 Python 中最基本的数据结构之一。序列中的每个元素都分配一个整数数字来唯一确定它的位置，
又称为索引，第一个索引总是从0开始，第二个索引是1，依此类推。

Python有多个序列的内置类型，但最常见的是列表和元组，很多函数接受序列作为参数，比如 str.join()。

序列支持的操作包括索引，切片，加，乘，成员检查。此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表（list）作为序列类型之一是很常用的 Python 数据类型，它以一个方括号内的逗号分隔值出现，例如 [1, "abc"]。

列表的数据项不需要具有相同的类型。

创建列表变量
-----------------

直接创建列表
~~~~~~~~~~~~~

注意：列表的数据项不需要具有相同的类型。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  # 每个值可以取相同类型的数据 
  list0 = [0, 1, 2, 3, 4]        
  list1 = [1.0, 2.0, 3.0]
  list2 = ["12", "ab", "he"]
  
  # 也可以取不同类型的数据，每个元素可以为任意数据类型
  list3 = ["123", 1, 3.0, [1, 2], {"key": "val"}]
  list4 = [list0, list1]

  for i in range(5):
      print(eval("list" + str(i)))
  >>>
  [0, 1, 2, 3, 4]
  [1.0, 2.0, 3.0]
  ['12', 'ab', 'he']
  ['123', 1, 3.0, [1, 2], {'key': 'val'}]
  [[0, 1, 2, 3, 4], [1.0, 2.0, 3.0]]

由列表组合生成新列表
~~~~~~~~~~~~~~~~~~~~~~~~~~~

"+" 运算符实现列表的拼接。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  list0 = [0, 1, 2, 3, 4]
  list1 = ['a', "bc", 1] + list0
  print(list1)

  >>>
  ['a', 'bc', 1, 0, 1, 2, 3, 4]

"*" 运算符实现列表的重复。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  list0 = ['*'] * 5
  list1 = [1, 2] * 5
  print(list0)
  print(list1)

  >>>
  ['*', '*', '*', '*', '*']
  [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

列表推导
~~~~~~~~~~~~~~~~

迭代语句方便对单个列表元素进行处理得到新列表，被称为列表推导(list comprehension)，它是一种简化代码的方法。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  lista = [1, 2]
  listb = ["ab", "cd"]
  list0 = [x * 2 for x in lista]
  list1 = [x[1] for x in listb]
  list2 = [x + ".txt" for x in listb]
  
  for i in range(3):
      print(eval("list" + str(i)))
  
  >>>
  [2, 4]
  ['b', 'd']
  ['ab.txt', 'cd.txt']  

其他类型转换列表
~~~~~~~~~~~~~~~~~~~

list()内建函数实现其他类型向列表的转换。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  # 将字符串转换为每个字符组成额list
  list0 = list("abcdef")
  # 将元组转化为list类型
  list1 = list((1, 2, 3))
  
  # 将字典转换为 list，默认转换key到list，以下方式是等同的
  dic0 = {"key0": "val0", "key1": "val1"}
  list2 = list(dic0)
  list3 = list(dic0.keys())
  
  # 将字典的值转换为list
  list4 = list(dic0.values())   
  
  for i in range(5):
      print(eval("list" + str(i)))
  
  >>>
  ['a', 'b', 'c', 'd', 'e', 'f']
  [1, 2, 3]
  ['key0', 'key1']
  ['key0', 'key1']
  ['val0', 'val1']

zip 合并
~~~~~~~~~~

zip() 方法结合类型转换，可以巧妙的把两个链表中的元素一一对应成元组类型，生成新的元组列表。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = list(zip(['one', 'two', 'three'], [1, 2, 3]))
  print(list0)

  >>>
  [('one', 1), ('two', 2), ('three', 3)]
  
复制列表
~~~~~~~~~~~~~

与字符串类似，列表作为序列类型，支持切片复制。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  list0 = ["ab", "cd"]
  list1 = list0[:]
  print(list1)
  
  list1[0] = "AB"  # 改变 list1 不会影响 list0
  print(list0)
  print(list1)

  >>>
  ['ab', 'cd']
  ['ab', 'cd']
  ['AB', 'cd']

切片复制是一种浅拷贝，只复制父对象一级，子对象不复制，还是引用，列表的 L.copy() 方法与切片复制都是浅拷贝。
如果要完全复制，需要借助 copy 模块进行深拷贝。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [1, 2, [1, 2]]   
  list1 = list0.copy()   # 浅拷贝，与切片复制等同
  
  import copy            # 深拷贝，完全复制
  list2 = copy.deepcopy(list0) 
  
  list0[2][0] = "a"      # 不会改变深拷贝 list2
  for i in range(3):
      print("list%d:\t%s" % (i, eval("list" + str(i))))

  >>>
  list0:  [1, 2, ['a', 2]]
  list1:  [1, 2, ['a', 2]]
  list2:  [1, 2, [1, 2]]

访问列表中的值
----------------

下标直接访问
~~~~~~~~~~~~~~~~~

通过下标直接取列表的单个元素，返回元素原来对应的类型。

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  list0 = [1, 2, 3, [4, 5]]
  print(list0[0])    # 1
  print(list0[-1])   # 4
  print(type(list0[-1]))

  >>>
  1
  [4, 5]
  <class 'list'>

切片取子列表
~~~~~~~~~~~~~~~~~

切片操作，取部分连续元素，返回列表类型，即便只取到一个元素。

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  list0 = [1, 2, 3, 4]
  print(list0[0:1])  # [1]
  print(type(list0[0:1]))
  
  print(list0[0:-1]) # 去掉尾巴元素的列表 
  print(list0[1:])   # 去掉头元素的列表

  >>>
  [1]
  <class 'list'>
  [1, 2, 3]
  [2, 3, 4]

过滤特定的元素
~~~~~~~~~~~~~~~~~

通过filter()函数提取特定元素生成新列表。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # 提取长度大于3的字符串元素
  listc = ["abc", 123, "defg", 456]
  list0 = list(filter(lambda s:isinstance(s, str) and len(s) > 3, listc))
  print(list0)
  
  >>>
  ['defg']

列表统计
------------------

统计元素个数
~~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [1, 1, 2, [2, 3]]
  print(len(list0))     
  
  >>>
  4

统计元素出现次数
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [1, 1, 2, [2, 3]] # 注意 [2, 3] 是一个列表元素
  print(list0.count(2))
  
  >>>
  1

统计列表不同元素数
~~~~~~~~~~~~~~~~~~~

通过集合 set() 方法求交集。

注意：元素不能为复杂数据类型，比如列表，字典等。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [1, 1, 2, "abc"]
  set0 = set(list0)
  print(list(set0))
  
  >>>
  [1, 2, 'abc']

统计最大最小值
~~~~~~~~~~~~~~~~

max() 和 min() 方法可以得到列表中的最大和最小值。

注意：列表中元素必须均为数值，否则需要先转换为数值。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [1, 1, 2, 3.0]
  print(max(list0)) 
  print(min(list0)) 
  
  >>>
  3.0
  1

列表排序和反向
----------------

列表排序
~~~~~~~~~~~

``L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*``

sort()函数直接对列表执行排序，无返回。注意：列表中元素类型必须相同。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # 正序排列，直接对list操作
  list0 = ['c1', 'b2', 'a0', 'd3']
  list0.sort(reverse=False)   
  print(list0)             
  
  >>>
  ['a0', 'b2', 'c1', 'd3']
  
  # 逆序排列
  list0.sort(reverse=True) 
  print(list0) 
  
  >>>
  ['d3', 'c1', 'b2', 'a0']

  # 可以指定key函数进行更复杂的排序
  list0.sort(key=lambda x:x[1]) 
  print(list0)
  
  >>>
  ['a0', 'c1', 'b2', 'd3']

列表反向
~~~~~~~~~

``L.reverse() -- reverse *IN PLACE*``

reverse()方法反向列表，元素颠倒。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  list0 = [1, 2, 3, 4, ['a', 'b']]
  list0.reverse()  
  print(list0)
  
  >>>
  ['a', 'b'], 4, 3, 2, 1]

字符串可以借助列表反向函数，实现反向。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  list0 = list("0123456")
  list0.reverse()
  print(''.join(list0))
  
  >>>
  6543210

列表元素插入和扩展
----------------------

索引位置插入
~~~~~~~~~~~~~~

``L.insert(index, object) ->None -- insert object before index``

在指定索引位置插入对象，其余元素后移，直接操作无返回。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [0, 1, 2, 3]
  list0.insert(2, 88) 
  print(list0) 

  # 如果索引超出list长度，则直接插入结尾
  list0.insert(len(list0) + 1, [100, 101])
  print(list0)
  
  >>>
  [0, 1, 88, 2, 3]
  [0, 1, 88, 2, 3, [100, 101]]

尾部追加
~~~~~~~~~~~~~~

尽管通过 list.insert(len(list), object) 实现尾部追加，为了高效处理，Python
提供了专门的尾部追加函数 append()

``L.append(object) -> None -- append object to end``

append() 方法在列表尾部追加，直接操作无返回，参数作为整体插入为1个元素。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [0, 1, 2, 3]
  list0.append([99,100])
  print(list0)
  
  >>>
  [0, 1, 2, 3, [99, 100]]

``L.extend(iterable) -> None -- extend list by appending elements from the iterable``

列表的extend()方法可以接受一个迭代对象，并把所有对象逐个追加到列表尾部。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [0, 1, 2, 3]
  list0.extend(["a", "b"])
  print(list0) 
  
  list0.extend("123")
  print(list0) 
  
  >>>
  [0, 1, 2, 3, 'a', 'b']
  [0, 1, 2, 3, 'a', 'b', '1', '2', '3']

列表元素的删除
---------------

根据索引删除
~~~~~~~~~~~~~~

del()函数根据索引删除元素，支持切片操作，直接作用在列表上，无返回。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [1, 2, 2, 3, 4]
  del(list0[0])    # 直接作用在list上
  print(list0)
     
  del(list0[0:3])  # 支持切片移除
  print(list0)

  >>>
  [2, 2, 3, 4]
  [4]

根据索引删除并返回元素
~~~~~~~~~~~~~~~~~~~~~~~~~~

``L.pop([index]) -> item -- remove and return item at index (default last).``
    ``Raises IndexError if list is empty or index is out of range.``
    
list的pop()方法删除指定索引元素并返回它，与append()配合可以实现队列或者堆栈。
如果索引超出范围，抛出 IndexError 异常。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [[1, 2], 2, 3, 4]
  print(list0.pop()) # 默认参数index=-1，也即移除最后一个元素
  print(list0.pop(0))
  print(list0)        

  >>>
  4
  [1, 2]
  [2, 3]

根据元素值删除元素
~~~~~~~~~~~~~~~~~~~~~~~~~~

``L.remove(value) -> None -- remove first occurrence of value.``
    ``Raises ValueError if the value is not present.``
    
remove()函数移除第一个匹配value值的元素，无返回。如果元素不存在，抛出 ValueError 异常。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  list0 = [1, 2, 2, 3, 4]
  list0.remove(2)     
  print(list0)

  >>>
  [1, 2, 3, 4]

元素索引和存在判定
-------------------------

获取元素索引
~~~~~~~~~~~~~~~~

``L.index(value, [start, [stop]]) -> integer -- return first index of value.``
    ``Raises ValueError if the value is not present.``

index()方法可以在指定范围获取第一个匹配值的索引。如果值不存在则抛出 ValueError 异常。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [1, 2, 2, 4]
  print(list0.index(2))      # 返回第一个匹配值2的元素索引
  print(list0.index(2, 2, 3))# 在list[2:3 + 1]中查找第一个匹配2的元素索引
  
  >>>
  1
  2

判断元素是否存在
~~~~~~~~~~~~~~~~~~

判断某元素是否存在使用 in 运算符；not in 运算符判断不存在，语句结果是布尔量。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [1, 2, 3, 5]
  if 5 in list0:
    print(list0.index(5))
  
  print(5 in list0)
  print(5 not in list0)
  
  >>>
  3
  True
  False

也可以通过 index() 方法捕获异常的方式判定元素是否存在。

列表比较
----------

直接使用比较运算符
~~~~~~~~~~~~~~~~~~~

比较运算费，又称为关系运算符，远算结果为布尔值。包括以下几种：

  ========= ===================================  ===============================
  运算符                   描述                              实例
  ========= ===================================  ===============================
  ==	      等于 - 比较对象是否相等	             (a == b) 返回 False
  !=	      不等于 - 比较两个对象是否不相等	     (a != b) 返回 true
  >	        大于 - 返回a是否大于b                (a > b) 返回 true
  <	        小于 - 返回a是否小于b                (a < b) 返回 true
  >=	      大于等于 - 返回a是否大于等于b        (a >= b) 返回 False
  <=	      小于等于 - 返回a是否小于等于b        (a <= b) 返回 true
  ========= ===================================  ===============================
 
- == 和 != 运算符比较对象可以为任何不同的类型。
- 含有 > 和 < 的运算符，比较对象类型必须相同。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  list0, list1 = [123, 'xyz'], [123, 'abc']
  print(list0 > list1)
  print(list0 == list0)
  print(list0 == "123xyz")
  print(list0 != 123)
  print(list0 >= 123) # '>='不支持不同类型对象的比较
  
  >>>
  True
  True
  False
  True
  
使用用cmp()函数
~~~~~~~~~~~~~~~~~~~

注意：cmp()函数返回值为整型，已在3.0版本移除，它等价于 (a > b) - (a < b)。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print cmp(list0, list1)
  print cmp(list1, list0)
  print cmp(list1, list1)
  
  >>>
  1
  -1
  0  
  
使用 operator模块
~~~~~~~~~~~~~~~~~~~

operator模块提供的比较函数是运算符的另一种表达形式，它们之间是等价的。
比如 operator.lt() 函数与 a < b 是等价的。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  operator.lt(a, b)  # '<'
  operator.le(a, b)  # '<='
  operator.eq(a, b)  # '=='
  operator.ne(a, b)  # '!='
  operator.ge(a, b)  # '>'
  operator.gt(a, b)  # '>='

注意：还有一组带有下划线的函数，比如 operator.__lt__() 它们是为了向前兼容才保留的。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  import operator
  print(operator.eq(list0, list0))
  print(operator.lt(list1, 0)) # '<'不支持不同类型对象的比较
  
  >>>
  True