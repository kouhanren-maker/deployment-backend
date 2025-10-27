from bottle import Bottle, run, request, response
import json

app = Bottle()

# =========================
# 允许跨域访问（前端 5175）
# =========================
@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5175'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'

# =========================
# 测试接口
# =========================
@app.get('/api/test')
def test():
    return {"message": "✅ 后端正常工作！"}

# =========================
# 模拟登录接口
# =========================
@app.post('/api/login')
def login():
    username = request.forms.get('userName')
    password = request.forms.get('userPw')

    if username == "admin" and password == "123":
        return {"success": True, "message": "登录成功"}
    else:
        return {"success": False, "message": "用户名或密码错误"}

# =========================
# 启动服务器
# =========================
if __name__ == '__main__':
    print("✅ 后端启动成功：http://127.0.0.1:8081")
    run(app, host='127.0.0.1', port=8081, debug=True)
