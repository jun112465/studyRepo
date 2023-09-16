# CPU Scheduler 

- 스케줄링 대상은 Ready Queue에 있는 프로세스들이다. 
- 메모리에 상주 중인 프로세스를 cpu에 할당하기 위한 스케줄러이다. 

### FCFS (First Come First Serve)

- 특징
    - 먼저 온 고객을 먼저 서비스해주는 방식, 즉 먼저 온 순서대로 처리한다. 
    - 비선점형(Non-Preemptive) 스케줄링이다.
    - 일단 CPU를 잡으면 CPU burst가 완료될 떄까지 CPU를 반환하지 않는다. 할당되었던 CPU가 반환될 때만 스케줄링이 이루어진다. 
- 문제점
    - convoy effect : 소요 시간이 긴 프로세스가 먼저 도달하여 효율성을 낮추는 현상이 발생한다. 

### SJF (Shortest Job First)
- 특징 
    - 다른 프로세스가 먼저 도착했어도 CPU birst time이 짧은 프로세스에게 선 할당
    - 비선점형 스케줄링 방식

- 문제점
    - starvation : 특정 프로세스 (cpu를 사용하는 시간이 긴 프로세스)가 영원히 cpu를 할당받지 못할수도 있다. 

### SRTF (Shortest Remaining Time First)
- 특징 
    - 새로운 프로세스가 도착할 때 마다 새로운 스케줄링이 이뤄진다. 
    - 선점형(Preemptive) 스케줄링 : 현재 수행중인 프로세스의 남은 burst time 보다 더 짧은 CPU birst time을 가지는 새로운 프로세스가 도착하면 CPU가 뺏긴다. 
- 문제점
    - starvation


### Priority Scheduling
- 특징
    - 우선순위가 가장 높은 프로세스에게 CPU 를 할당하는 스케줄링이다. 우선순위란 정수로 표현하게 되고 작은 숫자가 우선순위가 높다.
    - 선점형 스케줄링(Preemptive) 방식
    - 더 높은 우선순위의 프로세스가 도착하면 실행중인 프로세스를 멈추고 CPU 를 선점한다.
    - 비선점형 스케줄링(Non-Preemptive) 방식
    - 더 높은 우선순위의 프로세스가 도착하면 Ready Queue 의 Head 에 넣는다.
- 문제점
    - starvation
    - 무기한 봉쇄(Indefinite blocking) 실행 준비는 되어있으나 CPU 를 사용못하는 프로세스를 CPU 가 무기한 대기하는 상태
- 해결책
    - aging : 아무리 우선순위가 낮은 프로세스라도 오래 기다리면 우선순위를 높여주자.

### Round Robin

- 특징
    - 현대적인 CPU 스케줄링
    - 각 프로세스는 동일한 크기의 할당 시간(time quantum)을 갖게 된다.
    - 할당 시간이 지나면 프로세스는 선점당하고 ready queue의 제일 뒤에 가서 다시 줄을 선다. 
    - RR은 CPU 사용시간이 랜덤한 프로세스들이 섞여있을 경우에 효율적
    - RR이 가능한 이유는 프로세스의 context를 save할 수 있기 때문이다.

- 장점
    - Response time이 빨라진다 : n개의 프로세스가 ready queue에 있고 할당시간이 q(quantum time)인 경우 각 프로세스는 q단위로 cpu 시간의 1/n을 얻는다. 즉, 어떤 프로세스도 (n-1)/q time unit 이상 기다리지 않는다.
    - 프로세스가 기다리는 시간이 cpu를 사용할 만큼 증가한다. 공정한 스케줄링이라고 볼 수 있다. 
- 주의할 점
    - time quantum 이 너무 커지면 FSFS와 같은 효과를 가지게 된다. 
    - time quantum 이 너무 작아지면 잦은 context switch로 인해 overhead가 발생한다. 
    - 적당한 time quantum을 설정하는 것이 중요하다.