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

- " ，字符串由双引号表示，所以字符串中出现 " 需要转义。
- \\，用于转义，当字符串中出现 \\，需要使用 \\\\。
- 控制字符 \\r，\\n，\\f，\\t，\\b。
- \\u 加四个16进制数字，Unicode码值，用于表示一些特殊字符，例如 \\0，\\v等不可见字符。中文字符在默认 utf-8 编码下可以不转换，json 模块提供了一个 ensure_ascii 开关参数。

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


base64
-----------------

有时候我们需要把不可见字符变成可见字符来进行传输，比如邮件附件可以是图片等二进制文件，但是传输协议 SMTP 就只能传输纯文本数据，所以必须进行编码。
如果要把一个文件嵌入到另一个文本文件中，也可以使用这种方法。比如 JSON 文件中嵌入另一个 JSON 文件。

Base64 编码是一种非常简单的将任意二进制字节数据编码成可见字符的机制。

Base64 选用了"A-Z、a-z、0-9、+、/" 这 64 个可打印字符作为索引表，索引从 0-63。编码过程如下：

- 对二进制数据每 3 个 bytes 一组，每组有 3 x 8 = 24 个 bits，再将它划为 4 个小组，每组有 6 个 bits。
- 6 个 bits 的值的范围就是 0-63，通过查索引表，转换为对应的 4 个可见字符。
- 如果要编码数据字节数不是 3 的倍数，最后会剩下 1 或 2 个字节，Base64 用 \x00 字节在末尾补足后进行编码，再在编码的末尾加上 1 或 2 个 '=' 号，表示补了多少字节的 \x00，解码的时候去掉。

所以，Base64 编码会把 3 bytes 的二进制数据编码为 4 bytes 的文本数据，数据大小会比原来增加 1/3。

编解码
~~~~~~~~~~~~~~~

::

  b64encode(s, altchars=None)
      Encode the bytes-like object s using Base64 and return a bytes object.
  b64decode(s, altchars=None, validate=False)
      Decode the Base64 encoded bytes-like object or ASCII string s.
    
b64encode() 接受一个 bytes 类型参数，并返回一个 bytes 对象，所以如果需要转换为字符串，则需要格式化。
b64decode() 与 b64encode() 类似，用于解码。 

.. code-block:: python
  :linenos:
  :lineno-start: 0
        
  import base64
  
  encoded = base64.b64encode(b'\x00\x00\x00\xfb\xef\xff')
  print(encoded)
  
  str0 = '{}'.format(encoded) # 格式化为字符串
  print(str0[2:-1])
  
  print(base64.b64decode(encoded))
  
  >>>
  b'AAAA++//'
  AAAA++// 
  b'\x00\x00\x00\xfb\xef\xff'

altchars 参数接受一个 2 字节长度的 bytes 类型，用于替换字符串中的 + 和 /。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  encoded = base64.b64encode(b'\x00\x00\x00\xfb\xef\xff', altchars=b'-_')
  print(encoded)
  
  str0 = '{}'.format(encoded)
  print(str0[2:-1])
  
  print(base64.b64decode(encoded, altchars=b'-_'))
  
  >>>
  b'AAAA--__'
  AAAA--__
  b'\x00\x00\x00\xfb\xef\xff'

URL 编码
~~~~~~~~~~~~~~

- URI（Uniform Resource Identifier），统一资源标识符。
- URL（Uniform Resource Locater），统一资源定位符。
- URN（Uniform Resource Name），统一资源名称。

URI 由 URL 和 URN 组成，它们三者的关系如下：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
                 URL                                   Anchor
  ----------------------------                         ---- 
  http://www.fake.com:80/path/hello.html?query=hi&arg=0#id0
         ----------------------------------------------
                          URN
  -----------------------------------------------------
                        URI

URL 包含了获取资源协议，主机，端口和路径部分，它指定了一个地址位置。
URN 不含获取资源的协议部分，唯一定义了某个位置上的资源。

可以看到一个常见的 URI 可以包含如下部分：

- 获取协议（Scheme），例如 http, https, ftp 等。
- 主机和端口，以冒号分割，如果使用默认 80 端口，可以不提供端口信息。
- 路径，用 '/' 表示目录层次
- 查询字符串，以 ? 开始，& 连接多个查询参数。
- 片段（Anchor），以 # 开始，标记资源中的子资源，也即资源中的某一部分，不发送给服务器，由浏览器处理。

所以我们所说的 URL 编码准确的说是 URI 编码，现实是这两个概念常常混用。

RFC3986文档规定，URL 中允许字符为 [a-zA-Z0-9] 和 “-_.~4” 个特殊字符以及保留字符。

保留字符：URL可以划分成若干个组件，协议、主机、路径等。有一些字符（:/?#[]@）是用作分隔不同组件的。例如：冒号用于分隔协议和主机，/用于分隔主机和路径，?用于分隔路径和查询参数，等等。还有一些字符（!$&'()*+,;=）用于在每个组件中起到分隔作用的，如=用于表示查询参数中的键值对，&符号用于分隔查询多个键值对。当组件中的普通数据包含这些特殊字符时，需要对其进行编码。

RFC3986中指定的保留字符有 ! * ' ( ) ; : @ & = + $ , / ? # [ ]。

所有其他字符均需要编码，当保留字符出现在非功能分割字段时也需要编码。

URL 编码采用百分号编码方式：一个百分号 %，后跟两个表示字符 ASCII 码值的16进制数，例如 %20 表示空格。

RFC 推荐字符采用 UTF-8 编码方式，也即一个字符的 UTF-8 编码为 0x111213，那么 URL 编码对应 %11%12%13。

Base64对URL编码
~~~~~~~~~~~~~~~~

由于 URL 编码不支持标准的 Base64 索引表中的 + 和 / 字符，所以可以使用 - 和 _ 替代它们。

base64 模块内置了 urlsafe_b64encode() 和 urlsafe_b64decode() 方法用于 URL 编码：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  encoded = base64.urlsafe_b64encode(b'\0\0\0\xfb\xef\xff')
  print(encoded)
  
  str0 = '{}'.format(encoded)
  print(str0[2:-1])
  
  print(base64.urlsafe_b64decode(encoded))

  >>>
  b'AAAA--__'
  AAAA--__
  b'\x00\x00\x00\xfb\xef\xff'

由于=字符也可能出现在Base64编码中，但=在URL和Cookie中不是合法字符，所以，很多Base64编码后会把=去掉。
Base64 把3个字节变为4个字节，Base64编码的长度总是 4 的倍数，当发现编码后长度不是 4 的倍数后，补足= 再解码就可以了。

注意事项
~~~~~~~~~~~~~~~~

Base64 适用于轻量级编码，比如查询字段，Cookie内容和内嵌文件，例如在 JSON 或 XML 中内嵌一段二进制数据。

Base64 编码不适用于加密，它只是简单的字符映射，很容易被破解。
