import subprocess

def create_filter_diff(c):
    filter_diff_file_name='filter_diff.patch'
    changes=''
    i=0
    for _c in c:
        if i!=0:
            changes+=','
        changes+=str(_c)
        i+=1

    command = "cd data\nfilterdiff -#"+changes+" diff.patch > "+filter_diff_file_name

    print(command)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    p_status = p.wait()

    print("Command output: " + str(output))

    return filter_diff_file_name

def apply_patch(c):

    command = "cd data\npatch -b < "+create_filter_diff(c)

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    p_status = p.wait()

    print("Command output: " + str(output))

def reverse_patch(c):
    command = "cd data\npatch -R < "+create_filter_diff(c)

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    p_status = p.wait()

    print("Command output: " + str(output))

# apply_patch([1,2])
reverse_patch([1,2])