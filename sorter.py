import os

def list_directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def list_files(path):
    file_list = []
    for root, directories, files in os.walk(path):
        for filename in files:
            file_list.append(os.path.join(root, filename))
    return file_list

def remove_suffix(string, suffix):
    if string.endswith(suffix):
        return string[0:-len(suffix)]
    
    return string

def process_course_name(course_name):
    return course_name.upper().replace('-', ' ')

def get_files_by_course():
    directories_list = list_directories('.')
    files_by_course = {}

    print("List of directories:")
    for directory in [directory for directory in directories_list if not directory.startswith('.')]:
        course_name = process_course_name(remove_suffix(directory, "%3frecent%3dtrue"))
        
        files_by_course.setdefault(course_name, [])
        files = files_by_course.get(course_name)
        files.extend(list_files(directory))

    return files_by_course

print(get_files_by_course())