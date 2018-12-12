字典
================

字典是 Python 中内建的一种具有弹性储存能力的数据结构，可存储任意类型对象，与序列使用整数索引不同，它使用键(key)进行索引。

通常任何不变类型的对象均可作为索引，比如数字，字符串和元组，列表可以被修改，不可作为键。由于键作为索引使用，所以它必须是唯一的。

字典的每个键都有对应的值 (value)，键值对用冒号 ":" 分割，每个键值对之间用逗号 "," 分割，整个字典包括在花括号 {} 中。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {key0 : val0, key1 : value1}
 
创建和访问字典
----------------------

直接创建字典
~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0

  dict_empty = {} # 可以创建空字典
  
  key = 'abc'
  dict0 = {1: None,'abc': 1, (1, 2): "tuple key", key: "replaced"}
  print (dict0)
  print (dict0[1])
  print (dict0[key])
  print (dict0[(1,2)])

  >>>
  {1: None, 'abc': 'replaced', (1, 2): 'tuple key'}
  None
  replaced
  tuple key

可以看到如果，出现重复的键，比如这里的 'abc' ，则最后的一个键值会替换前面的，键对应的值可以是任意数据类型，
不同的键可以对应相同的值。

访问字典
~~~~~~~~~~~~~~~~

字典以键为索引访问对应的值，如果键不存在，抛出 KeyError ：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(dict0[2])
  
  >>>
    File "C:/Users/Red/.spyder/dictest.py", line 16, in <module>
      print (dict0[2])
  
  KeyError: 2

``D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.``

字典方法 D.get() 方法可以在键不存在时返回指定的值，如果不指定则默认返回 None 。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(dict0[2])
  print(dict0.get(2, "hello"))
  
  >>>
  None
  hello

间接创建字典
~~~~~~~~~~~~~~~~~~~

包含键值对的( key-value)序列，使用 dict() 进行类型转换。 

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  list0 = [('key0', 1), ('key2', None), (3, ['1', '2'])] # 可以是元组类型
  dict0 = dict(list0)
  print(dict0)
  
  >>>
  {'key0': 1, 'key2': None, 3: ['1', '2']}

通过参数对序列，也可以创建字典，但是关键字必须是字符串：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = dict(key0=1, key1="abc")
  print(dict0)

  >>>
  {'key0': 1, 'key1': 'abc'}
  
字典推导
```````````````

类似列表推导，字典推导(dict comprehension)，可以简化代码。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {x: x**2 for x in [1, 2, 3]}
  dict1 = {x: "/home/" + x + '.jpg' for x in ("pic0", "pic1")}
  print(dict0)
  print(dict1)

  >>>
  {1: 1, 2: 4, 3: 9}
  {'pic0': '/home/pic0.jpg', 'pic1': '/home/pic1.jpg'}

zip 合并
```````````

zip()函数名副其实，它的作用很像拉链，将两个列表合并成一个 zip 对象，dict() 可以把它转化为字典。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
  print(dict0)
  
  >>>
  {'one': 1, 'two': 2, 'three': 3}

由列表生成定值字典
````````````````````
::

   D.fromkeys(iterable, value=None, /) method of builtins.type instance
      Returns a new dict with keys from iterable and values equal to value.

D.fromkeys() 方法支持从迭代对象取键，并可指定值的字典。通常使用列表或者元组作为参数。

seq = ['key0', 'key1']
 
.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  seq = ['key0', 'key1']             # 也可为元组，字符串等可迭代对象
  dict0 = dict.fromkeys(seq)         # 字典所有值均为 None
  dict1 = dict.fromkeys(seq, 10)     # 字典所有值均为 10
  dict2 = dict.fromkeys(seq, [1, 2]) # 字典所有值均为 [1, 2]
  dict3 = dict.fromkeys('123', 10)   # 一次从字符串中取一个字符作为键
  
  for i in range(4):
      print("dict%d:\t%s" % (i, eval("dict" + str(i))))
  
  >>>
  dict0:  {'key0': None, 'key1': None}
  dict1:  {'key0': 10, 'key1': 10}
  dict2:  {'key0': [1, 2], 'key1': [1, 2]}
  dict3:  {'1': 10, '2': 10, '3': 10}

如果序列中出现重复成员，在生成的字典中它作为键只会出现一次。

字典操作
--------------------

键值添加和更新
~~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {}
  dict0['key0'] = "val0"  # 添加键值对
  print(dict0)
  
  dict0['key0'] = 123     # 更新键的值
  print(dict0)
  
  >>>
  {'key0': 'val0'}
  {'key0': 123}

键值不存在时更新
~~~~~~~~~~~~~~~~~~~

``D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D``

与直接对键赋值不同，D.setdefault() 方法可以在键存在时不做操作，而在键不存在时更新键值对。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {'key0': 'val0'}
  dict0['key1'] = 'val1' # 直接赋值
  print(dict0)
  
  dict0.setdefault('key1', "newval") # key1 存在，不做操作
  print(dict0)
  dict0.setdefault('key2', "newval") # key2 不存在，插入
  print(dict0)

  >>>
  {'key0': 'val0', 'key1': 'val1'}
  {'key0': 'val0', 'key1': 'val1'}
  {'key0': 'val0', 'key1': 'val1', 'key2': 'newval'}

更新键值对
~~~~~~~~~~~~~

D.update() 方法把一个迭代对象（通常为字典）中的键值对更新到当前字典中，如果键存在则覆盖。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  dict0 = {'key0': 'val0'}
  dict1 = {'key0': 0, "key1" : [1, 2]}  
  dict0.update(dict1)
  dict0.update([("name", "value")]) # 其他含键值对的可迭代对象

  # 即便释放 dict1 不影响 dict0 值，是完全复制
  del(dict1)        
  print(dict0)

  >>>
  {'key0': 0, 'key1': [1, 2], 'name': 'value'}

