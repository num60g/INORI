class LightTower:
    def __init__(self, center, radius, height, color):
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
