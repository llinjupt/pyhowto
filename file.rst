文件操作
================

文件操作是编程语言提供的最基本的功能，如果数据不能以文件形式存储在存储介质上，比如硬盘，那么信息就不能长期存储，也无法共享和传输。

Python 提供了强大的文件操作方法。操作系统不允许用户程序直接访问磁盘，而是要通过文件系统调用，Python 通过 C 函数库访问系统调用，进行文件读写。对文件读写操作需要通过文件描述符进行。 

文件打开和关闭
---------------

文件打开模式
~~~~~~~~~~~~~~~~~

打开文件获取文件描述符，打开文件时需要指定对文件的读写模式，和写追加模式。常见的文件模式如下：
                      
  ========= ===============================================================
   模式     描述
  --------- ---------------------------------------------------------------
  'r'       以只读方式打开文件（默认），不存在报错 FileNotFoundError
  'w'       以写方式打开文件，如果文件存在，首先清空原内容，如果不存在先创建文件
  'x'       以写方式打开文件，如果文件存在，则报错 FileExistsError
  'a'       以写方式打开文件，并追加内容到文件结尾，如果文件不能存在则先创建文件
  '+'       可同时读写
  ========= ===============================================================        

'+' 模式可以和其他模式组合，以同时支持读写，常用组合和特性如下：

  +-------------+----+-----+----+-----+----+-----+
  +打开模式     +r   +r+   +w   +w+   +a   +a+   +
  +=============+====+=====+====+=====+====+=====+
  +可读         ++   ++    +    ++    +    ++    +
  +-------------+----+-----+----+-----+----+-----+
  +可写         +    ++    ++   ++    ++   ++    +
  +-------------+----+-----+----+-----+----+-----+
  +创建         +    +     ++   ++    +    +     +
  +-------------+----+-----+----+-----+----+-----+
  +覆盖         +    +     ++   ++    +    +     +
  +-------------+----+-----+----+-----+----+-----+
  +指针在开始   ++   ++    ++   ++    +    +     +
  +-------------+----+-----+----+-----+----+-----+
  +指针在结尾   +    +     +    +     ++   ++    +
  +-------------+----+-----+----+-----+----+-----+ 

数据流在读写时又分为两种转换模式:

  ========= ===============================================================
   模式     描述
  --------- ---------------------------------------------------------------
  'b'       二进制模式（不转换）
  't'       文本模式（转换，默认）
  ========= ===============================================================  

二进制模式将内存中的数据信息直接写入到文件中，不做任何转换。如内存中的数据 0x01 以二进制写入就是直接写入 0x01 到文件中。

而文本模式是为解决操作系统兼容性引入的。

在文本中，有一些字符不是是用来显示的，而是用来控制的，称为控制符，比如告诉编辑器一行结束就是字符 ‘\\n’， 对应 ASCII 码 0x0d，但是不同的操作系统使用的控制符并不一致，这导致在A平台下编辑的文件到B平台下可能就无法正常显示。

类 Unix 操作系统采用单个 ‘\\n’ 表示行结束符。Windows 使用两个字符 “\\r\\n” 表示。而 Mac 系统使用 ‘\\r’ 表示。

所以当指明使用文本模式读取时，如果是在 Winodows 系统，那么当读取到 “\\r\\n” 或者 ‘\\r’ 时就会转换为 “\\r\\n” ，写的时候会将 ‘\n’ 转换为 “\\r\\n”。
如果是进行文本编辑，那么应该使用默认的文本打开模式，如果是多媒体等格式的文件就要使用二进制模式，以保证读取和写入的数据是一致的。
参见 `Windows 上的 fopen 手册 <https://docs.microsoft.com/zh-cn/cpp/c-runtime-library/reference/fopen-wfopen?view=vs-2017>`_。

在类 Unix 系统上这两种模式是等价的，也即均为 'b' 模式，遵循 POSIX 标准的 C 库函数不会对数据进行任何转换，而把这些处理交给用户空间的编辑器。

::
  
  open(file, mode='r', buffering=-1, encoding=None, errors=None, 
       newline=None, closefd=True, opener=None)
      Open file and return a stream.  Raise IOError upon failure.

