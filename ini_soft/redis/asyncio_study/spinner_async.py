import asyncio
import itertools
import sys

@asyncio.coroutine
def spin(msg):
# 스레드를 종료하기 위해 사용했던 signal 인수 필요 없음
    write = sys.stdout.write
    flush = sys.stdout.flush

    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
            # 이벤트 루프를 블로킹하지 않고 잠자기 위해 time.sleep대신에 yield~.sleep 사용
        except asyncio.CancelledError:
        #spin()이 깨어난 후 예외가 발생하면, 취소가 요청된 것 -> 루프 종료
            break
    write(' ' * len(status) + '\x08' * len(status))

@asyncio.coroutine
def slow_function():
# slow_function은 이제 코루틴으로서,
# 코루틴이 잠자면서 입출력을 수행하는 체 하는 동안 이벤트 루프가 진행될 수 있게 하기 위해
#yield from 사용

    yield from asyncio.sleep(3)
    # 메인루프의 제어흐름을 처리, 메인루프는 잠자고 난 후 코루틴을 계속 실행
    return 42

@asyncio.coroutine
def supervisor():
# 코루틴, yield from 을 사용해서 slow_function을 사용할 수 있음
    spinner = asyncio.async(spin('thinking!'))
    # asyncio.async는 spin() 코루틴의 실행을 스케줄링, task 객체 안에 넣어 task 객체 즉시 반환
    print('spinner object: ', spinner)
    # task 객체 출력
    result = yield from slow_function()
    # slow_function 함수를 구동해서 실행이 완료되면 반환된 값 가져옴
    # 이벤트 루프 게속 실행
    # slow_function이 yield from asyncio.sleep을 실행해서 메인루프로 제어권 넘김
    spinner.cancel()
    # task 객체는 cancel 메서드를 호출해서 취소할 수 있음
    # 그러면 예외 발생, 코루틴은 예외를 잡아서 지연시키거나 취소 요청을 거부
    return result

def main():
    loop = asyncio.get_event_loop()
    # 이벤트 루프에 대한 참조 가져옴
    result = loop.run_until_complete(supervisor())
    # supervisor 코루틴을 구동해서 완료
    # 코루틴의 반환값은 run_until_complete의 반환값이 됨
    loop.close()
    print('Answer: ', result)

if __name__ == '__main__':
    main()
