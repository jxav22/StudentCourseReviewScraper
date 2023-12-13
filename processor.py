import json 

from sorter import get_files_by_course
from extractor import extract_reviews

files_by_course = get_files_by_course()
reviews = {}

for course, files in files_by_course.items():
    reviews.setdefault(course, [])
    course_reviews = reviews.get(course)

    for file in files:
        review_batch = extract_reviews(file)
        course_reviews.extend(review_batch)

# Convert dictionary to JSON string
json_string = json.dumps(reviews)

# Write JSON string to a file
with open('reviews.json', 'w') as file:
    file.write(json_string)