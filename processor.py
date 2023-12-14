import json 

from sorter import get_files_by_course, find_directories_at_depth
from extractor import extract_reviews

# Provide the starting path and depth level
starting_path = '.\websites'  # Change this to the desired starting directory
desired_depth = 8    # Change this to the desired depth level
directories = find_directories_at_depth(starting_path, desired_depth)

files_by_course = {}

for directory in directories:
    files_by_course.update(get_files_by_course(directory))

reviews = {}

for course, files in files_by_course.items():
    reviews.setdefault(course, [])
    course_reviews = reviews.get(course)

    for file in files:
        review_batch = extract_reviews(file)
        course_reviews.extend(review_batch)

unique_reviews = {}
for code, reviews_list in reviews.items():
    unique_reviews.setdefault(code, [])
    seen = set()
    for review in reviews_list:
        hashable_review = review.copy()
        hashable_review['Content'] = ''.join(hashable_review['Content'])
        review_tuple = tuple(hashable_review.items())

        if review_tuple not in seen:
            seen.add(review_tuple)
            unique_reviews[code].append(review)

# Convert dictionary to JSON string
json_string = json.dumps(unique_reviews)

# Write JSON string to a file
with open('reviews.json', 'w') as file:
    file.write(json_string)