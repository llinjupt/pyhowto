连接数据库
============

对于数据库的操作通常分为以下几个步骤，Python 相关的数据库模块同样遵循它们：

- connect 连接数据库。
- 获取游标（Cursor），用于执行 SQL 语句。
- 数据库操作 execute：删除，插入，查询等。
- 提交数据 commit。
- 关闭游标和数据库 close。

所以 Python 提供了相对统一的数据库访问 API。

sqlite
----------

sqlite 是文件型轻量级数据库，也即所有数据信息都保存在一个文件中，对数据库操作也直接访问数据文件，无需服务端，无需网络通信。不需要安装和配置，简单易用，数据易于迁移。
适用于单一存储业务，嵌入式应用，移动应用和游戏。 sqlite 数据库同一时间只允许一个写操作，吞吐量有限，不适合大型并发应用。

sqlite3 默认使用 utf-8 编码存储数据。

连接和关闭
~~~~~~~~~~~~~

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  import sqlite3
  
  # 连接数据库 
  conn = sqlite3.connect('sqlite.db')
  cursor = conn.cursor()
  
  print(type(conn).__name__)
  print(type(cursor).__name__)
  
  # 表操作和提交
  
  cursor.close() # 关闭游标
  conn.close()   # 关闭数据库 
  
  >>>
  Connection
  Cursor

表的操作
~~~~~~~~~~~~

SQL语句中如果包含单引号或者双引号，应使用三引号引用语句。 

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  # 创建表
  cursor.execute('''create table test
                 (id      char(32) primary key not null,
                  name    text    not null,
                  age     int     not null);''')

  # 插入
  cursor.execute('''insert into test (id, name, age) values ('000', 'John', '23')''')
  cursor.execute('''insert into test (id, name, age) values ('001', 'Tom', '25')''')
  cursor.execute('''insert into test (id, name, age) values ('002', 'Jack', '29')''')

  cursor.execute('select * from test')
  
  print(cursor.fetchone()) # 从查询结果集中返回一条，无返回 None
  all = cursor.fetchall()  # 取查询结果集中所有行（如使用过fetchone，则返回其余行）无返回一个空列表。
  print (all)
  
  # 删除表
  cursor.execute('drop table test')
  conn.commit()
  
  # 返还磁盘空间，否则删除的空间只会插入空闲链表
  cursor.execute('vacuum') 

  cursor.close()
  conn.close()

  >>>
  ('000', 'John', 23)
  [('001', 'Tom', 25), ('002', 'Jack', 29)]


注意事项
~~~~~~~~~~

Connection 和 Cursor 对象，打开后一定记得关闭。

如果进行删除表并需要释放磁盘空间，应在 commit 后执行 vacuum 命令。

mysql
-----------

mysql 环境配置
~~~~~~~~~~~~~~~~~~~

使用 mysql 要比 sqlite 复杂一些，需要安装服务端和客户端并进行一些参数配置。它功能强大，支持高并发。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  # 如已配置过 mysql 环境，使用如下命令测试，应进入交互模式
  mysql -u root -p

  # 如果提示 host 无法解析，表示本机通信无法建立
  cat /etc/hostname  # 例如为 ubuntu，在 /etc/hosts 中添加 127.0.0.1 ubuntu
  
  # 以Ubuntu14.04 环境为例，杀死相关进程
  ps -A |grep mysql
  kill -9 xxxx
  
  # 删除安装包
  sudo apt-get remove mysql-*
  sudo rm -rf /usr/share/mysql/
  sudo rm -rf /etc/mysql/conf.d
  
  # 安装过程中会提示设置 root 密码
  sudo apt-get install mysql-server
  sudo apt-get install mysql-client
  
  # 查看运行状态
  sudo service mysql status
  # mysql start/running, process 12193
  
  # 如果没有运行则手动启动
  sudo service mysql start
  
为了保证数据的通用性，应该设置 UTF8 编码，通过如下方式查看：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  # 进入交互终端
  mysql -u root -p
  
  mysql> show variables like 'character_set%';
  +--------------------------+----------------------------+
  | Variable_name            | Value                      |
  +--------------------------+----------------------------+
  | character_set_client     | utf8                       |
  | character_set_connection | utf8                       |
  | character_set_database   | utf8                       |
  | character_set_filesystem | binary                     |
  | character_set_results    | utf8                       |
  | character_set_server     | utf8                       |
  | character_set_system     | utf8                       |
  | character_sets_dir       | /usr/share/mysql/charsets/ |
  +--------------------------+----------------------------+
  8 rows in set (0.00 sec)

