# Python 特殊方法（魔术方法）与特殊字段完整测试指南

> **版本**: 1.0\
> **适用 Python 版本**: 3.8+\
> **最后更新**: 2026-07-30\
> **说明**: 本文档提供 Python
> 常用特殊方法和特殊字段的说明、测试代码以及快速查询表。

## 📋 目录

-   环境准备
-   类生命周期管理
-   对象表示与类型转换
-   运算符重载
-   容器与序列协议
-   属性控制
-   上下文管理（with）
-   可调用对象
-   比较运算
-   特殊字段
-   综合示例
-   快速参考表 环境准备

## 1. 类生命周期管理

## 2. 对象表示与类型转换

## 3. 运算符重载

## 4. 容器与序列协议

## 5. 属性控制

## 6. 上下文管理（with 语句）

## 7. 可调用对象

## 8. 比较运算

## 9. 特殊字段（属性）

## 10. 完整综合示例

## 11. 快速参考表

## 🛠️ 环境准备

``` python
"""
Python 特殊方法测试环境
运行前请确保 Python 版本 >= 3.8
"""

import sys
import time
import weakref
from functools import total_ordering

print(f"🐍 Python 版本: {sys.version}")
print(f"📂 当前文件: {__file__ if '__file__' in dir() else '交互式环境'}")
print("=" * 70)
```

## 1. 类生命周期管理

**new** · **init** · **del**

``` python
class LifecycleDemo:
    """演示对象创建和销毁的生命周期"""
    
    def __new__(cls, *args, **kwargs):
        """创建并返回新实例（在 __init__ 之前调用）"""
        print(f"🔧 [__new__] 创建实例，参数: args={args}, kwargs={kwargs}")
        instance = super().__new__(cls)
        print(f"🔧 [__new__] 实例创建完成: {instance}")
        return instance
    
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


# === 测试 ===
print("\n" + "=" * 70)
print("1. 类生命周期管理测试")
print("=" * 70)

print("\n--- __new__ 和 __init__ 测试 ---")
obj = LifecycleDemo("测试对象")
print(f"创建的对象: {obj}")

print("\n--- __del__ 测试 ---")
del obj
print("对象已删除\n")
```

## 2. 对象表示与类型转换

**str** · **repr** · **bool** · **bytes** · **format**

``` python
class RepresentationDemo:
    """演示对象的字符串表示"""
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        """用户友好的字符串表示（print 时调用）"""
        return f"📝 对象: {self.name}, 值: {self.value}"
    
    def __repr__(self):
        """开发者友好的字符串表示（交互式环境调用）"""
        return f"RepresentationDemo(name='{self.name}', value={self.value})"
    
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
print(f"str(obj): {str(obj)}")        # __str__
print(f"repr(obj): {repr(obj)}")      # __repr__
print(f"print(obj): {obj}")           # __str__

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
```

## 3. 运算符重载

算术运算符 · 反向运算符 · 一元运算符

``` python
class Vector:
    """二维向量，演示运算符重载"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # === 算术运算符 ===
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented
    
    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x // other, self.y // other)
        return NotImplemented
    
    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x % other, self.y % other)
        return NotImplemented
    
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x ** other, self.y ** other)
        return NotImplemented
    
    # === 反向运算符 ===
    def __radd__(self, other):
        return self.__add__(other)
    
    def __rsub__(self, other):
        return Vector(other - self.x, other - self.y)
    
    # === 一元运算符 ===
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __pos__(self):
        return self
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# === 测试 ===
print("\n" + "=" * 70)
print("3. 运算符重载测试")
print("=" * 70)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}\n")

print(f"v1 + v2 = {v1 + v2}")       # __add__
print(f"v1 - v2 = {v1 - v2}")       # __sub__
print(f"v1 * 3 = {v1 * 3}")         # __mul__
print(f"3 * v1 = {3 * v1}")         # __rmul__
print(f"v1 / 2 = {v1 / 2}")         # __truediv__
print(f"v1 // 2 = {v1 // 2}")       # __floordiv__
print(f"v1 % 2 = {v1 % 2}")         # __mod__
print(f"v1 ** 2 = {v1 ** 2}")       # __pow__
print(f"-v1 = {-v1}")               # __neg__
print(f"abs(v1) = {abs(v1):.2f}")   # __abs__
```

## 4. 容器与序列协议

**len** · **getitem** · **setitem** · **delitem** · **iter** ·
**contains** · **reversed**

