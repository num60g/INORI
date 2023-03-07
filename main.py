import pygame
import random
import math

# ゲーム画面のサイズ
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 自機のクラス
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5

    def update(self, keys):
        move_x = 0
        move_y = 0
        if keys[pygame.K_LEFT]:
            move_x = -1
        elif keys[pygame.K_RIGHT]:
            move_x = 1
        if keys[pygame.K_UP]:
            move_y = -1
        elif keys[pygame.K_DOWN]:
            move_y = 1
        if move_x != 0 and move_y != 0:
            # 斜め移動の場合は移動量を調整する
            move_x *= math.sqrt(2) / 2
            move_y *= math.sqrt(2) / 2
        self.rect.x += move_x * self.speed
        self.rect.y += move_y * self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

# 弾のクラス
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 10
        self.angle = angle

    def update(self):
        rad = math.radians(self.angle)
        x = math.cos(rad) * self.speed
        y = -math.sin(rad) * self.speed
        self.rect.x += x
        self.rect.y += y
        if self.rect.bottom < 0:
            self.kill()

# 敵のクラス
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-200, -50)
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# メイン関数
def main():
    # Pygameの初期化
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('斜めスクロールシューティングゲーム')

    # スプライトグループの作成
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

    # 自機の作成
    player = Player()
    all_sprites.add(player)

    # ゲームループ
    clock = pygame.time.Clock()
    game_over = False
    score = 0
    while not game_over:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # 弾の作成
                    bullet = Bullet(player.rect.centerx, player.rect.top, -45)
                    bullet_sprites.add(bullet)
                    all_sprites.add(bullet)

        # キー入力の取得
        keys = pygame.key.get_pressed()

        # スプライトの更新
        all_sprites.update(keys)

        # 衝突判定
        hits = pygame.sprite.spritecollide(player, enemy_sprites, False)
        if hits:
            game_over = True

        hits = pygame.sprite.groupcollide(bullet_sprites, enemy_sprites, True, True)
        for hit in hits:
            score += 10

        # 敵の生成
        if random.randint(0, 100) < 5:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemy_sprites.add(enemy)

        # 背景の描画
        screen.fill((0, 0, 0))

        # スプライトの描画
        all_sprites.draw(screen)

        # スコアの表示
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text, (10, 10))

        # 画面の更新
        pygame.display.update()

        # フレームレートの設定
        clock.tick(60)

    # Pygameの終了
    pygame.quit()