在 Python 中，和 c 接口中的意义有所不同，只有 'b' 模式，且并不作为转换模式使用，而是指定参数的类型：指定了 'b' 模式，那么写入参数必须是 bytes 类型，同样读取返回的也是 bytes 类型：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  # 'b' 模式中，write 参数必须是 bytes 类型的
  with open('test.txt', 'wb') as fw:
    fw.write('一abc')
    
    # 正确写入方式为
    # fw.write(bytes('一abc', encoding='utf-8'))
    
  >>>
  TypeError: a bytes-like object is required, not 'str'

同样读取时如果指定了 'b' 模式，则返回 bytes 类型：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  with open('wb.txt', 'rb') as fr:
    print(fr.read())
  
  >>>
  b'\xe4\xb8\x80abc'

通常对文件操作时应该明确指定编码格式，例如：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  def test_file_encode():
    with open('wb.txt', 'w', encoding='utf-8') as fw:
      fw.write('一abc') # 非 'b' 模式可以直接写入字符串

    # 如果此处打开模式为 'rb' 则 fr.read() 返回 bytes 类型
    with open('wb.txt', 'r', encoding='utf-8') as fr:
      print(fr.read()) # 自动使用 encoding 参数进行解码

  test_file_encode()
  
  >>>
  一abc

可以通过 hexdump 查看写出的文件内容：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  # hexdump 查看写出文件，可以发现前三个字节为 '一' 的 unicode 码值的 utf-8 编码 
  $ hexdump -C wb.txt 
  00000000  e4 b8 80 61 62 63                                 |...abc|

指定文件编码
~~~~~~~~~~~~~~~

open() 函数实现文件的打开，它返回一个文件描述符，在 Python 里它是一个文件对象。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  f = open("test.txt", 'r')
  print(f)
  
  >>>
  # Windows 运行结果
  <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp936'>
  
  # Linux 运行结果
  <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

这里之所以打印文件对象，是要查看编码，发现在不同的平台上它的值是不同的，该参数可以在打开文件时指定，如果不指定，则使用 locale.getpreferredencoding() 获取。
它用于文本模式时如何解码读取的文件数据，或者如何编码写入到文件。关于编码格式参考 :ref:`general_encode` 。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(locale.getpreferredencoding(False))

  >>>
  cp936

cp936 编码，也即 GBK 编码，所以在 Windows 上默认读写文件使用该编码方式，在 Linux 上则是 UTF-8。那么相同的文件，由于解码不同，就会读取出错，写入也一样。

为了能够正确读取文件，应该指明要读写的文件的编码方式，通常我们使用 UTF-8 编码来保存中文文档。Python3.7 版本后，locale.getpreferredencoding() 总是返回 UTF-8，以和 Python 默认编码保持一致，不再依赖于系统环境。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  f = open("test.txt", 'r', encoding='UTF-8')
  print(f)

  >>>
  <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

当完成读写操作后，应关闭文件描述符，以将缓存数据写入磁盘，并释放系统资源，这非常简单：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  f.close()

文件描述符的属性
~~~~~~~~~~~~~~~~~

在 Python 中，文件描述符就是一个文件对象，它具有如下属性：

  =============== =============================================================
     属性         描述
  --------------- -------------------------------------------------------------
  file.closed     返回布尔值，True 已被关闭。
  file.mode       返回被打开文件的访问模式。
  file.name       返回文件的名称。
  =============== =============================================================

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  f = open("test.txt", 'r', encoding="UTF-8")
  print ("name: %s, closed: %s, mode:'%s'" % (f.name, f.closed, f.mode))
  f.close()
  print ("name: %s, closed: %s, mode:'%s'" % (f.name, f.closed, f.mode))
  
  >>>
  name: test.txt, closed: False, mode:'r'
  name: test.txt, closed: True, mode:'r'

文件对象内建方法
--------------------

按功能划分文件对象内建方法：

- 关闭

  - file.close() 关闭文件。

