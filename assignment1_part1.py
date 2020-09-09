{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The function returns the number of elements in the numbers list that are divisible\n",
    "# by the divide parameter.\n",
    "\n",
    "class ListDivideException(TypeError):\n",
    "    pass\n",
    "def listDivide(numbers, divide = 2):\n",
    "    counter = 0;\n",
    "    for i in numbers: \n",
    "        if (i % divide == 0): \n",
    "            counter = counter + 1\n",
    "    \n",
    "    return counter\n",
    "    raise ListDivideException\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def testlistdivide():\n",
    "    print(listDivide([1,2,3,4,5]))\n",
    "    print(listDivide([2,4,6,8,10]))\n",
    "    print(listDivide([30, 54, 63,98, 100], divide=10))\n",
    "    print(listDivide([])) \n",
    "    print(listDivide([1,2,3,4,5], 1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "5\n",
      "2\n",
      "0\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "testlistdivide()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
