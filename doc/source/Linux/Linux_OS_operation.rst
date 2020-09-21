
Linux 系统操作
========================




.. important:: **Linux 中一切皆文件**

    - 文件查看

    - 目录文件操作创建、删除、复制、移动

    - 通配符

    - 文件操作

    - 文本内容查看


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


2. 文件查看--``pwd``、``cd``、``ls``
---------------------------------------------------

2.1 ``pwd`` 显示当前的目录名称
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - ``pwd`` 显示当前的目录名称

        .. code-block:: shell

            $ man pwd
            $ pwd

    - ``/root``: root 用户的家目录

    - ``/``: 根目录

2.2 ``cd`` 更改当前的操作目录
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - ``cd`` 更改当前的操作目录

        - 绝对路径

            - ``cd /path/to/...``

        - 相对路径

            - ``cd ./path/to/...``

                - ``./`` 代表当前目录,可省略

            - ``cd ../path/to/...``

                - ``../`` 代表上级目录

        - 常用命令

            .. code-block:: shell

                # 回到之前的一个目录
                $ cd -
                $ cd ./
                $ cd .
                $ cd ../
                $ cd ..


2.3 ``ls`` 文件查看
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - ``ls`` 查看当前目录下的文件

        - ``ls [选项, 选项...] 参数...``
        - ``ls [选项] [文件夹...]``

    - 常用参数

        - ``-l`` 长格式显示文件

        - ``-a`` 显示隐藏文件

        - ``-r`` 逆序显示

        - ``-t`` 按照时间顺序显示

        - ``-R`` 递归显示
    
    - 使用示例

        .. code-block:: shell

            # 使用
            $ ls -l /root /
            $ ls -l .
            $ ls -l 
            $ ls -l -r
            $ ls -l -r -t
            $ ls -lrt
            $ ls -lartR
            $ clear(or Ctrl + l)

.. note:: 

    - ``-rw-------.``

        - ``-`` 第一个 ``-`` 代表普通文件

    - ``drwxr-xr-x.``

        - ``d`` 第一个 ``d`` 代表目录

3. 目录文件操作--创建、删除、复制、移动
---------------------------------------------------

3.1 创建目录
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - ``mkdir`` 新建目录

    - ``mkdir -p`` 建立多级目录

    - ``touch`` 新建文件

    - 使用方法

        .. code-block:: shell

            $ man mkdir

            # 相对目录
            $ mkdir ./dir_name1 dir_name2 dir_name3 ...

            # 绝对目录
            $ mkdir /path/dir_name1 dir_name2 dir_name3 ...

            # 创建多级目录
            $ mkdir ./a
            $ mkdir ./a/b
            $ mkdir ./a/b/c
            $ mkdir ./a/b/c/d
            # 与上面等效
            $ mkdir -p ./a/b/c/d

            $ ls -R ./a

            # 新建文件
            $ touch file1 file2 file3 ...

.. note:: 

    如果目录已经存在，创建目录会导致报错。

3.2 删除目录
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - ``rmdir`` 删除空目录

    - ``rm -r`` 删除非空目录

    - ``rm -rf`` 删除非空目录

    - 使用方法

        .. code-block:: shell

            $ rmdir ./a
            
            # 删除非空目录目录，需要确认删除
            $ rm -r ./dir1 ./dir2 ...

            # 删除非空目录目录，需要确认删除
            $ rm -rf ./dir1 ./dir2 ...


.. note:: text

    - ``rmdir`` 只能删除空目录

3.3 复制目录
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - ``cp`` 复制目录

    - 使用方法

        .. code-block:: shell
            
            # 复制文件
            $ cp 源文件 目的文件目录

            # 复制目录
            $ cp -r 源文件目录 目的文件目录

            # 复制目录并显示复制信息
            $ cp -v 源文件目录 目的文件目录

            # 复制目录并保持属主
            $ cp -p 源文件目录 目的文件目录

            # 复制目录并保持属主、时间...
            $ cp -a 源文件目录 目的文件目录


.. note:: 

    - ``/tmp`` 目录为临时文件目录


3.4 移动、重命名目录
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - ``mv`` 移动、重命名目录

    - 使用方法

        .. code-block:: shell

            # 移动文件
            $ mv 源文件 目的文件目录

            # 重命名文件名
            $ mv 源文件 重命名后的文件
            $ mv 源文件 目的文件目录/重命名后的文件

            # 移动目录
            $ mv 源文件目录 目的文件目录

            # 重命名目录
            $ mv 源文件 重命名后的文件 

4. 通配符
---------------------------------------------------

    - 定义：shell 内建的符号

    - 用途：操作多个相似(有简单规律)的文件

    - 常用通配符

        - ``*`` 匹配任何字符串

        - ``?`` 匹配 1 个字符串

        - ``[xyz]`` 匹配 xyz 任意一个字符

        - ``[a-z]`` 匹配一个范围

        - ``[!xyz]`` 或 ``[^xyz]`` 不匹配


5. 文件操作
---------------------------------------------------

5.1 用户与权限管理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    用户管理常用命令:

        - ``useradd username`` 新建用户

        - ``userdel username`` 删除用户

        - ``passwd`` 修改用户密码

        - ``usermod`` 修改用户属性

        - ``chage`` 修改用户属性(声明周期属性)

5.1.1 新建用户
^^^^^^^^^^^^^^^^^^^

    1.切换到 root 用户

    .. code-block:: shell

        $ su - root

    2.新建用户

    .. code-block:: shell

        $ useradd user_test

    3.查看用户信息

    .. code-block:: shell

        $ id

        $ id root
        $ id user_test

    4. 查看用户家目录

    .. code-block:: shell

        $ ls /root
        $ ls /home/user_test/
        $ ls -a /home/user_test/

    5.查看用户配置文件

    .. code-block:: shell

        # 用户记录
        $ tail -10 /etc/passwd

        # 用户密码记录
        $ tail -10 /etc/shadow


