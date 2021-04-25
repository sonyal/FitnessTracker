# Fitness Tracker

## Table of Contents
* [Description](#description)
* [Frontend](#frontend)
* [Backend](#backend)
* [Team Contributions](#team-contributions)

## Description
Fitness Tracker is a website to help generate a workout regime. Currently users are able to generate a workout through downloading the repository and following the instructions below.

## Frontend 

## Downloading the app
- Ensure git is installed on machine 
- Open your terminal and ensure git is running (if a PATH variable is set up, this would simply require entering the command "git") 
- Step into the directory in which you wish to save the code repo (app project/files)
- Retrieve the code by entering the command `git clone git@cmsc435.garrettvanhoy.com:adamag/fitness-tracker.git`
- The project will now sit in the `fitness-tracker` folder within the directory you are in currently

## Running the app using Docker (recommended)
- Ensure Docker is installed on your machine. Docker can be installed [here](https://docs.docker.com/get-docker/)
- Make sure the docker machine is running on your local machine
    - On MacOS, that can be done by using [Docker Desktop](https://docs.docker.com/docker-for-mac/install/) or by executing the following:
    - `docker-machine start` - Start virtual machine for docker
    - `docker-machine env` - It's helps to get environment variables
    - `eval "$(docker-machine env default)"` - Set environment variables
- Build the docker container using `docker build -t fitness-tracker .`
- Run the docker container using `docker run -p 5000:5000 fitness-tracker`
- On your browser, the website is now running on `http://0.0.0.0:5000/` or accessible [here](http://0.0.0.0:5000/)

### Troubleshooting Common Errors
- `Cannot connect to Docker daemon at ...` likely means you don't have the docker machine running
- Fixes for Linux and MacOS can be found [here](https://stackoverflow.com/questions/21871479/docker-cant-connect-to-docker-daemon)
- Fixing issue on Windows can be done through proper installation of docker [here](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)

## Running the app locally
- Ensure python3 is installed on your machine
- Install the required packages using `pip3 install -r requirements.txt`
- To run the app, run `python3 frontend/app.py`
- On your browser, the website is now running on `http://0.0.0.0:5000` or accessible [here](http://0.0.0.0:5000/)

### Home Page
- The homepage has a navigation bar that links to the Tutorial Search and Login pages. The app's name and logo are also buttons that link back to/refresh the homepage
- A jumbotron displays the basic purpose of the site and a button that leads to the Signup page
- 3 tile cards along bottom of homepage include more detailed information about the app and the team behind it. Below each description is a link to read more. These links do not redirect the user to another page, but rather opens modals that popover the homepage to provide more information on each card

### Tutorial Search Page
- The Tutorial Search Page has a navigation bar at the top which can go to the home page or back to the tutorial search page
- It also has a search bar. The search bar currently only searches Flexibility, Cardiovascular, and Strength. When a user searches for these words
it goes to the following page with the tutorial.
- signup button leads to a signup page 
-If a user fails to do a proper search, A notifications appears at the top that it is an invalid search.
- In the next Sprint:
     - Add many more possible searches
     - Make Page look more presentable to the user
     - Link to specific workouts if Searched

### Login Page
- allows users to login in by comparing input information to the database
- The system now will remember the user as long as the browser is on
- Flask message when login information is wrong
- Some pages are now requierd to be loged in to view

### Signup Page
- The signup page requires users to enter their username and password information (some other information is added)
- User information will be stored
- The password will be encrypted

### User page
- When user is loged in user can acess to the user page by the left up icon or the profile button in the home page
- This page will display the user information
- User is able to modify some of their information here

### Tutorial Page
- There's a search bar that allows the user (theoretically) to search specific workouts or workout categories such as Cardiovascular, Flexibility, and Strength.
- Searching for a specific exercise will open a new page where categories live in and will display a list of other similar exercises.
- Searching for a category will bring the user to a new page where the searched category is, displaying a list of popular exercises in that category.
- In the next Sprint:
     - YouTube videos for each exercise will either be embedded or linked to provide the user with a demonstration.
     - Style formatting for page will be added

### Flexibility workout page
- The user needs to enter their capability of certain exercises, in order to get a plan designed for him/her. 
- The exercises/workout generated includes:
   - upper body : triceps stretch, Neck-and-Shoulder Release. 
   - Lower body: sit and reach, up and over
- In the next Sprint:
   - complete flexibility workout input proxy
   - improve style, content and formatting of flexibility workout tutorial page. 

## database
- Stores all the information for this web

## Backend

### Creating a workout
- Requires python3, which can be installed via [python's webpage](https://www.python.org/downloads/) or [using homebrew](https://docs.python-guide.org/starting/install3/osx/)
- In terminal, ensure directory is set to `fitness-tracker`
- Run command `python3 backend/physical_fitness_proxy.py --overhead_press OVERHEAD_PRESS --bench_press BENCH_PRESS --squat SQUAT --deadlift DEADLIFT`
     - To see usage and help run `python3 backend/physical_fitness_proxy.py -h`
     - Example of valid input `python3 backend/physical_fitness_proxy.py --overhead_press 100 --bench_press 145 --squat 225 --deadlift 285`
     - Each parameter should be passed in as an integer representing your maximum weight on one repetition for the associated workout
- Will display a JSON object of the generated workout given your strength

### Workout Proxy
- Utilizes `argsparse` to required valid inputs
- Invalid inputs will stop execution and print out help and proper usage
- Example output of invalid arguments to workout proxy:
```
usage: physical_fitness_proxy.py [-h] --overhead_press OVERHEAD_PRESS --bench_press BENCH_PRESS --squat SQUAT --deadlift DEADLIFT
physical_fitness_proxy.py: error: the following arguments are required: --bench_press, --squat, --deadlift
```

### Searching within the Tutorial page
- In terminal, ensure directory is set to `fitness-tracker`
- Run command `python3 backend/app.py`

#Important for Coverage testing
- From our code design, we can't have coverage tested normally and our app to run
- To test backend coverage, first ensure the directory is set to `backend`
- this can be done by typing `cd backend` from the `fitness-tracker` folder in the terminal
- Run the command `coverage run -m unittest discover` 
- Run the command `coverage report`
- type `cd ..` to return to your home menu
- For testing frontend coverage
- this can be done by typing `cd frontend` from the `fitness-tracker` folder in the terminal
- Run the command `coverage run -m unittest discover` 
- Run the command `coverage report`
## Backend Tests
- Requires unittests, which can be installed using `pip install unittest`
- In terminal, ensure directory is set to `backend`
- Run the command `python -m unittest discover`

### Frontend Tests
- Requires unittests, which can be installed using `pip install unittest`
- In terminal, ensure directory is set to `fitness-tracker/frontend`
- Run the command `python -m unittest discover`


## Team-Contributions

### Adam Aguilera
- Sprint 2:
    - Integrated docker for running the application
    - Added a requirements.txt to make installing packages easier for local execution / docker
    - Added new testing for the proxy and increased test coverage
    - Updated README to include docker installation and running
- Sprint 1:
    - Added workout regime generation based on user input, calculates proper workout weight and repetition based on passed parameters
    - Added tests to validate input for workout parameters
    - Added continuous integration for the backed , running tests automatically when a merge is created
    - Added a proxy that validates input for workout regime returning helper output for incorrect inputs

### Gaurav Arora
- Created the Baseline Flask application that everyone merged with.
- Edited the home page and tutorial html pages to work with flask
- Created the tutorial Search html pages
- added basic navigation bar to tutorial and tutorial search pages
- Created the Tutorial search bar with its functionality 
- Added a proxy that validates the input for the search bar
- Created 4 tests to test for the input functionality
- Sprint 2
- Made test for frontend such as test_app
- Created Cardio workout code for backend
- Created Html files for the cardio schedule
- Modified app.py to include cardio workout
 
### John Blanco
- Static webpages for exercise Tutorials
- Merging with Tutorial search functionality
- README documentation writing, reviewing, and editing.

### Sonya Lew
- Designed homepage
- Created all graphics used
- Wrote part of frontend documentation 

### Roger Luo
Spint 1
- Login page
- modified sign up page so now it really creates an new user
- database to store the user information
Sprint 2
- Add functionality for login page
- Merged sign up page and workout page, stored all the information when a new user is created
- Updated database
- Created User page which display the user information which stored in the databse
- Format a little bit login, sign up and profile page makes them looks a little prettier


### Yifan Qin
- Sprint 1 
  - Workout page design
  - Sign up page design
  - Merging & link signup and home pages 
  - README editing
- Sprint 2 
  - Flexibility input page design (html files), as well as input proxy
  - implement flexibility workout plan generation algorithm and webpage
  - edit README about flexibility workout documentation
