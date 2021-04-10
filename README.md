# Fitness Tracker

## Frontend

### Tutorial Page
- There's a search bar that allows the user (theoretically) to search specific workouts or workout categories such as Cardiovascular, Flexibility, and Strength.
- Searching for a specific exercise will open a new page where categories live in and will display a list of other similar exercises.
- Searching for a category will bring the user to a new page where the searched category is, displaying a list of popular exercises in that category.
- In the next Sprint, YouTube videos for each exercise will either be embedded or linked to provide the user with a demonstration.

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
