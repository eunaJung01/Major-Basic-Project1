import os
from datetime import datetime, timedelta


# 시작메뉴
def start_menu():
    while True:
        print("------------------------------------------")
        print(" 1) 로그인")
        print(" 2) 회원가입")
        print("------------------------------------------")
        user1 = int(input("메뉴를 선택하세요 > "))
        if user1 == 1:
            user_id = LOGIN()
            break
        elif user1 == 2:
            s_num = student_number()
            s_name = student_name()
            s_pw = student_pw()
            s_college = student_college()
            s_bd = student_bd()
            save_student(s_num, s_name, s_pw, s_college, s_bd)

            start_menu()
            break
        else:
            print("메뉴를 다시 선택해주세요.")
    return user_id


# 로그인
def LOGIN():
    print("학번 > ")
    sid = input()
    print("비밀번호 > ")
    pw = input()

    f1 = open('student.txt', mode='rt')
    cnt = -1
    user_id = 0
    while True:
        line = f1.readline()
        if not line:
            f1.close()
            break
        line = line.split("/")
        stdnum = line[0]
        stdname = line[1]
        stdpw = line[2]
        if stdnum != sid + ' ':
            cnt = -1
        elif stdpw != ' ' + pw + ' ':
            cnt = 0
        else:
            cnt = 1
            break
        user_id += user_id
    if cnt == -1:
        print("없는 학번입니다.")
        LOGIN()
    elif cnt == 0:
        print("비밀번호가 틀립니다.")
        LOGIN()
    else:
        print(stdname, "님 반갑습니다!")
    f1.close()
    return user_id


# 회원가입 - 학번 입력
def student_number():
    while True:
        print("------------------------------------------")
        print(" 학번을 입력하세요.")
        print("------------------------------------------")
        number = input("학번 > ")
        if len(number) != 9:
            print("잘못된 학번입니다.")
            continue

        year = int(number[0:4])
        # print(year)
        if year < 2010 or year > 2021:
            print("잘못된 학번입니다.")
            continue

        # 학번 동치비교
        f1 = open('student.txt', mode='rt')
        while True:
            line = f1.readline()
            if not line:
                f1.close()
                break
            line = line.split("/")
            stdnum = line[0]
            if number == stdnum:
                print("동일한 학번이 존재합니다")
                f1.close()
                break
        break
    return number


# 회원가입 - 이름 입력
def student_name():
    while True:
        print("------------------------------------------")
        print(" 이름을 입력하세요.")
        print("------------------------------------------")
        name = input("이름 > ")
        # 공백제거
        name = name.replace(" ", "")

        if len(name) < 2:
            print("잘못된 이름입니다.")
            continue

        # 로마자로만 이루어져 있는지 확인
        a = english(name)
        if a == 1:
            break
        else:
            # 한글로만 이루어져 있는지 확인
            b = korean(name)
            if b == 1:
                break
            else:
                print("잘못된 이름입니다.")
                continue

    return name;


# 회원가입 - 이름 입력-영어인지 확인
def english(name):
    flag = 1
    for i in name:
        if ord('a') <= ord(i.lower()) <= ord('z'):
            continue
        else:
            flag = 0
            break
    if flag == 0:
        # 영어가 아닌 경우
        return 0
    else:
        return 1


# 회원가입 - 이름 입력-한글 확인
def korean(name):
    flag = 1
    for i in name:
        if ord('가') <= ord(i) <= ord('힣'):
            continue
        else:
            flag = 0
            break
    if flag == 0:
        # 한글이 아닌경우
        return 0
    else:
        return 1


# 회원가입 - 비밀번호 입력
def student_pw():
    while 1:
        print("------------------------------------------")
        print(" 비밀번호를 생성합니다.")
        print(" (비밀번호는 8자 이상 12자 이하의 로마자와 숫자로 구성되어야 합니다.)")
        print("------------------------------------------")
        pw = input("비밀번호 > ")  # 사용자 입력 비밀번호
        print()

        pw_Num = 0  # 숫자 개수
        pw_Roman = 0  # 로마자 개수
        count = 0

        if len(pw) < 8 or len(pw) > 12:
            print("비밀번호의 길이가 너무 짧거나 깁니다.")
            count += 1

        for item in pw:
            # '0'~'9':48~57, 'A'~'Z':65~90, 'a'~'z':97~122
            if ord(item) < 48 or 57 < ord(item) < 65 or 90 < ord(item) < 97 or ord(item) > 122:
                print("비밀번호는 로마자와 숫자로만 구성 되어야 합니다.")
                count += 1
                break

        for item in pw:
            if 48 <= ord(item) <= 57:
                pw_Num += 1
            elif 65 <= ord(item) <= 90 or 97 <= ord(item) <= 122:
                pw_Roman += 1
        if pw_Num == 0 or pw_Roman == 0:
            print("비밀번호는 최소 한 개 이상의 로마자와 최소 한 개 이상의 숫자로 구성 되어야 합니다.")
            count += 1

        for item in pw:
            if item == " " or item == "\t":
                print("비밀번호는 탭과 개행을 포함하지 않아야 합니다.")
                count += 1
                break

        if count == 0:
            # print("비밀번호 생성 완료\n")
            break
        print()

    return pw


