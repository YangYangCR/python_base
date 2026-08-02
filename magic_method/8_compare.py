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
