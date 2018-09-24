#
#Name: Sabal Jayaswal
#Student ID: 014331872
#Date (last modified):9/24/2018
#
# Lab 0
# Section 14
# Purpose of Lab: To calculate the user's weight on Mars and Jupiter
# additional comments



def weight_on_planets():
    user_weight = float(input("What do you weigh on earth? "))
    mars_weight = user_weight*0.38
    jupiter_weight = user_weight*2.34
    print ("\nOn Mars you would weigh",  mars_weight, "pounds.\n" +
           "On Jupiter you would weigh" , jupiter_weight , "pounds.")



if __name__ == '__main__':
    weight_on_planets()
