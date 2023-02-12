# 파이썬 메모

> * type()      : 자료형 확인
> * len()       : 문자열 길이
> * "//" 연산자 : 소수점 아래 버림
> * input()     : 사용자 입력 받음
> * int(), float(), str()   : 형변환
> * upper(), lower()
> * strip()     : 앞뒤 공백제거, lstrip(), rstrip()
> * 문자열 구성확인
>> * isalnum()
>> * isalpha()
>> * isidentifier()
>> * isdecimal()
>> * isdigit()
>> * issapce()
>> * islower()
>> * isupper()
> * find(), rfind()
> * "in"연산자  : 문자열내부 문자열 존재 확인
> * split()
> * f'문자열{표현식}문자열'
> * "*"         : 전개연산자
> * "pass"      : = todo
> * "raise NotImplementedError"
> * append(), insert()  : 리스트에 요소 추가
> * 
> * 
> * 

# PyQt
> * PyQt에서는 사용자가 버튼을 클릭하는 행위를 '시그널'이라고 하고 버튼을 클릭했을 때 수행할 함수를 '슬롯'이라고 합니다.
> * 이벤트루프에 의해 호출 당하는 함수를 콜백(callback) 함수라고 부릅니다. 
> * Window Icon : 16 x 16
> *
> *
> *
> *
> *
> *
> *
> *


|제목|내용|
|------|---|
|타이틀바 아이콘    |self.setWindowIcon(QIcon('./macro/icon03.png'))|
|윈도우 사이즈      |self.setGeometry(300,300,400,400)|
|버튼               |btnBuy = QPushButton(text="매수", parent=self)|
|                   |self.btn.clicked.connect(self.btn_clicked)|
|창닫기             |btnQuit.clicked.connect(QApplication.instance().quit)|
|                   |btnQuit.clicked.connect(self.btn_clicked)|
|                   |btnQuit.clicked.connect(self.close)|
|라벨               |self.label = QLabel("메시지:", self)|
|                   |self.label.clear()|
|                   |self.label.setText("버튼 클릭")|
|이미지             |label.setPixmap(QPixmap("./macro/logo.jpg"))|
|                   |self.setCentralWidget(label)|
|QLineEdit          |self.line_edit = QLineEdit(" ", self)|
|                   |self.line_edit.setEnabled(False) # 비활성화|
|                   |self.line_edit.setText("HELLO")|
|                   |text = self.line_edit.text()|
|QStatusBar         |self.statusBar = QStatusBar(self)|
|                   |self.setStatusBar(self.statusBar)|
|                   |self.statusBar.showMessage("PYSTOCK v1.0")|
|                   |print(self.statusBar.currentMessage())|
|                   |self.statusBar.clearMessage()|
|||
|||
|||
|||
|||



# 참고
> https://seday.tistory.com/45
>
> https://wikidocs.net/85581
>
> https://brownbears.tistory.com/198
>
> https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%AC%EB%A1%A4%EB%A7%81-%EA%B8%B0%EC%B4%88
>
> ■ PyQt<br>
> https://wikidocs.net/119616
>
> ■ 아이콘<br>
> https://www.iconfinder.com
>
> ■ 마크다운<br>
> https://inasie.github.io/it%EC%9D%BC%EB%B0%98/%EB%A7%88%ED%81%AC%EB%8B%A4%EC%9A%B4-%ED%91%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0/
>
>
>
>
>
>
>
>
>
