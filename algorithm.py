from testcase.test_runner import run_test
from util import apply_patch,reverse_patch

def dd1(c,r, changeset):
 if len(c)==1:
     changeset.append(c[0])
     return

 apply_patch(c[:int(len(c)/2)]+r)
 status1=run_test('testcase/test')
 reverse_patch(c[:int(len(c) / 2)]+r)

 if status1=='FAIL':
    dd1(c[:int(len(c)/2)], r,changeset)
    return

 apply_patch(c[int(len(c) / 2):] + r)
 status2 = run_test('testcase/test')
 reverse_patch(c[int(len(c) / 2):] + r)

 if status1 == 'FAIL':
     dd1(c[int(len(c) / 2):], r,changeset)
     return

 if status1=='PASS' and status2=='PASS':
     dd1(c[:int(len(c) / 2)], c[int(len(c) / 2):] + r,changeset)
     dd1(c[int(len(c) / 2):], c[:int(len(c) / 2)]+r,changeset)


def dd2(c,r, n,changeset):
 if len(c)==1:
     changeset.append(c[0])
     return

 lc=len(c)
 tc=int(lc/n)

 status=[]
 cstatus=[]

 cprime=set(c)
 rprime=set(r)

 for i in range(n):
     start=i*tc
     end=start+tc
     if(lc-end<tc):
         end=lc

     apply_patch(c[start:end]+r)
     status.append(run_test('testcase/test'))
     reverse_patch(c[start:end]+r)

     if status[len(status)-1] == 'FAIL':
         dd2(c[start:end], r, 2, changeset)
         return

     apply_patch(c[0:start] + c[end:lc] + r)
     cstatus.append(run_test('testcase/test'))
     reverse_patch(c[0:start] + c[end:lc] + r)

     if status[len(status)-1] == 'PASS' and cstatus[len(status)-1] == 'PASS':
         dd2(c[start:end], c[0:start] + c[end:lc] + r, 2, changeset)
         dd2(c[0:start] + c[end:lc], c[start:end]+r, 2, changeset)
         return

     if status[len(status) - 1] == 'UNRESOLVED' and cstatus[len(status) - 1] == 'PASS':
         dd2(c[start:end], c[0:start] + c[end:lc] + r, 2, changeset)
         return

     if cstatus[len(status) - 1] == 'FAIL':
        cprime=cprime.intersection(c[0:start] + c[end:lc])

     if status[len(status) - 1] == 'PASS':
         rprime = rprime.union(c[start:end])

 if n<lc:
     nprime=min(len(cprime), 2*n)
     dd2(list(cprime),list(rprime),nprime, changeset)

# print(run_test('testcase/test'))
