def format_log(message):
    """
    一个我们不关心的辅助函数
    """
    from datetime import datetime
    return f"[{datetime.now()}] - {message}"