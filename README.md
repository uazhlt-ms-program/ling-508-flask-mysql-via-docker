Sample Containerized Flask+MySQL project
----------------
A project with MySQL running in one Docker container (named `db`) and a Flask app running in
a second container (named `app`). These two containers connect over the Docker virtual network
interface, while the container running Flask also serves an API on the `localhost`
virtual network interface.

## Steps to use this repo with Pycharm:
* Make sure you've installed Docker on your system. I assume you're running
this in your Linux development environment. (Will this work if you
do all of this in Windows? I'm not sure, but you're welcome to try!)
* Clone the repository to your local machine.
* Make sure that in Pycharm you've:
  * set the root project directory (File > Settings > Project > Project Structure).
  * set the Python interpreter that Pycharm should use (File > Settings > Project > Project Interpreter).
  For any testing outside the Flask Docker container, you'll want to create a virtual environment using Python 3.10,
  and using the `requirements.txt` file.

### Issues to keep in mind
* *Communication*: MySQL will always be running in a Docker container, and the rest of our code will always connect
to it over a virtual network interface. ***Which interface*** it will use will depend on whether the rest of the code
is also running in a Docker container or in a Python virtual environment. In other projects, you may be accustomed
to running MySQL in Docker, and then mapping port 3306 on the container to some port on the `localhost` interface.
We'll only need to do this when the code that's connecting to MySQL is connecting from outside of Docker. When our
Flask app is itself in a Docker container, it can talk to the MySQL container over a virtual network that Docker
provides; in that situation, we don't need to map any ports on the MySQL container to `localhost`. This keeps all
the inter-container communication within Docker, and keeps your MySQL container a little more secure from outside
access. While you're testing your code, though, you likely ***do*** want to have that outside access. For this
reason, this project is set up with configurations to run Flask in a container or from a virtual environment.
* *Version compatibility*: The version of MySQL that you use (which is selected by setting a flag on the container
image that you select in the `docker-compose` file) needs to be compatible with the version of
`mysql-connector-python` that you also use. You can find a table of version compatibility 
[here](https://dev.mysql.com/doc/connector-python/en/connector-python-versions.html). The available versions of
MySQL are listed on the Docker Hub page for MySQL [here](https://hub.docker.com/_/mysql). You'll set the version of
`mysql-connector-python` in the `requirements.txt` file.
* *Configuration*: The password that you tell MySQL to use is found in an environment variable within the Docker
container for MySQL; you'll see that that is set in the `docker-compose` file. However, that password needs to
match the one that is set in the configuration used by `mysql-connector-python`, which is found in the MySQL
database implementation (`db/mysql_repo.py`). In the current state of this repository, that password is entered
in both places, and simply needs to match.

### To run only the database in a container
* Start MySQL in Docker: In Pycharm, open a terminal in the project root directory, and run `docker-compose -f docker-compose-mysql-only.yml up --build`
  (if you'll be running this repeatedly, you may also need to run `docker-compose -f docker-compose-mysql-only.yml down`
  between cycling the containers up.)
* Start Flask in the Python virtual environment:  Open a second terminal in the project root, make sure that the virtual environment is activated (look for `(venv)` to 
the left of the command prompt), and run `python app.py`
* You should now be able to access the API via `localhost:5000` and see that the Flask app has access to the MySQL
database.

### To run the whole app in containers
* Start both MySQL and Flask in Docker: In Pycharm, open a terminal in the project root directory, and run `docker-compose -f docker-compose-flask-mysql.yml up --build`
  (if you'll be running this repeatedly, you may also need to run `docker-compose -f docker-compose-flask-mysql.yml down`
  between cycling the containers up.)
* You should still be able to access the API via `localhost:5000` and see that the Flask app has access to the MySQL
database.