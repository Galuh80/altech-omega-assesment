<!-- ABOUT THE PROJECT -->
## About The Project

The library application serves as a digital repository for managing books authored by various writers. It provides functionalities for users to browse, search, and interact with books and authors.

### Solution Design

1. Modular Architecture:
    * Separation of Concerns: The application is designed with a clear separation between different layers such as models, views, serializers, and templates. This              modular approach improves maintainability and scalability.
    * Reusable Components: Common functionalities, like user authentication and book search, are implemented as reusable components, making it easier to extend the             application with new features.
2. RESTful API:
    * Django Rest Framework (DRF): Utilized DRF to create a RESTful API for managing books and authors. This allows for easy integration with front-end applications and         other external services.
    * Standard HTTP Methods: Followed REST conventions using standard HTTP methods (GET, POST, PUT, DELETE) for CRUD operations, ensuring a consistent and intuitive API         design.
3. Database Schema Design:
    * Normalized Database: The database schema is normalized to minimize redundancy and ensure data integrity. Tables for books, authors, and user interactions are              related using foreign keys.

### Performance Tuning Techniques

1. Caching:
    * Redis: Used Redis as the caching backend for its high performance and support for complex data structures.

### Built With

The library application created with some technologies, such as:

* [![Django][Django]][Django-url]
* [![DRF][DRF]][DRF-url]
* [![SQLite][SQLite]][SQLite-url]
* [![Redis][Redis]][Redis-url]
* [![Swagger][Swagger]][Swagger-url]


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Before running the library management application, make sure you have installed some of the tools below, because I use the Linux operating system, I will give an example using Linux.
* Python 3.10
  ```sh
  sudo apt install python3
  ```
* Redis
  ```sh
  sudo apt install redis
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Galuh80/altech-omega-assesment.git
   ```
2. Move to directory
   ```sh
   cd altech-omega-assesment
   ```
3. Install virtual environment
   ```sh
   python3 -m venv env
   ```
4. Activate the environmnet
   ```sh
   source env/bin/activate
   ```
6. Install requirements
   ```sh
   pip install -r requirments.txt
   ```
7. Copy .env.example to .env and configure it

<!-- USAGE EXAMPLES -->
## Usage

1. Database migrate
   ```sh
   python3 manage.py migrate
   ```
2. Author seeding
   ```sh
   python3 manage.py author_seed_data
   ```
3. Book seeding
   ```sh
   python3 manage.py book_seed_data
   ```
4. Run application
   ```sh
   python3 manage.py runserver
   ```

## Testing

1. Author Test
   ```sh
   python3 manage.py test author
   ```
   [![Author Test][author-test-screenshot]
      
2. Book Test
   ```sh
   python3 manage.py test book
   ```
   [![Book Test][book-test-screenshot]
   
3. Swagger UI
   ```sh
   http://127.0.0.1:8000/swagger/
   ```
   ![image](https://github.com/Galuh80/altech-omega-assesment/assets/33372417/73982ce9-1035-4fd6-8d4f-31fdf44dfe55)


<!-- ROADMAP -->
## To Do List

- [x] Authors Module
- [x] Books Module
- [x] Restfull API
- [x] Caching
- [x] Testing

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[author-test-screenshot]: images/test-authors.png
[book-test-screenshot]: images/test-books.png
[swagger-screenshot]: images/swagger.png
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[DRF]: https://img.shields.io/badge/django--rest--framework-3.12.4-blue?style=for-the-badge&labelColor=333333&logo=django&logoColor=white&color=blue
[DRF-url]: https://www.django-rest-framework.org/
[SQLite]: https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/
[Redis]: https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/
[Swagger]: https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white
[Swagger-url]: https://swagger.io/
