"""
__new__ 负责"创造"对象（分配内存），
__init__ 负责"初始化"对象（填充数据）
"""


class LifecycleDemo:
    """演示对象创建和销毁的生命周期"""

    def __new__(cls, *args, **kwargs):
        """创建并返回新实例（在 __init__ 之前调用）"""
        print("1. __new__ 被调用")
        instance = super().__new__(cls)  # 真正创建对象 分配内存 返回一个"空的"实例（还没有任何属性）
        print("2. 对象已创建，内存地址:", id(instance))
        return instance  # 必须返回实例

    def __init__(self, name):
        """初始化实例属性"""
        print(f"📦 [__init__] 初始化实例，name={name}")
        self.name = name
        self.created_at = "2024-01-01"

    def __del__(self):
        """对象被垃圾回收前调用（析构函数）"""
        print(f"🗑️ [__del__] 销毁实例: {self.name}")

    def __repr__(self):
        return f"LifecycleDemo(name='{self.name}')"

"""
    单例模式
"""
class Singleton:
    _instance = None  # 类属性，存储唯一实例

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("🔧 创建唯一实例")
            cls._instance = super().__new__(cls)
        else:
            print("♻️ 复用已有实例")
        return cls._instance

    def __init__(self, name):
        print(f"📦 初始化: {name}")
        self.name = name



def test_life_cycle():
    # === 测试 ===
    print("=" * 70)
    print("1. 类生命周期管理测试")
    print("=" * 70)

    print("\n--- __new__ 和 __init__ 测试 ---")
    obj = LifecycleDemo("lifecycle_object")
    print(f"创建的对象: {obj}")

    print("\n--- __del__ 测试 ---")
    del obj
    print("对象已删除\n")

print("===================================================================")

def test_singleton():
    # 测试
    s1 = Singleton("第一次")
    s2 = Singleton("第二次")
    print(f"s1 is s2: {s1 is s2}")  # True
    print(f"s1.name: {s1.name}")  # 第二次（因为第二次初始化覆盖了）
    print(f"s2.name: {s2.name}")  # 第二次

test_life_cycle()
test_singleton()