import os

def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating project' +directory)
		os.makedirs(directory)

def create_data_files(project_name, base_url):
	queue = project name + '/queue.txt'
	crawler = project name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, base_url)
		if not os.path.isfile(crawled)
		write_file(crawled, '')

#Create new file
def write_file(path, data):
	f  = open(path, 'w')
	f.write(data)
	f.close()

#Add data onto an existing file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data, + '\n')

# Delete the contents of file
def delete_file_contents(path):
	with open(path, 'w'):
		pass