删除键值和清空字典
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {"key0" : "val0", "key1" : "val1"}
  del dict0['key0'] # 删除键值
  print(dict0)
  
  dict0.clear()     # 清空字典
  print(dict0)
  
  del(dict0)        # 删除dict0变量，释放资源
  print(dict0)      # NameError 找不到 dict0 变量
  
  >>>
  {'key1': 'val1'}
  {}

  ......
  NameError: name 'dict0' is not defined

del() 函数删除dict0变量，不可再被使用。D.clear() 方法只清空字典，字典可以被访问。

按键访问并删除
~~~~~~~~~~~~~~~

``D.pop(k[,d]) -> v, remove specified key and return the corresponding value.``
    ``If key is not found, d is returned if given, otherwise KeyError is raised``

D.pop() 方法删除字典给定键 key 所对应的成员，并返回它对应的值，如果键不存在返回参数指定的默认值。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  dict0 = {'key0': 0, 'key1': [1, 2]}
  print(dict0.pop('key0', "default"))
  print(dict0)
  print(dict0.pop('key5', "default"))
  
  >>>
  0
  {'key1': [1, 2]}
  default

随机遍历访问
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {"key0" : "val0", "key1" : "val1"}
  for i in dict0:          # 默认迭代字典键序列
      print(i, end=' ')
  
  print("\n")
  for i in dict0.values(): # 迭代字典值序列
      print(i, end=' ')
  
  print("\n")
  for i in dict0.items():  # 迭代字典键值对
      print(i)
  
  >>>
  key0 key1 

  val0 val1 
  
  ('key0', 'val0')
  ('key1', 'val1')

使用字典内建的 D.values() 方法和 D.items()方法可以方便循环处理每一个成员。

遍历删除
~~~~~~~~~~~~

D.popitem() 内建方法随机返回并删除字典中的一对键和值，为元组类型。字典不可为空，否则会报错。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {'key0': 0, 'key1': [1, 2], 'name': 'value'}
  for i in range(len(dict0)):
     item = dict0.popitem()
     print(item)

  print(dict0)   # 空字典
  >>>
  ('name', 'value')
  ('key1', [1, 2])
  ('key0', 0) 
  {} 

示例中可以看出字典是无序的，并没有按照成员赋值的顺序，而是按照键的 ASCII 码排序。

字典复制
~~~~~~~~~~~~~

类似列表，字典也支持深浅拷贝，字典自带的 D.copy() 方法是浅拷贝，借助 copy 模块实现深拷贝。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {'key0': 'val0', 'list' : [1, 2, 3]}
   
  dict1 = dict0          # 引用对象
  dict2 = dict1.copy()   # 浅拷贝：只复制父对象一级，子对象不复制，还是引用
  
  import copy
  dict3 = copy.deepcopy(dict0) #深拷贝，完全复制
  
  dict1['key0'] = 'newval'
  del dict1['key0']      # 删除会影响引用 dict0
  dict0['list'][0] = 'a' # 改变子对象值，影响浅拷贝 dict2，不影响深拷贝 dict3
  
  for i in range(4):
      print("dict%d:\t%s" % (i, eval("dict" + str(i))))

  >>>
  dict0:  {'list': ['a', 2, 3]}
  dict1:  {'list': ['a', 2, 3]}
  dict2:  {'key0': 'val0', 'list': ['a', 2, 3]}
  dict3:  {'key0': 'val0', 'list': [1, 2, 3]}
  
字典和字符串转换
~~~~~~~~~~~~~~~~~~

通过 str() 类型转化方法可以把字典转换位字符串： 

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {'key0': 'val0', 'list' : [1, 2, 3]}
  str0 = str(dict0) 
  print(str0)
  
  >>>
  {'key0': 'val0', 'list': [1, 2, 3]}

字符串转字典通常有两种方式，eval() 方法和 json 模块提供的 json.loads() 方法。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  dict0 = eval(str0) # eval 方法
  print(dict0)
  
  import json        # 使用 json 模块
  dict1 = json.loads("\"" + str0 + "\"") # 或 repr(str0)
  print(dict1)

  >>>
  {'key0': 'val0', 'list': [1, 2, 3]}
  {'key0': 'val0', 'list': [1, 2, 3]}

注意，采用 json 模块时字符串前后必须添加引号，简单的方式为 ``repr(str0)`` 。

字典相等比较
~~~~~~~~~~~~~~~~~~~

Python2.x 版本使用 cmp() 方法比较字典，Python3 取消了该方法，直接使用比较运算符。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  dict0 = {'key0': 0, 'key1': [1, 2]}
  dict1 = {'key0': 0, 'key2': [1, 2]}

  print(dict0 == dict1)
  print(dict0 != dict1)
  
  >>>
  False
  True

字典不可以比较大小，只可以比较是否相等，相等即指字典所有的键值对完全相同。

统计和存在判定
----------------

统计字典元素个数
~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {'key0': 'val0', 'key1' : "val1"}
  print(len(dict0))
  
  >>>
  2

键存在判定
~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  dict0 = {'key0': 'val0', 'key1' : "val1"}
  
  #print(dict0.has_key('a'))    # False
  #print(dict0.has_key('key0')) # True
  
  # Python3.x 不再支持 has_key() 方法，被 __contains__(key) 替代
  print(dict0.__contains__('a'))
  print(dict0.__contains__('key0'))
  
  # 或者使用 key in 判断，not in 执行反操作
  print('a' in dict0)
  print('a' not in dict0)
  
  >>>
  False
  True
  False
  True

通常使用 ``in`` 或者 ``not in`` 成员运算符。