5.1.2 修改用户密码
^^^^^^^^^^^^^^^^^^^

    1.切换到 root 用户

    .. code-block:: shell

        $ su - root

    2.修改用户密码

    .. code-block:: shell

        # 修改自己密码
        $ passwd

        # 修改其他用户密码
        $ passwd user_test


5.1.3 删除用户
^^^^^^^^^^^^^^^^^^^

    1.切换到 root 用户

    .. code-block:: shell

        $ su - root

    2.删除用户

    .. code-block:: shell

        $ userdel user_test
        $ userdel -r user_test  # 彻底删除，包块/home目录下的用户目录
        $ id user_test
        $ tail -10 /etc/passwd

5.1.4 修改用户属性
^^^^^^^^^^^^^^^^^^^

    1.切换到 root 用户

    .. code-block:: shell

        $ su - root

    2.修改用户账号

    .. code-block:: shell

        # 修改用户家目录
        $ usermod -d /home/user_test_2 user_test

5.1.5 修改用户生命周期
^^^^^^^^^^^^^^^^^^^^^^^

    1.切换到 root 用户

    .. code-block:: shell

        $ su - root


5.1.6 组管理命令
^^^^^^^^^^^^^^^^^^^^^^^

    组管理命令:

        - ``groupadd`` 新建用户组

        - ``groupdel`` 删除用户组


    1.切换到 root 用户

    .. code-block:: shell

        $ su - root

    2.新建用户组

    .. code-block:: shell

        # 新建组、新建用户、修改用户组
        $ groupadd group1 
        $ useradd user1
        $ usermod -g group1 user1

        # 新建用户并加入组
        $ useradd -g group1 user2


    3.删除用户组

    .. code-block:: shell

        $ groupdel group1


5.1.7 用户切换
^^^^^^^^^^^^^^^^^^^^^^^

    用户切换命令：

        - ``su`` 切换用户

            - ``su - USERNAME`` 使用 login shell 方式切换用户

        - ``sudo`` 以其他用户身份执行命令

            - ``visudo`` 设置需要使用 ``sudo`` 的用户(组)

    1.普通用户 => root用户(需要输入 root 密码)

    .. code-block:: shell

        $ su - root
        $ 

    2.root用户 => 普通用户

    .. code-block:: shell

        # 完全切换
        $ su - user_test

        # 不完全切换
        $ su user_test
        $ cd /home/user_test


5.2 打包压缩和解压缩
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 最早的 Linux 备份介质是磁带，使用的命令是 ``tar``

- 可以打包后的磁带文件进行压缩存储，压缩的命令是 ``gzip`` 和 ``bzip2``

- 经常使用的扩展名是 ``.tar.gz``、``.tar.bz2``、``.tgz``

- ``tar`` 打包命令

    - ``c`` 打包

    - ``x`` 解包

    - ``f`` 指定操作类型为文件


- 打包

    - 打包
        
        .. code-block:: shell
        
            $ tar cf /new_path/new_file.tar /path_to_be_tar
    
    - 打包并压缩

        .. code-block:: shell

            # 压缩更快 (.tgz == .tar.gz)
            $ tar czf /new_path/new_file.tar.gz /path_to_be_tar_zip

            # 更高的压缩比例 (.tbz2 == .tar.bz2)
            $ tar cjf /new_path/new_file.tar.bz2 /path_to_be_tar_zip
    
    - 解包并解压缩

        .. code-block:: shell
        
            $ tar xf /new_path/new_file.tar -C /path_to_save
            $ tar zxf /new_path/new_file.tar.gz -C /path_to_save 
            $ tar jxf /new_path/new_file.tar.bz2 -C /path_to_save

- 压缩、解压缩

    - gzip new_file.tar

    - bzip2 new_file.tar




6. 文本内容查看
---------------------------------------------------

6.1 文件内容查看
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 文本查看命令

    - ``cat`` 文本内容显示到终端

        - ``cat filename``

    - ``head`` 查看文件开头

        - ``head -n filename``

    - ``tail`` 查看文件结尾

        - ``tail -3 filename``

        - 常用参数 ``-f`` 文件内容更新后，显示信息同步更新
            
            - ``tail -f filename``

    - ``wc`` 统计文件内容信息(文件长度)

        - ``wc -l filename``
    
    - ``less``

    - ``more``


6.2 强大的文本编辑器 :guilabel:`vi`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

多模式文本编辑器:
^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^

    - :guilabel:`I`: 进入插入模式，光标处于插入之前行的开头

    - :guilabel:`i`: 进入插入模式，光标处于插入之前的位置

    - :guilabel:`A`: 进入插入模式，光标处于插入之前的行结尾

    - :guilabel:`a`: 进入插入模式，光标处于插入之前的行的下一位

    - :guilabel:`O`: 进入插入模式，光标处于插入之前的行的上一行

    - :guilabel:`o`: 进入插入模式，光标处于插入之前的行的下一行

可视模式:
^^^^^^^^^^^^^^^^^^^^^^^^^

    - 进入可视模式

        - :guilabel:`v`: 字符可视模式

        - :guilabel:`V`: 行可视模式

        - :guilabel:`Ctrl + V`: 块可视模式

            - :guilabel:`d`: 多行删除

            - :guilabel:`I` + 连续两次按 :guilabel:`Esc`: 多行插入

命令模式:
^^^^^^^^^^^^^^^^^^^^^^^^^

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


7.其他命令
--------------------

- 系统关机

.. code-block:: shell

    # 当前用户 30 分钟后关闭系统
    $ shutdown -h 30
    
    # 当前用户取消关机
    $ shutdown -c
