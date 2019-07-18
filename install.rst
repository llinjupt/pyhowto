Python 环境配置
================

Python 语言是一种动态的脚本语言，需要动态解析，当前分为主流的 Python2 和 Python3 版本，它们的语法是不安全兼容的，也即 Python3 通常无法直接执行 Python2 版本的 .py 文件。

所以在安装之前需要确定需要安装的 Python 版本。由于不同的应用软件需要不同的 Python 开发环境，可能需要同时安装多个 Python 版本，那么防止冲突，可以使用 virtualenv 实现安装环境的隔离。

另外注意：在 Linux 环境中安装软件时确保磁盘的文件系统支持软连接，不要使用共享的 Windows 磁盘安装，FAT32 和 NTFS 由于不支持软连接，可能导致安装时出现异常错误。

简单安装
---------------

这里以 Ubuntu 为例，安装命令异常简单：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  # sudo apt-get install python2.7  
  $ sudo apt-get install python3.6

安装后通过查看版本验证环境是否安装成功：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ python3.6 --version
  Python 3.6.3

与此同时 Python 的软件包包管理器 pip 也被一同安装了：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip -V
  pip 19.1.1 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
  
通过 pip 安装的软件包将放置到 /usr/local/lib/python3.6/dist-packages 下。

直接使用 apt-get install 安装多个版本的 Python 可能导致 pip 包管理器混乱：此时会出现多个以 pip 开头的命名，例如 pip2，pip3。但是这并不意味着它们就分别对应 Python2 和 Python3，通过执行 pipx -V 查看它对应的 python 解释器版本，这样使用 pip install 就会安装到对应版本解释器的 dist-packages 文件夹下。

当然也可以通过源码直接安装，由于各种平台的软件管理工具已经非常成熟，通常不推荐这样做，例如：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ wget -c https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz  
  $ tar -xzvf Python-2.7.9.tgz  
  $ cd Python-2.7.9/  
  $ LDFLAGS="-L/usr/lib/x86_64-linux-gnu" ./configure  
  $ make  
  $ sudo make install   

Windows 平台有对应的 exe 或者 msi 安装文件，安装时选中安装环境变量即可，如果在命令行中无法运行 python，则需手动添加环境变量。

多版本安装
------------

直接使用 apt-get install 安装 Python3，当安装多个 Python3.x 版本时，pip 就会冲突。我们需要手动解决这种冲突，方法就是重装 pip。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  $ python get-pip.py

首先下载 get-pip.py 脚本，通过它就可以为不同版本的python安装对应的 pip 软件包了：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ python2.7 get-pip.py  
  $ python3.6 get-pip.py  
  
  # 安装完毕后查看版本对应情况
  $ pip -V
  $ pip2 -V
  $ pip3 -V

如果不对应需要将 pip 更名为对应版本，例如 pip3 对应 python3.6，更名为 pip3.6。

virtualenv
~~~~~~~~~~~~

virtualenv 是一个强大的 python 安装环境管理工具，可以实现不同 python 运行环境的隔离。特别适用于某种特殊应用，例如 tensorflow 可能依赖于一些特定版本的第三方软件包，所以即便同样是 python3.x 版本，由于其他软件包的依赖问题，应该单独为它建立一个 tensorflow 的开发环境。否则一旦更新软件包，很可能导致已经安装好的环境无法使用，恢复起来也非常麻烦。

virtualenv 基于当前系统中已经安装的 Python 环境来创建隔离的运行环境。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip install virtualenv

这里为 tensorflow 创建一个独立的Python运行环境：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  # 为项目环境创建目录，所有安装文件均被防止在该目录下，而与外部其他Python环境无关
  $ mkdir tfproj
  $ cd tfproj/

接着使用 virtualenv 创建运行环境：
  
.. code-block:: sh
  :linenos:
  :lineno-start: 0
    
  # --no-site-packages 表示不可访问外部软件包
  $ virtualenv --no-site-packages tfenv

virtualenv 默认使用系统中的 python 创建系统环境，使用 python -V 查看默认的 python 版本。

当然可以指定特定的 python 版本，例如：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ virtualenv -p /usr/bin/python3.6 --no-site-packages py36tfenv

创建完毕后，文件下将创建 tfenv 路径：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ ll
  total 8
  drwxrwxrwx 1 root root  144 Jul 13 17:58 ./
  drwxrwxrwx 1 root root 8192 Jul 13 18:05 ../
  drwxrwxrwx 1 root root  224 Jul 13 17:58 tfenv/
  
  # 默认安装了包管理软件 pip 
  $ find . -name pip
  ./tfenv/bin/pip
  ./tfenv/lib/python3.6/site-packages/pip

使用 source 使能虚拟开发环境:

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  # 进入虚拟环境，注意 shell 提示符出现的变化
  $ source tfenv/bin/activate
  (tfenv) hadoop@hadoop0:/home/red/sdd/tfproj$
  
  (tfenv) hadoop@hadoop0:/home/red/sdd/tfproj$ env |grep PATH
  PATH=/home/red/sdd/tfproj/tfenv/bin:...
 
