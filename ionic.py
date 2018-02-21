#! /usr/local/bin/python3
from subprocess import Popen, PIPE
from os import system, chdir


# naviagate to all mobile project
mobile_project_path = '/Users/vivek/Software/app/mobile/'
chdir(mobile_project_path)
projects = Popen(['ls'], stdout=PIPE)
project_list = list(str(projects.communicate()).split('\\n'))

# remove last index becaus it is None
# project_list.remove(None)
del project_list[-1]
print(project_list)
i = 1
for project in project_list:
    print("[ {option} ] = {project_name}".format(project_name=project, option=project_list.index(project)))


selected_project = int(input('Which project?'))
print(project_list[selected_project])
chdir(mobile_project_path + project_list[selected_project])
system('ionic serve')
# project_list.append(str())
