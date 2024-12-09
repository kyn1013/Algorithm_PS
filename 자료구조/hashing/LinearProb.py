def hashFnStr(key):
    sum = 0
    for c in key:
        sum = sum + (ord(c)) #문자의 아스키 코드값을 sum에 더함
    return sum % M #M:테이블의 크기

M = 13
table = [None] * M #크기가 M인 해시 테이블

def hashFn(key): #나머지 연산을 이용한 해시 함수
    return key % M

def lp_insert(key):
    id = hashFn(key)
    count = M #해시 테이블 크기만큼 탐색
    while count > 0 and (table[id] != None and table[id] != -1): #계산된 주소부터 비어 있는 위치를 찾음, 비어있지 않으면 다음 탐색
        id = (id + 1 + M) % M
        count -= 1

    if count > 0: #빈 버킷 찾으면 레코드 저장
        table[id] = key
    return

def lp_search(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None: #찾는 레코드가 없는 경우
            return None
        if table[id] == key: #찾은 레코드를 찾은 경우
            return table[id]
        id = (id + 1 + M) % M #그렇지 않은 경우 다음 버킷 조사
        count -= 1
    return None


def lp_delete(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:return
        if table[id] != -1 and table[id] == key: #삭제할 레코드를 찾고 -1을 사용하여 사용되었다가 삭제된 것을 표시
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1


print("   최초:", table )
lp_insert(45);  print( "45 삽입:", table )
lp_insert(27);  print( "27 삽입:", table )
lp_insert(88);  print( "88 삽입:", table )
lp_insert(9);   print( " 9 삽입:", table )

lp_insert(71);  print("71 삽입:", table )
lp_insert(60);  print("60 삽입:", table )
lp_insert(46);  print("46 삽입:", table )
lp_insert(38);  print("38 삽입:", table )
lp_insert(24);  print("24 삽입:", table )
lp_delete(60);  print("60 삭제:", table )
print("46 탐색:", lp_search(46) )
