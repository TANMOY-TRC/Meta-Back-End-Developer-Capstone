# Meta Back-End Developer Capstone Project

The **Little Lemon** web application is a full-stack project built using **Django** as part of the **Meta Back-End Developer Professional Certificate**. It features a **RESTful API** powered by **Django REST Framework (DRF)** and a **static frontend** that interacts dynamically with the API using **JavaScript**. Designed for managing the operations of Little Lemon, a fictional restaurant. The application allows users to view the menu and item details, while authenticated restaurant officials can add or modify menu items, book tables, and view reservations. It includes token-based authentication with Djoser, client-side form validation, and a responsive design to ensure a seamless experience across devices. With a structured backend, secure API endpoints, and a dynamic frontend, the project demonstrates best practices in modern web development.


## Project Highlights

- **Full-Stack Django Application**: Built with Django, featuring a structured API and a static website.
- **RESTful API with DRF**: Well-defined endpoints for seamless data interaction.
- **Token-Based Authentication**: Secure access using **Djoser**.
- **JavaScript-Powered Frontend**: Static website interacts dynamically with the API.
- **Mobile & Desktop Responsive**: Optimized UI for different screen sizes.
- **Database Integration**: Uses **MySQL** for efficient data storage and retrieval.
- **Comprehensive Testing**: Includes unit tests for models and views.


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [API Testing](#api-testing)
- [License](#license)


## Project Overview

This project serves as a demonstration of skills learned in the **Meta Back-End Developer Professional Certificate**. It is a full-stack web application consisting of two Django apps:

- **API App**: A backend service built with **Django REST Framework (DRF)** that provides structured API endpoints for data retrieval and manipulation.
- **Static Website App**: A frontend application serving static pages, where **JavaScript** is used to fetch and update data dynamically via API calls.

The project includes authentication, data validation, and interactive features to ensure a seamless user experience. It follows best practices in backend development, with a focus on security, scalability, and maintainability.


## Features

- **Responsive Design**: The static website is optimized for both desktop and mobile.
- **API Authentication**: Secure authentication using **Djoser**.
- **Client-Side Form Validation**: Ensures proper user input before submitting API requests.
- **JavaScript API Calls**: The static website fetches and updates data dynamically via API requests.
- **UI/UX**: Modern and intuitive design following UI/UX best practices.
- **Testing**: Includes unit tests for models and views of the API.


## Technologies Used

- **Backend**: Django, Django REST Framework (DRF)
- **Frontend**: HTML, CSS, JavaScript (for API interaction)
- **Authentication**: Djoser (Token-based authentication)
- **Database**: MySQL


## Setup Instructions

 1. Clone the repository:
    ```bash
    git clone https://github.com/TANMOY-TRC/Meta-Back-End-Developer-Capstone.git
    ```

 2. Navigate to the project directory:
    ```bash
    cd Meta-Back-End-Developer-Capstone
    ```

 3. Install dependencies and activate the virtual environment:
    ```bash
    pipenv install
    pipenv shell
    ```

 4. Log into MySQL Shell in SQL mode (Based on OS):
    ```bash
    mysql -u root -p --sql
    ```
    ```powershell
    mysqlsh -u root -p --sql
    ```

 5. Set up the database:
    ```mysql
    CREATE DATABASE littlelemon;
    CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
    GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
    ```

 6. Apply the migrations:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

 7. Create superuser:
    ```bash
    python3 manage.py createsuperuser
    ```

 8. Run the development server:
    ```bash
    python3 manage.py runserver
    ```

 9. Open your browser and navigate to:
    ```bash
    http://127.0.0.1:8000/
    ```

10. Run Django unit tests (Optional):
    ```bash
    python3 manage.py test
    ```


## API Endpoints

#### `/auth/users/`
| Method | Action | AUTH TOKEN | STATUS CODE |
| ------ | ------ | ---------- | ----------- |
| `POST` | Creates new user credential | Not Required | 201 |

**Payload**:
```js
{
   "email": "string",
   "username": "string",
   "password": "string"
}
```

#### `/auth/users/me/`
| Method | Action | AUTH TOKEN | STATUS CODE |
| ------ | ------ | ---------- | ----------- |
| `GET` | Returns user details | Required | 200 |

#### `/auth/token/login/`
| Method | Action | AUTH TOKEN | STATUS CODE |
| ------ | ------ | ---------- | ----------- |
| `POST` | Returns auth token | Not Required | 200 |

**Payload**:
```js
{
   "username": "string",
   "password": "string"
}
```

#### `/auth/token/logout/`
| Method | Action | AUTH TOKEN | STATUS CODE |
| ------ | ------ | ---------- | ----------- |
| `POST` | Destroys the auth token | Required | 204 |


#### `/api/menu-items/`
| Method | Action | AUTH TOKEN | STATUS CODE |
| ------ | ------ | ---------- | ----------- |
| `GET` | Retrives all menu items | Not Required | 200 |
| `POST` | Adds new menu item | Required | 201 |

**Payload**:
```js
{
   "title": "string",
   "price": "decimal",
   "inventory": number
}
```

#### `/api/menu-items/{id}/`
| Method | Action | AUTH TOKEN | STATUS CODE |
| ------ | ------ | ---------- | ----------- |
| `GET` | Retrives specific menu item | Not Required | 200 |
| `PUT` | Modifies specific menu item | Required | 200 |
| `PATCH` | Modifies specific fields | Required | 200 |
| `DELETE` | Deletes the menu item | Required | 204 |

**Payload**:
```js
{
   "title": "string",
   "price": "decimal",
   "inventory": number
}
```

#### `/api/bookings/tables/`
| Method | Action | AUTH TOKEN | STATUS CODE |
| ------ | ------ | ---------- | ----------- |
| `GET` | Retrives all bookings | Required | 200 |
| `POST` | Adds new booking | Required | 201 |

**Payload**:
```js
{
   "name": "string",
   "no_of_guests": number,
   "booking_date": "date",
   "booking_slot": number (hour in 24h format)
}
```

#### `/api/bookings/tables/{id}/`
| Method | Action | AUTH TOKEN | STATUS CODE |
| ------ | ------ | ---------- | ----------- |
| `GET` | Retrives specific booking | Required | 200 |
| `PUT` | Modifies specific booking | Required | 200 |
| `PATCH` | Modifies specific fields | Required | 200 |
| `DELETE` | Deletes the booking | Required | 204 |

**Payload**:
```js
{
   "name": "string",
   "no_of_guests": number,
   "booking_date": "date",
   "booking_slot": number (hour in 24h format)
}
```


## API Testing

The API can be tested by sending HTTP requests to the appropriate endpoints using tools such as [Insomnia](https://insomnia.rest/download).


## License

This project is licensed under the [MIT License](./LICENSE).
