# Django Calculator App

A clean and functional web calculator built using **Django**, capable of evaluating mathematical expressions using Python syntax. This project showcases dynamic rendering, alert messages, and clean Bootstrap styling — perfect for learning or demonstrating full-stack basics.

## Project Structure

calculator_app/ # Django root directory <br>
│<br>
├──calculator_app/ # One of the Django apps (used for logic/UI/views)<br>
|<br>
├── calculatorapp/ # Main Django app<br>
│ ├── views.py<br>
│ ├── urls.py<br>
│ └── init.py<br>
│<br>
├── rootapp/ # (Optional if unused, else mention its purpose)<br>
│<br>
├── static/ # Static files folder<br>
│ └── images/<br>
│ └── main.jpg # Image displayed on the page<br>
│<br>
├── templates/ # HTML templates<br>
│ └── index.html<br>
│<br>
├── myenv/ # Python virtual environment<br>
│<br>
├── db # SQLite database file (empty or auto-generated)<br>
│<br>
├── manage.py # Django CLI utility<br>
└── requirements.txt # Python package requirements<br>

## Key Features

- **Expression Evaluation**: Enter expressions like `3 + 5`, `10 / 2`, `4 * (3 - 1)` and get the result instantly.
- **Dynamic Result Rendering**: Displays result or error as a Bootstrap alert (green for success, red for failure).
- **Smart Error Handling**: Gracefully handles empty input or invalid expressions using `try-except`.
- **Django-Powered Backend**: Python handles expression logic and routing via Django views and URLs.
- **Responsive UI with Bootstrap CDN**: No local CSS or JS needed. Styled with Bootstrap 4 for a clean and modern interface.
- **Image Integration**: Displays a visual (calculator-themed) image stored in the `static/` folder.
- **Real-time** feedback using GET form submission

## Built With

| Technology                  | Purpose                                              |
|-----------------------------|------------------------------------------------------|
| Django                      | Core backend logic, URL routing, rendering templates |
| HTML5 + Bootstrap 4.4.1 CDN | Frontend layout, form UI, alerts, and responsiveness |
| Python 3.12                 | Expression evaluation logic using `eval()`           |
| SQLite                      | Default database (auto-generated)                    |

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/PoorvaJawale/calculator_app.git
   cd calculator_app

2. Create a virtual environment:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate     # (Windows)

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the development server:
   ```bash
   python manage.py runserver

5. Open in your browser:
   ```bash
   http://127.0.0.1:8000/

## How the Django Calculator App Works — Explained Step-by-Step

 1. User visits the site
The user opens [ http://127.0.0.1:8000/ ] 
The URL routing (defined in urls.py) sends the request to the index() view in views.py.

3. The index() view renders index.html
   ```bash
   def index(request):
    return render(request, 'index.html')
   It loads the main calculator page.
This page contains:
A search-style input box (<input type="search" name="query">)
A Submit button that sends the input to the server via the GET method

3. User enters a math expression and clicks Submit
Example input: 2 + 3 * (4 - 1)
The form sends this expression to the URL like:
[ http://127.0.0.1:8000/calculatorappsubmitquery?query=2+%2B+3+*+(4+-+1) ]
This triggers the submitquery() view.

4. The submitquery() view handles the input
   ```bash
   def submitquery(request):
    q = request.GET['query']     # Get the query string from the input field
    try:
        ans = eval(q)            # Evaluate the expression using Python's eval()
        mydictionary = {'q': q, 'ans': ans, 'error': False}
        return render(request, 'index.html', context=mydictionary)
    except:
        mydictionary = {'error': True}
        return render(request, 'index.html', context=mydictionary)
If the expression is valid:
  eval() calculates the result.
  The result (ans) and the original query (q) are sent to the template.
  A green success alert is shown on the page.
If the expression is invalid or empty:
  The except block catches the error.
  A red error alert is displayed.

5. How the template (index.html) responds
In index.html, you’ve written conditional code like:
   {% if error %}
  <!-- Show red error alert -->
  {% else %}
  <!-- Show green success alert with answer -->
  {% endif %} 
And the input field retains its value using:
   <input type="search" name="query" value="{{ q }}">
This keeps the user experience smooth by:
  Showing alerts
  Keeping the input visible
  Showing the result below the form

6. Styling and Display
The image (main.jpg) is loaded using:
  <img src="{% static 'main.jpg' %}">
Styling is done entirely using Bootstrap 4 CDN links, no local CSS or JS required.
Alerts, buttons, navbar, and layout are all Bootstrap components.

## Summary Flowchart

User Enters Expression (Frontend)<br>
        ↓<br>
Form Sends GET Request → /calculatorappsubmitquery?query=...<br>
        ↓<br>
Django View Handles It (views.py → submitquery)<br>
        ↓<br>
If Valid: eval() the expression → send result to template<br>
If Error: send error flag to template<br>
        ↓<br>
index.html displays either:<br>
✅ Green alert with answer<br>
❌ Red alert with error<br>

## Warning
This app uses Python's built-in eval() function for simplicity. It is not safe for production without proper input sanitization. Only use this for learning/demo purposes.

## Concepts Used
Django Views & URL Routing
HTML templating with context
Bootstrap 4 for frontend styling
Static file management (CSS, JS, Images)
GET method form submission and result rendering

For any queries, feedback, or collaboration opportunities, feel free to reach out to me at **poorvakjawale@gmail.com**.
