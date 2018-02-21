#! /usr/local/bin/python3

from subprocess import call, Popen, run
# project = input('Project Name?')
# call(['ls'])


class First:

    projects = {
        '1': {'name': 'spc', 'project_path': '~/Software/app/web/spc/', 'virtualenv_path': '~/Software/virtualenv/spc/'},
        '2': {'name': 'vidhaikalam', 'project_path': '~/Software/app/web/vidhaikalam/', 'virtualenv_path': '~/Software/virtualenv/vidhaikalam/'},
    }

    actions = {
        '1': {'name': 'run server', 'cmd': 'python manage.py runserver 0:8000'},
        '2': {'name': 'open shell', 'cmd': 'python manage.py shell_plus'},
        '3': {'name': 'activate env', 'cmd': 'source '},
    }

    def __init__(self):
        for project in self.projects:
            print('{project_name} = {key}'.format(key=project, project_name=self.projects[project]['name']), end=' | ')

        project_key = input()

        for action in self.actions:
            print('{action_name} = {key}'.format(key=action, action_name=self.actions[action]['name']), end=' | ')
        action_key = input()

        self.run_user_wise(project_key, action_key)

    def run_user_wise(self, project_key, action_key):
        print('project_name = {}, action name = {}' .format(self.projects[project_key]['name'], self.actions[action_key]['name']))

        print(self.actions['3']['cmd'] + self.projects[project_key]['virtualenv_path'] + 'bin/activate')
        # activate env
        call(self.actions['3']['cmd'] + self.projects[project_key]['virtualenv_path'] + 'bin/activate', shell=True)
        run(["source ~/Software/virtualenv/spc/bin/activate"])

if __name__ == '__main__':
    print('is a main funtion')
    f = First()



