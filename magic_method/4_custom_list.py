"""
  自定义的类，通过实现魔术方法
  从而可以使用相关方法
"""
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