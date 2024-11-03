# Django Project - Random Articles Management Site

This is a Django web application that allows users to register, log in, and add/view articles. Unauthenticated users can view articles but must register or log in to add new ones.

---

## Features

- **User Registration and Authentication**
  - Register a new account or log in with existing credentials.
- **Article Management**
  - View all the articles or a single article in detail.
  - Add a new articles (authenticated users only).
- **Home Page**
  - Displays the most recent articles.

---

## Project Setup

### Prerequisites

- Python 3.13
- Django 5.1.2
- SQLite (database)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mitchsaah/django-Project-T2.git
   cd djangoProjectT2
   
## References

This project was built using the following resources and documentation:

1. **Django Documentation**  
   Django's official documentation was essential in understanding the Django framework, especially for user authentication, URL routing, and database configuration with SQLite.  
   - [Django Documentation](https://docs.djangoproject.com/en/stable/)

2. **Django Tutorials with Mosh**  
   These beginner-friendly tutorials provided helpful insights into Django views, templates, and models. I mostly watched the second video before really trying PyCharm in the first week of the second assignment.
   - [Django 6h Tutorial - With Django](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=5574s&pp=ygULbW9zaCBweXRob24%3D)
   - [Django 1h Tutorial - With Django](https://www.youtube.com/watch?v=kqtD5dpn9C8&t=300s&pp=ygULbW9zaCBweXRob24%3D)

3. **ChatGPT**  
   ChatGPT was used for some of the urlpatterns, as I was still trying to figure out how to use new creations and how to write them down. 
   - These have been put into comments next to the code (urls.py)
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
