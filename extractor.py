from bs4 import BeautifulSoup
from datetime import datetime

def extract_name(element):
    name_element = element.find(class_='col-sm-3')
    return next(name_element.stripped_strings) if name_element else "Anonymous"

def extract_grade(element):
    grade_element = element.find(class_='col-sm-1')
    return next(grade_element.stripped_strings) if grade_element else "N/A"

def extract_metrics(element):
    metrics = {}
    metric_elements = element.find_all(class_='col-sm-2')
    for metric_element in metric_elements:
        metric = next(metric_element.stripped_strings)

        span_element = metric_element.find('span')
        stars = len(span_element.text) if span_element else 0

        metrics[metric] = stars
    return metrics

def extract_content(element):
    content_element = element.find('p', class_='review-text')
    return [text for text in content_element.stripped_strings] if content_element else []

def extract_date(element):
    date_element = element.find('span', class_='time_stamp')
    date_string = next(date_element.stripped_strings) if date_element else "unknown"

    date_part = date_string[len("This review was posted on "):]
    parsed_date = datetime.strptime(date_part, "%B %d, %Y")
    return parsed_date.strftime("%d/%m/%Y")

def extract_reviews(file_path):
    if not file_path.endswith('.html'):
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    reviews = []
    review_divs = soup.find_all(lambda tag: tag.name == 'div' and tag.get('id', '').startswith('review-'))

    for review_div in review_divs:
        review = {}

        review['Name'] = extract_name(review_div)
        review['Grade'] = extract_grade(review_div)

        metrics = extract_metrics(review_div)
        review.update(metrics)

        review['Content'] = extract_content(review_div)
        review['Date'] = extract_date(review_div)
        
        reviews.append(review)

    return reviews

file_path = 'softeng-306%3frecent%3dtrue\\index.html'
print(extract_reviews(file_path))