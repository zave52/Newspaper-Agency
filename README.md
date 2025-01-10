# Newspaper-Agency

## Overview

**Newspaper Agency** is a comprehensive web application designed to streamline the management and tracking of newspapers and their respective redactors within your agency. Built with Django and leveraging the sleek and responsive Material Kit templates, this system ensures that you, as the chief of the newspaper agency, can efficiently oversee your team of redactors and the newspapers they produce.

## Features

- **Redactor Management**
  - **Create, Read, Update, Delete (CRUD)** operations for redactors.
  - Track redactors' **years of experience**, ensuring you have insights into your team's expertise.
  - Assign multiple redactors to newspapers, fostering collaboration and accountability.

- **Newspaper Management**
  - Perform **CRUD** operations on newspapers.
  - Assign multiple redactors (publishers) to each newspaper, enabling transparent tracking of contributions.
  - Categorize newspapers under various **topics** for organized content management.

- **Topic Management**
  - Manage **topics** to categorize newspapers, enhancing searchability and organization.
  - Assign multiple topics to newspapers, allowing for versatile content classification.

- **User Authentication**
  - Secure user registration and login system.
  - Restrict access to management functionalities to authenticated users only, ensuring data integrity and security.

- **Responsive Design**
  - Utilizes **Material Kit** templates for a modern, intuitive, and responsive user interface.
  - Ensures a seamless experience across devices, from desktops to mobile phones.

- **Search and Filtering**
  - Implement search functionalities to quickly find redactors, newspapers, or topics based on specific criteria.
  - Filter lists based on various attributes to streamline content management.

- **Admin Interface**
  - Customizable Django admin panel for advanced management and oversight.
  - Enhanced admin capabilities to manage redactors, newspapers, and topics with ease.

- **Testing**
  - Comprehensive unit tests for models and views to ensure reliability and robustness.
  - Ensures that all functionalities perform as expected, maintaining high-quality standards.

## Technologies Used

- **Backend**
  - [Django](https://www.djangoproject.com/) - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

- **Frontend**
  - [Material Kit](https://www.creative-tim.com/product/material-kit) - A modern, responsive frontend framework based on Material Design principles.
  - [Bootstrap 5](https://getbootstrap.com/) - Utilized for styling and responsive design components.

- **Database**
  - SQLite - Default database for Django projects, suitable for development and testing purposes.

- **Additional Libraries**
  - **Crispy Forms** - For enhanced form rendering and styling.
  - **Debug Toolbar** - Assists in debugging and optimizing the application during development.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/zave52/Newspaper-Agency.git
   cd Newspaper-Agency
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   - Create a `.env` file in the root directory.
   - Add the following variables:

     ```env
     SECRET_KEY=your_secret_key_here
     ```

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   - Access the application at [http://localhost:8000](http://localhost:8000).

## Usage

- **Admin Panel**
  - Access the Django admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/).
  - Manage redactors, newspapers, and topics directly from the admin interface.

- **Application Interface**
  - **Redactors**: Manage your team of redactors, assign them to newspapers, and track their experience.
  - **Newspapers**: Create and manage newspapers, assign multiple redactors, and categorize them under various topics.
  - **Topics**: Organize newspapers under different topics for better content management and searchability.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Material Kit](https://www.creative-tim.com/product/material-kit)
- [Bootstrap](https://getbootstrap.com/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
