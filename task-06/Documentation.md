
---

### **2. Documentation.md**

```markdown
# Flask Blog - Documentation

## Overview
Flask Blog is designed to provide users with a simple blogging platform where they can create, update, and delete posts. The application also includes user authentication (registration and login) and allows users to manage their own posts. The project demonstrates key Flask concepts, including routing, database management with SQLAlchemy, and form handling.

### Features
- **User Authentication:** Secure user registration and login system.
- **Post Creation:** Users can create blog posts with a title and content.
- **Post Management:** Users can edit and delete their own blog posts.
- **Post Viewing:** Users can view a list of all posts or individual post details.

## Code Structure

### Main Application Logic
The main application logic is initialized in `run.py`, which sets up the Flask app, registers blueprints, and configures the necessary extensions such as SQLAlchemy and Flask-Login.

### Key Modules:
- **`models.py`:** Defines the database models, including `User` and `Post` classes. These models represent the database schema and relationships.
- **`routes.py`:** Contains the routes for the application, handling HTTP requests for the different pages (home, about, login, register, and post management).
- **`forms.py`:** Defines the forms used in the application, including forms for user registration, login, and creating/editing posts.
- **`__init__.py`:** Initializes the Flask app and configures extensions like SQLAlchemy, Flask-Login, and Migrate.

### Key Functions
- **`create_post()`:** Handles the logic for creating a new post, including form validation and saving the post to the database.
- **`update_post()`:** Handles the logic for updating an existing post, including fetching the post from the database and saving changes.
- **`delete_post()`:** Handles the logic for deleting a post from the database.
- **`login()`:** Manages the login process, including form validation and user authentication.
- **`register()`:** Manages user registration, including form validation and saving new user data to the database.

### How to Extend the Project
- **Add Features:** You can extend the project by adding features such as comments on posts, user profiles, or categories/tags for blog posts.
- **Integrate APIs:** You can integrate third-party APIs for enhanced functionality, such as social media sharing or embedding content from external sources.