# 회원가입 - 학과 입력
def student_college():
    COLLEGE_NUM = 60  # 학과 개수
    collegeFile = open("college.txt", mode="r", encoding='utf-8')
    collegeList = collegeFile.readlines()
    collegeFile.close()

    for item in collegeList:  # 대학명 제거 (*로 시작하는 값들)
        if item[0] == "*":
            collegeList.remove(item)
    temp = 0
    for item in collegeList:  # '\n' 제거
        collegeList[temp] = item[:-1]
        temp += 1

    while 1:
        print("------------------------------------------")
        print(" 학과를 입력하세요.")
        print("------------------------------------------")
        college = input("학과 > ")  # 사용자 입력 학과
        print()
        count = 0

        # " " 제거
        # index = []
        # for i in range(len(college)):
        #     if college[i] == " ":
        #         index.append(i)
        # i_re = 0
        # for i in range(len(index)):
        #     temp = college[:index[i] - i_re] + college[index[i] - i_re + 1:]
        #     college = temp
        #     i_re += 1
        college = college.replace(" ", "")

        if len(college) > 2:
            print("학과명은 2글자 이상이어야 합니다.")
            count += 1

        if not isKorean(college):
            print("학과명은 한글로 구성되어야 합니다.")
            count += 1

        # 학과명 존재 확인
        num = 0
        for item in collegeList:
            if college != item:
                num += 1
        if num == COLLEGE_NUM:
            # print("일치하는 학과명이 존재하지 않습니다.")
            print("학과명을 제대로 입력해주세요.")
            count += 1

        if count == 0:
            print("학과 저장 완료\n")
            break
        print()

    return college


# Unicode 문자열이 한글인지 감별
def isKorean(word):
    if len(word) <= 0:
        return False
    # UNICODE RANGE OF KOREAN: 0xAC00 ~ 0xD7A3
    for c in range(len(word)):
        if word[c] < u"\uac00" or word[c] > u"\ud7a3":
            return False
    return True


# 회원가입 - 생년월일 입력
def student_bd():
    while 1:
        print("------------------------------------------")
        print(" 생년월일을 입력하세요.")
        print(" ex) 2021-03-22 / 20210322 / 21-03-22 / 210322")
        print("------------------------------------------")
        bd = input("생년월일 > ")
        print()
        count = 0

        # "-" 제거
        # index = []
        # for i in range(len(bd)):
        #     if bd[i] == "-":
        #         index.append(i)
        # i_re = 0
        # for i in range(len(index)):
        #     temp = bd[:index[i] - i_re] + bd[index[i] - i_re + 1:]
        #     bd = temp
        #     i_re += 1
        bd = bd.replace("-", "")

        # YYMMDD (len=6) -> YYYYMMDD (len=8)
        if len(bd) == 6:
            if "80" <= bd[:2] <= "99":
                temp = "19" + bd
                bd = temp
            elif "00" <= bd[:2] <= "21":
                temp = "20" + bd
                bd = temp
            else:
                print("1980~2021년도 사이의 값을 입력해주세요.\n")
                continue

        # MM : 0+1~9
        if bd[4] == "0":
            if bd[5] == "0":
                count += 1
        # MM : 1+(0,1,2)
        if bd[4] == "1":
            if bd[5] != "0" and bd[5] != "1" and bd[5] != "2":
                count += 1

        # DD : 0+1~9 / DD : 1,2+0~9
        if bd[6] == "0":
            if bd[7] == "0":
                count += 1

        mm = int(bd[4:6])
        # MM : 01,03,05,07,08,10,12 -> DD : 3+(0,1)
        if (mm < 10 and mm % 2 == 1) or (mm >= 10 and mm % 2 == 0):
            if bd[6] == "3" and (bd[7] != "0" and bd[7] != "1"):
                count += 1
        # MM : 04,06,09,11 -> DD : 30
        if (mm < 10 and mm % 2 == 0) or (mm >= 10 and mm % 2 == 1):
            if bd[6] == "3" and bd[7] != "0":
                count += 1

        yyyy = int(bd[:4])
        # MM : 02 -> DD : 3x 불가
        if mm == 2:
            if bd[6] == "3":
                count += 1
            # MM : 02 -> DD : 2x일 때 (YYYY%4==0 or YYYY%(4,100,400)==0 : x=0~9 / YYYY&(4,100)==0 : x=0~8 / else : x=0~8)
            elif bd[6] == "2":
                if yyyy % 4 == 0 and yyyy % 100 == 0:
                    if bd[7] == "9":
                        count += 1
                elif not (yyyy % 4 == 0 or (yyyy % 4 == 0 and yyyy % 100 == 0 and yyyy % 400 == 0)):
                    if bd[7] == "9":
                        count += 1

        if count == 0:
            # print("생년월일 저장 완료\n")
            break
        print("생년월일을 제대로 입력해주세요.\n")

    return bd


