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
  For any testing outside the Flask Docker container, you'll want to create a virtual environment using Python 3.10, and using the requirements.txt file
* In Pycharm, open a terminal in the project root directory
  * type `docker-compose up --build`
    (if you'll be running this repeatedly, you may also need to run `docker-compose down` between cycling the containers up.)
* You should now be able to access the API via `localhost:5000` and see that the Flask app has access to the MySQL database. 
