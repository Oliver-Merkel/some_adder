# some_adder

## Creating an image from Dockerfile

Open a terminal window in the same directory where the `Dockerfile` from this repository is located. Build the Docker image:

```
docker build -t python_pytest .
```

Anyway on demand the docker image gets created in a build step inside the `Jenkinsfile` describing the build pipeline.
