import pyautogui as pg
print("------------------------------------------");
# alert()
a = pg.alert(text='내용입니다', title='제목입니다', button='OK')
print(a)
print("------------------------------------------");
# confirm()
b = pg.confirm(text='내용입니다', title='제목입니다', buttons=['OK', 'Cancel'])
print(b)
print("------------------------------------------");
# prompt()
c = pg.prompt(text='내용입니다', title='제목입니다', default='입력하세요')
print(c)
print("------------------------------------------");
# password()
d = pg.password(text='내용입니다', title='제목입니다', default='입력하세요', mask='*')
print(d)
print("------------------------------------------");
# ------------------------------------------
# OK
# ------------------------------------------
# Cancel
# ------------------------------------------
# asdf
# ------------------------------------------
# asdfasdfasdf
# ------------------------------------------