#/bin/bash

screen -S ocp -d -m
screen -S ocp -X screen -t server
screen -S ocp -X screen -t browser
screen -S ocp -X screen -t wrapper
screen -S ocp -p server -X stuff "source ~/.virtualenvs/build123d/bin/activate"$'\015'
screen -S ocp -p server -X stuff "~/.virtualenvs/build123d/bin/python -m ocp_vscode"$'\015'
sleep 5
screen -S ocp -p wrapper -X stuff "source ~/.virtualenvs/build123d/bin/activate"$'\015'
screen -S ocp -p wrapper -X stuff "wrapper $1 $2 $3"$'\015'
screen -S ocp -p browser -X eval 'stuff "open http://127.0.0.1:3939/viewer"\015'
screen -r ocp -X hardstatus alwayslastline '%{= .} %-Lw%{= .}%> %n%f %t*%{= .}%+Lw%< %-=%{g}(%{d}%H/%l%{g})'