# 정보 저장
def save_student(num, name, pw, college, bd):
    # student.txt 파일에 저장
    tempList = [num, name, pw, college, bd]  # 학번, 이름, 비밀번호, 학과, 생년월일
    studentList = [[]]  # 학생 정보 (및 예약 내역?) 저장
    s_number = 0  # 학생 고유 번호 = studentList's index
    for i in range(5):
        studentList[s_number].append(tempList[i])
    s_number += 1

    studentFile = open("student.txt", mode="a")
    studentFile.write("\n")
    for i in range(5):
        studentFile.write(studentList[s_number - 1][i] + " / ")
    studentFile.close()
    print("파일 저장 완료")


# 메인메뉴
def MAINMENU(user_id):
    # user_id 가지고있기
    print("------------------------------------------")
    print(" 1) 예약")
    print(" 2) 예약확인")
    print(" 3) 예약 취소")
    print(" 4) 로그아웃")
    print("------------------------------------------")
    print("번호를 선택해주세요 > ")
    num = input()
    if num == "1":
        # 예약
        p, dir = RESERVATION_ROOM()  # p는 수용가능 인원수, dir은 roomDB 위치
        space = int(p)
        gnum_list = ROOMNUM(space)
        date = DATE()
        pos = NOW(dir, date)
        rtime = TIME(dir, date, pos)
        RESERVATION(user_id, gnum_list, date, rtime, p, dir)

    elif num == "2":
        # 예약 확인
        CONFIRM()
    elif num == "3":
        # 예약 취소
        CANCLE()
    elif num == "4":
        # 로그아웃
        LOGOUT(user_id)
    else:
        print("잘못된 입력입니다")
        MAINMENU(user_id)


# 예약
def RESERVATION_ROOM():
    print("예약하실 K_CUBE가 위치한 건물의 번호를 입력해주세요.\n1.도서관 / 2.공학관 / 3. 법학관")
    print("* 예약 날짜를 다시 입력 하시려면 'r'을 입력해주세요")
    print("건물번호 > ")
    num = input()
    if num == "1" or num == "도서관":
        s_num, dir = ROOM_1()
    elif num == "2" or num == "공학관":
        s_num, dir = ROOM_2()
    elif num == "3" or num == "법학관":
        s_num, dir = ROOM_3()
    elif num == "r":
        MAINMENU()
    else:
        print("존재하지 않는 호실입니다")
        RESERVATION_ROOM()
    return s_num, dir


# 방1_도서관
def ROOM_1():
    print("도서관 K_CUBE에서 예약하실 방 번호를 입력해주세요.\n:1호실(3인실) / 2호실(6인실)")
    print("* 건물 번호를 다시 입력 하시려면 'r'를 입력해주세요")
    print("방 번호 > ")
    num = input()

    if len(str(num)) > 1:
        print("잘못된 입력입니다")
        ROOM_1()
    elif num == "r":
        RESERVATION_ROOM()
    elif num == "1" or num == "2":
        path_dir = 'library'
        file_list = os.listdir(path_dir)
        p = file_list[int(num) - 1][2:3]

        # 방 별 수용 인원
        print(file_list[int(num) - 1][2:3], "명 수용 가능")
        # 인원수 입력 함수 호출
        dir = 'library' + file_list[int(num) - 1]
    else:
        print("존재하지 않는 호실입니다")
        ROOM_1()
    return p, dir


