class PropertyDemo:
    """演示属性访问控制"""

    def __init__(self, name):
        self._name = name
        self._data = {}

    def __getattr__(self, name):
        """访问不存在的属性时调用"""
        print(f"🔍 [__getattr__] 访问不存在的属性: {name}")
        return f"属性 '{name}' 不存在"

    def __setattr__(self, name, value):
        """设置任何属性时调用"""
        print(f"✏️ [__setattr__] 设置属性: {name} = {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        """删除属性时调用"""
        print(f"🗑️ [__delattr__] 删除属性: {name}")
        super().__delattr__(name)

    def __getattribute__(self, name):
        """访问任何属性时调用（无论是否存在）"""
        print(f"👀 [__getattribute__] 访问属性: {name}")
        return super().__getattribute__(name)

    def __dir__(self):
        """自定义 dir() 返回的属性列表"""
        return ['_name', 'name', 'data', 'custom_attr']

    def get_name(self):
        return self._name


# === 测试 ===
print("\n" + "=" * 70)
print("5. 属性控制测试")
print("=" * 70)

pd = PropertyDemo("测试对象")

print("\n--- 访问现有属性 ---")
print(f"pd._name = {pd._name}")

print("\n--- 访问不存在的属性 ---")
print(f"pd.unknown = {pd.unknown}")

print("\n--- 设置属性 ---")
pd.new_attr = "新值"

print("\n--- 删除属性 ---")
del pd.new_attr

print("\n--- 查看 dir() ---")
print(f"dir(pd) = {dir(pd)}")
