import unittest
import os


class PhysicalFitnessProxyTests(unittest.TestCase):
    def test_valid_args(self):
        valid_request = 'python physical_fitness_proxy.py --overhead_press 100 --bench_press 145 ' + \
                        '--squat 225 --deadlift 285'
        # perform request, saving result into text file
        os.system(valid_request + ' > test_proxy_valid_args.txt')
        # make sure text file exists
        self.assertTrue(os.path.exists('test_proxy_valid_args.txt'))
        # read the text file
        fp = open('test_proxy_valid_args.txt', 'r')
        output = fp.read()
        fp.close()
        # remove the test file
        os.remove('test_proxy_valid_args.txt')
        self.assertTrue('week-1' in output)
        self.assertTrue('week-2' in output)
        self.assertTrue('week-3' in output)
        self.assertTrue('week-4' in output)
