# Flask Blog - Directory Structure

The project is organized as follows:

```bash
flask-blog/
│
├── blog/
│   ├── __init__.py         # Initializes the app and sets up configurations
│   ├── models.py           # Defines the database models (User, Post)
│   ├── routes.py           # Handles the routing for the application
│   ├── forms.py            # Defines the forms used in the application
│   └── templates/          # HTML templates for rendering pages
│       ├── layout.html     # Base layout template
│       ├── home.html       # Home page template
│       ├── post.html       # Individual post page template
│       ├── register.html   # Registration page template
│       └── login.html      # Login page template
│
├── static/                 # Static files (CSS, JS, images)
│   ├── main.css            # Main stylesheet
│
├── migrations/             # Database migration files
│
├── .env                    # Environment variables file
├── run.py                  # Main application entry point
├── requirements.txt        # List of dependencies
└── README.md               # Basic project overview and setup instructions
