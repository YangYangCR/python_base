import sys
import weakref

print("\n" + "=" * 70)
print("9. 特殊字段测试")
print("=" * 70)

# === 1. __name__ ===
print("\n--- __name__ ---")
print(f"当前模块的 __name__: {__name__}")
print(f"sys 模块的 __name__: {sys.__name__}")


def test_func():
    pass


print(f"函数的 __name__: {test_func.__name__}")

# === 2. __file__ ===
print("\n--- __file__ ---")
print(f"当前文件的 __file__: {__file__}")
print(f"sys 模块的 __file__: {sys.__name__}")

# === 3. __dict__ ===
print("\n--- __dict__ ---")


class DemoClass:
    class_var = "类变量"

    def __init__(self):
        self.instance_var = "实例变量"


obj = DemoClass()
print(f"DemoClass.__dict__: {list(DemoClass.__dict__.keys())}")
print(f"obj.__dict__: {obj.__dict__}")

# === 4. __slots__ ===
print("\n--- __slots__ ---")


class SlotDemo:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = SlotDemo("测试", 10)
print(f"SlotDemo.__slots__: {SlotDemo.__slots__}")
print(f"允许的属性: name={s.name}, age={s.age}")
try:
    s.extra_attr = "会报错"
except AttributeError as e:
    print(f"⚠️ 添加额外属性失败: {e}")

# === 5. __weakref__ ===
print("\n--- __weakref__ ---")


class WeakRefDemo:
    pass


w = WeakRefDemo()
weak_ref = weakref.ref(w)
print(f"弱引用对象: {weak_ref}")
print(f"弱引用指向: {weak_ref()}")

# === 6. __module__ ===
print("\n--- __module__ ---")
print(f"DemoClass 所属模块: {DemoClass.__module__}")

# === 7. __doc__ ===
print("\n--- __doc__ ---")


def documented_func():
    """这是一个有文档字符串的函数"""
    pass


print(f"函数的文档字符串: {documented_func.__doc__}")

# === 8. __all__ ===
print("\n--- __all__ ---")
print("(在模块顶层定义，控制 from module import * 的导出列表)")
