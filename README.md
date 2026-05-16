# 铜鼓纹样检测系统

基于 YOLOv11 的古代铜鼓纹样检测与编目全栈 Web 应用。

## 技术栈

- **后端**: Django 6.0 + Django REST Framework + MySQL
- **前端**: Vue 3 + Vite + Element Plus + Pinia
- **AI 推理**: YOLOv11（ultralytics），可检测太阳纹、蛙纹、云雷纹
- **认证**: JWT（djangorestframework-simplejwt）
- **部署**: Docker Compose / 宝塔面板 + Gunicorn + Nginx

## 快速开始

### 1. 环境要求

- Python 3.10+
- Node.js 18+
- MySQL 8.0+

### 2. 后端配置

```bash
# 复制环境变量模板并填写配置
cp .env.example .env
# 编辑 .env，填入 SECRET_KEY、数据库密码等敏感信息

# 创建虚拟环境并安装依赖
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt

# 初始化数据库
python manage.py migrate
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver
```

### 3. 前端配置

```bash
cd frontend
npm install

# 开发环境 — API 默认指向 http://localhost:8000
npm run dev

# 生产构建
npm run build
```

### 4. Docker 部署

```bash
# 复制生产环境变量模板并填写配置
cp .env.prod.example .env.production

docker compose up -d
```

## 环境变量说明

| 变量 | 说明 | 示例 |
|------|------|------|
| `SECRET_KEY` | Django 密钥，至少32字符 | `python -c "import secrets; print(secrets.token_urlsafe(50))"` |
| `DEBUG` | 调试模式，生产环境必须为 `False` | `False` |
| `ALLOWED_HOSTS` | 允许的域名，逗号分隔 | `api.tong-gu.cn,localhost` |
| `DB_NAME` | 数据库名 | `tonggu` |
| `DB_USER` | 数据库用户 | `tonggu` |
| `DB_PASSWORD` | 数据库密码 | - |
| `DB_HOST` | 数据库地址 | `127.0.0.1` |
| `DB_PORT` | 数据库端口 | `3306` |
| `SECURE_SSL_REDIRECT` | HTTPS 重定向（CDN/反向代理后设为 False） | `False` |
| `VITE_API_BASE_URL` | 前端 API 地址 | `https://api.tong-gu.cn` |

## API 端点

| 端点 | 方法 | 认证 | 说明 |
|------|------|------|------|
| `/api/users/register/` | POST | AllowAny | 用户注册 |
| `/api/users/login/` | POST | AllowAny | 用户登录 |
| `/api/users/logout/` | POST | IsAuthenticated | 用户登出 |
| `/api/detection/detect/` | POST | AllowAny | 上传图片运行 YOLO 推理 |
| `/api/detection/save-record/` | POST | IsAuthenticated | 保存检测记录 |
| `/api/detection/my-records/` | GET | IsAuthenticated | 获取用户检测记录 |
| `/api/detection/delete-record/<id>/` | DELETE | IsAuthenticated | 删除检测记录 |

## 项目结构

```
├── backend/            # Django 项目配置
├── users/              # 用户认证应用
├── detection/          # 检测功能应用
├── frontend/           # Vue 3 前端
│   ├── src/
│   │   ├── stores/     # Pinia 状态管理
│   │   ├── views/      # 页面组件
│   │   ├── components/ # 通用组件
│   │   └── i18n/       # 国际化
│   └── dist/           # 构建输出（不提交）
├── exp21/              # YOLO 模型权重
├── nginx.conf          # Nginx 配置
├── docker-compose.yml  # Docker 开发环境
└── requirements.txt    # Python 依赖
```

## 安全注意事项

- `.env` 文件包含敏感信息，已被 `.gitignore` 排除，**切勿提交到版本库**
- 生产环境务必设置 `DEBUG=False`
- `SECRET_KEY` 必须使用强随机密钥，不要使用默认值
- 数据库用户应使用最小权限原则
- 通过 CDN/反向代理部署时，`SECURE_SSL_REDIRECT` 设为 `False`，由代理层处理 HTTPS

## 常用命令

```bash
# 后端
python manage.py runserver          # 开发服务器 (:8000)
python manage.py migrate            # 数据库迁移
python manage.py collectstatic      # 收集静态文件
python manage.py createsuperuser    # 创建管理员

# 前端
cd frontend && npm run dev          # 开发服务器 (:3001)
cd frontend && npm run build        # 生产构建

# Docker
docker compose up -d                # 启动服务
docker compose down                 # 停止服务
```

## License

MIT