``` python
class CustomList:
    """自定义列表类，实现序列协议"""
    
    def __init__(self, items=None):
        self._items = list(items) if items else []
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return CustomList(self._items[index])
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __delitem__(self, index):
        del self._items[index]
    
    def __iter__(self):
        return iter(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __reversed__(self):
        return reversed(self._items)
    
    def __add__(self, other):
        if isinstance(other, CustomList):
            return CustomList(self._items + other._items)
        return NotImplemented
    
    def __repr__(self):
        return f"CustomList({self._items})"


# === 测试 ===
print("\n" + "=" * 70)
print("4. 容器与序列协议测试")
print("=" * 70)

cl = CustomList([10, 20, 30, 40, 50])

print(f"创建: {cl}")
print(f"长度 (__len__): {len(cl)}")
print(f"索引访问 (__getitem__): cl[2] = {cl[2]}")
print(f"切片 (__getitem__): cl[1:4] = {cl[1:4]}")

print("\n--- 修改测试 ---")
cl[2] = 99
print(f"修改后 (__setitem__): {cl}")
del cl[0]
print(f"删除后 (__delitem__): {cl}")

print("\n--- 迭代测试 (__iter__) ---")
print("遍历元素:", end=" ")
for item in cl:
    print(item, end=" ")
print()

print("\n--- 包含检查 (__contains__) ---")
print(f"30 in cl? {30 in cl}")
print(f"40 in cl? {40 in cl}")

print("\n--- 拼接测试 (__add__) ---")
cl2 = CustomList([60, 70])
print(f"cl + cl2 = {cl + cl2}")

print("\n--- 反转测试 (__reversed__) ---")
print(f"list(reversed(cl)): {list(reversed(cl))}")
```

## 5. 属性控制

**getattr** · **setattr** · **delattr** · **getattribute** · **dir**

``` python
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
```

## 6. 上下文管理（with 语句）

**enter** · **exit**

``` python
class Timer:
    """计时器上下文管理器"""
    
    def __init__(self, name="任务"):
        self.name = name
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        print(f"⏱️ 开始计时: {self.name}")
        self.start_time = time.time()
        return self
    
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
    
    def __enter__(self):
        print(f"📂 打开文件: {self.filename}")
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file
    
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
```

## 7. 可调用对象

**call**

``` python
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
```

## 8. 比较运算

**eq** · **lt** · **le** · **gt** · **ge** · **ne** · **hash**

``` python
@total_ordering
class Person:
    """人物类，演示比较运算符"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age
    
    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
    
    def __le__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age <= other.age
    
    def __gt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age > other.age
    
    def __ge__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age >= other.age
    
    def __ne__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age != other.age
    
    def __hash__(self):
        return hash(self.age)
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


# === 测试 ===
print("\n" + "=" * 70)
print("8. 比较运算测试")
print("=" * 70)

p1 = Person("张三", 25)
p2 = Person("李四", 30)
p3 = Person("王五", 25)

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p3 = {p3}\n")

print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")
print(f"p1 < p2: {p1 < p2}")
print(f"p1 > p2: {p1 > p2}")
print(f"p1 <= p2: {p1 <= p2}")
print(f"p1 >= p2: {p1 >= p2}")
print(f"p1 != p2: {p1 != p2}")

print("\n--- 排序演示 ---")
people = [p2, p1, p3]
print(f"排序前: {people}")
people.sort()
print(f"排序后: {people}")

print("\n--- 集合去重演示 ---")
unique = set(people)
print(f"去重后: {unique}")
```

## 9. 特殊字段（属性）

**name** · **file** · **dict** · **slots** · **weakref** · **module** ·
**doc** · **all**

``` python
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
print(f"sys 模块的 __file__: {sys.__file__}")

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
```

## 10. 完整综合示例

SmartDict ------ 融合多种特殊方法的实用类

