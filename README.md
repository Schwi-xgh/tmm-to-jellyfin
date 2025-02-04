# tmm-to-jellyfin
TMM导入演员图片到Jellyfin

​		

TMM刮削Jellyfin演员照片不显示的问题

使用Jellyfin演员图下载不全，每个影片最多拉取15张，之后的不会拉取

而TMM可以下载所有演员图，但是路径在每个影片资源路径下

Jellyfin的演员图路径在Jellyfin\ServerData\metadata\People下

可以利用TMM搜刮演员图片，通过脚本整理后导入到Jellyfin

​		

使用指南：

1.电影和电视节目两个都需要开启演员图片保存到 .actors 目录下

2.利用脚本提取演员图片重命名并整理至临时People图片文件夹

3.把整理好的图片文件夹剪切至Jellyfin\ServerData\metadata\People目录下（从安装路径找）

4.打开Jellyfin的计划任务，点击刷新演职人员

https://blog.csdn.net/Schwi_xgh/article/details/145435503