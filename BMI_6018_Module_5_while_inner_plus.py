{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e01eb42b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Carrie Gold\n",
    "#BMI 6030\n",
    "#Module 5 Advanced Functions and Logic, Part 1\n",
    "\n",
    "#while_inner_plus.py\n",
    "#1. Write a python program that, given an input list \n",
    "# of any level of complexity/nestedness, will return \n",
    "#the inner most list plus 1. This is to be done with a \n",
    "#while loop. Note: the input will contain only integers or lists. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "d795be37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "sample_list = [72, 2, 3, 4, [5, 6, 7, [8, 12,[72, 84,[99,[1,2,3]]]]]]\n",
    "def in_function(user_input, condition = None):\n",
    "    while condition is None:\n",
    "        try:\n",
    "            last_element = user_input[-1]\n",
    "            if isinstance(last_element, list):\n",
    "                user_input = user_input[-1]\n",
    "            else:\n",
    "                final_output = [i + 1 for i in user_input]\n",
    "                print(final_output)\n",
    "                break\n",
    "        except:\n",
    "            condition = 1\n",
    "in_function(sample_list)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
