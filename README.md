Play the game in the command line.

From the root directory, run `python main.py`. 

You'll then receive instructions on what to do. For example:

```
C:\Repos\Mastermind>python main.py
Code length (0-9): 4
Numeric (1) or verbal (2)? 2
Code set.
You can now try and guess the code. You will receive feedback on your answers:

     2 : a char in your guess matches the value and location of a char in the code.
     1 : a char matches the value of a char somewhere else
     0 : a char in your guess is incorrect in terms of location and value.

12 guesses
Enter the code (xxxx): warg
2 0 0 0
12 guesses left

Enter the code (xxxx): word
2 0 0 0
11 guesses left
```

Enjoy!
