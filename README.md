# Fitness Tracker

## Downloading the app
- Ensure git is installed on machine 
- Open your terminal and ensure git is running (if a PATH variable is set up, this would simply require entering the command "git") 
- Step into the directory in which you wish to save the code repo (app project/files)
- Retrieve the code by entering the command `git clone git@cmsc435.garrettvanhoy.com:adamag/fitness-tracker.git`
- The project will now sit in the `fitness-tracker` folder within the directory you are in currently
  
## Running the app
- Ensure Pycharm is installed on your machine. Pycharm can be installed [here](https://www.jetbrains.com/pycharm/download/)
- Also ensure python3 is installed. [here](https://www.python.org/downloads/)
- Open this folder inside Pycharm. This is used by doing File then Open.
- In the terminal inside Pycharm do `pip install -U WTForms`
- In the terminal inside Pycharm do `pip install -U Flask`
- In the terminal inside Pycharm do `pip install wtforms-validators`
- In the terminal inside Pycharm do `pip install Flask-WTF`
- After you have done the following instalations, you can run our app on your computer
- In your terminal go to the `frontend` directory. You can type `cd frontend` in your Pycharm terminal if you are already in `fitness-tracker` folder.
- To run our app, Type `python app.py`
- Go to the website in the terminal. It should be a link such as `http://127.0.0.1:5000/`. This may not be the exact link.


## Frontend
### Home Page
- The homepage has a navigation bar that links to the Tutorial Search and Login pages. The app's name and logo are also buttons that link back to/refresh the homepage
- A jumbotron displays the basic purpose of the site and a button that leads to the Signup page
- 3 tile cards along bottom of homepage include more detailed information about the app and the team behind it. Below each description is a link to read more. These links do not redirect the user to another page, but rather opens modals that popover the homepage to provide more information on each card

### Tutorial Search Page
- The Tutorial Search Page has a navigation bar at the top which can go to the home page or back to the tutorial search page
- It also has a search bar. The search bar currently only searches Flexibility, Cardiovascular, and Strength. When a user searches for these words
it goes to the following page with the tutorial.
- signup button leads to a signup page 
-If a user fails to do a proper search, A notifcations appears at the top that it is an invalid search.
- In the next Sprint:
     - Add many more possible searches
     - Make Page look more presentable to the user
     - Link to Spesific workouts if Searched

### Login Page
- 
- Style formatting for page will be added in next sprint

### Signup Page
- The signup page requires users to enter their username and password information 
- Style formatting for page will be added in next sprint
- navigation bar to workout page
- In the next sprint 
     - Be able to store user information 
     - validating user information 
     - proxy for invalid inputs

### Workout Page
- The workout page requires users to enter their pyhsical information, (weight, height)
- navigation bar to signup page 
- Style formatting for page will be added in next sprint
- In the next sprint 
     - provide a plan based on user's physical condition

### Tutorial Page
- There's a search bar that allows the user (theoretically) to search specific workouts or workout categories such as Cardiovascular, Flexibility, and Strength.
- Searching for a specific exercise will open a new page where categories live in and will display a list of other similar exercises.
- Searching for a category will bring the user to a new page where the searched category is, displaying a list of popular exercises in that category.
- In the next Sprint:
     - YouTube videos for each exercise will either be embedded or linked to provide the user with a demonstration.
     - Style formatting for page will be added

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


### Backend Tests
- Requires pytest, which can be installed using `pip install -U pytest`
- In terminal, ensure directory is set to `fitness-tracker`
- Run the command `pytest backend/tests/physical_fitness_regime_tests.py`

## Team Contributions

### Adam Aguilera
- Added workout regime generation based on user input, calculates proper workout weight and repetition based on passed parameters
- Added tests to validate input for workout parameters
- Added continuous integration for the backed , running tests automatically when a merge is created
- Added a proxy that validates input for workout regime returning helper output for incorrect inputs

### Gaurav Arora
- Designed tutorial webpage
- Wrote search functionality
- Added testing for searching in the search bar
 
### John Blanco
- Static webpages for exercise Tutorials
- Merging with Tutorial search functionality
- README documentation writing, reviewing, and editing.

### Sonya Lew
- Designed homepage
- Created all graphics used
- Wrote part of frontend documentation 

### Roger Luo

### Yifan Qin
- Workout page design
- Sign up page design
- Merging & link signup and home pages 
- README editing
- 