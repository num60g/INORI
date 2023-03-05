from elements.magic import Magic
from objects.tower import LightTower

# Magic クラスを使って魔法を生成する例
fireball = Magic("Fireball", 10, 20, (255, 0, 0, 255))
ice_shard = Magic("Ice Shard", 8, 15, (0, 0, 255, 255))

# LightTower クラスを使って光の塔を生成する例
lt = LightTower((0, 0), 10, 1, (255, 255, 255, 255))
