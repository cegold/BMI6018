{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e852027e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 22, 7]\n"
     ]
    }
   ],
   "source": [
    "#Carrie Gold\n",
    "#BMI 6030\n",
    "#Module 5 Advanced Functions and Logic, Part 3\n",
    "\n",
    "#3.    Write a python program that, given an input list, \n",
    "#will filter the input above a user-defined threshold. \n",
    "#This is to be done with a standard function.\n",
    "\n",
    "#That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), \n",
    "#it should return [1,2,3,4,5,6].\n",
    "\n",
    "example_list = [0,22,7,1,2,3,4,5,6]\n",
    "def cut_off(input_list, n):\n",
    "    new_list = []\n",
    "    for i in input_list:\n",
    "        if i == n:\n",
    "            new_list.append(i)\n",
    "            break\n",
    "        else:\n",
    "            new_list.append(i)\n",
    "    print(new_list)\n",
    "        \n",
    "cut_off(example_list, 7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da962caa",
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
