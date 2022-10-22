L,C = map(int, input().split())

alphabets = input().split()
alphabets.sort()

possible_pwd = list()
vowels = 'aeiou'

def recursive_search(li: list, pwd: str, v_cnt: int, c_cnt: int) -> None:
    if len(pwd) == L:
        if v_cnt>=1 and c_cnt>=2:
            possible_pwd.append(pwd)
        return
    if len(li)==0 and len(pwd)<L:
        return

    for i,l in enumerate(li):
        if l in vowels:
            recursive_search(li[i+1:], pwd+l, v_cnt+1, c_cnt)
        else:
            recursive_search(li[i+1:], pwd+l, v_cnt, c_cnt+1)

# 가능한 비밀번호 만들기
recursive_search(alphabets, "", 0, 0)

# 출력
for pwd in possible_pwd:
    print(pwd)

    
