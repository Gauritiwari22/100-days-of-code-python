# # 📘 Day 70 Notes – Deployment of Flask Web Applications

# # 🎯 Objective of Day 70
# Learn how to deploy a Flask application online so it can be accessed publicly instead of only running locally.

# Before deployment:
# http://127.0.0.1:5000

# After deployment:
# https://yourapp.onrender.com

# ---

# # 🧠 Core Concepts

# # 1. What is Deployment?

# Deployment means hosting your application on a server so users can access it online.

# ---

# # 2. Development vs Production

# | Development | Production |
# |---|---|
# | Local machine | Live server |
# | debug=True | debug=False |
# | Testing environment | Real users |
# | Flask dev server | Gunicorn |

# ---

# # 3. Why Flask’s Built-in Server is Not Used in Production

# This:
# ```python
# app.run(debug=True)

# Environment Variables

# Used to securely store sensitive information.

# Bad practice:

# app.secret_key = "secret123"

# Better:

# import os

# app.secret_key = os.environ.get("SECRET_KEY")

