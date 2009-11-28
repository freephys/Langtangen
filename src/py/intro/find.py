def find(func,dir,arg=None):
	files = os.listdir(dir)
	files.sort(lambda a,b : cmp(a.lower(),b.lower()))
	for file in files :
		filepath = os.path.join(dir,file)
		if os.path.islink(filepath):
			elif os.path.isdir(filepath):
				find(func,filepath,arg)
			elif os.path.isfile(filepath):
				func(filepath,arg)
			else:
				print 'find:can not treat ',filepath

def checksize2(filepath, bigfiles):
size = os.path.getsize(filepath)
if size > 1000000:
bigfiles.append('%.2fMb %s' % (size/1000000.0, filepath))
bigfiles = []
root = os.environ['HOME']
find(checksize2, root, bigfiles)
for fileinfo in bigfiles:
print fileinfo