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
  - **SQLite** - Used as the default database for development and testing purposes.
  - **PostgreSQL** - Utilized for production environments, providing a robust and scalable database solution.

- **Additional Libraries**
  - **Crispy Forms** - For enhanced form rendering and styling.
  - **Debug Toolbar** - Assists in debugging and optimizing the application during development.

## Deployment

The Newspaper Agency application is now live and can be accessed at the following link: [Newspaper Agency](https://newspaper-agency-y8oq.onrender.com/).

- **Authentication**
  - You can log in to the application using the following credentials:
    - **Username**: `test`
    - **Password**: `test_password1234`

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

   - Copy the sample environment variables file:

     ```bash
     cp .env.sample .env
     ```

   - Open the `.env` file in your preferred text editor and configure the following variables:

     ```env
     # Django
     SECRET_KEY=your_secret_key_here
     DJANGO_SETTINGS_MODULE=your_project.settings
     RENDER_EXTERNAL_HOSTNAME=your_domain

     # DB
     POSTGRES_DB=newspaper_agency
     POSTGRES_DB_PORT=5432
     POSTGRES_USER=your_db_user
     POSTGRES_PASSWORD=your_db_password
     POSTGRES_HOST=localhost
     ```

     - **SECRET_KEY**: Replace `your_secret_key_here` with a strong secret key.
     - **DJANGO_SETTINGS_MODULE**: Typically set to `newspaper_agency.settings`.
     - **RENDER_EXTERNAL_HOSTNAME**: Your deployment domain if applicable.
     - **POSTGRES_DB**: Name of your PostgreSQL database, e.g., `newspaper_agency`.
     - **POSTGRES_DB_PORT**: Port for PostgreSQL, usually `5432`.
     - **POSTGRES_USER**: Your PostgreSQL username.
     - **POSTGRES_PASSWORD**: Your PostgreSQL password.
     - **POSTGRES_HOST**: Host address for PostgreSQL, e.g., `localhost` or your database server address.

5. **Set Up the Database**

   - **For SQLite (Development):** No additional steps required.
   - **For PostgreSQL (Production):**
     - Ensure PostgreSQL is installed and running.
     - Create a new PostgreSQL database and user:

       ```bash
       psql
       CREATE DATABASE newspaper_agency;
       CREATE USER your_db_user WITH PASSWORD 'your_db_password';
       GRANT ALL PRIVILEGES ON DATABASE newspaper_agency TO your_db_user;
       \q
       ```

6. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**

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
