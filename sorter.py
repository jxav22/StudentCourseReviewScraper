import os

def find_directories_at_depth(start_path, depth):
    directories = []
    for root, dirs, files in os.walk(start_path):
        current_depth = root.count(os.sep)
        if current_depth == depth:
            directories.append(root)
    return directories

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

def get_files_by_course(path):
    directories_list = list_directories(path)
    files_by_course = {}

    for directory in directories_list:
        course_name = process_course_name(remove_suffix(directory, "%3frecent%3dtrue"))
        
        files_by_course.setdefault(course_name, [])
        files = files_by_course.get(course_name)
        files.extend(list_files(os.path.join(path, directory)))

    return files_by_course