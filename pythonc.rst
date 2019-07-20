C 语言模块
================

由于 Python 是解释型语言，非常适合处理 IO 密集型任务，但是不善于处理计算密集型任务，例如加解密，压缩解压缩等，这类任务如果全部使用 Python 开发，是非常低效的，通常的做法是将算法密集型任务使用 C 语言实现，并用 Python 封装接口以方便用户调用。

为了同时发挥 Python 快速开发和 C 语言的快速处理的优点，Python 支持调用 C 语言接口。实际上 Python 底层均是由 C 语言开发的，调用 C 语言接口是最基本的功能。通常有两种方式来与 C 语言开发的模块(win 上为 dll，linux 上为 so 文件)交互：

- 原生方式，直接使用 Python-dev 开发包开发 C 模块。
- 通过 ctypes 模块实现 Python 调用 C 接口。

原生方式
---------------

原生方式直接调用Python-dev 开发包开发 C 模块，这种方式必须使用开发包中的接口函数开发，需要熟悉相关数据类型和函数（这些函数通常被称为包裹函数）。通过这些函数可以方便实现任意参数类型的接口，但是开发出的 .so 通常作为 Python 的专用模块，不可以被其他 C 应用程序调用。

大部分依赖 C 模块的第三方软件库使用这种方式开发，例如科学计算中的 numpy，scipy 软件库。这里以一个累加函数为例，来阐述原生方式的开发流程。

必须说明，这里使用的是 Python3 环境，参考 `Extending Python3 with C <https://docs.python.org/3/extending/extending.html>`_ ；Python2 与此略有不同，参考 `Extending Python2.7 with C <https://docs.python.org/2.7/extending/extending.html>`_ 。

首先创建 C 语言文件 accumulate.c 和对应函数:

.. code-block:: c
  :linenos:
  :lineno-start: 0

  #include <stdio.h>

  unsigned int accumulate(unsigned int n)
  {
    unsigned int sum = 0;
    unsigned int i = 0;
    
    for(; i <= n; i++)
      sum += i;
    
    return sum;
  }
  
  int main()
  {
    printf("%u", accumulate(100));
  }

在进一步操作之前，我们必须保证这些函数是正确执行的，编译测试它们：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $  make accumulate && ./accumulate
  5050

为了让 Python 解析器 CPython 可以解析这里的 C 函数，需要使用 Python.h 头文件里面的类型和函数来封装我们的 C 语言函数和类型参数。这里需要安装 Python 编译环境，pythonx.y-dev 提供了相关头文件和库文件：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ sudo apt-get install python3.6-dev

接着使用 Python.h 相关类型和函数包裹我们的 C 函数，以编译为 Python 接口模块:

.. code-block:: c
  :linenos:
  :lineno-start: 0
  
  #include <Python.h>
  
  static unsigned int _accumulate(unsigned int n)
  {
    unsigned int sum = 0;
    unsigned int i = 0;
    
    for(; i <= n; i++)
      sum += i;
    
    return sum;
  }
  
  static PyObject *accumulate(PyObject* self, PyObject* args)
  {
    unsigned int n = 0;
    
    // 类型解析参考 https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple
    if(!PyArg_ParseTuple(args, "i", &n)) 
      return NULL;
    
    return Py_BuildValue("i", _accumulate(n));
  }
  
  static PyMethodDef accuMethods[] = 
  {
    {"accumulate", accumulate, METH_VARARGS, "Calculate the accumulation of n"},
    {NULL, NULL, 0, NULL}
  
  };
  
  static PyModuleDef accuModule = 
  {
    PyModuleDef_HEAD_INIT,
    "accuModule",                   // module name
    "accumulate module description",// module description
    -1,
    accuMethods
  };
  
  
  // 仅有的非 static 函数，对外暴露模块接口，PyInit_name 必须和模块名相同
  // only one non-static function
  PyMODINIT_FUNC PyInit_accuModule(void)
  {
    return PyModule_Create(&accuModule);
  }