# 방2_공학관
def ROOM_2():
    print("공학관 K_CUBE에서 예약하실 방 번호를 입력해주세요.\n:1호실(3인실) / 2호실 (4인실) / 3호실(4인실)")
    print("* 건물 번호를 다시 입력 하시려면 'r'를 입력해주세요")
    print("방 번호 > ")
    num = input()

    if len(str(num)) > 1:
        print("잘못된 입력입니다")
        ROOM_2()
    elif num == "r":
        RESERVATION_ROOM()
    elif num == "1" or num == "2" or num == "3":
        path_dir = '공학관'
        file_list = os.listdir(path_dir)
        p = file_list[int(num) - 1][2:3]

        # 방 별 수용 인원
        print(file_list[int(num) - 1][2:3], "명 수용 가능")
        # 인원수 입력 함수 호출
        dir = 'engineering' + file_list[int(num) - 1]
    else:
        print("존재하지 않는 호실입니다")
        ROOM_2()

    return p, dir


# 방3_법학관
def ROOM_3():
    print("법학관 K_CUBE에서 예약하실 방 번호를 입력해주세요.\n:1호실 (5인실) / 2호실 (10인실) / 3호실 (12인실) / 4호실 (20인실)")
    print("* 건물 번호를 다시 입력 하시려면 'r'를 입력해주세요")
    print("방 번호 > ")
    num = input()

    if len(str(num)) > 1:
        print("잘못된 입력입니다")
        ROOM_3()
    elif num == "r":
        RESERVATION_ROOM()
    elif num == "1" or num == "2" or num == "3" or num == "4":
        path_dir = '법학관'
        file_list = os.listdir(path_dir)
        p = file_list[int(num) - 1][2:3]

        # 방 별 수용 인원
        print(file_list[int(num) - 1][2:3], "명 수용 가능")
        # 인원수 입력 함수 호출
        dir = 'law' + file_list[int(num) - 1]
    else:
        print("존재하지 않는 호실입니다")
        ROOM_3()
    return p, dir


