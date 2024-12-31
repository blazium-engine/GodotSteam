import os

def can_build(env, platform):
	if os.path.isfile("modules/godotsteam/sdk/put SDK here"):
		print("Missing Steamworks SDK. Please add it to sdk/")
		return False
	return platform=="linuxbsd" or platform=="windows" or platform=="macos" or platform=="server"

def configure(env):
	pass

def get_doc_classes():
	return [
		"Steam",
	]

def get_doc_path():
	return "doc_classes"