``` python
class SmartDict:
    """
    智能字典类
    综合演示多种特殊方法的应用场景
    """
    
    def __init__(self, **kwargs):
        self._data = dict(kwargs)
        self._call_count = 0
    
    # === 容器协议 ===
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, key):
        return self._data.get(key, None)
    
    def __setitem__(self, key, value):
        self._data[key] = value
    
    def __delitem__(self, key):
        del self._data[key]
    
    def __iter__(self):
        return iter(self._data)
    
    def __contains__(self, key):
        return key in self._data
    
    # === 对象表示 ===
    def __str__(self):
        return f"SmartDict({self._data})"
    
    def __repr__(self):
        return f"SmartDict(**{self._data})"
    
    # === 比较运算 ===
    def __eq__(self, other):
        if not isinstance(other, SmartDict):
            return False
        return self._data == other._data
    
    def __lt__(self, other):
        if not isinstance(other, SmartDict):
            return NotImplemented
        return len(self) < len(other)
    
    # === 运算符重载 ===
    def __add__(self, other):
        if isinstance(other, SmartDict):
            new_data = {**self._data, **other._data}
            return SmartDict(**new_data)
        return NotImplemented
    
    # === 可调用 ===
    def __call__(self, key, default=None):
        self._call_count += 1
        return self._data.get(key, default)
    
    # === 上下文管理 ===
    def __enter__(self):
        print("🔓 进入 SmartDict 上下文")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("🔒 退出 SmartDict 上下文")
        if exc_type:
            print(f"⚠️ 异常: {exc_type.__name__}")
        return False
    
    # === 属性控制 ===
    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"SmartDict 没有属性 '{name}'")
    
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            self._data[name] = value
    
    def get_call_count(self):
        return self._call_count


# === 测试综合示例 ===
print("\n" + "=" * 70)
print("10. 综合示例: SmartDict 完整测试")
print("=" * 70)

sd = SmartDict(name="Python", version=3.10, year=2024)
print(f"创建: {sd}")

print("\n--- 容器协议 ---")
print(f"长度: {len(sd)}")
print(f"访问 'name': {sd['name']}")
sd['author'] = "Guido"
print(f"设置后: {sd}")
print(f"'author' in sd: {'author' in sd}")
print("迭代:", end=" ")
for key in sd:
    print(key, end=" ")
print()

print("\n--- 属性控制 ---")
print(f"sd.name = {sd.name}")
sd.country = "荷兰"
print(f"属性设置后: {sd}")

print("\n--- 可调用 ---")
print(f"sd('name') = {sd('name')}")
print(f"调用次数: {sd.get_call_count()}")

print("\n--- 比较运算 ---")
sd2 = SmartDict(a=1, b=2)
print(f"sd == sd2? {sd == sd2}")
print(f"len(sd) > len(sd2)? {len(sd) > len(sd2)}")

print("\n--- 运算符重载 ---")
sd3 = sd + sd2
print(f"sd + sd2 = {sd3}")

print("\n--- 上下文管理 ---")
with sd:
    print(f"在上下文中: {sd}")
```

## 11. 快速参考表

类生命周期 特殊方法 作用 调用时机 **new**(cls, ...) 创建新实例 obj =
Class() **init**(self, ...) 初始化实例 obj = Class() **del**(self)
销毁实例 垃圾回收时 对象表示 特殊方法 作用 调用时机 **str**(self)
用户友好字符串 print(obj), str(obj) **repr**(self) 开发者友好字符串
repr(obj), 交互式 **bool**(self) 布尔值 if obj, bool(obj)
**bytes**(self) 字节表示 bytes(obj) **format**(self, spec) 格式化
format(obj, spec) 运算符重载 特殊方法 作用 调用时机 **add**(self, other)
加法 obj + other **sub**(self, other) 减法 obj - other **mul**(self,
other) 乘法 obj \* other **truediv**(self, other) 除法 obj / other
**floordiv**(self, other) 整除 obj // other **mod**(self, other) 取模
obj % other **pow**(self, other) 幂运算 obj \*\* other **neg**(self)
取负 -obj **pos**(self) 取正 +obj **abs**(self) 绝对值 abs(obj) 容器协议
特殊方法 作用 调用时机 **len**(self) 长度 len(obj) **getitem**(self,
key) 获取元素 obj\[key\] **setitem**(self, key, val) 设置元素 obj\[key\]
= val **delitem**(self, key) 删除元素 del obj\[key\] **iter**(self)
迭代器 iter(obj), for **contains**(self, item) 包含检查 item in obj
**reversed**(self) 反转 reversed(obj) 属性控制 特殊方法 作用 调用时机
**getattr**(self, name) 不存在的属性 obj.unknown **setattr**(self, name,
val) 设置属性 obj.attr = val **delattr**(self, name) 删除属性 del
obj.attr **getattribute**(self, name) 任何属性访问 obj.attr
**dir**(self) 属性列表 dir(obj) 其他特殊方法 特殊方法 作用 调用时机
**call**(self, ...) 可调用对象 obj() **enter**(self) 进入上下文 with
obj: **exit**(self, ...) 退出上下文 with obj: **eq**(self, other) 等于
obj == other **lt**(self, other) 小于 obj \< other **hash**(self) 哈希值
hash(obj), 集合键 特殊字段 字段名称 作用 **name** 模块/函数/类的名称
**file** 模块文件路径 **dict** 对象的属性字典 **slots** 限制允许的属性
**weakref** 弱引用支持 **module** 类所属模块 **doc** 文档字符串 **all**
公共导出列表
