# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 语言要求

**思考和回复时必须使用中文。** 所有与用户的交流、代码注释、提交信息等均应使用中文。

## 项目概述

铜鼓纹样检测系统 — 基于YOLOv11的古代铜鼓纹样检测与编目全栈Web应用。

## 技术架构

- **后端** (`backend/`): Django 6.0 + DRF + MySQL，配置模块为 `backend.settings`
  - `users/` 应用 — 自定义用户模型（AbstractUser），通过 `djangorestframework-simplejwt` 实现JWT认证，接口路径 `/api/users/`
  - `detection/` 应用 — YOLOv11推理（ultralytics），检测记录增删改查，接口路径 `/api/detection/`
  - YOLO模型在启动时从 `exp21/weights/best.pt` 全局加载（模块级单例）；可检测3个类别：`sun`（太阳纹）、`wa`（蛙纹）、`lei`（云雷纹）
  - 视图全部使用函数式 `@api_view` 装饰器，错误响应格式统一为 `{message, errors}`
- **前端** (`frontend/`): Vue 3 + Vite + Element Plus + Pinia + Vue Router，开发服务器端口3001，`/api` 代理到后端 :8000
- **部署**: Docker Compose（MySQL 8.0 + Gunicorn + Nginx），详见 `docker-compose.yml` 和 `Dockerfile`

## 常用命令

```bash
# 后端
python manage.py runserver          # 开发服务器 (:8000)
python manage.py migrate            # 执行数据库迁移
python manage.py collectstatic      # 收集静态文件
python manage.py createsuperuser    # 创建管理员用户
python manage.py check              # 验证配置

# 前端
cd frontend
npm install                         # 安装依赖
npm run dev                         # Vite开发服务器 (:3001)
npm run build                       # 生产构建 → frontend/dist/
npm run preview                     # 预览生产构建

# Docker
docker compose up -d                # 启动所有服务
docker compose down                 # 停止所有服务
```

项目无测试配置（无 pytest/Django test/Vitest/Jest）。

## 关键约定

- **认证流程**: JWT令牌存储在localStorage中，键名为 `access_token`/`refresh_token`；`frontend/src/utils/axios.js` 中的axios拦截器处理401时自动刷新令牌；登出时将refresh token加入黑名单
- **API基础URL**: 通过 `VITE_API_BASE_URL` 环境变量配置；默认值为 `http://localhost:8000`
- **Django配置**: 通过 `python-dotenv` 使用 `.env` 文件；所有密钥/配置从环境变量读取，`settings.py` 中设有回退值
- **自定义用户模型**: `users.User` — 设置为 `AUTH_USER_MODEL`，包含 `phone`（唯一，用于密码重置）和 `role`（admin/user）字段
- **密码规则**: 至少8位，包含大写字母、小写字母和数字（见 `users/validators.py`）
- **文件上传**: 图片存储在 `media/detections/`；标注图片压缩至最大800px，JPEG质量85；自动生成Markdown报告至 `media/detections/markdown/`
- **CORS**: 预配置允许localhost端口3000-3004和8080
- **路由守卫**: 仅 `/detection`、`/profile`、`/change-password` 需要认证（通过localStorage中的 `user` 检查）；未登录访问时重定向到登录页并保留 `redirect` 查询参数
- **路径别名**: `@` 在Vite配置中映射到 `frontend/src/`
- **语言**: 代码注释和界面文本使用中文
- **国际化**: 使用 vue-i18n@9（Composition API模式），配置在 `frontend/src/i18n/index.ts`，中英文翻译分别在 `locales/zh.ts` 和 `locales/en.ts`；通过 AppNav 中的 `中/EN` 按钮切换，语言偏好存储在 localStorage `lang` 键
- **UI框架**: Element Plus 已全局注册（`main.ts` 中 `app.use(ElementPlus)`），同时注册了 `@element-plus/icons-vue` 图标；ElMessage 样式已通过 archive-theme.css 覆盖为青铜档案馆风格
- **组件系统**: 自定义组件 ArchiveCard、ArchiveButton、ArchiveInput、BronzeDivider、SectionHeader、StatCard、DetectionCard、TermsDialog、AppNav、AppLayout、Footer、BackToTop；使用 archive-theme.css 中的 CSS 变量

## 前端状态管理

Pinia stores 使用 Composition API 模式，位于 `frontend/src/stores/`：
- **auth.ts**: 管理用户认证状态（login/logout/token刷新/从localStorage恢复），兼容旧版 `token` 键
- **detection.ts**: 管理检测记录（分页查询/图片检测/保存记录/删除记录），含 `patternFilter` 过滤功能

## 部署与CI/CD

- **生产部署**: `docker-compose.prod.yml` 使用 host 网络模式，镜像从 Docker Hub (`recardomlu/tonggu-backend`) 拉取
- **自动更新**: Watchtower 每3600秒检查新镜像并自动部署
- **CI**: GitHub Actions 在 push 到 master 时自动构建并推送 Docker 镜像
- **生产环境变量**: `frontend/.env.production` 设置 `VITE_API_BASE_URL=https://api.tong-gu.cn`
- **Nginx**: 配置SSL（TLS 1.2/1.3）、安全头、SPA fallback（`try_files $uri $uri/ /index.html`）

## 检测API端点

| 端点 | 方法 | 认证 | 说明 |
|---|---|---|---|
| `/api/detection/detect/` | POST | AllowAny | 上传图片运行YOLO推理，返回检测结果和标注图片(base64) |
| `/api/detection/save-record/` | POST | IsAuthenticated | 保存检测记录并生成Markdown报告 |
| `/api/detection/my-records/` | GET | IsAuthenticated | 分页获取用户检测记录 |
| `/api/detection/delete-record/<id>/` | DELETE | IsAuthenticated | 删除检测记录 |
