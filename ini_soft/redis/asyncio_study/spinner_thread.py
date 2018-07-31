import threading
import itertools
import time
import sys

class Signal:
    go = True
# 이 클래스는 외부에서 스레드를 제어하기 위해 사용할
# go 속성 하나만 있는 간단한 가변 객체를 정의

def spin(msg, signal):
#이 함수는 별도의 스레드에서 실행, signal 인자는 Signal 클래스의 객체를 받음

    write = sys.stdout.write
    flush = sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
    #itertools.cycle()은 주어진 시퀀스를 순환하면서 끝없이 항목을 생성
    # 사실상 무한루프

        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        # 텍스트 모드 애니메이션 기법,
        # 문자열 길이만큼 백스테이스(\x08)를 반복해서 커서를 앞으로 이동

        time.sleep(.1)

        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))
    # 공백 문자로 덮어쓰고 다시 커서를 처음으로 이동해서 메시지 출력행을 clean

def slow_function():
#입출력을 위해 장시간 기다리는 것처럼 보이게 만듦

    time.sleep(5)
    # 주 스레드에서 sleep( ) 함수를 호출할 때 GIL이 해제, 두번째 스레드 진행

    return 42

def supervisor():
#두번째 스레드를 만들고, 스레드 객체를 출력, 시간이 오래 걸리는 연산 수행 후 스레드 제거

    signal = Signal()
    spinner = threading.Thread(target=spin, args=('Thinking!', signal))
    print('spinner object:', spinner) # 두번째 스레드 객체 출력

    spinner.start() # 두번째 스레드 실행
    result = slow_function()
    # 이 함수가 실행되면, 주 스레드가 블로킹 됨
    # 그리고 두번째 스레드가 텍스트 애니메이션 출력

    signal.go =False # spin 안의 for loop 중단
    spinner.join() # spinner 스레드가 끝날 때까지 기다림

    return result

def main():
    result = supervisor()
    print('Answer: ', result)

if __name__ == '__main__':
    main()
