from bottle import Bottle, run, request, response
import os

app = Bottle()

# =========================
# 允许跨域访问（部署后）
# =========================
@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = 'https://deployment-frontend.vercel.app'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'

# =========================
# 首页
# =========================
@app.get('/')
def home():
    return {"message": "✅ Bottle backend is running on Render!"}

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
    port = int(os.environ.get("PORT", 10000))
    print(f"✅ 后端启动成功：http://0.0.0.0:{port}")
    run(app, host='0.0.0.0', port=port, debug=True)
