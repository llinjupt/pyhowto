错误和异常处理
================

语法错误
----------------------

解释器在运行代码之前，首先进行代码的语法错误检查，有些代码编辑器，也可以给出语法错误的提示。

.. code-block:: none
  :linenos:
  :lineno-start: 0

  if True
      print("OK")
  
  >>>
    File "C:/Users/Red/.spyder/exception.py", line 10
      if True
             ^
  SyntaxError: invalid syntax

语法错误信息中第一行给出出错的文件和行号，第二行给出出错的语句，第三行由一个向上的小箭头指出语法错误的位置。
最后一行给出错误类型为 SyntaxError，也即语法错误，并给出一个简短的说明。

以上几类信息帮助快速定位和解决语法错误。

标准异常类型
------------------

代码运行时出现导致解释器无法继续执行的错误被称为异常。
异常在Python中被表示为一个异常对象。当异常发生时，如果不捕获处理它，则会导致程序终止执行。 

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  1/0
  
  >>>
    File "C:/Users/Red/.spyder/except.py", line 42, in <module>
      1/0
  
  ZeroDivisionError: division by zero

与语法错误的提示类似，给出文件和行号等，不同的是，由于异常是语句运行时导致的错误，无法用小箭头指出位置。
上面是一个除0异常(ZeroDivisionError)。

