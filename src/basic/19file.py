import os
import os.path

ls = []

def getAppointFile(path,ls):
	# print('read',path)
	fileList = os.listdir(path)
	try:
		for tmp in fileList:
			pathTmp = os.path.join(path,tmp)
			if True == os.path.isdir(pathTmp):
				getAppointFile(pathTmp,ls)
			elif pathTmp[pathTmp.rfind('.')+1:].upper() == 'PY':
				ls.append(pathTmp)
	except PermissionError:
		pass

def main():
	while True:
		path = 'F:/DMInAction/src/basic'.strip()
		if os.path.isdir(path) == True:
			break

	getAppointFile(path,ls)
	print(ls)
	print(len(ls))

main()