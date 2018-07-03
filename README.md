# elasticLogger
Simple django project sends logs to Elastic search using Logstash.
It simply is an API to add/update/delete/list code snippets. It sends logs to Elastic search.

## Programming Language and Libraries

* python 2.

* django.

* django rest framework.

* python-logstash.


## Prerequisites

What things you need to install the software and how to install them on Linux os.

* **docker** [how to install](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

* **docker-compose** [how to install](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04)

* **pip** python package manager

```
sudo apt-get install python-pip
```

* **virtual env**

```
sudo pip install virtualenv
```

## Installing


A step by step series of examples that tell you how to get a development env running

* **Clone the project.**

* **Run this command inside project directory**

```
virtualenv env
```

* **Activate the env and install the requirements**

```
source env/bin/activate

pip install -r requirements.txt
```

* **Start the server**

```
python elasticLogger/manage.py runserver
```

* **Open another terminal and Run**

```
docker-compose up
```


