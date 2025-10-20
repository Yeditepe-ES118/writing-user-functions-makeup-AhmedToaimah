import sys
from pathlib import Path
import pytest
import numpy as np

parent_dir = str(Path(__file__).parent.parent)  # Adjust based on your structure
print(parent_dir)
sys.path.insert(0, parent_dir)

from lab4 import throw_rock

def test_throw_rock(capsys):
    args1 = (1.5, 0.3, 35.20)
    args2 = (2.5, 1.4, 50.00)
    args3 = (1.75, 0.7, 10.15)

    args = [args1, args2, args3]
    results = ["""For a rock with 1.500 kg mass thrown with 0.300 m/s at an angle of  35.20 degrees:
Time of flight is    3.5e-02 s
The range in x-direction is    8.6e-03 m
Maximum height is    1.5e-03 m
The speed at maximum height is    2.5e-01 m/s
Kinetic energy at the maximum height is 4.27e-07 J
""",
        """For a rock with 2.500 kg mass thrown with 1.400 m/s at an angle of  50.00 degrees:
Time of flight is    2.2e-01 s
The range in x-direction is    2.0e-01 m
Maximum height is    5.9e-02 m
The speed at maximum height is    9.0e-01 m/s
Kinetic energy at the maximum height is 3.87e-03 J
""",
        """For a rock with 1.750 kg mass thrown with 0.700 m/s at an angle of  10.15 degrees:
Time of flight is    2.5e-02 s
The range in x-direction is    1.7e-02 m
Maximum height is    7.8e-04 m
The speed at maximum height is    6.9e-01 m/s
Kinetic energy at the maximum height is 3.63e-07 J
"""
    ]

    for i in range(3):
        throw_rock(args[i][0], args[i][1], args[i][2])
        captured = capsys.readouterr()
        
        assert captured.out == results[i]

"""
@pytest.fixture
def get_results():
    num_arr = np.loadtxt("tests/num_arr.csv", delimiter=",")
    return num_arr

def test_values_arr(get_results):
    num_arr = get_results
    num_arr = np.int64(num_arr)
    
    for i in num_arr:
        test_a = np.int64(np.loadtxt("tests/test_a"+str(i)+".csv", delimiter=","))
        test_b = np.int64(np.loadtxt("tests/test_b"+str(i)+".csv", delimiter=","))
        true_res = np.int64(np.loadtxt("tests/true_res"+str(i)+".csv", delimiter=","))
        res = find_circumference(test_a, test_b)

        assert res.all() == true_res.all()
"""
