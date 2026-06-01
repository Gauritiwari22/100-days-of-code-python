# # 📘 Day 71 Notes – Blog Capstone Project (Upgrading the Blog)

# # 🎯 Objective

# Build a more complete and professional blog website by improving the project from previous days.

# Instead of:
# - hardcoded data
# - simple pages

# You now create:
# - a proper blog
# - reusable templates
# - dynamic content
# - better user experience

# ---

# # 🧠 Main Concepts

# ## 1. Capstone Project

# A capstone project combines everything learned so far:

# - Flask
# - Jinja Templates
# - Bootstrap
# - Routing
# - Forms
# - Databases
# - CRUD Operations

# ---

# ## 2. Reusable Templates

# Instead of repeating HTML:

# ```html
# <html>
# <head>
# </head>
# <body>
# </body>
# </html>

# Add bootstrap CDN
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

# Nav bar
# <nav class="navbar navbar-dark bg-dark">
#     <a class="navbar-brand" href="/">My Blog</a>
# </nav>

# CRUD Revision

# CRUD =

# Create
# Read
# Update
# Delete

# Examples:

# Create:

# db.session.add(post)


# Redirects

# Used after actions:

# return redirect(url_for("home"))


# Database Models

# Example:

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200))
#     content = db.Column(db.Text)


# Primary Key
# id = db.Column(db.Integer, primary_key=True)

# Purpose:

# Unique identifier
# No duplicates