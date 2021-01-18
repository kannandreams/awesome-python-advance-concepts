from hero import Hero
from ironman import IronMan

if __name__ == "__main__":
    hero = Hero.get_hero()
    hero_obj = Hero.factory(hero,'Luke')
    hero_obj.set_hit_points()
    hero_obj.set_health_points()
    hero_obj.get_info()
    print(hero_obj.type)


