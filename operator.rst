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

contextlib
--------------

contextlib 是一个用于生成上线文管理器（Context Manager）模块，它提供了一些装饰器，可以把一个生成器转化成上下文管理器。

所谓上下文管理器，就是实现了上下文方法（__enter__ 和 __exit__）的对象，采用 with as 语句，可以在执行一些语句前先自动执行准备工作，当语句执行完成后，再自动执行一些收尾工作。参考 :ref:`enter_exit` 。

contextmanager
~~~~~~~~~~~~~~~~
要实现一个自定义的上下文管理器，就需要定义一个实现了__enter__和__exit__两个方法的类，这很麻烦，
contextmanager 是一个装饰器，可以把生成器装换成上下文管理器，在 with as 语句中调用。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  from contextlib import contextmanager
  @contextmanager
  def ctx_generator():
      print("__enter__")   # 这里做 __enter__ 动作
      yield 1
      print("__exit__")    # 这里做 __exit__ 动作

  print(type(ctx_generator()))
  with ctx_generator() as obj:
      print(obj)

  >>>
  __enter__
  1
  __exit__

当然我们也可以不返回任何对象，比如锁机制，这时只需要使用 with 语句：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  @contextmanager
  def locked(lock):
      lock.acquire()
      yield
      lock.release()

  with locked(lock):
      ......
  # 自动释放锁

closing 类
~~~~~~~~~~~~~~

contextlib 中定义了一个 closing 类，这个类的定义很简单，它把传入的对象转换成一个支持 with as 语句上下文管理器。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  class closing(AbstractContextManager):
      def __init__(self, thing):
          self.thing = thing
      def __enter__(self):
          return self.thing
      def __exit__(self, *exc_info):
          self.thing.close()

可以看到 closing 类会把传入的对方赋值给 with as 后的变量，并在 with 语句块退出时执行对象的 close() 方法。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  from contextlib import closing    
  class CloseCls():
      def close(self):
          print("close")
  
  with closing(CloseCls()):
      pass

  >>>
  close

注意事项
~~~~~~~~~~~~~

contextlib 主要用于用户自定义的类或者自定义的上线文管理器，大部分的 Python 内置模块和第三方模块都已经实现了上线文管理器方法，例如 requests 模块，
首先应该尝试 with 语句。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  with requests.Session() as s:
      ......

即便一个对象没有实现上线文管理器方法，系统也会给出报错提示，然后再借用 contextlib。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  with object:
      pass

  >>>
  AttributeError: __enter__

json
------------

JSON（JavaScript Object Notation, JS对象标记法）是一种轻量级的数据交换格式。它原是 JavaScript 用于存储交换对象的格式， 采用完全独立于编程语言的文本格式来存储和表示数据。由于它的简洁和清晰的层次结构，易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率，使得 JSON 成为理想的数据交换格式，被很多语言支持。 相对于 xml 格式，JSON 没有过多的冗余标签，编辑更简洁，更轻量化。

JS对象的 JSON 表示
~~~~~~~~~~~~~~~~~~

在 JavaScript 中，任何支持的类型都可以通过 JSON 来表示，例如字符串、数字、对象、数组等。这里简单看下 JSON 是如何表示这些对象的：

.. code-block:: js
  :linenos:
  :lineno-start: 0 
  
  // test.js
  var num0 = 0
  var num1 = 3.14
  var str0 = "string"
  var bool0 = true
  var bool1 = false
  var n = null
  var array = [1, "abc"]
  
  str = JSON.stringify(num0);
  console.log(str)
  //......
  
JSON.stringify() 实现 JS 数据类型向 JSON 格式的转换，由于 JSON 永远是由可视的字符串构成，可以直接打印到终端。以上内容保存在 test.js 中，通过 nodejs test.js 查看输出结果：

.. code-block:: sh
  :linenos:
  :lineno-start: 0 
  
  0
  3.14
  "string"
  [1,"abc"]
  true
  false
  null

与各种编程语言类似，数组以 [] 表示，字符串放在双引号（JSON 不支持单引号）中，其他数字，布尔量和 null 直接输出值。再看下一个对象是怎么表示的：

.. code-block:: js
  :linenos:
  :lineno-start: 0 
  
  // test1.js
  testObj = new Object();
  testObj.str0="string";
  testObj.num0=0;
  testObj.num1=3.14;
  testObj.array=[1, 'abc'];
  testObj.bool0=true;
  testObj.bool1=false;
  testObj.nop=null;
  testObj.subobj = new Object();
  
  str = JSON.stringify(testObj, null, 2);
  console.log(str) 

一个对象由 {} 表示，内容为键值对，每个键都是一个字符串，是对象的属性名，而值可以为其他任意数据类型。

.. code-block:: sh
  :linenos:
  :lineno-start: 0 
  
  {
    "str0": "string",
    "num0": 0,
    "num1": 3.14,
    "array": [
      1,
      "abc"
    ],
    "bool0": true,
    "bool1": false,
    "nop": null,
    "subobj": {}
  }

将 JSON 格式转换为 JS 对象使用 JSON.parse()：

.. code-block:: js
  :linenos:
  :lineno-start: 0 

  str = JSON.stringify(testObj, null, 2);
  newObj = JSON.parse(str)
  console.log(newObj.str0) // 输出 string

JSON特殊字符
~~~~~~~~~~~~~~~~~~~~

JSON 中的特殊字符有以下几种，使用时需要转义：

- " ，字符串由双引号表示，所以字符串中出现 " 需要使用转义符 \\"。
- \\，用于转义，所以字符串中出现 \\，需要使用 \\\\。
- 控制字符 \\r，\\n，\\f，\\t，\\b。
- \\u 加四个16进制数字，Unicode码值，用于表示一些特殊字符，例如 \\0，\\v。中文字符在默认 utf-8 编码下可以不转换，json 模块提供了一个 ensure_ascii 开关参数。

