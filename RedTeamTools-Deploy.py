import os
import json


def clone_tool(url, toolpath):
	if os.path.exists(toolpath):
		return
	os.system("git clone " + url + " " + toolpath)

def install_tool(cmd,path):
	os.chdir(path)
	os.system(cmd.format(path))
	os.chdir(rootpath)

def deploy(toolinfo,path):
	name = toolinfo["url"].split('/')[-1]
	toolpath = path + "/"+name
	url = toolinfo["url"]
	clone_tool(url,toolpath)
	if "install" in toolinfo:
		cmd = toolinfo["install"]
		install_tool(cmd,toolpath)


def get_dependencies():
	os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
	os.system("python get-pip.py")

def read_json():
	with open('tools.json') as json_file:
		return json.load(json_file)


def parse_folders(folders,folderpath):
	for subfolder in folders:
		if isinstance(folders[subfolder],list):
			for tool in folders[subfolder]:
				toolpath = folderpath + "/" + subfolder 
				toolpath = toolpath[1:]
				deploy(tool,toolpath)
		else:
			parse_folders(folders[subfolder], folderpath + "/" + subfolder)


rootpath = os.getcwd()

 
if os.geteuid()==0:
	tools_list = read_json()
	get_dependencies()
	parse_folders(tools_list["root"],"")
else:
  print "You must run the script as root"
