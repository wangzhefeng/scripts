
Linux 系统操作
===================

1. Linux Help
-----------------

为什么要学习帮助命令?

    - Linux 的基本操作方式是命令行

    - 海量的命令不适合“死记硬背”

    - 你要升级你的大脑

常用帮助方式:

    - man 帮助

    - help 帮助

    - info 帮助

1.1 ``man``: 有问题找男人帮忙
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``man`` 是 manual 的缩写

- ``man`` 帮助用法演示

    .. code-block:: shell

        $ man 1 ls
        $ man ls

- ``man`` 也是一条命令, 分为 9 章，可以用 ``man`` 命令获得 ``man`` 的帮助

    - 获取 ``man`` 的帮助

        .. code-block:: shell

            $ man man

    - 获取 ``man`` 章节的帮助

        .. code-block:: shell
        
            $ man 7 man
        
        - 1 Command

        - 2 System calls(编程函数)

        - 3 Library calls(编程函数)

        - 4 Special files(文件)

        - 5 File formats and conventions(文件)

        - 6 Games

        - 7 Macro packages and conventions

        - 8 System management commands

        - 9 Kernel routines(废弃)

    - 使用示例:

        .. code-block:: shell

            # 命令帮助
            $ man 1 password

            # 配置文件帮助
            $ man 5 password
            
            # 只知道名字获取帮助
            $ man -a password

- 其他

    -  根据命令部分关键字搜索

        .. code:: shell

            $ man date
            $ man -k date

    -  命令参数及使用方法

        .. code:: shell

            $ man ls

1.2 ``help``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- shell(命令解释器) 自带的命令称为内部命令，其他的是外部命令

- 内部命令使用 ``help`` 帮助

    .. code-block:: shell

        $ help cd

- 外部命令使用 ``help`` 帮助

    .. code-block:: shell

        $ ls --help

- 查看命令的类型

    .. code-block:: shell

        $ type cd 
        $ type ls


1.3 ``info``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``info`` 帮助比 ``help`` 帮助更详细，作为 ``help`` 帮助的补充

    .. code:: shell

        $ info ls


1.4 其他
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  命令简要说明

    .. code:: shell

        $ whatis ls
        $ whatis -w "mkd*"

-  查看程序的binary文件所在路径

    .. code:: shell

        $ which python

-  查看程序的搜索路径

    .. code:: shell

        $ whereis python


2.常用命令详解
---------------

.. important:: **Linux 中一切皆文件**

    - 文件查看

    - 目录文件操作创建、删除、复制、移动

    - 通配符

    - 文件操作

    - 文本内容查看


2.1 文件查看--``pwd``、``cd``、``ls``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.1.1 ``pwd`` 显示当前的目录名称
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    - ``pwd`` 显示当前的目录名称

        .. code-block:: shell

            $ man pwd
            $ pwd

    - ``/root``: root 用户的家目录

    - ``/``: 根目录

2.1.2 ``cd`` 更改当前的操作目录
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


    - ``cd`` 更改当前的操作目录

        - 绝对路径

            - ``cd /path/to/...``

        - 相对路径
        
            - ``cd ./path/to/...``

            - ``cd ../path/to/...``

2.1.3 ``ls`` 文件查看
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

    - ``ls`` 查看当前目录下的文件

        - ``ls [选项, 选项...] 参数...``
        - ``ls [选项] [文件夹]``

    - 常用参数

        - ``-l`` 长格式显示文件

        - ``-a`` 显示隐藏文件

        - ``-r`` 逆序显示

        - ``-t`` 按照时间顺序显示

        - ``-R`` 递归显示
    
    - 使用示例

        .. code-block:: shell

            # 使用
            $ ls -l /

            # 切换 root 用户
            $ su - root



2.2 目录文件操作--创建、删除、复制、移动
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.2.1 创建目录
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    $ mkdir dir_name



2.2.2 删除目录
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    $ rm 


2.2.3 复制目录
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
    
    $ cp 

2.2.4 移动、重命名目录
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell

    $ mv 




2.3 通配符
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






2.4 文件操作
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.4.1 用户与权限管理
^^^^^^^^^^^^^^^^^^^^^^^

用户管理常用命令:

    - ``useradd`` 新建用户

    - ``userdel`` 删除用户

    - ``passwd`` 修改用户密码

    - ``usermod`` 修改用户属性

    - ``chage`` 修改用户属性










2.4.2 打包压缩和解压缩
^^^^^^^^^^^^^^^^^^^^^^^^






