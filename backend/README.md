# Installation Prerequisites

To get started, you will need a clean Ubuntu 20.04 server instance with a non-root user set up. The non-root user must be configured with sudo privileges. Make sure you have Python 3. Ubuntu 20.04 should have this by default but if not, please install it.

To check the version of Python you have installed:

    python3 -V

Next install the ubuntu package prerequisites for this system.

    sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib postgis nginx curl

# Install with pip in a Virtual Environment

The most flexible way to install Django on your system is within a virtual environment that we will create with the venv module.
This tool allows you to create virtual Python environments and install Python packages without affecting the rest of the system.
You can therefore select Python packages on a per-project basis, regardless of conflicts with other projects’ requirements.

    sudo apt update
    sudo apt install python3-pip python3-venv

# Install Django Project Requirements within a Virtual Environment

We will be installing our Python requirements within a virtual environment for easier management.

To do this, we first need access to the virtualenv command. We can install this with pip.

If you are using Python 3, upgrade pip and install the package by typing:

    sudo -H pip3 install --upgrade pip
    sudo -H pip3 install virtualenv

With virtualenv installed, we can start forming our project. Create and move into a directory where we can keep our project files:

    mkdir ~/myprojectdir
    cd ~/myprojectdir

Within the project directory, create a Python virtual environment by typing:

    virtualenv myprojectenv 

This will create a directory called myprojectenv within your myprojectdir directory. Inside, it will install a local version of Python and a local version of pip. We can use this to install and configure an isolated Python environment for our project.

Before we install our project’s Python requirements, we need to activate the virtual environment. You can do that by typing:

    source myprojectenv/bin/activate

Your prompt should change to indicate that you are now operating within a Python virtual environment. It will look something like this:

    (myprojectenv)user@host:~/myprojectdir$.

With your virtual environment active, we can now clone the project:

    git clone https://gitlab.com/mgmgl/pbn5.git

Note: Make sure you have clone access to this repository.

Once the cloning is complete, you can install the project's python requirements:

    cd pbn5
    pip install -r requirements.txt

# Migrate the Database and Test your Project

Now that the Django settings are configured, we can migrate our data structures to our database and test out the server.

Since we don't have any actual data yet, this will simply set up the initial database structure:

    python manage.py migrate

After creating the database structure, we can create an administrative account by typing:

    python manage.py createsuperuser

You will be asked to select a username, provide an email address, and choose and confirm a password for the account.

Test that your database is performing correctly by starting up the Django development server:

    python manage.py runserver 0.0.0.0:8000

In your web browser, visit your server's domain name or IP address followed by :8000 to reach default Django root page:

    http://server_domain_or_IP:8000/admin

You should see the fish-i admin page. Enter the username and password you just created using the createsuperuser command. You will then be taken to the admin interface:

When you're done investigating, you can stop the development server by hitting CTRL-C in your terminal window.

By accessing the admin interface, we have confirmed that our database has stored our user account information and that it can be appropriately accessed.

# Install Redis as a Task Queue

The project makes use of Redis as a task queue/broker. This enables the project to run smoother by scheduling and delagating the ETL processes while also maintaining the front facing database and website.
We’ll use the APT package manager to install redis from the official Ubuntu repositories. As of this writing, the version available in the default repositories is 5.0.7.

    sudo apt install redis-server

This will download and install Redis and its dependencies. Following this, there is one important configuration change to make in the Redis configuration file, which was generated automatically during the installation.

Open this file with your preferred text editor:

    sudo nano /etc/redis/redis.conf
 
Inside the file, find the supervised directive. This directive allows you to declare an init system to manage Redis as a service, providing you with more control over its operation. The supervised directive is set to no by default. Since you are running Ubuntu, which uses the systemd init system, change this to **systemd**.

**/etc/redis/redis.conf**
```
...
# If you run Redis from upstart or systemd, Redis can interact with your
# supervision tree. Options:
#   supervised no      - no supervision interaction
#   supervised upstart - signal upstart by putting Redis into SIGSTOP mode
#   supervised systemd - signal systemd by writing READY=1 to $NOTIFY_SOCKET
#   supervised auto    - detect upstart or systemd method based on
#                        UPSTART_JOB or NOTIFY_SOCKET environment variables
# Note: these supervision methods only signal "process is ready."
#       They do not enable continuous liveness pings back to your supervisor.
supervised systemd
...
```

That’s the only change you need to make to the Redis configuration file at this point, so save and close it when you are finished. If you used nano to edit the file, do so by pressing CTRL + X, Y, then ENTER.

Then, restart the Redis service to reflect the changes you made to the configuration file:

    sudo systemctl restart redis.service

With that, you’ve installed and configured Redis and it’s running on your machine. Before you begin using it, though, it’s prudent to first check whether Redis is functioning correctly.

# Optional: Create a Postgres Database and Database User

We’re going to jump right in and create a database and database user for our Django application.

Note: A postgres database is not required as Django supports SQLite by default. Set this up only if you will deploy to production or if you need a database with spacial features.

By default, Postgres uses an authentication scheme called “peer authentication” for local connections. Basically, this means that if the user’s operating system username matches a valid Postgres username, that user can login with no further authentication.

During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. We need to use this user to perform administrative tasks. We can use sudo and pass in the username with the -u option.

Log into an interactive Postgres session by typing:

    sudo -u postgres psql

You will be given a PostgreSQL prompt where we can set up our requirements.

First, create a database for your project:

    CREATE DATABASE myproject;

Note: Every Postgres statement must end with a semi-colon, so make sure that your command ends with one if you are experiencing issues.

Next, create a database user for our project. Make sure to select a secure password:

    CREATE USER myprojectuser WITH PASSWORD 'mypassword';

Afterwards, we’ll modify a few of the connection parameters for the user we just created. This will speed up database operations so that the correct values do not have to be queried and set each time a connection is established.

We are setting the default encoding to UTF-8, which Django expects. We are also setting the default transaction isolation scheme to “read committed”, which blocks reads from uncommitted transactions. Lastly, we are setting the timezone. By default, our Django projects will be set to use UTC. These are all recommendations from the Django project itself:

    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myprojectuser SET timezone TO 'UTC';

Now, we can give our new user access to administer our new database:

    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser; 

If you need your database to support spacial features. Connect to the newly created database and create a POSTGIS extension:

    \connect myproject;
    CREATE EXTENSION postgis;

When you are finished, exit out of the PostgreSQL prompt by typing:

    \q

# Optional: Configure the Django Database Settings to use Postgres

    TO FOLLOW
