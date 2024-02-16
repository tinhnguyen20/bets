# Betz

Bets for anything.

## Running the backend

```bash
cd bets-backend

# activate environment
poetry shell
# install requirements
poetry config virtualenvs.in-project true
poetry install --no-root

# day0
python manage.py createsuperuser

# running the backend
python manage.py runserver

# running tests
python manage.py test
```

## Auth

Access Token
```
curl -X POST -H "Content-Type: application/json" -d '{"username": "<YOUR-USERNAME>", "password": "<YOUR-PASSWORD>"}' http://localhost:8000/api/token/
```

## TODO

1. **Project Setup**
   - [X] Create a new Django project.
   - [X] Set up a virtual environment for your project.
   - [X] Install Django and necessary dependencies.

2. **Database Configuration**
   - [X] Configure database settings in `settings.py`.
   - [X] Define models for User, Bet, BetChoice, BetParticipant.
   - [ ] Implement Notification Model for Bet Validation (ASYNC CELERY)

3. **Authentication**
   - [X] Implement user authentication using Django's built-in authentication system (Token Auth for now).
   - [ ] Create endpoints for user login and logout.

4. **Bets Management**
   - [X] Create CRUD (Create, Read, Update, Delete) endpoints for managing bets.
   - [X] Implement logic for creating, updating, and deleting bets.

5. **Bet Participants**
   - [ ] Implement endpoints for managing participants in a bet (joining, leaving, updating choice).
   - [ ] Ensure proper validation and authorization for participant actions.

6. **Notifications**
   - [ ] Design notification models and database schema.
   - [ ] Implement endpoints for sending and receiving notifications.
   - [ ] Integrate Celery for asynchronous notification tasks.

7. **Celery Setup**
   - [ ] Install Celery and message broker (e.g., RabbitMQ, Redis).
   - [ ] Configure Celery settings in `settings.py`.
   - [ ] Define Celery tasks for asynchronous bet result calculation and notification sending.

8. **Testing**
   - [ ] Write unit tests and integration tests for API endpoints and Celery tasks.
   - [ ] Test authentication, CRUD operations, participant actions, and notification functionalities.

9. **Documentation**
   - [ ] Generate API documentation using tools like Swagger or Django Rest Framework's built-in documentation.
   - [ ] Write a comprehensive README file with setup instructions, API endpoints, and usage examples.

10. **Deployment**
    - [ ] Choose a deployment platform (e.g., Heroku, AWS, DigitalOcean).
    - [ ] Set up deployment configurations and environment variables.
    - [ ] Deploy the application and ensure it's accessible and functional.

11. **Monitoring and Maintenance**
    - [ ] Implement logging and monitoring solutions to track application health and performance.
    - [ ] Regularly update dependencies and libraries to address security vulnerabilities.
    - [ ] Handle bug fixes, feature enhancements, and user feedback promptly.

12. **Contributing**
    - [ ] Set up contribution guidelines and a code of conduct for contributors.
    - [ ] Encourage contributions and review pull requests from the community.
