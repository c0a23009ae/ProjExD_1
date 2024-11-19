import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    bgf_img = pg.transform.flip(bg_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        kk_rct.move_ip((-1, 0))
        key_lst = pg.key.get_pressed()
        # if key_lst[pg.K_UP]:#上矢印キーが押されたら
        #     kk_rct.move_ip((0, -1))
        # if key_lst[pg.K_DOWN]:#下矢印キーが押されたら
        #     kk_rct.move_ip((0, 1))
        # if key_lst[pg.K_LEFT]:#左矢印キーが押されたら
        #     kk_rct.move_ip((-1, 0))
        # if key_lst[pg.K_RIGHT]:#右矢印キーが押されたら    
        #     kk_rct.move_ip((2, 0))
        kk_rct.move_ip((-key_lst[pg.K_LEFT] + (key_lst[pg.K_RIGHT] * 2),
                         -key_lst[pg.K_UP] + key_lst[pg.K_DOWN]))
        

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])#scereen surfaceに背景画像surfaceを張り付ける
        screen.blit(bgf_img, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])
        screen.blit(bgf_img, [-x + 4800, 0])
        #screen.blit(kk_img, [300, 200]) #こうかとんを配置
        screen.blit(kk_img, kk_rct) #こうかとんを配置rectを用いて
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()