# Flask Blog

## Overview
Flask Blog is a simple blog application built using Flask, a micro web framework in Python. It allows users to create, read, update, and delete blog posts. This project demonstrates basic CRUD operations, user authentication, and form handling with Flask.

## Features
- User authentication (register, login, and logout)
- Create, update, and delete blog posts
- View a list of all blog posts
- View individual blog posts

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/flask-blog.git
   cd flask-blog
Create a Virtual Environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables: Create a .env file in the root directory and add the following variables:

bash
Copy code
FLASK_APP=run.py
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
Apply Migrations:

bash
Copy code
flask db upgrade
Run the Development Server:

bash
Copy code
flask run
Access the Application: Open your browser and navigate to http://127.0.0.1:5000/.

Usage
Create Post: Log in, navigate to the "New Post" page, enter post details, and submit.
Update Post: Edit existing posts by navigating to the "Edit Post" page.
Delete Post: Remove posts from the list using the delete option.
Contribution Guidelines
Reporting Issues: Please report any issues or bugs using the GitHub Issues tab.
Submitting Pull Requests: Fork the repository, make your changes, and submit a pull request with a detailed description.