默认安装了包管理软件 pip，和在主机上一样，使用它为这个独立环境安装第三方软件包。

若要退出当前的 tfenv 环境，使用 deactivate 命令。

virtualenv 在创建独立虚拟运行环境时把指定的 python 命令和它依赖的库文件复制一份到当前虚拟环境， 命令 source tfenv/bin/activate 会修改相关环境变量，此时交互 shell 中的 PATH 等环境变量指向了当前虚拟环境所在路径，所以 python 和 pip 也指向当前的虚拟环境。

安装编译环境
~~~~~~~~~~~~~~~~

有些第三方安装包在安装前需要编译，如果没有安装编译环境，安装时将提示找不到 Python.h，例如：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  ...
  # include <Python.h>
                       ^
  compilation terminated.
  error: command 'i686-linux-gnu-gcc' failed with exit status 1

安装对应编译环境的头文件和库文件命令：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ sudo apt-get install python3.6-dev
  Reading package lists... Done
  Building dependency tree       
  Reading state information... Done
  The following extra packages will be installed:
    libpython3.6 libpython3.6-dev
  ...

安装时应指定对应的 Python 版本，例如 python3.6-dev 或 python2.7-dev。
 
pip 管理软件包
---------------

pip 安装软件包
~~~~~~~~~~~~~~~~

pip 安装 python 软件包非常方便，首先通过 pip -V 查看是否是我们要安装的 python 环境，如果不是这要安装多版本方式重新安装，或者对 pip 重命名。如果所有用户都可以使用该开发环境，那么需要在安装命令前使用 sudo 安装。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ whereis pip
  pip: /usr/local/bin/pip3.6 /usr/local/bin/pip2.7 \
  /usr/local/bin/pip /usr/local/bin/pip3.4

whereis 命令查看 pip 命令，笔者环境中存在多个版本的 pip 管理器，此时 pip 通常是一个软连接，执行实际的某个版本的 pipx。

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip install numpy

  # 要用 pip 安装指定版本的 Python 包，只需通过 == 操作符指定
  $ pip install robotframework==2.8.7

如果软件包比较大，而网络不稳定，可能导致安装失败，可以通过 wget 等方式下载 pip 要安装的软件包：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip install numpy
  Collecting numpy
  Downloading https://.../numpy-1.16.4-cp36-cp36m-manylinux1_i686.whl (14.8MB)

pip 安装时会打印出下载的软件包的路径，此时使用 wget 或者浏览器直接下载，下载的文件直接通过 pip install filename 安装即可，例如:

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip install numpy-1.16.4-cp36-cp36m-manylinux1_i686.whl
  Processing ./numpy-1.16.4-cp36-cp36m-manylinux1_i686.whl
  Installing collected packages: numpy
  Successfully installed numpy-1.16.4

如果我们想更新已有软件包，命令为：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  # 或者 pip install -U pip
  $ pip install --upgrade pip

pip 卸载软件包
~~~~~~~~~~~~~~~~~

卸载与安装相对应，使用 uninstall 命令，例如：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip uninstall numpy

pip 查看软件包
~~~~~~~~~~~~~~

查看所有通过当前 pip 安装的软件包：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip list
  Package                       Version           
  ----------------------------- ------------------
  appdirs                       1.4.3             
  atomicwrites                  1.3.0         
  ...    

pip show 查看单个软件包信息，包含版本，官网，作者，发布协议，安装路径和对其他软件包的依赖关系：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip show urllib3
  Name: urllib3
  Version: 1.25.3
  Summary: HTTP library with thread-safe connection pooling, file post, and more.
  Home-page: https://urllib3.readthedocs.io/
  Author: Andrey Petrov
  Author-email: andrey.petrov@shazow.net
  License: MIT
  Location: /usr/local/lib/python3.6/dist-packages
  Requires: 
  Required-by: requests, pyppeteer

查看 pip 帮助
~~~~~~~~~~~~~~~

普通的 linux 命令使用 man cmd 查看帮助信息，但是 pip 是 python 脚本，查看帮助信息方式为：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  # 或者 pip --help
  $ pip -h

  Usage:   
    pip <command> [options]
  
  Commands:
    install                     Install packages.
    download                    Download packages.
    uninstall                   Uninstall packages.
    freeze                      Output installed packages in requirements format.
    list                        List installed packages.
    ...

也可以针对单个命令字查看它支持的选项，例如：

.. code-block:: sh
  :linenos:
  :lineno-start: 0
  
  $ pip install -h

  Usage:   
    pip install [options] <requirement specifier> [package-index-options] ...
    pip install [options] -r <requirements file> [package-index-options] ...
    pip install [options] [-e] <vcs project url> ...
    pip install [options] [-e] <local project path> ...
    pip install [options] <archive url/path> ...
    ...