如果编码相关值不是 utf8 ，应该通过配置文件 /etc/mysql/my.cnf 配置：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  [client] # client 字段下添加
  default-character-set = utf8
  
  [mysqld] # mysqld 字段下添加
  character-set-server = utf8

  sudo service mysql restart

  # 如果在更改配置文件后启动失败，查看日志文件，根据提示修改
  cat /var/log/mysql/error.log

设置完毕后进入交互终端确认编码生效。

Python 链接 mysql 数据库需要安装第三方驱动，例如 mysql-connector：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  pip install mysql-connector

数据库操作
~~~~~~~~~~~~~~~

mysql 数据库操作与 sqlite 流程基本一致：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  import mysql.connector
  
  # 如果数据库已经存在，可以直接指定  db='dbname' 参数
  conn = mysql.connector.connect(host='127.0.0.1', port=3306, user='root', 
                                 password='password', charset='utf8')
  cursor = conn.cursor()
  cursor.execute('show databases') # 查询数据库
  print(cursor.fetchall())         # 查询命令后必须进行 fetch 操作
  
  # 创建 test 数据库
  cursor.execute('create database if not exists test')
  cursor.execute('use test')
  
  try:
      cursor.execute('''create table test
                     (id      char(32) primary key not null,
                      name    test    not null,
                      age     int     not null);''')
  except:
      pass
  
  cursor.execute('''insert into test (id, name, age) values ('000', 'John', '23')''')
  cursor.execute('''insert into test (id, name, age) values ('001', 'Tom', '25')''')
  cursor.execute('''insert into test (id, name, age) values ('002', 'Jack', '29')''')
  
  cursor.execute('''select * from test''')
  
  # 查询一个结果
  print(cursor.fetchone())
  print(cursor.fetchall())
  
  conn.commit()
  cursor.close()
  conn.close()

要注意的是查询命令后必须进行 fetch 操作，并取完所有结果，否则会报 Unread result found 错误。

ORM 框架
---------------

如果我们要使用多套数据库，那么就要实现多套数据库SQL接口，例如查询，删除等等，这导致代码重复繁琐，是否可以提供一个抽象层，把对数据库的SQL操作转化为对象操作呢？

对象关系映射（ORM，Object Relational Mapping）通过使用描述对象和数据库之间映射的元数据，将程序中的对象操作自动关联到关系数据库中。
ORM 是一种技术解决方案， Python 下提供了很多 ORM 的模块实现，如 peewee，Storm，SQLObject 和 SQLAlchemy。

peewee
~~~~~~~~~~~~~~~~

peewee 是一个非常轻量级的 Python ORM 实现，它简便，非常易于上手。

peewee 中定义了 Model 类，Field 和 Nodel 实例与数据库的映射关系如下：

========== =====================
peewee对象 数据库对象
========== =====================
Model类    数据库表
Field 实例 表中的列
Model 实例 表中的行
========== =====================

安装第三方模块 peewee 非常简单 pip install peewee 。

创建表
`````````````````

一个表对应一个类，它继承 Model 类。例如定义一个 Person 类，那么将自动生成一个名为 person 的表，在元类中指定使用的数据库。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  from peewee import *

  db = SqliteDatabase('people.db')
  db.connect()  # 可选，无需显式连接数据库，但是要显式 close()
          
  class Person(Model):
      name = TextField()       # Field 对应列
      age = IntegerField()
      
      # 元类中指定连接的数据库，这里以Sqlite 数据库为例
      class Meta:
          database = db
  
  # 在 people.db 中自动创建名为 person 的表
  Person.create_table()

  # 同时创建多个表
  # database.create_tables([Person])
  
  # sqlite 命令查询表
  sqlite> .table
  person

插入行
````````````````````

表的插入非常简单，调用类函数 Model.create() 即可，并且会自动生成主键 id：

.. code-block:: python
  :linenos:
  :lineno-start: 0 

  def print_person(item):
      print(item.id, item.name, item.age)
  
  # Person() 实例对应行
  grandma = Person.create(name='Grandma', age = 60)
  grandpa = Person.create(name='Grandpa', age = 62)
  
  print_person(grandma)
  print_person(grandpa)
  
  >>>
  1 Grandma 60
  2 Grandpa 62

采用 sqlite 查看建表语句和 person 表中的数据：

.. code-block:: sh
  :linenos:
  :lineno-start: 0 

  sqlite> .schema person
  CREATE TABLE "person" ("id" INTEGER NOT NULL PRIMARY KEY, 
                         "name" DATE NOT NULL, "age" INTEGER NOT NULL);

  sqlite> select * from person;
  1|Grandma|60
  2|Grandpa|62

由于会自动生成 id ，所以我们在插入前需要判断当需要插入的数据是否存在。

查询
``````````

使用 Model.select() 或者 Model.get() 类函数可以查询特定行，或者所有行：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  person = Person.select().where(Person.name == 'Grandma').get()
  print_person(person)
  
  >>>
  1 Grandma 60
  
  # 简化的查询方法
  person = Person.get(Person.name == 'Grandma')
  print_person(person)
  
  >>>
  1 Grandma
  
  # 查询所有行
  for person in Person.select():
      print_person(person)
  
  >>>
  1 Grandma 60
  2 Grandpa 62

也可以指定条件查询：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  for person in Person.filter(Person.id > 1):
      print_person(person)

在查询是可以使用 Model.order_by() 方法进行排序：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  for person in Person.select().order_by(Person.name):
      print_person(person)

更新数据
```````````

