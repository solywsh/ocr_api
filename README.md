# OCR_API

## dokcer部署

在文件目录下：

```sh
docker build -t ocr:latest .
docker run -dt --name ocr_api --restart=always -p 5000:80 ocr:latest
```

## 接口定义

`[POST]http://{ip}:5000/ocr`

| 参数   | 值                                                           |
| ------ | ------------------------------------------------------------ |
| method | `url`：图片url链接`base64`：图片base64编码 `file`：文件      |
| data   | 图片url链接或base64编码数据，注意去除`data:image/png;base64,`部分 |
| img    | `method=file`时传入的文件                                    |
