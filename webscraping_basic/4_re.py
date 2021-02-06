# 주민등록번호
# 901201-1111111

# 이메일 주소
# aaaaa@gmail.com

# 차량번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.168.1.1

import re

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case | caffe(x)
# ^ (^de)  : 문자열로 시작 > desk, destination | fede(x)
# $ (se$)  : 문자열의 끝 > case, base | face(x)

def print_mach(m):
    if m:
        print("  m.group() :", m.group())
        print("  m.string  :", m.string)
        print("  m.start() :", m.start())
        print("  m.end()   :", m.end())
        print("  m.span()  :", m.span())
    else:
        print("  매칭되지 않음")

print("- match")
m = p.match("caffe")
print_mach(m)

print("- search")
m = p.search("good care")
print_mach(m)

print("- findall")
lst = p.findall("good care cafe")
print(" ", lst)