import random

class Prayer:
    def __init__(self, magic_power, magical_skill):
        """
        いのりの初期化

        Parameters:
            magic_power (float): 魔力量
            magical_skill (float): 魔術技量
        """
        self.magic_power = magic_power
        self.magical_skill = magical_skill

    def grasp_space(self, targets):
        """
        いのりの効果を適用する

        Parameters:
            targets (list): 効果を受けるターゲットのリスト

        Returns:
            list: 効果が適用されたターゲットのリスト
        """
        grasped_targets = []
        for target in targets:
            magic_power_bonus = random.uniform(0.1, 0.3) * self.magic_power
            magical_skill_bonus = random.uniform(0.1, 0.3) * self.magical_skill
            grasped_targets.append((target[0], target[1], target[2] * (1 + magic_power_bonus), target[3] + (0, 0, 0, int(magical_skill_bonus * 255))))
        return grasped_targets