常见的异常类型如下：

  ==========================  =====================================
  异常名称                     类型描述
  ==========================  =====================================
  BaseException               所有异常的基类
  SystemExit                  解释器请求退出
  KeyboardInterrupt           用户中断执行(通常是输入^C)
  Exception                   常规错误的基类
  StopIteration               迭代器没有更多的值
  GeneratorExit               生成器(generator)发生异常来通知退出
  StandardError               所有的内建标准异常的基类
  ArithmeticError             所有数值计算错误的基类
  FloatingPointError          浮点计算错误
  OverflowError               数值运算超出最大限制
  ZeroDivisionError           除(或取模)零
  AssertionError              断言语句失败
  AttributeError              对象没有这个属性
  EOFError                    没有内建输入,到达EOF
  EnvironmentError            操作系统错误的基类
  IOError                     输入/输出操作失败
  OSError                     操作系统错误
  WindowsError                系统调用失败
  ImportError                 导入模块/对象失败
  LookupError                 无效数据查询的基类
  IndexError                  序列中没有此索引(index)
  KeyError                    映射中没有这个键
  MemoryError                 内存溢出错误(对于Python
  NameError                   未声明/初始化对象
  UnboundLocalError           访问未初始化的本地变量
  ReferenceError              弱引用(Weak
  RuntimeError                一般的运行时错误
  NotImplementedError         尚未实现的方法
  SyntaxError                 Python
  IndentationError            缩进错误
  TabError                    Tab
  SystemError                 一般的解释器系统错误
  TypeError                   对类型无效的操作
  ValueError                  传入无效的参数
  UnicodeError                Unicode
  UnicodeDecodeError          Unicode
  UnicodeEncodeError          Unicode
  UnicodeTranslateError       Unicode
  Warning                     警告的基类
  DeprecationWarning          关于被弃用的特征的警告
  FutureWarning               关于构造将来语义会有改变的警告
  OverflowWarning             旧的关于自动提升为长整型(long)的警告
  PendingDeprecationWarning   关于特性将会被废弃的警告
  RuntimeWarning              可疑的运行时行为(runtime
  SyntaxWarning               可疑的语法的警告
  UserWarning                 用户代码生成的警告
  ==========================  =====================================

Python中异常类的层次关系，详见 `Exception hierarchy <https://docs.python.org/3/library/exceptions.html>`_ 。

捕获异常
------------------

Python 使用 try/except 或 try/except/else 语句用来捕获异常。

try/except语句
~~~~~~~~~~~~~~~~~~

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  def divide0():
    return 1 / 0
  
  def divide1():
    return divide0()
  
  try:
      divide1()
      print("can't reach here!")
  except ArithmeticError:
      print("ArithmeticError")
  except ZeroDivisionError:
      print("ZeroDivisionError")
  except:
    print("Wildcard Error")
    
  print("still running...")
  
  >>>
  ArithmeticError
  still running...

由以上实例，可以得出以下结论：

- try 后放置我们需要捕获异常的语句，即便是子函数中的异常也会被捕获。
- try 中一旦某一条语句异常发生，后面的语句不再被执行，而是执行 except 分支语句。
- try 后可以跟多条 except 语句，用于处理每一种异常，也可以不指明异常类型，这样会匹配所有异常。
- except 语句只能匹配其中的一条，子类异常可以匹配基类的异常类型，比如这里的 ZeroDivisionError 继承自 ArithmeticError，所以除0错误会首先匹配第一个异常分支。
  所以需要将最希望匹配的异常类型放在前面。
- 异常在捕获后，程序不会退出，而会继续执行。

except 语句可以同时处理多种异常，避免为每一种异常书写一条处理代码。

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  try:
      a = b + 1
  except (RuntimeError, TypeError, NameError):
      pass
  
  print("still running...")
  
  >>>
  still running...
  
try/except/else 语句
~~~~~~~~~~~~~~~~~~~~~~

try/except/else 是最常用的异常捕获语句，这允许在没有异常发生时得以做特定的处理。

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  try:
      a = 1 + 2
  except:
      print("except")
  else:
      print("Everything is OK!")

  >>>
  Everything is OK!

try/finally 语句
~~~~~~~~~~~~~~~~~~~~~~

finally 语句无论异常是否发生都会被执行，它常用来做清理动作，比如关闭文件描述符或者网络套接字。

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  try:
      f.write("something...")
  except:
      print("except")
  esle:
      print("write ok!")
  finally:
      f.close()

注意：try/finally 语句中可以使用 else 分支。

Python 的 with 语句，可以更好的实现资源清理功能。如下所示，系统都将自动关闭文件描述符。

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  with open('fname', 'r') as f:
      data = f.read()

打印异常信息
~~~~~~~~~~~~~~~~~~~~~~

在 except 语句中的异常名(或多个异常名)后可以以 as VAR 的形式添加一个变量，
该变量会返回异常的一个实例，异常的详细信息存储在该实例的 args 成员中。
它通常是一个对当前异常的说明信息。 

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  try:
      1 / 0
  except Exception as inst:
      print(type(inst))     # the exception instance
      print(type(inst.args))
      print(inst.args)      # arguments stored in .args
      print(inst)   
    
  >>>
  <class 'ZeroDivisionError'>
  <class 'tuple'>
  ('division by zero',)
  division by zero 

异常类中的 __str__() 方法让 print() 函数可以直接打印异常的说明信息。 异常的 args 成员是一个元组 (tuple) 类型。 
  
主动触发异常
~~~~~~~~~~~~~~~~~~

raise 语句用于主动在程序中触发异常。

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  try:
      raise ValueError 
  except Exception as e:
      print(e)         
  
  try:
      raise ValueError('Invalid value')
  except Exception as e:
      print(e)    

  >>>
  Invalid value

第一个示例抛出不带参数的异常，raise ValueError 是 raise ValueError() 的简写。此时 print(e) 只会打印一个空行。

也可以给异常传递多个参数，实际上它可以接受任意多个任意类型的参数，在异常处理中可以单独处理这些以元组类型返回的参数。
当然把这些信息统一到一个用户自定的类型中是一个更明智的选择。

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  try:
      raise ValueError('string', 1, ['abc', 123])
  except Exception as e:
      print(e.args[0])
      print(e)
  
  >>>
  string
  ('string', 1, ['abc', 123])

用户自定义异常
~~~~~~~~~~~~~~~~~~~

自定义的异常类 Networkerror 继承了运行时异常，与内建的异常类不同，它不能接受任意多个参数，
参数的多少由 __init__() 初始化函数决定。

.. code-block:: none
  :linenos:
  :lineno-start: 0
    
  class Networkerror(RuntimeError):
      def __init__(self, arg):
          self.args = (arg,)
  
  try:
      raise Networkerror("Bad hostname")
  except Networkerror as e:
      print(e)
      
  >>>
  Bad hostname

在一个用户模块中，可能需要定义一系列私有的异常，它通常继承自名为 Error 的自定义类，它继承异常的基类 Exception，
没有任何方法，是为了以后的扩展考虑。

.. code-block:: none
  :linenos:
  :lineno-start: 0
  
  class Error(Exception):
      """Base class for exceptions in this module."""
      pass
  
  class InputError(Error):
      """Exception raised for errors in the input.
  
      Attributes:
          expression -- input expression in which the error occurred
          message -- explanation of the error
      """
  
      def __init__(self, expression, message):
          self.expression = expression
          self.message = message