- 读取

  - file.read([size=-1]) 从文件读取指定的字节数，如未指定或为负则读取所有，返回读取数据，无数据时返回空字符串 ''。
  - file.readline([size=-1]) 读取一行含换行符，如指定正整数，则最多返回 size 个字符。
  - file.readlines([hint=-1]) 读取所有行以列表返回，如指定整数，至少读取 hint 个字符，确保最后读取的行是完整的。     

- 写入和截断
  
  - file.write(str) 将字符串写入文件，返回写入的字符长度。
  - file.writelines(sequence) 向文件写入字符串序列（必须是字符串序列），比如列表，元组，如需要换行需自行加入换行符。
  - file.flush() 刷新缓冲区数据到文件。
  - file.truncate([size]) 截断文件，截断文件指针偏移处之后数据，如指定正整数，则把文件截断为 size 字节，不影响指针偏移。

- 文件指针偏移

  - file.seek(offset[, whence]) 移动文件指针到指定偏移位置。如指定参数 whence，则移动偏移相对于 0 文件开始, 1 当前位置, 2 文件末尾。
  - file.tell() 返回文件指针偏移位置。

- 文件描述符
  
  - file.fileno() 返回整型文件描述符，用于 os 模块方法。
    
- 判定

  - file.isatty() 如果文件连接到一个终端设备返回 True。

.. admonition:: 注意

  任何对文件的读取和写入动作，都会自动改变文件的指针偏移位置。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  with open("sample.py", 'r') as f:
    data = f.read()
    data = f.read()
    print(repr(data))
  
  >>>
  ''

文件或目录常用操作
-------------------

文件或目录创建删除
~~~~~~~~~~~~~~~~~~~

创建删除文件
``````````````

普通文件使用 open() 写模式即可创建。对应的删除方法为 os.remove()。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  fname = "test.txt"
  with open(fname, 'w'):
      pass
  
  os.remove(fname) # 删除当前目录下 test.txt 文件  
  os.unlink(fname)

os.unlink() 行为与 os.remove() 一致，函数无返回，如果文件不存在，报错 FileNotFoundError。

创建删除目录
``````````````

在当前文件夹下创建单级目录使用 os.mkdir(dirname)，创建多级目录使用 os.makedirs(dirpath)。

.. code-block:: python
  :linenos:
  :lineno-start: 0
          
  print(os.mkdir("folder")) 
  print(os.makedirs("parent/folder"))

函数无返回，如果文件夹存在则抛出 FileExistsError 错误。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  import os,shutil
  
  os.rmdir("parent/folder")     # 一级目录删除
  os.removedirs("parent/folder")# 递归删除
  
  shutil.rmtree("parent")       # 强制删除 parent 文件夹
  shutil.rmtree("parent/folder")# 强制删除 folder 文件夹

与创建函数类似，以上函数均无返回值，如果删除目录不存在，不会报错。

- os.rmdir() 只删除最后一级目录 folder，并且 folder 必须为空，否则报错目录非空的 OSError。
- os.removedirs() 与 os.rmdir() 类似，文件夹必须为空，首先删除 folder，然后再删除 parent。
- shutil.rmtree() 无论目录是否非空，强制删除整个文件夹，应慎用。

临时文件和目录
``````````````

手动创建和删除临时文件。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  filename = '/tmp/tmp_file_%s.txt' % os.getpid()
  try:
      f = open(filename, 'w')
  except:
      pass
  else:
      print(f.name)
      f.close()
      os.remove(f.name)
  
  >>>  
  /tmp/tmp_file_10973.txt

手动创建临时文件有几个缺点，首先需要获得一个唯一的临时文件名称，其次其他程序也可以访问该文件，这为信息安全留下隐患。

使用 tempfile 模块创建临时文件是最好的选择。其他程序无法找到或打开该文件，因为它并没有引用文件系统表，同时用这个函数创建的临时文件，关闭后会自动删除。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  import tempfile
  
  try:
      tempf = tempfile.TemporaryFile()
  except:
      pass
  else:
      print(tempf)
      print(tempf.name)
      tempf.close() # 关闭时自动删除
   
  >>>
  <_io.BufferedRandom name=4>
  4
  
使用 tempfile 模块创建临时文件无需指定文件名。需要注意的是默认使用 w+b 权限创建文件，文本模式请使用参数 'w+t' 生成临时文件。

