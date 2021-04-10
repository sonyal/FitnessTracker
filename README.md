# Fitness Tracker

## Downloading the app
- Ensure git is installed on machine 
- Open your terminal and ensure git is running (if a PATH variable is set up, this would simply require entering the command "git") 
- Step into the directory in which you wish to save the code repo (app project/files)
- Retrieve the code by entering the command "git clone git@cmsc435.garrettvanhoy.com:adamag/fitness-tracker.git"
- The project will now sit in the 'fitness-tracker' folder within the directory you are in currently
  
## Running the app
- 

## Frontend
### Home Page
- The homepage has a navigation bar that links to the Tutorial Search and Login pages. The app's name and logo are also buttons that link back to/refresh the homepage
- A jumbotron displays the basic purpose of the site and a button that leads to the Signup page
- 3 tile cards along bottom of homepage include more detailed information about the app and the team behind it. Below each description is a link to read more. These links do not redirect the user to another page, but rather opens modals that popover the homepage to provide more information on each card

### Tutorial Search Page
- 
- Style formatting for page will be added in next sprint
  

### Login Page
- 
- Style formatting for page will be added in next sprint

### Signup Page
- 
- Style formatting for page will be added in next sprint

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
