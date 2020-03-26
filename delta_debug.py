import subprocess
from algorithm import dd1,dd2

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

c=[]
r=[]

for i in range(1,total_change+1):
    c.append(i)

bug_changes=[]
dd2(c,r,2,bug_changes)

print("Buggy changes are: ", bug_changes)