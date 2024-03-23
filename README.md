## README

The raw files are downloaded using: [wayback-machine-downloader](https://github.com/hartator/wayback-machine-downloader)

*Usage:*
```
wayback_machine_downloader http://www.studentcoursereview.com/q/new-zealand/university-of-auckland/faculty-of-engineering
```

Note that the path is currently restricted to the faculty of engineering - it will only download engineering related courses

The wayback machine can be browsed to find other paths, and in turn other courses:

[https://web.archive.org/web/20190314182459/http://www.studentcoursereview.com/q/new-zealand/university-of-auckland/faculty-of-engineering](https://web.archive.org/web/20190314182459/http://www.studentcoursereview.com/q/new-zealand/university-of-auckland/faculty-of-engineering)

### `processor.py`
The entry point for the application. 

Extracts and processes the course reviews from the scraped files, then outputs the result to `reviews.json`
