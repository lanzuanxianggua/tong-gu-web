#!/bin/bash

# 数据库备份脚本

# 配置
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="./backups"
DB_CONTAINER="tonggu-db"
DB_USER="app_user"
DB_PASSWORD="Zx9!cV7@bN3#mK5"
DB_NAME="tong-gu"

# 创建备份目录
mkdir -p $BACKUP_DIR

# 执行备份
echo "开始备份数据库 $DB_NAME..."
docker exec $DB_CONTAINER mysqldump -u $DB_USER -p$DB_PASSWORD $DB_NAME > $BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql

if [ $? -eq 0 ]; then
    echo "备份成功: $BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql"
    
    # 压缩备份文件
    gzip $BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql
    echo "备份文件已压缩: $BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql.gz"
    
    # 保留最近7天的备份
    echo "清理7天前的备份文件..."
    find $BACKUP_DIR -name "${DB_NAME}_*.sql.gz" -mtime +7 -delete
    echo "清理完成"
else
    echo "备份失败"
    exit 1
fi
