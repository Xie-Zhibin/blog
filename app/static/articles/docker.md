# docker 笔记

****
### 简介
Docker是基于Linux 64bit下的一个轻量级的开源应用容器引擎。
Docker 是一个开源项目，诞生于 2013 年初，最初是 dotCloud 公司内部的一个业余项目。它基于 Google 公司推出的 Go 语言实现。 项目后来加入了 Linux 基金会，遵从了 Apache 2.0 协议，项目代码在 GitHub 上进行维护。
Docker容器除了运行其中应用外，基本不消耗额外的系统资源，使得应用的性能很高，同时系统的开销尽量小。相比于传统虚拟机，docker容器占用的资源非常少，启动速度也非常快。

利用docker可以实现网站应用一键部署，大量地节约了部署测试的时间。

***
### 常用命令
* 获取镜像：docker pull REPO_NAME:TAG_NAME
* 创建容器：docker run --name CONTAINER_NAME [params...]
* 创建容器时挂载数据卷: docker run -v local_dir:docker_dir  (冒号前为宿主机目录，必须为绝对路径，冒号后为镜像内挂载的路径)
* 清楚所有未打过标签的本地镜像：docker rmi $(docker images -q -f "dangling=true")
* 清除所有容器：docker rm $(docker ps -a -q)，需要清除正在运行的容器需加 -f 参数

docker 的很多操作都与git相似，可以类比学习。
***

### 注意事项
* Dockerfile 中的CMD 指定启动容器时执行的命令，每个 Dockerfile 只能有一条 CMD 命令。如果指定了多条命令，只有最后一条会被执行。如果确实要执行多条命令，那么可以将命令写在shell脚本中，再由CMD命令运行这个shell脚本。

* Dockerfile 中不支持将主机目录作为数据卷这种用法，这是因为 Dockerfile 是为了移植和分享用的。然而，不同操作系统的路径格式不一样，所以目前还不能支持。只能在创建容器的时候以参数的形式传递。