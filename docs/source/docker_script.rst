.. _header-n0:

Docker
======

.. _header-n3:

Docker Hello World
------------------

.. _header-n4:

在容器内运行一个应用程序
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   docker run ubuntu:15.10 /bin/echo "Hello world"

.. _header-n6:

运行交互式的容器
~~~~~~~~~~~~~~~~

.. code:: shell

   docker run -i -t ubuntu:15.10 /bin/bash
   cat /proc/version
   ls
   # 退出容器
   exit # or Ctrl+D

.. _header-n8:

启动容器（后台模式）
~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"

.. _header-n10:

停止容器
~~~~~~~~

.. code:: shell

   docker stop <>
   docker ps
   docker stop amazing_cori

.. _header-n12:

Docker 容器
-----------

.. _header-n13:

Docker 客户端
~~~~~~~~~~~~~

.. code:: shell

   docker
   docker <command> --help

.. _header-n15:

Docker 容器使用
~~~~~~~~~~~~~~~

获取镜像

.. code:: shell

   docker pull ubuntu

启动容器

.. code:: shell

   docker run -it ubuntu /bin/bash

启动已停止运行的容器

.. code:: shell

   docker ps -a

.. _header-n22:

Docker 安装 Ubuntu
------------------

.. _header-n23:

1.查看可用的 Ubuntu 版本
~~~~~~~~~~~~~~~~~~~~~~~~

`Ubuntu 镜像库地址 <https://hub.docker.com/_/ubuntu?tab=tags&page=1>`__

.. _header-n25:

2.拉取最新版的 Ubuntu 镜像
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   docker pull ubuntu
   docker pull ubuntu:latest

.. _header-n27:

3.查看本地镜像
~~~~~~~~~~~~~~

.. code:: shell

   docker images

.. _header-n29:

4.运行容器，并且可以通过 ``exec`` 命令进入 ubuntu 容器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   docker run -itd --name ubuntu-test ubuntu

.. _header-n31:

5.安装成功
~~~~~~~~~~

.. code:: shell

   docker ps

.. _header-n33:

Docker 安装 Python
------------------
