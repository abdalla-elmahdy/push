# Push

Push is a platform that helps learners with shared goals collaborate together on projects used to apply what they learn, or even go through a certain book or MOOC together to help make the learning process easier.

## Table of Contents

- [Prerequisites](#Prerequisites)
- [Getting Started](#Getting-Started)
- [Screenshots](#Screenshots)
- [Built With](#Built-With)
- [Contributing](#Contributing)

## Prerequisites

In order to be able to run Push locally you will need to have docker and docker-compose installed on your machine.
You can install them by following instructions in these links:

- https://docs.docker.com/engine/install/
- https://docs.docker.com/compose/install/

## Getting Started

1. Clone the repo to your machine.\
   `git clone https://github.com/abdalla-elmahdy/push.git`
2. Spin the docker containers.\
   `docker-compose up -d --build`
3. Apply DB migrations.\
   `docker-compose exec web python manage.py migrate`
4. Run the tests to make sure everything is working fine.\
   `docker-compose exec web python manage.py test`
5. Create a superuser to be able to acces the admin panel.\
   `docker-compose exec web python manage.py createsuperuser`\
   and you are good to go with a working instance of Push you can access at http://localhost:8000/

## Screenshots

![push-homepage](https://imgur.com/sxTNyA2.png "Homepage")
![search-form](https://imgur.com/vBKSvEG.png "Search Form")
![my-projects](https://imgur.com/ZXB6FOp.png "My Projects")
![project-details](https://imgur.com/YLVnLi3.png "Project Details Page")
![proposal-form](https://imgur.com/rd0Zaie.png "Proposal Form")
![received-proposals](https://imgur.com/rBGEYVI.png "Received Proposals")
![my-favorites-page](https://imgur.com/qkUULEX.png "My Favorites Page")

## Built With

- Python: https://www.python.org/
- Django: https://www.djangoproject.com/
- Postgres: https://www.postgresql.org/
- HTMX: https://htmx.org/docs/

## Contributing

If you would like to contribute to this project check [CONTRIBUTING.md](CONTRIBUTING.md)