Model.save() 用于更新数据，也可以用来插入新的行，它返回行 id， 例如：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  # 更新 id 为 1 的行
  p = Person(name='Mother', age=28)
  p.id = 1
  p.save()

  # 添加新行
  father = Person(name='Father', age=30)
  id = father.save()
  print(id)

  # 更新 Father 行的 age 信息
  father = Person.get(Person.name == 'Father')
  father.age = 32
  id = father.save()
  print(id)
  
  >>>
  2
  2

Model.delete() 类函数可以清空表或某个表项，instance.delete_instance() 用于删除一个特定表项：
 
.. code-block:: python
  :linenos:
  :lineno-start: 0 

  # 选择删除，成功返回 1，否则返回 0
  Person.delete().where(Person.name == 'father').execute()
  
  # 清空 Person 表项
  Person.delete().execute()

  # 已实例化的数据删除
  father = Person.get(Person.id == 3)
  id = father.delete_instance()
  print(id)

  >>>
  2

连接各类数据库
````````````````

上面的示例使用 SQLite 数据库，peewee 目前支持 SQLite, MySQL 和 Postgres。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
   
  # SQLite 数据库，支持外键，启用 WAL 日志模式，缓存64MB
  sqlite_db = SqliteDatabase('test.db', pragmas={
                             'foreign_keys': 1, 
                             'journal_mode': 'wal',
                             'cache_size': -1024 * 64})
  
  # 连接 MySQL 数据库 dbname
  mysql_db = MySQLDatabase('dbname', user='username', password='password',
                           host='127.0.0.1', port=3306)
  
  # 连接 Postgres 数据库
  pg_db = PostgresqlDatabase('dbname', user='username', password='password',
                             host='127.0.0.1', port=5432)


peewee 使用 pymysql 或 MySQLdb 作为 MySQL 驱动模块，如果没有安装会提示错误。

Foreign Keys
````````````````

如果一个表中一列要引用另一个表中的表项，例如一个家庭成员的表和一个宠物表，每个宠物都有它的主人，那么在主人这一项里面就可以引用家庭成员表中某个成员的 id，这种引用被称为外键。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  db = SqliteDatabase('people.db')
  
  class Person(Model):
      name = CharField()
      birthday = DateField()

      class Meta:
          database = db
          
  class Pet(Model):
    name = CharField()
    animal_type = CharField()
    
    # 定义外键
    owner = ForeignKeyField(Person, backref='pets')

    class Meta:
        database = db 

    # 创建 person 和 pet 表
    db.create_tables([Person, Pet])
    
上面定义了个两个类，一个用于定义家庭成员，一个用于定义宠物。它们对应数据库中的两张表 person 和 pet，pet 中的主人一栏引用 person 中的 id。

为两个表插入一些表项：

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  bob = Person.create(name='Bob', age=60)
  herb = Person.create(name='Herb', age=30)
  
  bob_kitty = Pet.create(owner=bob, name='Kitty', animal_type='cat')
  herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
  herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')

  sqlite> select * from person;
  1|Bob|60
  2|Herb|30
  sqlite> select * from pet;
  1|1|Kitty|cat
  2|2|Fido|dog
  3|2|Mittens|cat

通过 sqlite 可以查询到每个 pet 的 owner 一项都对应它主人的 id 。

.. code-block:: python
  :linenos:
  :lineno-start: 0 
  
  query = Pet.select().where(Pet.animal_type == 'cat')
  for pet in query:
      print(pet.name, pet.owner.name)

  >>>
  Kitty Bob
  Mittens Herb

注意事项
```````````````

由于会自动生成 id，插入数据时应该判断是否已经存在，否则会被重复插入。

数据库使用完毕后应该显式关闭，也即  db.close()。

更详细用法参考 `peewee 官方文档 <http://docs.peewee-orm.com/en/latest/index.html>`_ 。
