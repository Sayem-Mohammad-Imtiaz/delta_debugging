import subprocess

#This command could have multiple commands separated by a new line \n
command = "diff -U 0 data/version_1.py data/version_2.py > data/diff.patch"

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

(output, err) = p.communicate()

p_status = p.wait()

# print("Command output: " + str(output))


#count how many change set
total_change=0

with open('data/diff.patch', 'r') as file:
    Lines = file.readlines()

    for line in Lines:
        if line.startswith('@@'):
            total_change+=1

print("Print total change sets: "+str(total_change))