2.5 文本内容查看
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.5.1 文件内容查看
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




2.5.2 强大的文本编辑器 :guilabel:`vi`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

多模式文本编辑器:
'''''''''''''''''

    - 四种模式

        - 正常模式(Normal-mode)

        - 插入模式(Insert-model)

        - 命令模式(Command-mode)

        - 可视模式(Visual-mode)

    - 进入编辑器

        .. code-block:: shell

            $ vi
            $ vim
            $ vim file_name


正常模式:
''''''''''''''''''''

    - 进入正常模式
        
        - :guilabel:`Esc`

    - 光标移动

        - :guilabel:`h`: 左

        - :guilabel:`j`: 上

        - :guilabel:`k`: 下

        - :guilabel:`l`: 右

    - 复制文本

        - :guilabel:`yy`: 复制当前整行

        - :guilabel:`[n]yy`: 复制当前行下面的多行

        - :guilabel:`y$`: 复制光标位置到当前行的结尾

    - 粘贴文本

        - :guilabel:`p`
    
    - 剪切文本

        - :guilabel:`dd`: 剪切光标所在的行

        - :guilabel:`[n]dd`: 剪切当前行下面的多行

        - :guilabel:`d$`: 剪切光标位置到当前行的结尾
    
    - 撤销

        - :guilabel:`u`: 撤销

        - :guilabel:`Ctrl + r`: 重做(撤销撤销)
    
    - 单个字符删除

        - :guilabel:`x`: 光标移动到要删除的字符上
    
    - 单个字符替换

        - :guilabel:`r`: 光标移动到要删除的字符上
    
    - 移动到指定的行

        - :guilabel:`[n]G`: 移动到第 n 行

        - :guilabel:`g`: 移动到第一行

        - :guilabel:`G`: 移动到最后一行

        - :guilabel:`^`: 移动到当前行的开头

        - :guilabel:`$`: 移动到当前行的结尾


插入模式:
''''''''''''''''''''

    - :guilabel:`I`: 进入插入模式，光标处于插入之前行的开头

    - :guilabel:`i`: 进入插入模式，光标处于插入之前的位置

    - :guilabel:`A`: 进入插入模式，光标处于插入之前的行结尾

    - :guilabel:`a`: 进入插入模式，光标处于插入之前的行的下一位

    - :guilabel:`O`: 进入插入模式，光标处于插入之前的行的上一行

    - :guilabel:`o`: 进入插入模式，光标处于插入之前的行的下一行

可视模式:
''''''''''''''''''''

    - 进入可视模式

        - :guilabel:`v`: 字符可视模式

        - :guilabel:`V`: 行可视模式

        - :guilabel:`Ctrl + V`: 块可视模式

            - :guilabel:`d`: 多行删除

            - :guilabel:`I` + 连续两次按 :guilabel:`Esc`: 多行插入

命令模式:
''''''''''''''''''''

    - 进入命令模式、末行模式

        - :guilabel:`:`

    - 保存

        - :guilabel:`:w /zfwang/filename.sh`: 保存到指定文件

        - :guilabel:`:w`: 保存到当前文件

    - 退出

        - :guilabel:`:q`

    - 保存退出

        - :guilabel:`:wq` 

    - 不保存退出

        - :guilabel:`:q!` 

    - 执行 Linux 命令

        - :guilabel:`:![command]`
        
        - :guilabel:`:!ifconfig`: 查看ip地址
    
    - 查找字符

        - :guilabel:`/[str]`

        - :guilabel:`/[str]` + :guilabel:`n` 查找到的字符下移光标

        - :guilabel:`/[str]` + :guilabel:`N`: 查找到的字符上移光标

    - 替换查找到的字符

        - :guilabel:`:s/old_str/new_str`: 只替换光标所在行的目标字符

        - :guilabel:`:%s/old_str/new_str`: 替换整个文件的第一个目标字符

        - :guilabel:`:%s/old_str/new_str/g`: 替换整个文件的目标字符

        - :guilabel:`:[n],[m]s/old_str/new_str/g`: 替换第n行到第m行的目标字符
    
    - 显示/不显示行号

        - :guilabel:`:set nu`

        - :guilabel:`:set nonu`
    
    - 去掉高亮显示

        - :guilabel:`:set nohlsearch` 
    
    - 设置 vim 的配置文件

        .. code-block:: shell
        
            # 打开 /etc/vimrc
            $ vim /etc/vimrc

            # /etc/vimrc 文件修改
            set nu




