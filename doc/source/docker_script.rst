
Docker
==================

- 学前准备

   - Linux

   - Srping Boot

- Docker 学习

   - Docker 概述

   - Docker 安装

   - Docker 命令

      - 镜像命令
      - 容器命令
      - 操作命令
      - test

   - Docker 镜像

   - 容器数据卷

   - DockerFile

   - Docker 网络原理

   - IDEA 整合 Docker

   - Docker Compose

   - Docker Swarm

   - CI/CD jenkins












1.Docker Hello World
---------------------------

在容器内运行一个应用程序
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   docker run ubuntu:15.10 /bin/echo "Hello world"


运行交互式的容器
~~~~~~~~~~~~~~~~

.. code:: shell

   docker run -i -t ubuntu:15.10 /bin/bash
   cat /proc/version
   ls
   # 退出容器
   exit # or Ctrl+D

.. _header-n8docker:

启动容器（后台模式）
~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"

.. _header-n10docker:

停止容器
~~~~~~~~

.. code:: shell

   docker stop <>
   docker ps
   docker stop amazing_cori

.. _header-n12docker:

2.Docker 容器
------------------

.. _header-n13docker:

Docker 客户端
~~~~~~~~~~~~~

.. code:: shell

   docker
   docker <command> --help

.. _header-n15docker:

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

.. _header-n22docker:

3.Docker 安装 Ubuntu
------------------------

.. _header-n23docker:

1.查看可用的 Ubuntu 版本
~~~~~~~~~~~~~~~~~~~~~~~~

`Ubuntu 镜像库地址 <https://hub.docker.com/_/ubuntu?tab=tags&page=1>`__

.. _header-n25docker:

2.拉取最新版的 Ubuntu 镜像
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   docker pull ubuntu
   docker pull ubuntu:latest

.. _header-n27docker:

3.查看本地镜像
~~~~~~~~~~~~~~

.. code:: shell

   docker images

.. _header-n29docker:

4.运行容器，并且可以通过 ``exec`` 命令进入 ubuntu 容器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   docker run -itd --name ubuntu-test ubuntu

.. _header-n31docker:

5.安装成功
~~~~~~~~~~

.. code:: shell

   docker ps




.. _header-n33docker:

3.Docker 安装 Python
-------------------------
