This project is a personal, for fun project I made to practice and learn web development but I would love if you have any improvements you want to implement or any suggestion really

## Table of Contents

- [Code Style and Linters](#Code-Style-and-Linters)
- [Testing](#Testing)
- [App Design](#App-Design)
- [Trello Board](#Trello-Board)

## Code Style and Linters

### Code Style

I prefer using Black, isort, and Djlint packages for code style but I like to user them as the editor extensions for instant feedback and modification on save so feel free to install them on your editor.

### Linters

for linters I am using flake8 I prefer to use it in the pre-commit hooks and not as instant feedback because I find it distracting and often inturrpting my train of thoughts, but if you like to use it in the editor feel free to do so but the pre-commit hook will run it anyway.

## Testing

- Whenever you implement a new feature or fix a bug, run all the tests to make sure nothing broke.
- Also please include tests for anything you implement, this helps keeping the project maintainable.
- Pushing your code or creating a pull request will trigger a ci workflow to run the tests, so make sure your code passes the checks

## App Design

The features of the project are broken into small django apps:

- accounts: handles all user features such as registering, authentication, editing the profile, password management. and it's using django-allauth 3rd party app as well
- projects: handles CRUD operations and pages of the Project model.
- pages: handles the static pages
- favorites: handles adding a project to a user's favorites to save for later
- proposals: handles sending contributing proposals to project owners to let them know what users are interested in collaborating

## Trello Board

Also feel free to pick any task from the backlog and contact me for any clarifications
https://trello.com/b/jgFhDJ6H/push-project
