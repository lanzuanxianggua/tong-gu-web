#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """设置环境变量"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入 Django或"
            "未激活虚拟环境？"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
