# ReviewGram - backend
Repo for backend of reviewgram - a full stack webAPI for finding reviews and ratings of TV shows and movies, and keep your own watchlists
 
## Feature Set

We connected our back-end to TMDB API which gave us all the tvshows and movie information. For the front-end to work we created the following endpoints:

 - User Routes
	 - CRUD routes for user
	 - Get reviews from user
	 - Add review to Media
	 - Add to user watchlist
	 - Add to user watched list
	 - Get user watchlist
	 - Get user watched list
	 
 - Media Routes
	 - Get Img url (TMDB api requires to look up for the images in different serves regularly)
	 - Search media
	 - Get trending tv shows
	 - Get trending movies
	 - Get movie details
	 - Get show details
	 - Get reviews for tv show
	 - Get reviews for movie
	   
 - Authorization Routes
	 - Get authorization Token

## Endpoints Definition table
To see a more detailed definition of each endpoint you can consult this document [Endpoints Definition](/docs/endpoints.md)

## Technology used
This back-end has been entirely programmed in ***Python***, using ***flask*** and ***SQLAlchemy***. The database used is ***Postgres***.

## Configuration and installation for local running

ReviewGram needs python 3 installed to function. Afterwards:

1. Create a virtual environment for python

	### MacOS
   
	```bash
	python3 -m venv venv
	```
 
	### Windows

	```powershell
	python -m venv c:\path\to\myenv
	```

2. Activate the virtual environment
   
	### MacOS
   
	```bash
	source venv/bin/activate
	```
 
	### Windows

	```powershell
	/venv/Scripts/Activate.ps1
	```


4. Install dependencies
	### MacOS and Windows
   
	```bash
	pip install -r requirements.txt
	```

 5. Install postgreSQL
    
 7. Create postgreSQL databases for prod and test
    
 8. Obtain a TMDB API key and bearer token here: [TMDB API](https://developer.themoviedb.org/reference/intro/getting-started)
    
 9. Create a local env file with this variables:

    ```
    FLASK_DEBUG = True / False
    JWT_SECRET_KEY = the secret key for generating connecting tokens
    SQLALCHEMY_DATABASE_URI = the uri of the prod database
    SQLALCHEMY_TEST_DATABASE_URI = the uri for the testing database
    TMDB_API_KEY = key for using TMDB
    TMDB_BEARER_TOKEN = bearer token for using TMDB
    ```
    	

## Running

1. To run the app locally you need to first run the migrations that will create the table for the database. Therefore, while running the virtual environment you need to execute this commands:

	```bash
	flask db init
	```
	
	```bash
	flask db migrate -m "<custom message>"
	```
	
	```bash
	flask db upgrade
	```
 
 2. To finally run the application
    
	```bash
	flask run
	```

	This command will run the API in debug mode depending on the value of the FLASK_DEBUG variable on the env file
    
