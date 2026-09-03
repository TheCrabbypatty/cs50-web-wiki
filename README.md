# CS50W Project 1: Wiki

This is a Wikipedia-like online encyclopedia web application built using the Django web framework. It allows users to view encyclopedia entries, search for specific topics, create new pages, edit existing pages, and visit random entries. All content is written and edited in Markdown syntax and dynamically rendered into HTML using the `markdown2` package.

## Features

* **Entry Page**: Visiting `/wiki/TITLE` displays the content of that specific encyclopedia entry. If the requested page does not exist, a custom 404 error page is rendered.
* **Index Page**: The home page welcomes users and lists all available encyclopedia entries. Each entry title functions as a clickable link leading directly to its page.
* **Search Functionality**: A sidebar search utility allows users to type a query. 
  * If the query exactly matches an entry title, the user is redirected straight to that entry page.
  * If the query is a partial match, the application generates a search results page displaying all entries containing the query text as a substring.
* **Create New Page**: Clicking "Create New Page" opens a form featuring fields for a title and Markdown content. The application checks for title conflicts; if the page is entirely unique, it saves the file and redirects to the new entry.
* **Edit Page**: Every entry page includes an "Edit Page" button. Clicking it loads a form pre-populated with the existing Markdown text. Submitting the form saves the updates and returns the user to the updated page.
* **Random Page**: Clicking the "Random Page" link instantly routes the user to a randomly chosen entry from the system.
* **Markdown to HTML Conversion**: The application leverages `markdown2` to seamlessly translate raw entry markdown formatting (such as headings, bold text, links, and lists) into proper HTML when viewed in the browser.

## Project Structure

```text
wiki/
│
├── encyclopedia/               # Main Django application directory
│   ├── static/encyclopedia/    # CSS stylesheets and global assets
│   ├── templates/encyclopedia/ # HTML templates (Index, Entry, New, Edit, Error)
│   ├── urls.py                 # Application URL routing configurations
│   ├── util.py                 # Helper functions for saving, retrieving, and listing entries
│   └── views.py                # Main views containing the backend controller logic
│
├── entries/                    # Directory storing encyclopedia entries as Markdown (.md) files
│   ├── CSS.md
│   ├── Django.md
│   └── HTML.md
│
├── wiki/                       # Root project configuration directory
│   ├── settings.py             # Global Django configuration settings
│   └── urls.py                 # Project level URL routing
│
└── manage.py                   # Django command-line execution utility
```

## Installation and Execution

1. Clone the repository or download and extract the project files.
2. Open a terminal and navigate to the project root directory.
3. Install Django and the `markdown2` package:
   ```bash
   pip install django markdown2
   ```
4. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
5. Open your preferred web browser and navigate to `http://127.0.0` to explore the wiki app.

## Challenges Faced

* **Navigating the Django Multi-Folder Architecture**: Coming into Django, managing the distributed folder layout was a major hurdle. Constantly jumping between the project configuration folder (`wiki/`), the specific app directories (`encyclopedia/`), backend views (`views.py`), templates, and entry storage files required a steep mental learning curve. While tracking the connections between URLs, views, and templates was complicated at first, building this project ultimately made the system design click and demonstrated the scalability of isolating these components.



## Last Updated

<!-- TIMESTAMP_START -->
_Last updated: 2026-09-03 21:22 UTC_
<!-- TIMESTAMP_END -->
