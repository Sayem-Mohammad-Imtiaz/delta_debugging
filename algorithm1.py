from testcase.test_runner import run_test
from util import apply_patch,reverse_patch

def dd1(c,r):
 if len(c)==1:
     return

 apply_patch(c[:len(c)/2])
 d1=run_test('testcase/test')
 reverse_patch(c[:len(c) / 2])

 dd1(c[:len(c)/2], r)
 dd1(c[len(c) / 2:], r)



print(run_test('test'))