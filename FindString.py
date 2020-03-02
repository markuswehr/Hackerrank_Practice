{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Find a string"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://www.hackerrank.com/challenges/find-a-string/problem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_substring(string, sub_string):\n",
    "    \"\"\"Counts how often a string contains a given sub-string\"\"\"\n",
    "    count=0\n",
    "    for i in range(len(string)-(len(sub_string)-1)):\n",
    "        test = False\n",
    "        test = sub_string in string[i:i+len(sub_string)]\n",
    "        if test==True:\n",
    "            count+=1\n",
    "    return count"
   ]
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
 "nbformat_minor": 4
}
