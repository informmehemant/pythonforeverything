#!/bin/bash

# Ask the user for the age

echo "Please enter your age:"
read age

# Check if the user is old enoght to vote
if [$age -ge 18]
then 
    echo "You are old enough to vote"
else 
    echo "Sorry, you are not old enought to vode "
fi

