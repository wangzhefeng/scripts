
Linux 背景介绍
=================

1.什么是 Linux
-----------------

1.1 Linux 有两种含义
~~~~~~~~~~~~~~~~~~~~~~

    - Linus 编写的开源操作系统的内核

         - Linus Benedict Torvalds(著名的电脑程序员)开发的系统

    - 广义的操作系统

1.2 Linux 的第一印象
~~~~~~~~~~~~~~~~~~~~~~

    - 服务端操作系统和客户端操作系统要做的事情不一样

    - 命令行操作方式与图形界面的差异


1.3 Linux 环境准备
~~~~~~~~~~~~~~~~~~~~~~

    - 执行环境

        - 云主机

        - 无数据的 PC

        - 虚拟机


2.Linux 的内核版本及常见发行版
-------------------------------

2.1 内核版本
~~~~~~~~~~~~~~~~~~


    - Linus Torvalds 开发的 Linux 内核: https://www.kernel.org/

    - 内核版本分为三个部分

    - 主版本号、此版本号、末版本号

    - 次版本号是奇数为开发版本、偶数为稳定版本

2.2 发行版本
~~~~~~~~~~~~~~~~~~

    - RedHat Enterprise Linux
        
        - 软件经过专业人员的测试

    - Fedora

        - 组件社区免费提供软件

    - CentOS

        - 基于 RedHat 编译
    
    - Debian
        
        - 华丽的桌面

    - Ubuntu

        - 华丽的桌面


3. 安装 VirtualBox 虚拟机
---------------------------

    - https://www.virtualbox.org/wik/Downloads

4. 在虚拟机中安装 Linux 系统
----------------------------

    - http://isoredirect.centos.org/centos/7/isos/x86_64/


5. 第一次启动 Linux
-----------------------

5.1 图形页面
~~~~~~~~~~~~~~~~~~~~

    - root 用户账号、密码：

        - ``root``

        - ``123456``

    - 普通用户账号、密码：

        - ``wangzf``

        - ``Tinker711235813``

5.2 终端页面
~~~~~~~~~~~~~~~~~~~~

    - 进入终端页面：

        .. code-block:: shell

            # in Shell

            init 3

    - 登录用户：

        - root 用户

            - ``root`` 

            - ``123456``


        - 普通用户：

            - ``wangzf``

            - ``Tinker711235813``

    - 退出当前登录用户(切换用户)：

        .. code-block:: shell

            # in Shell

            exit

    - 关机

        .. code-block:: shell

            # in Shell

            init 0


5.3 终端的使用
~~~~~~~~~~~~~~~~~~~~

    - 终端(Shell)

        - 图形终端

        - 命令行终端

            - 服务器维护

        - 远程终端(SSH、VNC)

5.4 常见目录介绍
~~~~~~~~~~~~~~~~~~~~

    - ``/`` 根目录

    - ``/root`` root 用户的家目录

    - ``/home/username`` 普通用户的家目录

    - ``/etc`` 配置文件目录

    - ``/bin`` 命令目录

    - ``/sbin`` 管理命令目录

    - ``/usr/bin`` ``/usr/sbin`` 系统预装的其他命令

    使用示例：

    .. code-block:: shell

        ls /
        ls /root
        ls /bin
