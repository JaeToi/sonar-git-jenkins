# 사용자 데이터 저장소
users = {}

def signup():
    # 사용자로부터 입력 받기
    username = input("새 사용자 이름을 입력하세요: ")
    
    if username in users:
        print("사용자 이름이 이미 존재합니다. 다른 이름을 선택하세요.")
        return

    password = input("새 비밀번호를 입력하세요: ")
    confirm_password = input("비밀번호를 다시 입력하세요: ")

    if password != confirm_password:
        print("비밀번호가 일치하지 않습니다. 다시 시도하세요.")
        return

    # 사용자 데이터 저장
    users[username] = password
    print("회원가입 성공!")

def login():
    # 사용자로부터 입력 받기
    username = input("사용자 이름을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    
    # 사용자 검증
    if username in users and users[username] == password:
        print("로그인 성공!")
    else:
        print("로그인 실패. 사용자 이름이나 비밀번호를 확인하세요.")

def main():
    while True:
        print("\n1. 로그인")
        print("\n2. 회원가입")
        print("\n3. 종료")
        choice = input("선택하세요 (1/2/3): ")

        if choice == '1':
            login()
        elif choice == '2':
            signup()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

# 메인 함수 호출
main()