如果需要和其他程序共享临时文件，需要生成具名的临时文件：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  try:
      tempf = tempfile.NamedTemporaryFile('w+t')
  except:
      pass
  else:
      print(tempf)
      print(tempf.name)
      tempf.close() # 关闭时自动删除
  
  >>>
  <tempfile._TemporaryFileWrapper object at 0xb71d7a2c>
  /tmp/tmpas7rymlm

这里使用权限 'w+t' 生成的临时文件将使用文本模式读写，它在关闭后也会被自动删除。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  tempdir = tempfile.mkdtemp()
  print(tempdir)
  
  os.removedirs(tempdir) # 手动删除临时文件夹

  >>>
  /tmp/tmpffpyahtn

.. admonition:: 注意

  tempfile.mkdtemp() 生成的临时文件夹，必须手动删除。

文件和目录重命名
~~~~~~~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  try:
      os.rename('fname0', 'fname1')
  ......

文件和文件夹均使用 os.rename() 方法更名，成功无返回，如果文件不存在，则报错 FileNotFoundError。

.. admonition:: 注意

  当目标文件或文件夹存在时，os.rename() 不会报错，而是直接覆盖。

获取文件或文件夹大小
~~~~~~~~~~~~~~~~~~~~

os.path.getsize(fname) 返回文件大小，如果文件不存在报错 FileNotFoundError：

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  fname = "test.txt"
  # os.stat(fname).st_size ，实际上 getsize() 方法与此等价
  fsize = os.path.getsize(fname)
  print(fsize)
  
  >>>
  30

注意，如果参数指定文件夹，并不会报错，而是返回文件夹节点占用的物理存储空间大小，而不是整个文件夹内容的大小。
获取文件夹大小需要 os.walk() 遍历函数实现。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  def get_folder_size(path):
      total_size = 0
      for item in os.walk(path):
          for file in item[2]:
              try:
                  total_size += os.path.getsize(os.path.join(item[0], file))
              except Exception as e:
                  print("error with file:  " + os.path.join(item[0], file))
      return total_size
  
  print(get_folder_size('.'))
  
  >>>
  51171

复制或移动文件和目录
~~~~~~~~~~~~~~~~~~~~~

文件复制
```````````
::

  shutil.copyfile(src, dst, *, follow_symlinks=True)
          Copy data from src to dst.

shutile 模块的 copyfile() 方法将 src 指定的文件复制为 dst 文件，注意：

- src 和 dst 必须都是文件路径，不可以是文件夹。
- 如果 src 不存在，报错 FileNotFoundError。
- 如果 dst 文件已存在，那么会覆盖。
- follow_symlinks 为 True ，则 src 如果为软连接，则复制后 dst 也是软连接。
- 复制成功，返回新文件的路径。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  try:
      shutil.copyfile("oldfile", "newfile")
  .....

目录复制
```````````

shutile 模块的 copytree() 方法用于复制目录，symlinks 参数指明是复制软连接还是复制文件。

::

  copytree(srcdir, dstdir, symlinks=False, ignore=None, copy_function=<function copy2>, 
    ignore_dangling_symlinks=False)
      Recursively copy a directory tree.

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  try:
      shutil.copytree("srcdir", "dstdir") 
  ......
  
注意 srcdir 和 newdir 都只能是目录，且 newdir 必须不存在，否则报 FileExistsError。成功返回目标目录路径。

