import base64
import easyocr
from flask import Flask, request, jsonify

app = Flask(__name__)

def ocr(image, result_method="0"):
    """
    使用本地ocr模型
    :param result_method:
    :param image: url/本地图片路径/bytes
    :return: 识别内容集合
    """
    reader = easyocr.Reader(['ch_sim', 'en'])
    result = reader.readtext(image, paragraph="False")
    if result_method == "origin":
        return result
    elif result_method == "text":
        content = ""
        for i in result:
            content = content + i[-1]
        return content
    else:
        content = ""
        for i in result:
            content = content + i[-1]
        return content


@app.route('/ocr', methods=['POST'])
def receive():
    method = request.form.get("method")
    data = request.form.get("data")
    result_method = request.form.get("result")
    result = ""
    msg = ""
    ok = 0
    try:
        if method == "url":
            result = ocr(data, result_method)
        elif method == "base64":
            result = ocr(base64.b64decode(data), result_method)
        elif method == "file":
            result = ocr(request.files["img"].read(), result_method)
        else:
            ok = -1
    except:
        ok = -2
    if ok == 0:
        msg = "识别成功"
    elif ok == -1:
        msg = "请传入正确的method参数"
    elif ok == -2:
        msg = "ocr识别过程中故障"
    return jsonify({"code": str(ok), "msg": msg, "result": result})


@app.errorhandler(404)
def internal_server_error(e):
    return jsonify({"code": "-3", "msg": "无效路径"})


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
