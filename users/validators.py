import re


def validate_password_strength(value):
    """
    通用密码强度验证器
    - 至少 8 个字符
    - 包含至少一个大写字母
    - 包含至少一个小写字母
    - 包含至少一个数字
    """
    if len(value) < 8:
        raise ValueError('密码长度至少为 8 位')
    if not re.search(r'[A-Z]', value):
        raise ValueError('密码必须包含至少一个大写字母')
    if not re.search(r'[a-z]', value):
        raise ValueError('密码必须包含至少一个小写字母')
    if not re.search(r'\d', value):
        raise ValueError('密码必须包含至少一个数字')
    return value
