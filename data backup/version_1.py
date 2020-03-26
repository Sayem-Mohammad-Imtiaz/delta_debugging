import sys

def process(command):
    supported_op = ['add']
    # command = "add 20 and 3"

    _len = len(command)

    flag = True
    tmp = ''
    op = ''
    num1 = ''
    num2 = ''

    for i in range(_len):
        if command[i] != ' ':
            tmp += command[i]
        else:
            if tmp == 'and':
                tmp = ''
                continue

            if op == '':
                op = tmp

                if op not in supported_op:
                    flag = False
                    break

            elif num1 == '':
                num1 = int(tmp)
            tmp = ''

    if flag == True and num2 == '':
        num2 = int(tmp)

    result = 0

    if flag == False:
        print("Invalid command")
    else:
        if op == 'add':
            result = num1 + num2

        print(op, num1, ' and ', num2, '= ', result)


if __name__ == "__main__":
    process(sys.argv[1])







