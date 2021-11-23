class Character:
    def __init__(self, name):
        self.name = name

    def show_profile(self):
        profile = '名前:{0} 種族:Character'.format(self.name)
        print(profile)


# クラス名(親クラス名)
class Monster(Character):
    def __init__(self, name, hp=20):
        super().__init__(name)
        self.hp = hp

    # オーバーライド
    def show_profile(self):
        profile = '名前:{0} 種族:Monster HP{1}'.format(self.name, self.hp)
        print(profile)


char_a = Character('キャラA')
print(char_a.name)

monster_a = Monster('モンスターA')
print(monster_a.name)
monster_a.show_profile()
