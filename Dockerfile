# 使用 Python 3.12 作为基础镜像
FROM python:3.12-slim

# 设置环境变量
# 防止 Python 生成 .pyc 文件
ENV PYTHONDONTWRITEBYTECODE=1
# 确保 Python 输出不缓冲
ENV PYTHONUNBUFFERED=1
# 设置 Django 设置模块
ENV DJANGO_SETTINGS_MODULE=backend.settings

# 创建非 root 用户
RUN useradd -m appuser

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    # 图像处理依赖
    libgl1 \
    libglib-2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    # MySQL 客户端依赖
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 依赖
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . /app/

# 更改文件所有权
RUN chown -R appuser:appuser /app

# 切换到非 root 用户
USER appuser

# 创建必要的目录
RUN mkdir -p /app/logs /app/media /app/staticfiles

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 8000

# 启动命令（使用 gunicorn 作为生产服务器）
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "backend.wsgi:application"]
