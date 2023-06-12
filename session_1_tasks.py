{
  "cells": [
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "A05OG15VqOPF"
      },
      "source": [
        "# Task : Session 1\n",
        "Solve these questions own your own and try to test yourself what you have learned in the session.\n",
        "\n",
        "Happy Learning!"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "2doIXf8bqe9_"
      },
      "source": [
        "### Q1 :- Print the given strings as per stated format.\n",
        "\n",
        "**Given strings**: \n",
        "```\n",
        "\"Data\" \"Science\" \"Mentorship\" \"Program\" \n",
        "\"By\" \"CampusX\"\n",
        "```\n",
        "**Output**: \n",
        "``` \n",
        "Data-Science-Mentorship-Program-started-By-CampusX\n",
        "```\n",
        "\n",
        "Concept- [Seperator and End]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "-em6d3KErDtp"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Data-Science-Mentorship-Program-By-CampusX\n"
          ]
        }
      ],
      "source": [
        "# Write your code here\n",
        "print(\"Data\", \"Science\", \"Mentorship\", \"Program\",\"By\", \"CampusX\", sep='-')"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "1KUpN7ZTrC3_"
      },
      "source": [
        "### Q2:- Write a program that will convert celsius value to fahrenheit."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "yxKYhYQiqWfj"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "109.4\n"
          ]
        }
      ],
      "source": [
        "# Write your code here\n",
        "celsius = int(input(\"Enter degree celsius to be converted to fahrenheight: \" ))\n",
        "fahrenheight = (celsius * 9/5) + 32\n",
        "print(fahrenheight)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "RLrOBBJurLB2"
      },
      "source": [
        "### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "yPn7if0TrJ4F"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "6 4\n"
          ]
        }
      ],
      "source": [
        "# Write your code here\n",
        "x = int(input(\"Enter the value of x: \"))\n",
        "y = int(input(\"Enter the value of y: \"))\n",
        "x, y = y, x\n",
        "print(x, y)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "waLCP1bjr7ML"
      },
      "source": [
        "### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {},
      "outputs": [
        {
          "data": {
            "text/plain": [
              "8"
            ]
          },
          "execution_count": 10,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "2**3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "Pl1Sv-xnrxnH"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Euclidian distance between two points is:  {2.23606797749979}\n"
          ]
        }
      ],
      "source": [
        "# Write your code here\n",
        "import math\n",
        "x1 = int(input(\"Enter x1: \"))\n",
        "y1 = int(input(\"Enter y1: \"))\n",
        "x2 = int(input(\"Enter x2: \"))\n",
        "y2 = int(input(\"Enter y2: \"))\n",
        "euclidean_distance = math.sqrt((x2-x1)**2 - (y2-y1)**2)\n",
        "print(\"Euclidian distance between two points is: \", {euclidean_distance})"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "VLrhg-FRsHjR"
      },
      "source": [
        "### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "s40DlReZsTmY"
      },
      "outputs": [],
      "source": [
        "# Write your code here\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "LMy0BTUktYKa"
      },
      "source": [
        "### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.\n",
        "\n",
        "For example:\n",
        "Input:\n",
        "heads -> 4\n",
        "legs -> 12\n",
        "<br>\n",
        "Output:\n",
        "dogs -> 2\n",
        "chicken -> 2\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "id": "XSBvJoA4tXaG"
      },
      "outputs": [
        {
          "ename": "ValueError",
          "evalue": "invalid literal for int() with base 10: 'num_chicken'",
          "output_type": "error",
          "traceback": [
            "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[1;32mc:\\Users\\Sonu Kumar Sony\\Downloads\\session_1_tasks.ipynb Cell 14\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/Sonu%20Kumar%20Sony/Downloads/session_1_tasks.ipynb#X15sZmlsZQ%3D%3D?line=1'>2</a>\u001b[0m heads \u001b[39m=\u001b[39m \u001b[39mint\u001b[39m(\u001b[39minput\u001b[39m(\u001b[39m\"\u001b[39m\u001b[39mEnter number of heads: \u001b[39m\u001b[39m\"\u001b[39m ))\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/Sonu%20Kumar%20Sony/Downloads/session_1_tasks.ipynb#X15sZmlsZQ%3D%3D?line=2'>3</a>\u001b[0m legs \u001b[39m=\u001b[39m \u001b[39mint\u001b[39m(\u001b[39minput\u001b[39m(\u001b[39m\"\u001b[39m\u001b[39mEnter number of legs: \u001b[39m\u001b[39m\"\u001b[39m ))\n\u001b[1;32m----> <a href='vscode-notebook-cell:/c%3A/Users/Sonu%20Kumar%20Sony/Downloads/session_1_tasks.ipynb#X15sZmlsZQ%3D%3D?line=3'>4</a>\u001b[0m a \u001b[39m=\u001b[39m \u001b[39mint\u001b[39;49m(\u001b[39m'\u001b[39;49m\u001b[39mnum_chicken\u001b[39;49m\u001b[39m'\u001b[39;49m)\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/Sonu%20Kumar%20Sony/Downloads/session_1_tasks.ipynb#X15sZmlsZQ%3D%3D?line=4'>5</a>\u001b[0m b \u001b[39m=\u001b[39m \u001b[39mint\u001b[39m(\u001b[39m'\u001b[39m\u001b[39mnum_dogs\u001b[39m\u001b[39m'\u001b[39m)\n\u001b[0;32m      <a href='vscode-notebook-cell:/c%3A/Users/Sonu%20Kumar%20Sony/Downloads/session_1_tasks.ipynb#X15sZmlsZQ%3D%3D?line=5'>6</a>\u001b[0m heads \u001b[39m=\u001b[39m a \u001b[39m+\u001b[39m b\n",
            "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: 'num_chicken'"
          ]
        }
      ],
      "source": [
        "# Write your code here\n",
        "heads = int(input(\"Enter number of heads: \" ))\n",
        "legs = int(input(\"Enter number of legs: \" ))\n",
        "\n",
        "heads = a + b\n",
        "legs = a * 2 + b * 4\n",
        "\n",
        "print(a)\n"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "gJ7C5kZYt4BP"
      },
      "source": [
        "### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "_tHsmEHzt2nX"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "385.0\n"
          ]
        }
      ],
      "source": [
        "# Write your code here\n",
        "n = int(input('Enter the nutural number: '))\n",
        "sum_square_first_natural_num = (n*(n+1)*(2*n+1))/6\n",
        "print(sum_square_first_natural_num)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "FHrMM7g-yG1h"
      },
      "source": [
        "### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "id": "go4_kmZmyVSx"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "6\n"
          ]
        }
      ],
      "source": [
        "# Write your code here\n",
        "a = int(input('Enter first term: '))\n",
        "b = int(input('Enter second term: '))\n",
        "nth_value  = int(input('Enter nth value: '))\n",
        "nth_term = a + (nth_value - 1) * (b - a)\n",
        "print(nth_term)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "QgyRX_es1oum"
      },
      "source": [
        "### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "X05xqFS1yW16"
      },
      "outputs": [],
      "source": [
        "# Write your code here"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "eaql38ln13u7"
      },
      "source": [
        "### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.\n",
        "\n",
        "\n",
        "\n",
        "Input:<br>\n",
        "Dimensions of the milk tank<br>\n",
        "H = 20cm, L = 20cm, B = 20cm\n",
        "<br><br>\n",
        "Dimensions of the glass<br>\n",
        "h = 3cm, r = 1cm"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "FePZqno74eWv"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "40.12738853503185\n"
          ]
        }
      ],
      "source": [
        "# Write your code here\n",
        "H = int(input('Enter height value of milk tank: '))\n",
        "L = int(input('Enter length value of milk tank: '))\n",
        "B = int(input('Enter width value of milk tank: '))\n",
        "\n",
        "vol_milk_glass = H * L * B\n",
        "\n",
        "h = int(input('Enter height value of glass: '))\n",
        "r = int(input('Enter radius value of glass: '))\n",
        "\n",
        "vol_glass = 3.14*r*r*h\n",
        "\n",
        "num_glass = vol_milk_glass/vol_glass\n",
        "\n",
        "print(num_glass)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "3\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.6"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
