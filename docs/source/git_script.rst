.. _header-n0:

Git
===

.. _header-n3:

1.创建SSH Key
-------------

.. code:: shell

   $ ssh-keygen -t rsa -C "wangzhefengr@163.com"

.. _header-n5:

2.安装Git
---------

.. code:: shell

   $ sudo apt-get install git
   $ git --version

.. _header-n7:

3.Git 配置
----------

.. _header-n8:

3.1 配置Git
~~~~~~~~~~~

.. code:: shell

   $ git config --global user.name "wangzhefeng"
   $ git config --global user.email "wangzhefengr@163.com"
   $ git config --global core.editor gedit

.. _header-n10:

3.2 Git配置文件
~~~~~~~~~~~~~~~

.. code:: shell

   # 包含系统上每一个用户及它们仓库的通用配置
   $ sudo gedit /etc/gitconfig

   # 只针对当前用户
   $ sudo gedit ~/.gitconfig

or

.. code:: shell

   $ sudo gedit ~/.config/git/config

   # 针对该仓库
   $ sudo gedit .git/config

.. _header-n14:

3.3 检查Git配置信息
~~~~~~~~~~~~~~~~~~~

.. code:: shell

   $ git config --list
   $ git config user.name
   $ git config user.email
   $ git config core.editor

.. _header-n16:

4.获取帮助
----------

.. code:: shell

   $ git help <verb>
   $ git <verb> help
   $ man git-<verb>

   $ git help config

.. _header-n18:

5.Git工作流程
-------------

.. _header-n19:

5.1 创建Git仓库(2种)
~~~~~~~~~~~~~~~~~~~~

1. 在现有项目或目录下导入所有的文件到Git中；

   -  建立本地仓库目录(项目目录)

   -  初始化版本库

      -  创建版本库(repository) => .git

         -  暂存区 => stage(index)

         -  唯一一个分支 => master

         -  指向master的一个指针 => HEAD

2. 新建远程库 => 从一个服务器克隆一个现有的Git仓库

方法一：

.. code:: shell

   $ mkdir git_test
   $ git init

方法二：

.. code:: shell

   $ git clone https://github.com/wangzhefeng/git_test.git
   $ git clone https://github.com/wangzhefeng/git_test.git git_test

.. _header-n44:

5.2 添加版本库中的文件到暂存区
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   $ git .
   # or
   $ git add .
   # or
   $ git add file_name
   # or
   $ git add path_name\file_name
   # or
   $ git add path_name\*.txt

.. _header-n46:

5.3 把暂存区的所有内容提交到当前分支
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git commit -m 'initial project version'

.. _header-n48:

5.4 把一个已有的本地仓库和远程git库关联
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git remote add origin https://github.com/wangzhefeng/resp.git

.. _header-n50:

5.5 把本地库的内容推送到远程(把当前分支推送到远程)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git push -u origin master

.. _header-n53:

5.6 从远程分支拉取最新的版本到本地并合并
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. git fetch

   -  从远程获取最新版本到本地，不会自动merge

2. git pull

   -  从远程获取最新版本到本地，自动merge

方法一：

.. code:: shell

   # 从远程的origin的master主分支下载最新的版本到origin/master分支上
   $ git fetch origin master

   # 比较本地的master分支和origin/master分支的差别
   $ git log -p master..origin/master

   # 合并
   $ git merge origin/master

or

.. code:: shell

   $ git fetch origin master:tmp
   $ git diff tmp
   $ git merge tmp

方法二：

.. code:: shell

   $ git pull origin master

.. _header-n71:

6.查看当前信息
~~~~~~~~~~~~~~

.. _header-n72:

6.1 查看当前文件状态
^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git status
   $ git status -s
   $ git status --short

.. _header-n74:

6.2 查看已暂存和未暂存的修改
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git diff 
   $ git diff --cached
   $ git diff --staged

.. _header-n76:

6.3 查看工作区和版本库里最新版本的区别
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git diff HEAD --file.txt

.. _header-n78:

7.移除文件(从暂存区域移除)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _header-n79:

7.1 确定要从版本库中删除文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git rm
   $ git commit -m "message"

or

.. code:: shell

   $ git add .

.. _header-n83:

7.2 误删工作区文件，将版本库中的文件替换工作取得文件
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git checkout -- test.txt

.. _header-n85:

8.版本回退
~~~~~~~~~~

.. _header-n86:

8.1 提交日志
^^^^^^^^^^^^

.. code:: shell

   $ git log --pretty=oneline

.. _header-n88:

8.2 查看命令历史, 记录每次命令
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git reflog

.. _header-n90:

8.3 版本回退
^^^^^^^^^^^^

.. _header-n91:

8.3.1 回退到上一个版本(HEAD：当前版本)
''''''''''''''''''''''''''''''''''''''

.. code:: shell

   $ git log
   $ git reset --hard HEAD^
   $ git reset --hard HEAD~10
   $ git reset --hard commit_id

.. _header-n93:

8.3.2 前进到某个版本
^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git reflog
   $ git reset --hard commit_id

.. _header-n95:

9.撤销修改
~~~~~~~~~~

.. _header-n97:

9.1 丢弃工作区的修改，
^^^^^^^^^^^^^^^^^^^^^^

-  自修改后还未被放到暂存区(还未进行git add) => 回到和版本库一样的状态

-  添加到暂存区后又作了修改(进行了git add) => 添加到暂存区后的状态

.. code:: shell

   $ git checkout -- file.txt

.. _header-n104:

9.2 把暂存区的修改回退到工作区(丢弃暂存区的修改)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git reset HEAD file.txt
   $ git checkout --file.txt

.. _header-n107:

10.分支管理
~~~~~~~~~~~

.. _header-n108:

10.1 创建与合并分支
^^^^^^^^^^^^^^^^^^^

.. _header-n109:

10.1.1 创建tinker分支，然后切换到tinker分支
'''''''''''''''''''''''''''''''''''''''''''

.. code:: shell

   $ git checkout -b tinker

.. code:: shell

   $ git branch tinker
   $ git checkout tinker

.. _header-n113:

10.1.2 查看当前分支
^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git branch

.. _header-n115:

10.1.3 切换回master分支
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   git checkout master

.. _header-n117:

10.1.4 将tinker分支的工作成果合并到master分支上
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git checkout master
   $ git merge tinker

.. _header-n119:

10.1.5 删除tinker分支
^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ git branch -d tinker






