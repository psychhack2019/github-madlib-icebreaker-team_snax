# -*- coding: utf-8 -*-
"""
@author: annabel wing-yan fan 2019

INSTRUCTIONS

1) Git pull (unless you're starting)
2) Change your word selections, this can be done in any text editor
3) Git add -A
4) Git commit -m"Type in your name"
5) Git push
6) Stand up and cheer for the rest of your team!
7) Next person repeats steps 2 - 6
8) Last person runs the code to generate the madlib text file. (this person needs to have python installed)

Check that the file is created successfully,
When the team is done have everyone sit back down.

credits: adapted from PhD Comics
"""

#person 1
teamName = ""
synonymForNew = ""
sciencyVerb = ""
buzzword = ""

#person 2
number = ""
buzzword2 = ""
sexyAdjective = ""
somethingYouDidntInvent = ""


#person 3
number2 = ""
buzzword3 = ""
scientistThatScoopsYourLabConstantly = ""
dependentVariable = ""

#person 4
units = ""
buzzword4 = ""
supremeSocialogicalConcern = ""
nounFewPeopleHaveHeardOf = ""







""" STOP HERE! -------------------------------------------------------------"""














story = ("This paper presents a " + synonymForNew + " method for " +
         sciencyVerb + "\nthe " + nounFewPeopleHaveHeardOf + ". Using " +
         somethingYouDidntInvent + ", the \n" + dependentVariable + " was measured to be " +
         number + " +/- " + number2 + "\n" + units + ". " +
         "Results show " + sexyAdjective + " agreement with \ntheoretical predictions and significant improvement over \nprevious efforts by " +
         scientistThatScoopsYourLabConstantly + " et al. The work presented \nhere has profound implications for future studies of \n" +
         buzzword + " and may one day help solve the problem of \n" + supremeSocialogicalConcern + ". \n\n\n"

         "Keywords: " + buzzword2 + ", " +  buzzword3 + ", " +  buzzword4
        )


madlib = open(teamName + "_madlib.txt", "w")
madlib.write(story)
madlib.close()
