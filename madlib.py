# -*- coding: utf-8 -*-
"""
Icebreaker exercise for PyschHacks 2019

INSTRUCTIONS
Make sure everyone on the team has accepted the GitHub Classroom invite,
and has cloned the repo locally.

1) Git pull (unless you're starting)
2) Change your word selections, this can be done in any text editor
3) Git add -A
4) Git commit -m"Type in your name"
5) Git push
6) Next person repeats steps 2 - 6
8) Last person runs the code to generate the madlib text file.
(this person needs to have python installed)

Check that the file is created successfully!

credits: adapted from PhD Comics
"""
import os

#person 1
teamName = "Team_snax"
synonymForNew = "novel"
sciencyVerb = "conduct"
buzzword = "data_science"

#person 2
number = "101"
buzzword2 = "network"
sexyAdjective = "hawt"
somethingYouDidntInvent = "the p-value"


#person 3
number2 = "11"
buzzword3 = "big data"
scientistThatScoopsYourLabConstantly = "no one what"
dependentVariable = "RAVLT A6 score"

#person 4
units = "pixels"
buzzword4 = "machine_learning"
supremeSocialogicalConcern = "women's_rights"
nounFewPeopleHaveHeardOf = "dentate_gyrus"







""" STOP HERE! -------------------------------------------------------------"""













cwd = os.getcwd()

story = ("This paper presents a " + synonymForNew + " method for " +
         sciencyVerb + "\nthe " + nounFewPeopleHaveHeardOf + ". Using " +
         somethingYouDidntInvent + ", the \n" + dependentVariable + " was measured to be " +
         number + " +/- " + number2 + "\n" + units + ". " +
         "Results show " + sexyAdjective + " agreement with \ntheoretical predictions and significant improvement over \nprevious efforts by " +
         scientistThatScoopsYourLabConstantly + " et al. The work presented \nhere has profound implications for future studies of \n" +
         buzzword + " and may one day help solve the problem of \n" + supremeSocialogicalConcern + ". \n\n\n"

         "Keywords: " + buzzword2 + ", " +  buzzword3 + ", " +  buzzword4
        )


madlib = open(os.path.join(cwd, teamName + "_madlib.txt"), "w")
madlib.write(story)
madlib.close()
