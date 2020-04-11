ref: https://techacademy.jp/magazine/26403

## app
app name: heroku-postgres-flask-simple
url: https://heroku-postgres-flask-simple.herokuapp.com/
git: https://git.heroku.com/heroku-postgres-flask-simple.git

- check
	- curl(local): curl localhost:5002/myapi -d "arg01=hello_flask"
	- curl(web)  : curl https://heroku-postgres-simple.herokuapp.com/myapi -d "arg01=hello_flask"

- postgres
	- connect: heroku pg:psql -a heroku-postgres-flask-simple

- database info: https://data.heroku.com/datastores/d008e05d-6956-4367-ae79-e13dd77eb0da#administration