# 예약 - 인원수 입력
def ROOMNUM(space):
    # space는 수용 가능 인원수
    print("방 번호를 다시 입력하시려면 'r'를 입력하세요")
    print("인원 수 > ")
    rnum = input()

    if rnum == 'r':
        rnum = int(0)
        MAINMENU()
    else:
        rnum = int(rnum)
        cnum = rnum - 1

    if (rnum < 0) or (rnum > 99):
        print('잘못된 입력입니다.')
        ROOMNUM()

    if (space % 2) != 0:
        if rnum < (space // 2) + 1:
            print('예약 인원 수는 수용 인원의 절반 이상이어야 합니다.')
            ROOMNUM(space)
        elif rnum > space:
            print('수용 최대 인원수와 예약 인원수를 다시 확인해주세요.')
            ROOMNUM(space)
        else:
            print("동반 사용자 ", cnum, "명 입니다")
            print("동반 사용자의 학번을 입력하셔야 합니다.")
    else:
        if rnum < (space // 2):
            print('예약 인원 수는 수용 인원의 절반 이상이어야 합니다.')
            ROOMNUM(space)
        elif rnum > space:
            print('수용 최대 인원수와 예약 인원수를 다시 확인해주세요.')
            ROOMNUM(space)
        else:
            print("동반 사용자 ", cnum, "명 입니다")
            print("동반 사용자의 학번을 입력하셔야 합니다.")

    # 동반 사용자
    gnum_list = []
    f1 = open('student.txt', mode='rt')
    cnt = -1
    for i in range(cnum):
        sid = input('동반 사용자 학번 > ')

        while True:
            line = f1.readline()
            if not line:
                f1.close()
                break
            line = line.split("/")
            stdnum = line[0]
            if stdnum == sid + ' ':
                if len(line) > 6:
                    print(len(line))
                    cnt = -1
                else:
                    gnum_list.insert(stdnum)
                    cnt = 0
            else:
                cnt = 1

        if cnt == -1:
            print("다른 호실에 예약되어 있는 사용자 입니다. 예약이 불가능합니다.")
            ROOMNUM(space)
        elif cnt == 0:
            print('예약 가능한 사용자 입니다.')

        else:
            print('K-CUBE 예약시스템에 저장되어 있지 않는 사용자입니다.')
            ROOMNUM(space)
    f1.close()
    return gnum_list


# 예약 - 날짜 입력
def DATE():
    now = datetime.now()

    day1 = now + timedelta(days=1)
    day2 = now + timedelta(days=2)
    day3 = now + timedelta(days=3)

    while True:
        print("인원수를 다시 입력하시려면 'r'를 입력하세요")
        print("ex) 2021-03-22 / 20210322 / 21-03-22 / 210322")
        nowdate = input('예약날짜를 입력하시오 > ')

        if nowdate == 'r':
            MAINMENU()

        if (nowdate == day1.strftime("%Y-%m-%d")) or (nowdate == day1.strftime("%Y%m%d")) or (
                nowdate == day1.strftime("%y-%m-%d")) or (nowdate == day1.strftime("%y%m%d")):
            date = day1.strftime("%y%m%d")
            print('가능')
            break
        elif (nowdate == day2.strftime("%Y-%m-%d")) or (nowdate == day2.strftime("%Y%m%d")) or (
                nowdate == day2.strftime("%y-%m-%d")) or (nowdate == day2.strftime("%y%m%d")):
            date = day2.strftime("%y%m%d")
            print('가능')
            break
        elif (nowdate == day3.strftime("%Y-%m-%d")) or (nowdate == day3.strftime("%Y%m%d")) or (
                nowdate == day3.strftime("%y-%m-%d")) or (nowdate == day3.strftime("%y%m%d")):
            date = day3.strftime("%y%m%d")
            print('가능')
            break
        else:
            date = 0
            print('예약날 기준 1일 이후부터 3일 이후 까지만 예약 가능')
            DATE()
    return date


# 예약 - 현황
def NOW(dir, date):
    print("예약 현황 입니다")
    list = []
    time_list = []
    pos_list = []
    now = datetime.now()
    day1 = now + timedelta(days=1)
    day2 = now + timedelta(days=2)
    day3 = now + timedelta(days=3)

    f = open(dir, mode='r')

    line = f.readline()
    line = line.split('\t')

    time_list = line
    print(date[2:4], "월 ", date[4:6], "일 사용 가능 시간 ")
    if not line:
        f.close()

    if date == day1.strftime("%y%m%d"):
        print("hello")
        line = f.readline()
        line = line.split('\t')
        list = line
        for i in range(1, 22):
            if list[i] == '0':
                pos_list.insert(i)
                print(time_list[i])

    elif date == day2.strftime("%y%m%d"):
        print("hi")
        line = f.readline()
        line = f.readline()
        line = line.split('\t')
        list = line
        for i in range(1, 22):
            if list[i] == '0':
                pos_list.insert(i)
                print(time_list[i])
    else:
        print("wewew")
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = line.split('\t')
        list = line
        for i in range(1, 22):
            if list[i] == '0':
                pos_list.insert(i)
                print(time_list[i])
    return pos_list


# 예약 - 시간 입력
def TIME(dir, date, pos):
    print("------------------------------------------")
    print(" 사용 시간을 입력해주세요.(예약은 30분 단위로 가능합니다.)")
    print(" ex) HH: MM-HH:MM / H.M - H.M")
    print("------------------------------------------")
    time = input("사용 시간 입력 > ")
    f = open(dir, mode='w')
    print(dir)
    lines = f.readlines()
    for item in time:
        if item == " " or item == "\t":
            time.remove(item)
    start = time.split("-")
    end = time
    if ':' in time:
        s_hour = start[0:2]
        s_min = start[3:5]
        e_hour = end[0:2]
        e_min = start[3:5]
    elif '.' in time:
        s_hour = start[0:2]
        s_min = start[3:4]
        e_hour = end[0:2]
        e_min = start[3:4]
    else:
        print("올바른 형태의 시간이 아닙니다")

    s_idx = s_hour * 2 - 20
    e_idx = e_hour * 2 - 20

    if s_min == '30' or s_min == '5':
        s_min = '30'
        s_idx = s_idx + 1
    if e_min == '30' or e_min == '5':
        e_min = '30'
        e_idx = e_idx + 1
    for i in range(s_idx, e_idx):
        if pos[i] == 1:
            print("예약 불가능한 시간이 포함되어 있습니다.")
            break
        else:
            print("예약합니다.")
            continue
    rtime = s_hour + ':' + s_min + '-' + e_hour + ':' + e_min
    return rtime


# 진짜 예약
def RESERVATION(user_id, gnum_list, date, rtime, p, dir):
    # user_id만 있으면 뒤에 추가 가능
    # 동반사용자 학번, 날짜 시간, 장소, 사용 인원
    if dir[0:3] == 'law':
        if p == '5':
            b = 3
            r = 1
        elif p == '10':
            b = 3
            r = 2
        elif p == '12':
            b = 3
            r = 3
        else:
            b = 3
            r = 4
    elif dir[0:3] == 'lib':
        if p == '3':
            b = 1
            r = 1
        elif p == '6':
            b = 1
            r = 2
    else:
        if p == '3':
            b = 2
            r = 1
        elif p == '4':
            b = 2
            r = 2
        else:
            b = 2
            r = 3

    resList = [date, rtime, b, r, p] # 예약 날짜, 예약 시간, 건물 번호, 방 번호, 예약 인원수?? gnum_list?
    f1 = open('student.txt', mode='a')

    while True:
        line = f1.readline()
        if not line:
            f1.close()
            break

        if line[0:9] == user_id:
            for i in range(5):
                f1.write(resList[i] + " / ")
                break

        for i in range(len(gnum_list)):
            if line[0:9] == user_id:
                for j in range(5):
                    f1.write(resList[i] + " / ")


# 삭제하기
def CANCLE():
    print('------------------------------------------')
    print('예약을 정말 취소하시겠습니까?')
    print('------------------------------------------')
    print('1) 예')
    print('1) 아니오')
    print('------------------------------------------')
    c = int(input('메뉴를 선택하세요 > '))

    room = []  # 호실 txt의 정보를 저장한 2차원 배열
    date = 1  # 3일 중 언제인지

    if c == 1:
        # if(data[9][3:5] == '00'):
        for i in range(0, len(room[0])):
            if data[9][3:5] == '00' and data[9][0:2] == room[0][i]: # data?
                s = i
            elif data[9][3:5] == '30' and data[9][0:2] == room[0][i]:
                s = i + 1
            elif data[9][9:11] == '00' and data[9][6:8] == room[0][i]:
                f = i
            elif data[9][9:11] == '30' and data[9][6:8] == room[0][i]:
                f = i + 1

        for i in range(s, f):
            room[date][i] = 0

        # MAINMENU(); 메인 메뉴

    elif c == 2:
        print('')
        # MAINMENU(); 메인 메뉴
    else:
        print('잘못 입력하셨습니다.')
        CANCLE()


# 예약 확인
def CONFIRM():
    with open('student.txt', 'r') as file:
        line = file.readlines()

    user_id = 1
    data = line[user_id].split(' / ')

    print('------------------------------------------')
    print(data[0], data[1], "님의 K-CUBE 예약 내역")
    print('------------------------------------------')
    print("예약 날짜 : ", data[8][0:4], "년 ", data[8][4:6], "월", data[8][6:8], "일")
    print("예약 시간 : ", data[9], end='')
    if data[5] == '1':
        p = "도서관"
    elif data[5] == '2':
        p = "공학관"
    elif data[5] == '3':
        p = "법학관"
    print("장소 : ", p, data[6], "호실")
    print("사용 인원 : ", data[7], "명")

    print('------------------------------------------')
    print('1) 확인 (메인메뉴로 돌아가기)')
    print('2) 예약 취소')
    print('------------------------------------------')
    c = int(input('메뉴를 선택하세요 > '))

    if c == 1:
        print('')
        # MAINMENU(); 메인 메뉴
    elif c == 2:
        CANCLE()
    else:
        print('잘못 입력하셨습니다.')
        CONFIRM()


# 로그아웃
def LOGOUT(user_id):
    print('------------------------------------------')
    answer = input('로그아웃 하시겠습니까? (y/n): ')
    print('------------------------------------------')
    if answer == 'y' or answer == 'Y':
        user_id = -1  # 로그인 정보 삭제
        # start_menu(); 시작메뉴로 돌아가기
    elif answer == 'n' or answer == 'N':
        print()
        MAINMENU()  # 메인 메뉴로 돌아가기
    else:
        print('잘못 입력하셨습니다.')
        LOGOUT(user_id)


user_id = start_menu()
MAINMENU(user_id)
