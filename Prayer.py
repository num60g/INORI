class Prayer:
def init(self, magic_power, magic_skill):
"""
いのりの初期化

    Parameters:
        magic_power (int): 魔力量
        magic_skill (int): 魔術技量
    """
    self.magic_power = magic_power
    self.magic_skill = magic_skill
    self.effect_strength = self._calculate_effect_strength()

def _calculate_effect_strength(self):
    """
    ランダムな効果の強弱を計算する

    Returns:
        float: 効果の強弱
    """
    return 1 + (random.random() - 0.5) * self.magic_skill * 0.1

def use_prayer(self, tower):
    """
    光の塔に対していのりを唱える

    Parameters:
        tower (LightTower): 光の塔

    Returns:
        LightTower: 強化された光の塔
    """
    if self.magic_power < tower.required_magic_power or self.magic_skill < tower.required_magic_skill:
        raise ValueError("魔力量または魔術技量が足りません。")

    buffed_tower = copy.deepcopy(tower)
    buffed_tower.height *= self.effect_strength
    buffed_tower.color = tuple([int(min(255, max(0, c * self.effect_strength))) for c in buffed_tower.color])

    return buffed_tower

class LightTower:
def init(self, center, radius, height, color):
"""
光の塔の初期化

    Parameters:
        center (tuple): 円の中心座標 (x, y)
        radius (float): 円の半径
        height (float): 光の塔の高さ
        color (tuple): 色のRGBA値 (r, g, b, a)
    """
    self.center = center
    self.radius = radius
    self.height = height
    self.color = color

def apply_buff(self, targets):
    """
    光の塔のバフを適用する

    Parameters:
        targets (list): バフを受けるターゲットのリスト

    Returns:
        list: バフが適用されたターゲットのリスト
    """
    buffed_targets = []
    for target in targets:
        distance = ((target[0] - self.center[0]) ** 2 + (target[1] - self.center[1]) ** 2) ** 0.5
        if distance <= self.radius:
            buffed_targets.append((target[0], target[1], target[2] * self.height, target[3] + self.color))
        else:
            buffed_targets.append(target)
    return buffed_targets

class Inori:
def init(self, magic_power, magic_skill):
"""
いのりの初期化

    Parameters:
        magic_power (float): 魔力量
        magic_skill (float): 魔術技量
    """
    self.magic_power = magic_power
    self.magic_skill = magic_skill

def cast(self, light_tower):
    """
    いのりを唱える

    Parameters:
        light_tower (LightTower): 掌握する光の塔

    Returns:
        float: いのりの効果値
    """
    # ランダムな効果値を計算する
    effect = self.magic_power * self.magic_skill * random.uniform(0.5, 1.5)
    # 光の塔の高さを変更する
    light_tower.height += effect
    return effect
