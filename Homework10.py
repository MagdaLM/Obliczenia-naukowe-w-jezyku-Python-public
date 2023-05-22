print ("EXERCISE 10.1")
a = """
C:\\WINDOWS\\system32>cd C:\\Users\Magda\\Desktop\\EXERCISE_10

C:\\Users\\Magda\\Desktop\\EXERCISE_10>python3 -m venv exercise_10

C:\\Users\\Magda\\Desktop\\EXERCISE_10>exercise_10\\Scripts\\activate.bat

(exercise_10) C:\\Users\\Magda\\Desktop\\EXERCISE_10>pip install numpy
Collecting numpy
  Using cached numpy-1.24.3-cp311-cp311-win_amd64.whl (14.8 MB)
Installing collected packages: numpy
Successfully installed numpy-1.24.3

[notice] A new release of pip available: 22.3.1 -> 23.1.2
[notice] To update, run: python3.exe -m pip install --upgrade pip

(exercise_10) C:\\Users\\Magda\\Desktop\\EXERCISE_10>pip install matplotlib
Collecting matplotlib
  Using cached matplotlib-3.7.1-cp311-cp311-win_amd64.whl (7.6 MB)
Collecting contourpy>=1.0.1
  Using cached contourpy-1.0.7-cp311-cp311-win_amd64.whl (162 kB)
Collecting cycler>=0.10
  Using cached cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting fonttools>=4.22.0
  Using cached fonttools-4.39.4-py3-none-any.whl (1.0 MB)
Collecting kiwisolver>=1.0.1
  Using cached kiwisolver-1.4.4-cp311-cp311-win_amd64.whl (55 kB)
Requirement already satisfied: numpy>=1.20 in c:\\users\\magda\\desktop\\exercise_10\\exercise_10\lib\site-packages (from matplotlib) (1.24.3)
Collecting packaging>=20.0
  Using cached packaging-23.1-py3-none-any.whl (48 kB)
Collecting pillow>=6.2.0
  Using cached Pillow-9.5.0-cp311-cp311-win_amd64.whl (2.5 MB)
Collecting pyparsing>=2.3.1
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
Collecting python-dateutil>=2.7
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pyparsing, pillow, packaging, kiwisolver, fonttools, cycler, contourpy, python-dateutil, matplotlib
Successfully installed contourpy-1.0.7 cycler-0.11.0 fonttools-4.39.4 kiwisolver-1.4.4 matplotlib-3.7.1 packaging-23.1 pillow-9.5.0 pyparsing-3.0.9 python-dateutil-2.8.2 six-1.16.0

[notice] A new release of pip available: 22.3.1 -> 23.1.2
[notice] To update, run: python3.exe -m pip install --upgrade pip

(exercise_10) C:\\Users\\Magda\\Desktop\\EXERCISE_10>pip install pandas
Collecting pandas
  Downloading pandas-2.0.1-cp311-cp311-win_amd64.whl (10.6 MB)
     ---------------------------------------- 10.6/10.6 MB 1.9 MB/s eta 0:00:00
Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\magda\\desktop\\exercise_10\\exercise_10\\lib\\site-packages (from pandas) (2.8.2)
Collecting pytz>=2020.1
  Downloading pytz-2023.3-py2.py3-none-any.whl (502 kB)
     ---------------------------------------- 502.3/502.3 kB 2.1 MB/s eta 0:00:00
Collecting tzdata>=2022.1
  Downloading tzdata-2023.3-py2.py3-none-any.whl (341 kB)
     ---------------------------------------- 341.8/341.8 kB 1.9 MB/s eta 0:00:00
Requirement already satisfied: numpy>=1.21.0 in c:\\users\\magda\\desktop\\exercise_10\\exercise_10\\lib\\site-packages (from pandas) (1.24.3)
Requirement already satisfied: six>=1.5 in c:\\users\\magda\\desktop\\exercise_10\\exercise_10\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
Installing collected packages: pytz, tzdata, pandas
Successfully installed pandas-2.0.1 pytz-2023.3 tzdata-2023.3

[notice] A new release of pip available: 22.3.1 -> 23.1.2
[notice] To update, run: python3.exe -m pip install --upgrade pip

(exercise_10) C:\\Users\\Magda\\Desktop\\EXERCISE_10>
"""
print (a)

print ("EXERCISE 10.2")
import pandas
import datetime
import random

start_may = datetime.datetime(2023, 5, 1)
end_may = datetime.datetime(2023, 5, 31)

index = pandas.date_range(start=start_may, end=end_may, freq="D").strftime("%d-%m-%Y")

may = [random.uniform(4.49, 4.60) for _ in range(len(index))]

series = pandas.Series(may, index=index)

print("Kurs euro w maju:")
print(series)

print ("EXERCISE 10.3")
import pandas

data = [
    ('Hydrogen', 'H', 1.008),
    ('Helium', 'He', 4.0026),
    ('Lithium', 'Li', 6.94),
    ('Beryllium', 'Be', 9.0122),
    ('Boron', 'B', 10.81),
    ('Carbon', 'C', 12.01),
    ('Nitrogen', 'N', 14.01),
    ('Oxygen', 'O', 16.00),
    ('Fluorine', 'F', 19.00),
    ('Neon', 'Ne', 20.18)
]

table = pandas.DataFrame(data, index=range(1, len(data) + 1), columns=['Name', 'Symbol', 'Weight'])

print(table)


