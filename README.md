# Task-Manager

# Setup

- python -m venv venv
- source venv/Scripts/activate
- pip install -r requirements.txt


## Class

- User
    - Attr
        - user_id
        - name
        - username
        - password
        - tasks
    - Methods
        - regiter
        - login
    
- Task
    - Attr
        - title
        - description
        - created_at
        - deadline
        - completed
    - Method
        - mark_as_completed

- Manager
    - Attr
        - user
    - Methods
        - get_user


