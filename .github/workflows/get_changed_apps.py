import os
import sys
import json

github_output = os.getenv('GITHUB_OUTPUT')
target_path = os.getenv('TARGET_PATH')

with open(sys.argv[1], "r") as input:
	changed_files = input.read().split(',')
	changed_apps = []

	for file in changed_files:
		if file.startswith(target_path):
			changed_apps.append(file.replace(target_path, '').split("/")[0])

	output_changed_apps = []

	for i in set(changed_apps):
		output_changed_apps.append({ "app-name": i  })

with open(github_output, "a") as output:
	output.write(f"app-list={output_changed_apps}" + '\n')
	print(output_changed_apps)
