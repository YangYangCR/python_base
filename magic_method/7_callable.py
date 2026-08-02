class CallableDemo:
    """使对象可以像函数一样被调用"""

    def __init__(self, prefix="[CALL]"):
        self.prefix = prefix
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"🔔 [__call__] 第 {self.call_count} 次调用")
        print(f"   参数: args={args}, kwargs={kwargs}")
        return f"{self.prefix} 调用结果: {args}"


# === 测试 ===
print("\n" + "=" * 70)
print("7. 可调用对象测试")
print("=" * 70)

callable_obj = CallableDemo("[RESULT]")

print("将对象当作函数调用:")
result1 = callable_obj(1, 2, 3)
print(f"结果: {result1}\n")

result2 = callable_obj(a=10, b=20)
print(f"结果: {result2}\n")

print(f"callable(callable_obj) = {callable(callable_obj)}")
print(f"调用次数: {callable_obj.call_count}")
