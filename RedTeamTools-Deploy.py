import os
import json

rootpath = "Tools"

def clone_tool(url, toolpath):
	name = url.split('/')[-1]
	toolpath = rootpath + toolpath + "/"+name
	if os.path.exists(toolpath):
		return
	print toolpath
	os.system("git clone " + url + " " + toolpath)

def install_tool(cmd,path):
	toolpath = rootpath + path
	os.system(cmd.format(toolpath))


def read_json():
	with open('tools.json') as json_file:
		return json.load(json_file)

tools_list = read_json()

def parse_folders(folders,folderpath):
	for subfolder in folders:
		if isinstance(folders[subfolder],dict):
			parse_folders(folders[subfolder], folderpath + "/" + subfolder)
		else:
			toolpath = folderpath + "/" + subfolder
			for tool in folders[subfolder]:
				if isinstance(tool,dict):
					for cmd in tool["Install"]:
						install_tool(cmd,toolpath)
					continue
				clone_tool(tool,toolpath)

parse_folders(tools_list["root"],"")
