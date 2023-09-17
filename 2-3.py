import re

p = re.compile('([a-zA-Z0-9\-_]+\@[a-zA-Z0-9\-]+\.[a-z]{2,6})')

while True:
    text = input("텍스트를 입력하세요: ")
    text = text.strip()  
    email = p.findall(text)
    
    if email:
        print("추출된 이메일 주소:")
        print(email)
    else:
        print("이메일 주소가 발견되지 않았습니다")