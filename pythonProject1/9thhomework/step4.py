class Person:
    def __init__(self, name, age, base_mood=50):
        self.name = name
        self.age = age
        self.feed_count = 0
        self.base_mood = base_mood

    def feed(self, cat):
        self.feed_count += 1
        self.base_mood += 10
        cat.eat(self)
        print(f"{self.name} 投喂了 {cat.name}，{self.name} 的心情指数提升了 10，现在心情指数是 {self.base_mood}。")


class Cat:
    def __init__(self, name, breed, base_affection=30):
        self.name = name
        self.breed = breed
        self.feed_count = 0
        self.base_affection = base_affection

    def eat(self, person):
        self.feed_count += 1
        self.base_affection += 5
        print(
            f"{self.name} 被投喂了 {self.feed_count} 次，对 {person.name} 的好感度提升了 5，目前好感度是 {self.base_affection}。")


# 实例化人和宠物猫
person = Person("张三", 28)
cat = Cat("小花", "布偶猫")

# 进行交互
person.feed(cat)
person.feed(cat)
