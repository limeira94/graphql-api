# FastAPI & GraphQL API with Automated Deployment
This project is a complete demonstration of how to build a modern GraphQL API using FastAPI and Strawberry, containerize it with Docker, and set up a professional CI/CD pipeline using GitHub Actions to automatically test and deploy it to a DigitalOcean Droplet.

The API serves a mock database of authors and books, showcasing how to handle data relationships in GraphQL.

### Features
- **Modern GraphQL API:** Built with FastAPI for high performance and Strawberry for a clean, type-safe GraphQL implementation.

- **Containerized Environment:** Fully containerized with Docker and Docker Compose for consistent and portable development and production environments.

- **Automated Testing:** Includes a test suite using pytest to ensure API reliability.

- **Continuous Integration (CI):** The GitHub Actions workflow automatically runs all tests on every push to the main branch.

- **Continuous Deployment (CD):** On a successful test run, the workflow automatically deploys the latest version of the application to a DigitalOcean Droplet.

- **Zero-Downtime Deployments:** The deployment script on the server uses Docker Compose to rebuild and restart the application seamlessly.

- **Mock Database:** Comes with a script that generates 1000+ random data points (authors and books) for realistic API testing.

### Tech Stack
- Backend: FastAPI, Strawberry (GraphQL), Uvicorn

- Containerization: Docker, Docker Compose

- CI/CD: GitHub Actions

- Testing: Pytest

- Hosting: DigitalOcean Droplet

### Local Development Setup
To run this project on your local machine, you will need Git and Docker installed.

1. Clone the Repository:

```
git clone https://github.com/limeira.felipe94/graphql-api.git
cd graphql-api
```

2. Run the Application:
Use Docker Compose to build the image and start the container. The --build flag ensures it builds from the Dockerfile the first time.

`docker compose up --build`


The application will be running in the background.

3. Access the API:
Open your web browser and navigate to the interactive GraphQL playground:

- URL: http://localhost/graphql

You can stop the application at any time by running:

- `docker compose down`


### Testing
The project includes a suite of tests located in the /tests directory. To run the tests locally, first ensure your application container is running, then run the tests inside the container:

### Automated Deployment (CI/CD)
This project uses a GitHub Actions workflow defined in .github/workflows/deploy.yml to achieve fully automated testing and deployment.

**How It Works**

1. Trigger: The workflow is triggered on every git push to the main branch.

2. Test Job:

    - A fresh Ubuntu environment is spun up.

    - The code is checked out.

    - Python and all project dependencies are installed using uv.

    - The pytest suite is executed.

3. Deploy Job:

    - This job only runs if the test job completes successfully.

    - It securely connects to the DigitalOcean Droplet via SSH using secrets stored in GitHub.

    - Once connected, it runs a script that:

        - Navigates to the project directory.

        - Pulls the latest code changes from the main branch.

        - Uses docker compose to gracefully stop the old container, rebuild the image with the new code, and start the new container.

        - Prunes any old, unused Docker images to save server disk space.

### Required GitHub Secrets
To enable the deployment, the following secrets must be configured in your GitHub repository's Settings > Secrets and variables > Actions:

- `DROPLET_HOST`: The public IP address of your DigitalOcean Droplet.

- `DROPLET_USERNAME`: The username for SSH access (e.g., root).

- `SSH_PRIVATE_KEY`: The private SSH key that corresponds to a public key added to your Droplet's authorized_keys.

### API Usage
You can interact with the live API via the GraphiQL interface, which is available at your deployment URL.

- Endpoint: `http://YOUR_DROPLET_IP/graphql`
