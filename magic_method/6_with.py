import time

class Timer:
    """计时器上下文管理器"""

    def __init__(self, name="任务"):
        self.name = name
        self.start_time = None
        self.end_time = None

    # 使用with语句进入代码块时执行
    def __enter__(self):
        print(f"⏱️ 开始计时: {self.name}")
        self.start_time = time.time()
        return self

    # 退出with语句代码块时执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"⏱️ {self.name} 耗时: {elapsed:.4f} 秒")

        if exc_type:
            print(f"⚠️ 捕获到异常: {exc_type.__name__}: {exc_val}")
        return False


class FileHandler:
    """文件处理器，演示资源管理"""

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    # 使用with语句进入代码块时执行
    def __enter__(self):
        print(f"📂 打开文件: {self.filename}")
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file

    # 退出with语句代码块时执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"📂 关闭文件: {self.filename}")
            self.file.close()
        return False


# === 测试 ===
print("\n" + "=" * 70)
print("6. 上下文管理测试")
print("=" * 70)

print("\n--- Timer 示例 ---")
with Timer("睡眠测试"):
    time.sleep(0.1)

print("\n--- 异常处理示例 ---")
try:
    with Timer("异常测试"):
        raise ValueError("模拟异常")
except ValueError:
    print("✅ 异常被正确捕获")

print("\n--- 文件管理示例 ---")
with open("test.txt", "w", encoding='utf-8') as f:
    f.write("Hello, 世界!")

with FileHandler("test.txt", "r") as f:
    content = f.read()
    print(f"📄 文件内容: {content}")

# 清理
import os

os.remove("test.txt")