移动文件和目录
```````````````

::

  move(src, dst, copy_function=<function copy2>)
      Recursively move a file or directory to another location. This is
      similar to the Unix "mv" command. Return the file or directory's
      destination.
      
移动文件和目录均使用 shutil.move()函数，类似于 Unix 下的 mv 命令。成功返回目标文件或目录。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  try:
      shutil.move("src", "dst") 
  ......

需要注意以下几点：

- src 文件或者目录必须存在，否则报错 FileNotFoundError
- dst 如果存在并且是目录，则把 src 复制到 dst/ 下
- dst 如果不存在，则直接把 src 复制为 dst。

文件和目录属性判定
---------------------

有时候，我们需要判断特定路径的属性，比如是文件还是目录，如果路径不存在，这类函数不会触发异常，而是返回 False，常见判定操作如下：

  =========================  ==========================================
   判定方法                   描述
  =========================  ==========================================
  os.path.isabs()            判断是否为绝对路径，以 "/" 开始的路径均为 True
  os.path.isfile()           判断路径是否为文件，支持软连接
  os.path.isdir()            判断路径是否为目录，支持软连接
  os.path.islink(path)       判断路径是否为链接
  os.path.ismount(path)      判断路径是否为挂载点
  os.path.exists(path)       路径存在则返回 True, 否则返回 False
  =========================  ==========================================

以下函数，如果参数不合法，则会报相应的异常错误：

  =================================  ==========================================
   判定方法                            描述
  =================================  ==========================================
  os.path.samefile(src, dst)         两个路径名是否指向同个文件后者文件夹
  os.path.sameopenfile(fp1, fp2)     判断 fp1 和 fp2 文件描述符是否指向同一文件
  os.path.samestat(stat1, stat2)     判断文件状态 stat1 和 stat2 是否指向同一个文件
  =================================  ==========================================

文件名和路径操作
------------------

文件名和路径分割
~~~~~~~~~~~~~~~~~

下列方法不关心目录或者文件是否真实存在，它们只进行字符层面的处理，不会触发异常错误。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  abspath = os.path.abspath("tmp.txt") # 返回绝对路径
  basename = os.path.basename(abspath) # 返回文件名
  dirname = os.path.dirname(abspath)   # 返回文件路径
  
  print(abspath)
  print(basename)
  print(dirname)
  print(os.path.split(abspath))        # 分割路径和文件名，返回元组类型
  print(os.path.splitext(abspath))     # 分割扩展名，返回元组类型
  
  >>>
  /home/red/sdc/lbooks/ml/tmp.txt
  tmp.txt
  /home/red/sdc/lbooks/ml
  ('/home/red/sdc/lbooks/ml/tmp', '.txt')
  ('/home/red/sdc/lbooks/ml', 'tmp.txt')

还有 os.path.splitdrive(path) 方法一般用于 Windows 平台，返回驱动器名和路径组成的元组。

最长路径
~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  path_list0 = ["/home/red/", "/home/john", "/home/lily"]
  path_list1 = ["/home/VIPred/", "/home/VIPjohn", "/home/VIPlily"]
  commonpath0 = os.path.commonprefix(path_list0)
  commonpath1 = os.path.commonprefix(path_list1) 

  print(commonpath0)
  print(commonpath1)
  
  >>>
  /home/
  /home/VIP

os.path.commonprefix() 方法返回所有 path 共有的最长的路径，示例可以看出，它只是在字符层面进行匹配，它返回的不一定是路径，而只是最长匹配的字符串。

路径合成
~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0

  path = os.path.join("123", "456", "tmp")  #把目录和文件名合成一个路径
  print(path)
  
  >>>
  
  123/456/tmp   # Linux 平台
  123\456\tmp   # Windows 平台

os.path.join() 方法只进行字符层面的拼接，不同的平台拼接字符可能不一致，这与 ``'/'.join()`` 不同。

路径转换和规范化
~~~~~~~~~~~~~~~~

绝对路径和相对路径
````````````````````

::

   os.path.relpath(path, start=os.curdir)  Return a relative version of a path

os.path.relpath() 方法支持设定参考路径，默认为 Python 当前工作路径。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  path = "/tmp/text.txt"
  realpath = os.path.realpath(path)  # 返回 path 的真实路径，将忽略任何软连接
  relpath = os.path.relpath(path)   

  print(realpath)
  print(relpath)
  >>>
  
  # Linux 平台
  C:\tmp\text.txt
  ..\..\..\..\tmp\text.txt

  # Windows 平台
  /tmp/text.txt
  ../../../../../tmp/text.txt

路径相关的方法是以来于系统平台的，不同平台有不同的路径表示方法，注意区别。

路径规范化
````````````````````
.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  path = "/tmp/../text.txt"
  normcase = os.path.normcase(path) 
  normpath = os.path.normpath(path)
  
  print(normcase)
  print(normpath)
  
  >>>
  # Linux 平台
  \tmp\..\text.txt
  \text.txt
  
  # Winodws 平台
  /tmp/../text.txt
  /text.txt

- os.path.normcase(path) 通常用于路径大小写不敏感的文件系统，路径转化为小写，在Unix 和 Mac 不对路径做任何改变，Winodws 上会把 "/" 转化为 "\"。
- os.path.normpath(path) 标准化路径，消除路径冗余，比如将 A//B, A/B/, A/./B and A/foo/../B 转化为 A/B。

文件相关的时间
-----------------

时间戳分类
~~~~~~~~~~~~~~

每一个文件或者目录都有记录相应操作的时间戳，通常将它们分为以下几类：

- 最后的访问时间（access time）标记为   atime。通常访问文件，比如读取时会更新访问时间。但是由于文件的时间戳是要记录在磁盘上的，如果每次访问都要写磁盘，将严重影响I/O效率，所以通常使用 relative atime 策略，也即当访问时，发现文件的 ctime 或者 mtime 比 atime 新时才更新。
- 最后的修改时间（modify time）标记为 mtime。当文件内容发生改变时更新该时间。
- 最后的更改时间（change time）标记为 ctime。Linux上，当文件内容，或者属性（所有者，操作权限，所在目录）改变时更新该时间。
- 文件的创建时间（create time）被标记为 Birth，依赖文件系统格式 Linux 上目前不支持获取该时间，在 Winodes 上它被标记为 ctime。 

在 Linux 上获取时间戳的命令是 stat ：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  # stat tmp.txt 
    File: ‘test.txt’
    Size: 0         	Blocks: 0          IO Block: 4096   regular empty file
  Device: 821h/2081d	Inode: 334232      Links: 1
  Access: (0777/-rwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
  Access: 2017-08-02 12:08:03.475780700 +0800
  Modify: 2017-08-02 12:08:03.475780700 +0800
  Change: 2017-08-02 12:08:03.475780700 +0800
   Birth: -

获取时间戳
~~~~~~~~~~~~~~

os.path 模块提供了三种方法来获取时间戳，其中 getctime() 在 Linux 上表示为 change time，而在 Windows 上获取的则是文件的创建时间。
这三个函数均是返回从 epoch (1970.1.1 00:00:00) 到当前时刻的秒数，浮点表示，参数也可以为路径，如果文件或目录不存在，报错 FileNotFoundError。 

.. code-block:: python
  :linenos:
  :lineno-start: 0

  fname = "test.txt"
  
  try:
      atime = os.path.getatime(fname) 
      mtime = os.path.getmtime(fname) 
      ctime = os.path.getctime(fname)  
  except:
      pass
  else:
      print(atime)
      print(mtime)
      print(ctime)
    
  >>>
  1501646883.4757807
  1501646892.1091917
  1501646892.1091917

文件的时间戳常被用于数据同步，编译等操作。更详细的描述请参考 `Unix 文件系统中的时间戳 <https://www.unixtutorial.org/atime-ctime-mtime-in-unix-filesystems/>`_。