.. code-block:: js
  :linenos:
  :lineno-start: 0
  
  // 输出 "\u000b\u0000你好"
  console.log(JSON.stringify('\v\0你好'))

为了JSON的通用性，应该保证输出的JSON文件使用 utf-8 编码。

Python类型和JSON转换
~~~~~~~~~~~~~~~~~~~~~~

json 模块当前支持如下的 Python 类型和 JSON 之间互相转换。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  +-------------------+---------------+
  | Python            | JSON          |
  +===================+===============+
  | dict              | object        |
  +-------------------+---------------+
  | list, tuple       | array         |
  +-------------------+---------------+
  | str               | string        |
  +-------------------+---------------+
  | int, float        | number        |
  +-------------------+---------------+
  | True              | true          |
  +-------------------+---------------+
  | False             | false         |
  +-------------------+---------------+
  | None              | null          |
  +-------------------+---------------+

dumps 和 dump
`````````````````````

::
  
  dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, 
        cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
      Serialize ``obj`` to a JSON formatted ``str``.

json 中的 dumps() 函数序列化 Python 对象，生成 JSON 格式的字符串。

- indent=n， 用于缩进显示。
- sort_keys=False， 表示是否对输出进行按键排序。
- ensure_ascii=True，表示是否保证输出的JSON只包含 ASCII 字符。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  dict0 = {'str0': 'string', 'num0' : 0, 'num1' : 3.14, 
           'list': [1, 'abc'], 'tuple': (1, 'abc'), 'True': True,
           'False': False, 'nop': None, 'subdict': {}}
  
  jsonstr = json.dumps(dict0, indent=2) # indent 用于格式化输出
  print(jsonstr)
  
  >>>
  {
    "str0": "string",
    "num0": 0,
    "num1": 3.14,
    "list": [
      1,
      "abc"
    ],
    "tuple": [
      1,
      "abc"
    ],
    "True": true,
    "False": false,
    "nop": null,
    "subdict": {}
  }

ensure_ascii 参数默认为 True，它保证输出的字符只有 ASCII 码组成，也即所有非 ASCII 码字符，例如中文会被转义表示，格式为 \\u 前缀加字符的 Unicode 码值。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  json0 = json.dumps('hello 你好', ensure_ascii=True)
  json1 = json.dumps('hello 你好', ensure_ascii=False)
  print(json0, json1)
  
  >>>
  "hello \u4f60\u597d" "hello 你好"

如果 Python 对象含有 JSON 特殊字符，dumps() 方法将自动转义：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  json0 = json.dumps('"\\\r\n\f\t\b\x00你好', ensure_ascii=True)
  print(json0)
  
  >>>
  "\"\\\r\n\f\t\b\u0000\u4f60\u597d"

dump() 方法支持的参数与 dumps() 基本一致，它将生成的 JSON 写入文件描述符，无返回：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
  with open('test.json', 'w') as fw:
      json.dump(data, fw)

loads 和 load
`````````````````````

loads() 和 load() 将 JSON 转化为 Python 对象。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  json_str = '{"key0": 1, "key1": "abc", "key3": [1,2,3]}'
  dict0 = json.loads(json_str)
  print(type(dict0).__name__)
  print(dict0)
  
  >>>
  dict
  {'key0': 1, 'key1': 'abc', 'key3': [1, 2, 3]}

load() 从文件描述符加载 JSON 并转化为 Python 对象。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  with open('test.json', 'r') as fr:
      dict0 = json.load(fr)    
      print(type(dict0).__name__)

  >>>
  list

Python对象和JSON转换
~~~~~~~~~~~~~~~~~~~~~~

上面已经介绍过，json 模块默认支持的类型如何与 JSON 互相转换。然而使用最多的用于自定义的 class 实例是否无法转换呢？

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  class JSONCls():
      def __init__(self, name, num):
          self.name = name
          self.num = num
  
  obj = JSONCls('json', 0)
  print(json.dumps(obj))
  
  >>>
  TypeError: Object of type 'JSONCls' is not JSON serializable
  
默认情况下，dumps()方法无法实现用户自定义对象和JSON的转换。注意到 default 参数，它可以接受一个函数，用于把对象转换为字典：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def JSONObj2dict(obj):
      d = {
          '__class__': obj.__class__.__name__,
          '__module__': obj.__module__,
      }
      d.update(obj.__dict__)
      return d
  
  print(json.dumps(obj, default=JSONObj2dict))
  
  >>>
  {"__class__": "JSONCls", "__module__": "__main__", "name": "json", "num": 0}

loads() 参数中的 object_hook 指定反向转换函数可以实现逆转换：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  def dict2JSONObj(d):
      if '__class__' in d:
          class_name = d.pop('__class__')
          module_name = d.pop('__module__')
          module = __import__(module_name)
          cls = getattr(module, class_name)
  
          args = {
              key: value
              for key, value in d.items()
          }
          return cls(**args)
      return d
        
  jsonstr = '{"__class__": "JSONCls", "__module__": "__main__", "name": "json", "num": 0}'
  
  obj = json.loads(jsonstr, object_hook=dict2JSONObj)
  print(type(obj), obj.name, obj.num)
  
  >>>
  <class '__main__.JSONCls'> json 0

当然，如果我们不保存模块名和类名，也可以导入，只是要保证当前保存的JSON也生成的类实例是要匹配的，并明确使用 JSONCls() 对参数进行实例化：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def JSONObj2dict(obj):
      return obj.__dict__
      
  def dict2JSONObj(d):
      args = { key: value
               for key, value in d.items()}
      return JSONCls(**args)
