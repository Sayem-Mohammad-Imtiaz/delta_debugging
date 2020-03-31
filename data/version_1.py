import sys

def process(command):
    print("Given a math operation command, the program parses and performs it")

    supported_op=['add','subtract','multiply','subtract','divide']
    # command="divide 20 and 10"

    _len=len(command)

    flag=True
    tmp=''
    op=''
    num1=''
    num2=''

    print("In version 2, additonal operations has been supported")

    for i in range(_len):
        if command[i]!=' ':
            tmp+=command[i]
        else:
            if tmp=='and':
                tmp=''
                continue

            if op=='':
                op=tmp

                if op not in supported_op:
                    flag=False
                    break

            elif num1=='':
                num1=int(tmp)
            tmp=''

    if flag==True and num2=='':
        num2=int(tmp)

    result = 0

    if flag == False:
        print("Invalid command")
    else:
        if op == 'add':
            result = num1 + num2

        print(op, num1, ' and ', num2, '= ', result)


if __name__ == "__main__":
    process(sys.argv[1])







