{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "10b51a3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100]\n"
     ]
    }
   ],
   "source": [
    "#Carrie Gold\n",
    "#BMI 6030\n",
    "#Module 5 Advanced Functions and Logic, Part 2\n",
    "\n",
    "#2. Write the a python program that, given an input list of any level \n",
    "#of complexity/nestedness, will return the inner most list plus 1. \n",
    "#This is to be done with recursion. \n",
    "#Note: the input will contain only integers or lists. \n",
    "sample_list = [72, 2, 3, 4, [5, 6, 7, [8, 12,[72, 84,[99]]]]]\n",
    "def in_fun_r(user_input, condition=None):\n",
    "    if condition is None: \n",
    "        try:\n",
    "            last_element = user_input[-1]\n",
    "            if isinstance(last_element, list):\n",
    "                #print(\"current last element:\",last_element)\n",
    "                in_fun_r(user_input[-1])\n",
    "            else:\n",
    "                final_output = [i + 1 for i in user_input]\n",
    "                print(final_output)\n",
    "        except:\n",
    "            condition = 1\n",
    "in_fun_r(sample_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b90feb1c",
   "metadata": {},
   "outputs": [],
   "source": []
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
