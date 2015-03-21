#!/usr/bin/env python
#coding=utf-8

import random
import pygame
from pygame.locals import *
from sys import exit
from plane_class_method import *
from plane_init import *
#导入模块




while 1:
	enemy_add_speed(enemies,score)
	interval_e-=1	
	interval_b-=1
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
		if event.type==pygame.KEYDOWN and bomb.bomb_index<4:
				bomb.launch()
#如果按下空格键，那么发射一枚炸弹
	if not gameover:

		screen.blit(background,(0,0))
		if interval_b<0:
	 		bullets[index_b].restart()
	 		interval_b=100
# 重置间隔时间
			index_b=(index_b+1)%count_b
		if interval_e<0:
			enemies.append(Enemy())
			interval_e=10000
		for b in bullets:
			if b.active:
				for e in enemies:
					if checkHit(e,b):
						score+=100
				b.move()
				screen.blit(b.image,(b.x,b.y))
	#只处理激活的子弹

		
		if bomb.active:
			screen.blit(bomb.image,(bomb.x,bomb.y))
			bomb.move()
			for e in enemies:
				if check_hit(bomb,e):
					screen.blit(enemy_down1,(bomb.x,bomb.y))
					pygame.display.update()
					for enem in enemies:
						explosion_contain(enem,bomb)
					bomb.restart()
					break
				else: 
					pass
		for e in enemies:
			if checkCrash(e,plane):
				gameover=True
			e.move()
			screen.blit(e.image,(e.x,e.y))
#绘制一大波敌机
		plane.move()
		screen.blit(plane.image,(plane.x,plane.y))

		text=font.render("Score: %d" % score,1,(0,0,0))
		screen.blit(text,(0,0))
		pygame.display.update()


#如果阵亡了
	else:
		f_score=open("high_score.txt")
		top_score=int(f_score.readline())
		f_score.close()
		f_score=open("high_score.txt",'w')
#将最高分写入文件
		if score >top_score:
			f_score.write(str(score))
			f_score.close()
			break_score=font.render("WOW,Break the score!",1,(100,100,0))
			screen.blit(break_score,(50,300))
		else:
			f_score.write(str(top_score))
			f_score.close()
		score_get=font.render("GG~~The score you got is %d" % score,1,(0,80,170))
		screen.blit(score_get,(50,500))
		pygame.display.update()
#在屏幕中央显示您的得分
	if gameover and event.type==pygame.MOUSEBUTTONUP:
#如果按下鼠标	
		plane.restart()
		for e in enemies:
			e.restart()
		for b in bullets:
			b.restart()
		bomb.restart()
		bomb.bomb_index=0
		score=0
		gameover=False
		



