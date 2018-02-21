#! /bin/bash
echo 'Which project you want to run: '
read project_name
echo $project_name
if [ $project_name == "spc" ]; then
	cd ~/Software/app/web/spc/ && source ~/Software/virtualenv/spc/bin/activate && python manage.py runserver 0:8000
elif [ $project_name == 'vidhaikalam' ]; then
	cd ~/Software/app/web/vidhaikalam/ && source ~/Software/virtualenv/vidhaikalam/bin/activate && python manage.py runserver 0:8000
fi
