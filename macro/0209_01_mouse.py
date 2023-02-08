# --------------------------------------------
# - https://seday.tistory.com/45
# - https://wikidocs.net/85581
# - https://wikidocs.net/85709
# -
# -
# -
# -
# --------------------------------------------
import pyautogui as pag
import time
# --------------------------------------------
# 화면 크기 출력
print("------------------------------------------")
print(pag.size())
print(pag.size().width)
print(pag.size().height)
# Size(width=3840, height=2160)
# 3840
# 2160
Point(x=2293, y=562)
# --------------------------------------------
# 마우스 현재 위치 출력
print("------------------------------------------")
print(pag.position())
# Point(x=2293, y=562)
# --------------------------------------------
# 마우스 이동
print("------------------------------------------")
time.sleep(2)
pag.moveTo(100,200) # 바로이동
pag.moveTo(1400,1000,2) # 2초동안 이동
# --------------------------------------------
# 마우스 클릭
print("------------------------------------------")
pag.click()
pag.click(button='right')
pag.doubleClick()
pag.click(clicks=3, interval=1) # 3번을 1초마다 클릭함
# --------------------------------------------
# 마우스 드래그
print("------------------------------------------")
pag.moveTo(1000, 1000, 2)
pag.dragTo(1300, 1200, 2)

# --------------------------------------------
# 
print("------------------------------------------")
# --------------------------------------------
# 
print("------------------------------------------")
# --------------------------------------------
# 
print("------------------------------------------")
# --------------------------------------------
# 
print("------------------------------------------")
# --------------------------------------------
# 
print("------------------------------------------")
