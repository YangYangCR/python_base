class RepresentationDemo:
    """演示对象的字符串表示"""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    """
       给用户展示提供的，提供可读性强的展示
    """
    def __str__(self):
        """用户友好的字符串表示（print 时调用）"""
        return f"📝 对象: {self.name}, 值: {self.value}"

    """
       给开发者调试者提供的，返回可用于重建对象的字符串
    """
    def __repr__(self):
        """开发者友好的字符串表示（交互式环境调用）"""
        return f"RepresentationDemo(name='{self.name}', value={self.value})"

    """
    控制对象在真假判断时的行为
    """
    def __bool__(self):
        """定义布尔上下文中的真假值"""
        return self.value > 0

    def __bytes__(self):
        """定义 bytes() 调用时的行为"""
        return f"{self.name}:{self.value}".encode('utf-8')

    def __format__(self, format_spec):
        """定义 format() 调用时的行为"""
        if format_spec == 'upper':
            return self.name.upper()
        if format_spec == 'lower':
            return self.name.lower()
        return str(self)


# === 测试 ===
print("\n" + "=" * 70)
print("2. 对象表示与类型转换测试")
print("=" * 70)

obj = RepresentationDemo("测试数据", 42)

print("\n--- __str__ 和 __repr__ 测试 ---")
print(f"str(obj): {str(obj)}")  # __str__
print(f"repr(obj): {repr(obj)}")  # __repr__
print(f"print(obj): {obj}")  # __str__

print("\n--- __bool__ 测试 ---")
obj_positive = RepresentationDemo("正数", 10)
obj_negative = RepresentationDemo("负数", -5)
print(f"bool(正数对象): {bool(obj_positive)}")
print(f"bool(负数对象): {bool(obj_negative)}")
if obj_positive:
    print("✅ 对象为真")

print("\n--- __bytes__ 测试 ---")
print(f"bytes(obj): {bytes(obj)}")

print("\n--- __format__ 测试 ---")
print(f"format(obj): {format(obj)}")
print(f"format(obj, 'upper'): {format(obj, 'upper')}")
print(f"format(obj, 'lower'): {format(obj, 'lower')}")