# upload-web-docker
简单的可以上传和共享自己文件的web网页部署

## 文件结构

在你的服务器上建一个目录，比如叫 `file-server`，结构如下：

```
file-server/
├── app.py
├── templates/
│   └── index.html
├── files/
│   ├── 文件1.zip
│   ├── 文件2.pdf
│   └── 文件3.txt
├── Dockerfile
└── requirements.txt
```



### 构建并运行

在 `file-server` 目录下执行：

```
docker build -t file-server .
docker run -d -p 5000:5000 --name my-file-server file-server
```



浏览器打开：

```
http://<你的服务器IP>:5000
你就能看到文件列表，点击即可下载。
```

**查看日志**

```
docker logs my-file-server --tail 50
```

