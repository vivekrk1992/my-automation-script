#! /bin/bash

green='\033[32m'
nc='\033[0m'
echo '==================================='
echo 'Project'
echo 'spc - 1'
echo 'vidhaikalam -2'
echo '==================================='
echo 'Action'
echo 'run server - 1'
echo 'shell -2'
echo -e "${green} =================================== ${nc}"

read -p 'Project & Action : ' project_name action
case $project_name in 
	1)
		case $action in
			1) cd ~/Software/app/web/spc/ && source ~/Software/virtualenv/spc/bin/activate && python manage.py runserver 0:8000;;
			2) cd ~/Software/app/web/spc/ && source ~/Software/virtualenv/spc/bin/activate && python manage.py shell_plus;;
			*)
		esac
		echo "Processing SPC ===>";;
	2)
		case $action in
			1) cd ~/Software/app/web/vidhaikalam/ && source ~/Software/virtualenv/vidhaikalam/bin/activate && python manage.py runserver 0:8000;;
			2) cd ~/Software/app/web/vidhaikalam/ && source ~/Software/virtualenv/vidhaikalam/bin/activate && python manage.py  shell;;
			*)
		esac
		echo "Processing Vidhaikalam ===>";;
	*)
		echo "Project not available"
esac
echo "========================================="
