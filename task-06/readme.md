
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
   
2. **Create a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:** Create a `.env` file in the root directory and add the following variables:
   ```bash
   FLASK_APP=run.py
   SECRET_KEY=your_secret_key
   SQLALCHEMY_DATABASE_URI=sqlite:///site.db
   ```

5. **Apply Migrations:**
   ```bash
   flask db upgrade
   ```

6. **Run the Development Server:**
   ```bash
   flask run
   ```

7. **Access the Application:** Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage
- **Create Post:** Log in, navigate to the "New Post" page, enter post details, and submit.
- **Update Post:** Edit existing posts by navigating to the "Edit Post" page.
- **Delete Post:** Remove posts from the list using the delete option.
