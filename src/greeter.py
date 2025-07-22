def get_greeting(language_code):
    """
    根据语言代码返回问候语，模拟 switch-case
    """
    greetings = {
        "en": "Hello",
        "es": "Hola",
        "fr": "Bonjour"
    }
    # 使用 .get() 方法处理找不到 key 的情况
    return greetings.get(language_code, "Greeting not available")

def say_hello(name, language="en"):
    """
    打印完整的问候信息
    """
    if not name:
        return "Error: Name cannot be empty."
    greeting = get_greeting(language)
    return f"{greeting}, {name}!"