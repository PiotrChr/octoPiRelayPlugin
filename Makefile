SYNCIP := 192.168.1.177
SYNCUSER := pi
SYNCFOLDER := /home/pi/.octoprint/plugins/octoPiRelayPlugin

sync:
	rsync -av --exclude='venv' --exclude='.idea' --exclude='__pycache__' --exclude='node_modules' --exclude='build' ./ ${SYNCUSER}@${SYNCIP}:${SYNCFOLDER}

