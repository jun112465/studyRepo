'''
그래프의 edge를 생성할 때 반드시 dictionary로 만들 필요는 없다는 것을 깨달았다.
set()을 통해서도 충분히 중복을 제거할 수 있다는 것을 기억하자.
'''
def solution(dirs):
    answer = 0
    
    edges = set()
    move = {
        'U':(0,1),
        'D':(0,-1),
        'L':(-1,0),
        'R':(1,0)
    }
    
    x,y = 0,0
    for d in dirs:
        nx,ny = x+move[d][0], y+move[d][1]
        if -5<=nx<=5 and -5<=ny<=5:
            edges.add((x,y,nx,ny))
            edges.add((nx,ny,x,y))
            x, y = nx, ny
        
    return len(edges)/2