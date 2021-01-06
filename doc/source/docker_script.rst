
Docker
==================

   - 学前准备

      - Linux
      - Spring Boot

   - Docker 学习

      - Docker 概述
      - Docker 安装
      - Docker 命令

         - 镜像命令
         - 容器命令
         - 操作命令
      
      - Docker 镜像
      - 容器数据卷
      - DockerFile
      - Docker 网络原理
      - IDEA 整合 Docker
      - Docker Compose
      - Docker Swarm
      - CI/CD jenkins

1.Docker 概述
-------------------------------------------

1.1 Docker 历史
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   - Docker 历史

      -  2010 年，几个搞 IT 的年轻人，就在美国成立了一加公司 dotCloud，做一些 PASS 的云计算服务！LXC 有关的容器技术。
         他们将自己的技术(容器化技术)命名就是 Docker。Docker 刚刚诞生的时候，没有引起行业的注意，doctCloud 活不下去了。
      
      -  2013 年 Docker 开源。Docker 的优点越来越多地被人发现。Docker 每个月都会更新一个版本！

      -  2014 年 4月9日，Docker 1.0 发布。

         -  Docker 为什么这么火？十分轻巧！
      
         -  在容器技术出来之前，我们都是使用虚拟技术。通过虚拟机可以虚拟出来一台或者多台电脑，
            非常笨重。虚拟机也是属于虚拟化技术，Docker 容器技术，也是一种虚拟化技术。

   - Docker 是基于 Go 语言开发的一个开源项目

      - 管网：https://www.docker.com/
      - 文档：https://docs.docker.com/
      - 仓库：https://hub.docker.com/

1.2 Docker 概述
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.2.1 Docker Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


1.2.2 Docker Engine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. image:: image/engine-components-flow.png

   - Docker 是一个客户端-服务器应用程序，具有以下组件:
      
      - docker daemon prcess
      
         - ``dockerd`` 命令
      
      - REST API 
      
      - command line interface(CLI) client
         
         - ``docker`` 命令

1.2.3 Docker 术语
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. image:: image/architecture.png
   
   - Image

      - Docker 镜像就好比一个模板，可以通过这个模板来创建容器服务
         
         - 镜像->run->容器(提供服务器)

      - 通过镜像可以创建多个容器，最终服务运行或者项目运行就是在容器中。
   
   - Container
   
      - Docker 利用容器技术，独立运行一个或者一组应用，通过镜像来创建、启动、停止、删除、基本命令
      - 可以把容器理解为就是一个简易的 Linux 系统
   
   - Repository
   
      - 仓库就是存放镜像的地方
      - 仓库分为公有仓库、私有仓库

         - 公有仓库:

            - 国内: Docker Hub
            - 国外: 阿里云
         
         - 私有仓库

2.Docker 安装
----------------------------------------------

2.1 环境准备
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - 1.Linux 基础
   - 2.CentOS 7
   - 3.使用 Xshell 连接远程服务器进行操作

2.2 环境查看
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. code-block:: shell

      # 系统内核
      uname -r

      # 系统配置
      cat /etc/os-release

2.3 Dcoker 安装
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 安装目录: https://docs.docker.com/get-docker/

   - macOS: https://docs.docker.com/docker-for-mac/install/
   - Linux: https://docs.docker.com/engine/install/

2.3.1 macOS
^^^^^^^^^^^^^^^^^^

2.3.2 Ubuntu
^^^^^^^^^^^^^^^^^^

1. 删除旧版本

   .. code-block:: shell

      $ sudo apt-get remove docker docker-engine docker.io containerd runc

2. 设置存储库

   .. code-block:: shell

      # 1.更新apt软件包索引并安装软件包以允许apt通过HTTPS使用存储库
      $ sudo apt-get update
      $ sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
      
      # 2.添加Docker的官方GPG密钥
      $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      $ sudo apt-key fingerprint 0EBFCD88
      
      # 3.设置稳定的存储库
      $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

3. 安装 Docker Engine

   .. code-block:: shell

      # 1.更新apt软件包索引
      $ sudo apt-get update
      
      # 2.安装最新版本的Docker Engine和容器化的容器，或转到下一步以安装特定版本
      $ sudo apt-get install docker-ce docker-ce-cli containerd.io

      # 3.查看可用的仓库版本(如果想安装特定版本的Docker Engine)
      $ apt-cache madison docker-ce
      $ sudo apt-get install \
         docker-ce=<VERSION_STRING> \
         docker-ce-cli=<VERSION_STRING> \
         containerd.io

4. 运行 hello-world

   .. code-block:: shell

      # 启动 Docker
      $ systemctl start docker
      $ docker version
      
      # 运行 hello-world
      $ docker run --help
      $ sudo docker run hello-world

      # 查看下载的 image
      $ docker images

5. 升级 Docker Engine

   .. code-block:: shell

      # 按照安装说明进行
      $ sudo apt-get update

6. 卸载 Docker Engine

   - 卸载 Docker Engine, CLI, Containerd packages

      .. code-block:: shell

         $ sudo apt-get purge docker-ce docker-ce-cli containerd.io
      
   - 删除 Images, containers, volumes

      .. code-block:: shell

         $ sudo rm -rf /var/lib/docker

.. note:: 

   customized configuration files 需要手动删除

3.Docker 命令
------------------------------------------------



4.Docker 镜像
------------------------------------------------












4.Docker 安装环境
---------------------------------------------------

4.1 Docker 安装 Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4.1.1 查看可用的 Ubuntu 版本
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - `Ubuntu 镜像库地址 <https://hub.docker.com/_/ubuntu?tab=tags&page=1>`__

4.1.2 拉取最新版的 Ubuntu 镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      docker pull ubuntu
      docker pull ubuntu:latest

4.1.3 查看本地镜像
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      docker images

4.1.4 运行容器
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - 可以通过 ``exec`` 命令进入 ubuntu 容器

   .. code:: shell

      docker run -itd --name ubuntu-test ubuntu

4.1.5 安装成功
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code:: shell

      docker ps

4.2 Docker 安装 Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4.2.1 test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


4.2.2 test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


5.Docker 使用示例
----------------------------------------------------

5.1 公司工作站环境
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   1. 查看容器

      .. code-block:: shell
      
         $ sudo docker ps -a

   2. 开启 TensorFlow 环境

      .. code-block:: shell

         $ sudo docker attach tf_env

   3. 数据目录

      .. code-block:: shell

         $ cd /workspace/work_dir/dataSets
      
   4. 退出 TensorFlow Docker(容器还在运行)

      .. code-block:: shell

         $ Ctrl + P + Q