更新访问和修改时间
~~~~~~~~~~~~~~~~~~~~~~

::

  utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True)
      Set the access and modified time of path.

os.utime() 方法可以更新文件或者目录的访问和修改时间，如果不提供 times 参数，则使用当前时间，否则 times 参数应该是形为 (atime, mtime) 的元组。它们是相对于 epoch 以来的秒数。

注意路径必须存在，否则报错 FileNotFoundError。

.. code-block:: python
  :linenos:
  :lineno-start: 0

  fname = "test.txt"
  
  try:
      #os.utime(fname)，更新为当前时间
      os.utime(fname, (1530714880.9, 1530714592))
  except:
      pass
  else:
      print(os.path.getatime(fname))  
      print(os.path.getmtime(fname))  
  
  >>>
  1530714880.9
  1530714592.0
  1543464892.8930445

返回指定目录下的所有文件和目录名:os.listdir()

文件属性和权限
-----------------

::

  stat(path, *, dir_fd=None, follow_symlinks=True)
      Perform a stat system call on the given path.
    
os.stat() 方法获取文件各类属性，主要包括文件权限，文件所属，链接状态，大小和时间戳。
os.path.getsize() 方法底层就是调用该方法获取文件大小的。

.. code-block:: python
  :linenos:
  :lineno-start: 0
  
  print(os.stat("test.txt"))
  
  >>> 
  os.stat_result(st_mode=33206, st_ino=1125899907973557, st_dev=2028413472, 
  st_nlink=1, st_uid=0, st_gid=0, st_size=30, st_atime=1543471075, 
  st_mtime=1543471075, st_ctime=1543236918)  
  
