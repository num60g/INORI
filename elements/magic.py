import random

class Magic:
    def __init__(self, name, power):
        """
        魔法の初期化

        Parameters:
            name (str): 魔法の名前
            power (float): 魔法の威力
        """
        self.name = name
        self.power = power

    def cast(self, targets):
        """
        魔法を発動する

        Parameters:
            targets (list): 魔法の対象となるターゲットのリスト

        Returns:
            list: 魔法が発動したターゲットのリスト
        """
        casted_targets = []
        for target in targets:
            if random.random() > 0.5:
                casted_targets.append((target[0], target[1], target[2] * self.power, target[3]))
            else:
                casted_targets.append(target)
        return casted_targets
