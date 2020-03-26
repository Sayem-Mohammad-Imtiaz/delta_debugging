import subprocess
import py_compile


def run_test(testcasefile):
    status=''
    testcase=''
    with open(testcasefile, 'r') as file:
        Lines = file.readlines()

        for line in Lines:
            if line.strip()!='':
                testcase=line.strip()

    try:
        py_compile.compile(testcase.split()[1], doraise=True)
    except py_compile.PyCompileError:
        print('compile fail')
        return 'UNRESOLVED'


    try:
        subprocess.check_call([testcase], shell=True)
        status='PASS'
    except subprocess.CalledProcessError as e:
        print("An exception occured!!")
        status='FAIL'

    return status



print(run_test('test'))