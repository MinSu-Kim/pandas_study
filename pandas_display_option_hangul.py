"""
full, half-widthPermalink
간단하게 말하면, 한글로 된 문자열의 경우 가령 "이승훈"이 있다면 길이는 3이지만, 
출력될 때는 6칸이 출력됩니다. 이를 full-width character라고 합니다.
영어로 된 문자열의 경우 가령 "abc"는 길이는 3이며, 출력될 때도 3입니다.

이승훈과 abc는 동일하게 같은 length를 가지고 있지만, 출력되어 질 때는 한글의 경우가 더 많은 공간이 필요하게 되고, 
따라서, 밀려서 표현된다는 것이죠.
아래 코드를 보면, a와 b의 길이는 같지만, 출력은 다르게 됩니다. 
“5칸을 출력하라고 했고 공백은 *으로 채워라”라는 명령을 내렸고 정확히 명령을 수행했지만, 
“이승훈”은 6칸이 되고, “abc”는 3칸이므로 문제가 발생하죠
"""
import sys

a = '이승훈'
b = 'abc'
assert len(a)==len(b)
print(f"{a:*<5s}")
print(f"{b:*<5s}")

print(sys.getdefaultencoding())
"""
# solution: unicodedata.east_asian_widthPermalink
해당작업은 unicodedata.east_asian_width()를 사용하여, 이 함수에 문자를 넘겨주면 해당 문자가 어느 정도의 간격을 차지하는지 출력해줍니다. 
실행 결과는 다음으로 분류 됩니다.
A: Ambiguous
F: Fullwidth
H: Halfwidth
N: Neutral
Na: Narrow
W: Wide
"""
import unicodedata


def fill_str_with_space(input_s="", max_size=40, fill_char="*"):
    """
    - 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함.
    - 최대 길이(max_size)는 40이며, input_s의 실제 길이가 이보다 짧으면
    남은 문자를 fill_char로 채운다.
    """
    l = 0
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else:
            l+=1
    return input_s+fill_char*(max_size-l)


a = "abc"
b = "이승훈"

print(unicodedata.east_asian_width("이"), unicodedata.east_asian_width("a"))
print(fill_str_with_space("abc", max_size=10))
print(fill_str_with_space("이승훈", max_size=10))


'''

'''
from wcwidth import wcswidth

def fmt(x, w, align='r'):
    """ 동아시아문자 폭을 고려하여, 문자열 포매팅을 해 주는 함수. w 는 해당 문자열과 스페이스문자가 차지하는 너비. align 은 문자열의 수평방향 정렬 좌/우/중간. """
    x = str(x)
    l = wcswidth(x)
    s = w-l
    if s <= 0:
        return x
    if align == 'l':
        return x + ' '*s
    if align == 'c':
        sl = s//2
        sr = s - sl
        return ' '*sl + x + ' '*sr
    return ' '*s + x

l = [ '김철수', '이열', 'Meg']
l2 = [ 33, 23, 145 ]
for a, b in zip(l, l2): #print('%-10s %10s %10s'%(a, b, a))
    print('%s %s %s | %s |'%(fmt(a, 10, 'l'), fmt(b, 10), fmt(a, 10), fmt(a, 10, 'c')))
