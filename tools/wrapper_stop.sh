#/bin/bash

ps aux | grep ocp_vscode | awk -F' ' {'print $2'} | xargs -n 1 kill -9
screen -ls | grep ocp | awk -F'.' {'print $1'} | xargs -n 1 kill
