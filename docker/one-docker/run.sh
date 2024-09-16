# 使用当前目录下的 Dockerfile 构建一个名为 fastapi-app 的镜像
sudo docker build -t fastapi-app .

# 以后台模式运行一个名为 fastapi1 的容器，使用前面构建的 fastapi-app 镜像
# 将容器内的 8000 端口映射到宿主机的 80 端口
sudo docker run -d --name fastapi1 -p 80:8000 fastapi-app
