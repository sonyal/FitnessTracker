# Fitness Tracker

## Frontend

## Backend

### Creating a workout
- In terminal, change directory to `fitness-tracker`
- Run command `python3 backend/physical_fitness_proxy.py --overhead_press OVERHEAD_PRESS --bench_press BENCH_PRESS --squat SQUAT --deadlift DEADLIFT`
     - To see usage and help run `python3 backend/physical_fitness_proxy.py -h`
     - Example of valid input `python3 backend/physical_fitness_proxy.py --overhead_press 100 --bench_press 145 --squat 225 --deadlift 285`
     - Each parameter should be passed in an integer representing your maximum weight on one repetition for the associated workout
- Will display a JSON object of the generated workout given your strength

### Workout Proxy
- Utilizes `argsparse` to required valid inputs
- Invalid inputs will stop execution and print out help and proper usage

### Backend Tests
- Open PyCharm
- Open the `physical_fitness_regime_tests.py` file
- Click run tests on class `PhysicalFitnessTests`
