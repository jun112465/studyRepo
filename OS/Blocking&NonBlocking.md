# Blocking I/O Model 
- I/O 작업은 User Level(application)에서 직접 수행할 수 없다.
- 실제 I/O 작업은 Kernel Level(OS)에서 일어나는 과정이다.
- 따라서 유저 프로세스는 커널에게 I/O 작업에 대한 요청을 해야 한다.
- I/O 작업을 처리하기 위해 User Level에 있던 Application이 시스템 함수를 호출한다. 이때 context-switching이 발생한다.
- Kernel Level에서 해당 I/O 작업이 끝나고 데이터를 반환하게 되면 그 때가 되서야 애플리케이션 단의 스레드에 걸렸던 **block**이 풀린다
- 애플리케이션 관점에서 보면 아무런 동작도 안하는 것처럼 보이지만 실제로는 커널에서 I/O 작업을 수행하느라 block 되어 있는 것이다. 바로 이 부분이 blocking I/O의 문제점이며 개선 포인트이다.


# Non-blocking I/O Model
- I/O 작업은 CPU 자원을 거의 쓰지 않기 때문에 blocking 방법은 CPU 자원 낭비가 심하다
- 이러한 blocking 방식의 비효율성을 극복하고자 만들어진 것이 non-blocking 방식이다.
- non-blocking 방식은 I/O 작업을 진행하는 동안 유저 프로세스의 작업을 중단시키지 않는다. 
- 유저 프로세스가 I/O를 처리하기 위해 커널에 함수를 호출하면, 커널에서 함수의 진행 상황과 상관없이 **바로 결과를 반환한다**.
- 이때, 반환되는 결과는 반환하는 순간에 가져올 수 있는 데이터에 해당한다. 처음에는 가져올 수 있는 데이터가 없겠지만 시간이 지나면서 가져올 수 있는 데이터가 생겨날 것이다.
- 서버는 클라이언트가 요청한 사이즈에 맞는 데이터를 반환하기 위해 데이터를 축적해야한다.
- 데이터의 축적이 끝났을 때, 반환되어 클라이언트에서 요청한 사이즈의 데이터를 받아올 수 있게 된다. 
- 하지만 이 구현 방식의 문제는 클라이언트가 따로 반환되는 값이 원하는 사이즈가 되었는지 계속해서 확인해줘야 한다는 것이다. **(Polling)**
- 반환되는 데이터가 준비됐는지 확인하는 과정에서 수많은 클라이언트의 요청이 동시 다발적으로 일어날 경우, CPU에게 적지 않은 부담이 될 수 있는 I/O Model이다.