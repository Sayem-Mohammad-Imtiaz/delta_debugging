import subprocess
import py_compile
import os

def run_test(testcasefile):
    # print(testcasefile)
    # print(os.getcwd())
    status=''
    testcase=''
    with open(os.path.join(os.getcwd(), testcasefile), 'r') as file:
        Lines = file.readlines()

        for line in Lines:
            if line.strip()!='':
                testcase=line.strip()

    try:
        py_compile.compile(testcase.split()[1], doraise=True)
    except py_compile.PyCompileError:
        # print('compile fail')
        return 'UNRESOLVED'


    try:
        subprocess.check_call([testcase], shell=True)
        status='PASS'
    except subprocess.CalledProcessError as e:
        # print("An exception occured!!")
        status='FAIL'

    return status



# print(run_test('test'))