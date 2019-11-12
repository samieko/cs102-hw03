# cs102-hw03
Write a program that computes the means of lists of numbers.
The input will be a file containing one or more rows, where each row is a list of numbers.
Your program should print the mean of the numbers in each row.
The name of the input file should be passed as argv[1].

For example, if these are the contents of `example_input.csv`:
```
1,2,3
0.5,1,1.5,1
0
```

and you run your program with the following command:
```
python main.py example_input.csv
```

it should print:
```
Processing input file: example_input.csv
2.0
1.0
0.0
```

Make sure that your program works if you pass a different input file path!
Once your program works on `example_input.csv`, try making your own input file and passing that to your Python program.

If you are using PyCharm to run your program, you can add command line arguments by going to the Run menu and selecting "Edit Configurations".
Put the path to your input csv in the "Parameters" box, then click "OK".
Now when PyCharm runs your program, it will pass your custom parameter as a command line argument.
For more details and pictures, see the [PyCharm documentation](https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html).
