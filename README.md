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

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png

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
