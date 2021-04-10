import physical_fitness_regime
import unittest


def get_valid_request():
    return {
        'deadlift': 100,
        'squat': 100,
        'overhead_press': 100,
        'bench_press': 100
    }


class PhysicalFitnessTests(unittest.TestCase):
    def test_weeks_exist(self):
        request = get_valid_request()
        output = physical_fitness_regime.make_month_workout(request)
        self.assertTrue('week-1' in output)
        self.assertTrue('week-2' in output)
        self.assertTrue('week-3' in output)
        self.assertTrue('week-4' in output)

    def test_days_exist(self):
        request = get_valid_request()
        output = physical_fitness_regime.make_month_workout(request)
        # first week
        self.assertTrue('sunday' in output['week-1'])
        self.assertTrue('monday' in output['week-1'])
        self.assertTrue('wednesday' in output['week-1'])
        self.assertTrue('friday' in output['week-1'])
        # second week
        self.assertTrue('sunday' in output['week-2'])
        self.assertTrue('monday' in output['week-2'])
        self.assertTrue('wednesday' in output['week-2'])
        self.assertTrue('friday' in output['week-2'])
        # third week
        self.assertTrue('sunday' in output['week-3'])
        self.assertTrue('monday' in output['week-3'])
        self.assertTrue('wednesday' in output['week-3'])
        self.assertTrue('friday' in output['week-3'])
        # fourth week
        self.assertTrue('sunday' in output['week-4'])
        self.assertTrue('monday' in output['week-4'])
        self.assertTrue('wednesday' in output['week-4'])
        self.assertTrue('friday' in output['week-4'])

    def test_has_core_and_accessory_workouts(self):
        request = get_valid_request()
        output = physical_fitness_regime.make_month_workout(request)
        workout_days = ['sunday', 'monday', 'wednesday', 'friday']
        for week_num in range(1, 5):
            week = 'week-' + str(week_num)
            for day in workout_days:
                self.assertTrue('core' in output[week][day])
                self.assertTrue('accessory' in output[week][day])

    def test_number_of_workouts_in_core_and_accessory(self):
        request = get_valid_request()
        output = physical_fitness_regime.make_month_workout(request)
        workout_days = ['sunday', 'monday', 'wednesday', 'friday']
        for week_num in range(1, 5):
            week = 'week-' + str(week_num)
            for day in workout_days:
                self.assertEqual(2, len(output[week][day]['core']))
                self.assertEqual(3, len(output[week][day]['accessory']))

    def test_number_of_sets_in_core(self):
        request = get_valid_request()
        output = physical_fitness_regime.make_month_workout(request)
        workout_days = ['sunday', 'monday', 'wednesday', 'friday']
        for week_num in range(1, 5):
            week = 'week-' + str(week_num)
            for day in workout_days:
                for workout_name in output[week][day]['core']:
                    workout = output[week][day]['core'][workout_name]
                    self.assertTrue(len(workout) == 5 or len(workout) == 6)