最后创建 setup.py 以编译目标 .so 文件，

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  from distutils.core import setup, Extension
 
  module = Extension('accuModule', sources = ['accumulate.c'])
  
  setup(name = 'accuModule',
  	    version = '1.0',
  	    description = 'This is a demo package',
  	    ext_modules = [module])

此时文件夹中包含源码文件 accumulate.c 和 setup.py，开始编译:

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ python3.6 setup.py build
  running build
  running build_ext
  building 'accuModule' extension
  creating build
  creating build/temp.linux-i686-3.6
  ...

编译后当前路径文件目录如下所示：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ tree
  .
  ├── accumulate.c
  ├── build
  │   ├── lib.linux-i686-3.6
  │   │   └── accuModule.cpython-36m-i386-linux-gnu.so # 目标模块文件
  │   └── temp.linux-i686-3.6
  │       └── accumulate.o
  └── setup.py

最后安装模块：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ sudo python3.6 setup.py install --record install.txt
  running install
  running build
  running build_ext
  running install_lib
  copying build/lib.linux-i686-3.6/accuModule.cpython-36m-i386-linux-gnu.so \
          -> /usr/local/lib/python3.6/dist-packages
  running install_egg_info
  Writing /usr/local/lib/python3.6/dist-packages/accuModule-1.0.egg-info
  
可以看到模块被安装在了 /usr/local/lib/python3.6/dist-packages 目录下。

开发中我们可能要多次删除和安装模块，但是 setup.py 没有提供对应的下载命令，这里使用 record 记录了安装到所有文件，如果要卸载，直接删除 install.txt 中记录的文件即可：

.. code-block:: sh
  :linenos:
  :lineno-start: 0

  $ cat install.txt
  /usr/local/lib/python3.6/dist-packages/accuModule.cpython-36m-i386-linux-gnu.so
  /usr/local/lib/python3.6/dist-packages/accuModule-1.0.egg-info

  # 卸载软件包
  $ cat install.txt | xargs rm -rf

最后测试模块，创建 test.py:

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  from accuModule import accumulate
   
  print(accumulate(100))
 
执行 python3.6 test.py 可以得到结果 5050。

ctypes
-------------

采用原生方式对每一个 C 语言接口进行打包是很繁琐的，为了简化接口调用，ctypes 模块提供了和 C 语言兼容的数据类型和函数来加载模块(dll或so)文件，因此在调用时不需对源文件做任何的修改。

关于 ctypes 的更多信息参考 `A foreign function library for Python <https://docs.python.org/3/library/ctypes.html>`_ 。

.. code-block:: c
  :linenos:
  :lineno-start: 0
  
  #include <stdio.h>
  
  unsigned int accumulate(unsigned int n)
  {
    unsigned int sum = 0;
    unsigned int i = 0;
    
    for(; i <= n; i++)
      sum += i;
    
    return sum;
  }

注意对外接口不可定义为 static 的，通过 gcc 编译得到 .so 文件：

.. code-block:: shell
  :linenos:
  :lineno-start: 0

  # Mac
  $ gcc -shared -Wl,-install_name,accumulate.so -o accumulate.so -fPIC accumulate.c
  
  # windows
  $ gcc -shared -Wl,-soname,adder -o accumulate.dll -fPIC accumulate.c
  
  # Linux
  $ gcc -shared -Wl,-soname,adder -o accumulate.so -fPIC accumulate.c

修改 test.py 直接通过 ctypes 模块中的 CDLL 方法加载模块：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  from ctypes import *
  
  #load the module file
  accuModule = CDLL('./accumulate.so')
  print(accuModule.accumulate(100))

ctypes 接口允许我们在调用 C 函数时使用Python 中默认的字符串型和整型。

但是对于其他类型，例如布尔型和浮点型，必须要使用对应的 ctype 类型才可以。这种方法虽然简单，清晰，但是却有很大限制：例如，不能在 C 中对 Python 对象进行操作。
