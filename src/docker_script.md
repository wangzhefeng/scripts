
# Docker

## Docker Hello World

### 在容器内运行一个应用程序

```shell
docker run ubuntu:15.10 /bin/echo "Hello world"
```

### 运行交互式的容器

```shell
docker run -i -t ubuntu:15.10 /bin/bash
cat /proc/version
ls
# 退出容器
exit # or Ctrl+D
```

### 启动容器（后台模式）

```shell
docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
```

### 停止容器

```shell
docker stop <>
docker ps
docker stop amazing_cori
```

## Docker 容器

### Docker 客户端

```shell
docker
docker <command> --help
```

### Docker 容器使用

获取镜像

```shell
docker pull ubuntu
```

启动容器

```shell
docker run -it ubuntu /bin/bash
```

启动已停止运行的容器

```shell
docker ps -a
```

## Docker 安装 Ubuntu

### 1.查看可用的 Ubuntu 版本

[Ubuntu 镜像库地址](https://hub.docker.com/_/ubuntu?tab=tags&page=1)

### 2.拉取最新版的 Ubuntu 镜像

```shell
docker pull ubuntu
docker pull ubuntu:latest
```

### 3.查看本地镜像

```shell
docker images
```

### 4.运行容器，并且可以通过 `exec` 命令进入 ubuntu 容器

```shell
docker run -itd --name ubuntu-test ubuntu
```

### 5.安装成功

```shell
docker ps
```

## Docker 安装 Python

