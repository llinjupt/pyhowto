模块和包
================

模块和包是 Python 组织代码的形式。这如同 C 语言中的 .c 和 .a 文件一样。

模块和模块的导入
-----------------

为了编写可维护可重用的代码，通常把代码按功能分类，
分别放在不同的文件里，这样每个文件中的代码就相对较少，且功能统一。
在Python中，一个 .py 脚本源码文件就称之为一个模块 （module）。

使用模块还可以避免函数名和变量名冲突。每一个模块都有自己的全局符号表，包含所有可以被其他模块使用的变量，函数等，
同名函数和变量可以同时存在不同的模块中，因此在编写模块时，
不必考虑名字会与其他模块冲突，这在多人协同编程时至关重要。

import 导入模块
~~~~~~~~~~~~~~~~

在当前目录下创建三个文件 module0.py，module1.py 和 test_module.py，也即创建了三个模块，
它们的名字和文件名一致，分别为 module0，module1 和 test_module。

我们在 test_module 模块中引用 module0 和 module1 中的函数：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  # module0.py
  module_name = 'module0'
  def module_info():
    print("func in module0")
    
  # module1.py
  module_name = 'module1'
  def module_info():
    print("func in module1") 

  # test_module.py
  import module0, module1 # 导入模块

  print(module0.module_name)
  print(module1.module_name)
  module0.module_info()
  module1.module_info()     

  >>>
  module0
  module1
  func in module0
  func in module1

import 语句是导入模块的一种方式，它具有以下特点：

- 一条 import 语句可以同时导入多个模块，以逗号分隔
- import 将整个模块的全局符号表导入到当前模块的符号表中，可以使用模块中所有全局变量，类和函数
- import 导入的模块，对其中的变量和函数访问时要加上模块名
- 导入的模块中相同函数名和变量名不会冲突

import 语句通常放在文件开头，这不是必须的，它也可以放在靠近引用模块的代码前。
重复导入相同的模块不会产生错误，解释器只在最早出现的 import 该模块的语句处导入。

导入模块时，解释器按照 sys.path 给出的路径顺序查找要导入的模块，以下是 Linux环境上的一个实例：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  import sys
  print(sys.path)
  
  >>>
  ['/home/red/sdc/lbooks/ml', '/usr/lib/python3.4', 
   '/usr/lib/python3.4/plat-i386-linux-gnu', '/usr/lib/python3.4/lib-dynload', 
   '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']

当前路径具有最高优先级，所以模块命名不可与 Python 自带模块或第三方模块命名冲突，也不可和类，全局变量，内建函数命名冲突。sys.path 是一个路径的列表变量，
可以添加指定的路径：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  sys.path.append('/sdc/lib/python')

重命名模块
``````````````

使用 import 导入时可以为模块重新命名，将长命名模块进行缩写，可以让代码更简洁：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  import module0 as m0
  import module1 as m1
  
  print(m0.module_name)
  print(m1.module_name)
  m0.module_info()
  m1.module_info()

模块部分导入
~~~~~~~~~~~~~~~~

与 import 语句不同，from 语句可以选择导入模块的某些变量或者函数，把它们直接加入到当前脚本的全局符号表中，引用时无需添加模块名前缀。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  from module0 import module_info
  from module1 import module_info
  from module1 import module_info as mi

  module_info()
  mi()
  print(module_name)
  
  >>>
  func in module1
  func in module1
  Traceback (most recent call last):
    File "test_module.py", line 21, in <module>
      print(module1.module_name)
  NameError: name 'module_name' is not defined

由以上示例，可以得出如下结论：

- from 只把语句中指定的变量或函数从模块导入
- from 语句也支持重命名，此时重命名的是特定变量或者函数
- from 导入和变量或者函数不需要加模块名，直接访问，这导致在出现同名冲突时，后导入模块覆盖先导入模块，比如这里 module_info() 输出的是 func in module1
- 未导入变量或函数不能访问，比如这里提示 module_name 未定义

from 也可以把模块的全局符号表均导入到当前脚本全局符号表中：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  from module0 import * # 导入所有符号表到当前脚本
  
这种方法不该被过多使用，或者说大多数情况，都不要使用这种方法，因为它引入的符号命名很可能覆盖已有的定义，这也是上面示例所要强调的。

模块内代码应该高内聚，模块间应该低耦合，这是规范编码的基本要求，使用 import as 语句是推荐的做法。

包和包模块的导入
------------------

在实际的编码环境中，已经存在成千上万的模块，并且新模块还在不停被创建，此外多人协同编码时，不同的人编写的模块名也可能相同。基于这样的事实，
为了避免模块名冲突，Python 又引入了按目录来组织模块的方法，称为包（Package）。

简单说包就是一个文件夹，这个文件夹包含一个 __init__.py 文件，它可以是一个空文件。

引入了包以后，只要顶层的包名不冲突，那么所有的模块都不会冲突。

import 导入包模块
~~~~~~~~~~~~~~~~~~~
.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  ├── package0
  │   ├── __init__.py
  │   └── module0.py
  ├── package1
  │   ├── __init__.py
  │   └── module0.py
  └── test_package.py

以上是示例的目录结构，由于包是一个目录，那么导入包中的模块时，就要指明模块所在包中的路径，Python 将路径“圆点化”表示，称为包路径：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # test_package.py

  import package0.module0
  import package1.module0 as p1_m0
  
  package0.module0.module_info()
  p1_m0.module_info()

import 参数的最后部分必须是模块名(文件名)，而不能是包名(目录名)，比如 ``import package0``，那么访问 package0.module0 会提示找不到 module0 的错误：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  Traceback (most recent call last):
    File "test_package.py", line 15, in <module>
      package0.module0.module_info()
  AttributeError: 'module' object has no attribute 'module0'

import 语句也可以为包或其中的模块重命名，这使得代码更简洁。导入包与直接导入模块不同的是：

- 导入包指定的是“圆点化”路径，比如例子中的 ``package0.module0`` ，引用时需要完整的包路径。
- __init__.py 脚本会在第一次导入包中模块时被执行，它常用来做包的预处理。
- 使用包中模块时，必须带上完整的包路径(包名)，比如这里的 ``package0.module0.module_info()``，重命名可使代码更简洁。

部分导入包内模块
~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # from package0 import *  # 可以导入 package0 包中所有模块
  from package0 import module0
  from package0.module0 import module_info
  
  module0.module_info()
  module_info()
  
  from package1 import module0 as p1_m0
  from package1.module0 import module_info as m0
  
  p1_m0.module_info()
  m0()

from 后的参数可以为包路径，也可以为模块名路径，并且可以精确指定 import 模块中各成员。

尽管可以通过 ``from package0 import *`` 导入包中的所有模块或子包，但这种方法不要使用，很容易造成命名冲突，代码不清晰，导入应该明确要导入的模块名。

包内导入
~~~~~~~~~~~~~~~

sys.path
sys.modules
https://docs.python.org/3/reference/import.html
https://blog.csdn.net/u013571243/article/details/77734346
https://realpython.com/absolute-vs-relative-python-imports/