修改文件权限，文件所属操作请参考 `os.chmod() 和 os.chown() 手册 <https://docs.python.org/3/library/os.html?highlight=os%20chmod#os.chmod>`_。

文件路径遍历
-----------------

遍历当前目录
~~~~~~~~~~~~~~~

os.listdir(path) 返回 path 指定的文件夹包含的文件或文件夹的名字的列表。参数必须是文件夹，否则报错 NotADirectoryError。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  try:
      paths = os.listdir('.')
  except:
      pass
  else:
    print(paths)
  
  >>>
  ['text.py', 'fileopt.py', ......]

遍历所有子目录
~~~~~~~~~~~~~~~

::

  os.walk(top, topdown=True, onerror=None, followlinks=False)
       Directory tree generator.

os.walk() 中的 top 参数指定遍历文件夹， topdown 指定遍历顺序，默认从上层到子文件夹。
可以通过 os.walk() 统计文件夹大小，对每个文件进行特定处理等。

os.walk() 返回目录树迭代对象，对象成员是一个三元组，形式为 (root, dirs, files)，分别对应目录，目录中文件夹和目录中文件。

.. code-block:: python
  :linenos:
  :lineno-start: 0
    
  import os
  from os.path import join, getsize
  for root, dirs, files in os.walk('.'):
      print(root, "consumes", end="")
      print(sum([getsize(join(root, name)) for name in files]), end="")
      print("bytes in", len(files), "non-directory files")
      if '.git' in dirs:
          dirs.remove('.git')  # don't visit .git directories

  >>>
  . consumes 44843bytes in 31 non-directory files
  ./folder consumes 0bytes in 0 non-directory files
  ......

以上示例，统计每个文件夹中文件所占大小，并忽略 .git 文件夹。  os.walk() 非常适合对文件进行信息统计和批处理操作，以下是一个用于把文件夹下所有文件扩展名改为小写的函数实现：

.. code-block:: python
  :linenos:
  :lineno-start: 0

  import os
  def lower_file_extname(path):
      for root, dirs, files in os.walk(path):
          for i in files:
                oldpath = os.path.join(root, i)
                splits = os.path.splitext(oldpath)
                if len(splits) != 2:
                    continue
                
                newpath = splits[0] + splits[1].lower()
                try:
                    os.rename(oldpath, newpath)
                except Exception as e:
                    print(e)

文件操作模块  
--------------------

os 模块提供一些可移植的功能函数，它们的底层依赖于操作系统。 其中 os.path 模块封装了路径相关的方法。

tempfile 模块主要提供临时文件的创建和使用。shutil 模块提供更高层的文件和目录操作方法。

其他常用的文件操作模块如下：

===================   ==========================================
  模块                描述
===================   ==========================================
base64                提供二进制字符串和文本字符串间的编码/解码操作
binascii              提供二进制和 ASCII 编码的二进制字符串间的编码/解码操作
bz2a                  访问 BZ2 格式的压缩文件
csv                   访问 csv 文件(逗号分隔文件)
filecmpb              用于比较目录和文件
fileinput             提供多个文本文件的行迭代器
getopt/optparsea      提供了命令行参数的解析/处理
glob/fnmatch          提供 Unix 样式的通配符匹配的功能
gzip/zlib             读写 GNU zip( gzip) 文件(压缩需要 zlib 模块)
shutil                提供高级文件访问功能
c/StringIO            对字符串对象提供类文件接口
tarfilea              读写 TAR 归档文件, 支持压缩文件
tempfile              创建一个临时文件(名)
uu                    格式的编码和解码
zipfilec              用于读取 ZIP 归档文件的工具
===================   ==========================================
