{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "counties = [\"Araphoe\", \"Denver\" \"Jeffferson\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Denver\n"
     ]
    }
   ],
   "source": [
    "if counties [1] == 'Denver':\n",
    "    print(counties[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El Paso is not in the list of counties.\n"
     ]
    }
   ],
   "source": [
    "counties = [\"Arapahoe\",\"Denver\",\"Jefferson\"]\n",
    "if \"El Paso\" in counties:\n",
    "    print(\"El Paso is in the list of counties.\")\n",
    "else:\n",
    "    print(\"El Paso is not in the list of counties.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arapahoe or El Paso is in the list of counties.\n"
     ]
    }
   ],
   "source": [
    "if \"Arapahoe\" in counties or \"El Paso\" in counties:\n",
    "    print(\"Arapahoe or El Paso is in the list of counties.\")\n",
    "else:\n",
    "    print(\"Arapahoe and El Paso are not in the list of counties.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arapahoe\n",
      "Denver\n",
      "Jefferson\n"
     ]
    }
   ],
   "source": [
    "for county in counties:\n",
    "    print(county)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arapahoe\n",
      "Denver\n",
      "Jefferson\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(counties)):\n",
    "    print(counties[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Iterate Through a Dictionary\n",
    "counties_dict = {\"Arapahoe\": 422829, \"Denver\": 463353, \"Jefferson\": 432438}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arapahoe\n",
      "Denver\n",
      "Jefferson\n"
     ]
    }
   ],
   "source": [
    "#Retrieve only keys using a for loop\n",
    "for county in counties_dict:\n",
    "    print(county)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arapahoe\n",
      "Denver\n",
      "Jefferson\n"
     ]
    }
   ],
   "source": [
    "#Retrieve only keys using keys()\n",
    "#This will print each key in order\n",
    "for county in counties_dict.keys():\n",
    "    print(county)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "422829\n",
      "463353\n",
      "432438\n"
     ]
    }
   ],
   "source": [
    "#Retrieve only values using values()\n",
    "for voters in counties_dict.values():\n",
    "    print(voters)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "422829\n",
      "463353\n",
      "432438\n"
     ]
    }
   ],
   "source": [
    "#Retrieve only values using dictionary_nane[key]\n",
    "for county in counties_dict:\n",
    "    print(counties_dict[county])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "422829\n",
      "463353\n",
      "432438\n"
     ]
    }
   ],
   "source": [
    "#Retrieve only values using get() \n",
    "for county in counties_dict:\n",
    "    print(counties_dict.get(county))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arapahoe 422829\n",
      "Denver 463353\n",
      "Jefferson 432438\n",
      "Arapahoe county has 422829 registered voters.\n",
      "Denver county has 463353 registered voters.\n",
      "Jefferson county has 432438 registered voters.\n"
     ]
    }
   ],
   "source": [
    "#Retrieve key-value pairs using items()\n",
    "for county, voters in counties_dict.items():\n",
    "    print(county, voters)\n",
    "for county, voters in counties_dict.items():\n",
    "    print(county, \"county has\", str(voters), \"registered voters.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'county': 'Arapahoe', 'registered_voters': 422829}\n",
      "{'county': 'Denver', 'registered_voters': 463353}\n",
      "{'county': 'Jefferson', 'registered_voters': 432438}\n",
      "{'county': 'Arapahoe', 'registered_voters': 422829}\n",
      "{'county': 'Denver', 'registered_voters': 463353}\n",
      "{'county': 'Jefferson', 'registered_voters': 432438}\n"
     ]
    }
   ],
   "source": [
    "#Retrieve dictionaries from a list of dictionaries\n",
    "voting_data = [{\"county\":\"Arapahoe\", \"registered_voters\": 422829},\n",
    "    {\"county\":\"Denver\", \"registered_voters\": 463353},\n",
    "    {\"county\":\"Jefferson\", \"registered_voters\": 432438}]\n",
    "for county_dict in voting_data:\n",
    "    print(county_dict)\n",
    "for i in range(len(voting_data)):\n",
    "    print(voting_data[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Arapahoe\n",
      "422829\n",
      "Denver\n",
      "463353\n",
      "Jefferson\n",
      "432438\n",
      "422829\n",
      "463353\n",
      "432438\n",
      "Arapahoe\n",
      "Denver\n",
      "Jefferson\n"
     ]
    }
   ],
   "source": [
    "#Retreive values from a list of dictionaries\n",
    "for county_dict in voting_data:\n",
    "    for value in county_dict.values():\n",
    "        print(value)\n",
    "#Retrieve only the number of registered voters from each dictionary\n",
    "for county_dict in voting_data:\n",
    "    print(county_dict['registered_voters'])\n",
    "#Retrieve only the county name from each dictionary\n",
    "for county_dict in voting_data:\n",
    "    print(county_dict['county'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Printing Formats\n",
    "#Concatenate strings with: + str()\n",
    "#Original:\n",
    "#   my_votes = int(input(\"How many votes did you get in the election?\"))\n",
    "#   total_votes = int(input(\"What is the total votes in the election?\"))\n",
    "#   percentage_votes = (my_votes / total_votes) * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_votes = int(input(\"How many votes did you get in the election? \"))\n",
    "total_votes = int(input(\"What is the total votes in the election? \"))\n",
    "print(f\"I received {my_votes / total_votes * 100}% of the total votes.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "counties_dict = {\"Arapahoe\": 369237, \"Denver\":413229, \"Jefferson\": 390222}\n",
    "for county, voters in counties_dict.items():\n",
    "    print(county + \" county has \" + str(voters) + \" registered voters.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for county, voters in counties_dict.items():\n",
    "    print(f\"{county} county has {voters} registered voters.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "candidate_votes = int(input(\"How many votes did the candidate get in the election?\"))\n",
    "total_votes = int(input(\"What is the total votes in the election?\"))\n",
    "message_to_candidate = (\n",
    "    f\"You received {candidate_votes} number of votes. \"\n",
    "    f\"The total number of votes in the election was {total_votes}. \"\n",
    "    f\"You received {candidate_votes/total_votes*100}% of the total votes.\")\n",
    "print(message_to_candidate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "message_to_candidate = (\n",
    "    f\"You received {candidate_votes:,} number of votes. \"\n",
    "    f\"The total number of votes in the election was {total_votes:,}. \"\n",
    "    f\"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for county, voters in counties_dict.items():\n",
    "    print(f\"{county} county has {voters:,} registered voters.\")"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
