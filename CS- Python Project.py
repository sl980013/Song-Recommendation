# Bringing in a module to open a website from Python standard library
import webbrowser

# Write a list of songs that will be assigned to each weather and feeling outside.
songlist = ["You Hee Yeol- In the Park", "Damien Rice- I don't want to change you", "Soran- Perfect Day", "Mot- Cloudy Seoul",
            "Jack Johnson- Banana Pancakes", "Stella Jang- It's raining", "Jung Seung Hwan- Snowman", "Zion. T- Snow"]

# Create a function by using define and write the parameter list by it.


def recommendation(songlist):

    # Make a while loop to repeat error message and question in certain conditions
    while True:
        # String inputs are typed inside the loop to make conditions.
        weather = str(input("What is the weather today? Type in one of the followings: sunny, cloudy, raining, snowing "))
        error = str("Please check the spelling including capitalization. Do not put any space.")

        # if created for repetition when weather conditions are not met.
        if weather != "sunny" and weather != "cloudy" and weather != "raining" and weather != "snowing":
            # prints an error message and continues the loop until one of the conditions is met
            print(error)
            continue
        # elif written to give more instructions for specific conditions.
        elif weather == "sunny":
            # Make a while loop to repeat error message and question in certain conditions
            while True:
                # String input is typed inside the loop to make conditions.
                feeling = str(input("How are you feeling? Type in one of the followings: happy, sad "))
                # if used for repetition when feeling conditions are not met.
                if feeling != "happy" and feeling != "sad":
                    # prints an error message and continues the loop until one of the conditions is met
                    print(error)
                    continue
                # elif written to give more instructions for the specific conditions.
                elif feeling == "happy":
                    # prints a chosen element from the list and breaks to avoid continuous repetition when condition is met.
                    print(songlist[0])
                    # webbrowser.open used to open the url in a web browser and play music video
                    webbrowser.open("https://youtu.be/BeEu0GQ6Nz4")
                    break
                # elif written to give more instructions for the specific conditions.
                elif feeling == "sad":
                    # prints a chosen element from the list and breaks to avoid continuous repetition when condition is met.
                    print(songlist[1])
                    # webbrowser.open used to open the url in a web browser and play music video
                    webbrowser.open("https://youtu.be/FnzHOsiaJns")
                    break

        # elif written to give more instructions for specific conditions.
        elif weather == "cloudy":
            # Make a while loop to repeat error message and question in certain conditions
            while True:
                # String input is typed inside the loop to make conditions.
                feeling = str(input("How are you feeling? Type in one of the followings: happy, sad "))
                # if used for repetition when feeling conditions are not met.
                if feeling != "happy" and feeling != "sad":
                    # prints an error message and continues the loop until one of the conditions is met
                    print(error)
                    continue
                # elif written to give more instructions for specific conditions.
                elif feeling == "happy":
                    # prints a chosen element from the list and breaks to avoid continuous repetition when condition is met.
                    print(songlist[2])
                    # webbrowser.open used to open the url in a web browser and play music video
                    webbrowser.open("https://youtu.be/M0wRIsGXc3c")
                    break
                # elif written to give more instructions for specific conditions.
                elif feeling == "sad":
                    # prints a chosen element from the list and breaks to avoid continuous repetition when condition is met.
                    print(songlist[3])
                    # webbrowser.open used to open the url in a web browser and play music video
                    webbrowser.open("https://youtu.be/GRh_V_7QSyc")
                    break
        # elif written to give more instructions for specific conditions.
        elif weather == "raining":
            # Make a while loop to repeat error message and question in certain conditions
            while True:
                # String input is typed inside the loop to make conditions.
                feeling = str(input("How are you feeling? Type in one of the followings: happy, sad "))
                # if used for repetition when feeling conditions are not met.
                if feeling != "happy" and feeling != "sad":
                    # prints an error message and continues the loop until one of the conditions is met
                    print(error)
                    continue
                # elif written to give more instructions for specific conditions.
                elif feeling == "happy":
                    # prints a chosen element from the list and breaks to avoid continuous repetition when condition is met.
                    print(songlist[4])
                    # webbrowser.open used to open the url in a web browser and play music video
                    webbrowser.open("https://youtu.be/OkyrIRyrRdY")
                    break
                # elif written to give more instructions for specific conditions.
                elif feeling == "sad":
                    # prints a chosen element from the list and breaks to avoid continuous repetition when condition is met.
                    print(songlist[5])
                    # webbrowser.open used to open the url in a web browser and play music video
                    webbrowser.open("https://youtu.be/ZSITj0NLBL4")
                    break
        # elif written to give more instructions for specific conditions.
        elif weather == "snowing":
            # Make a while loop to repeat error message and question in certain conditions
            while True:
                # String input is typed inside the loop to make conditions.
                feeling = str(input("How are you feeling? Type in one of the followings: happy, sad "))
                # if used for repetition when feeling conditions are not met.
                if feeling != "happy" and feeling != "sad":
                    # prints an error message and continues the loop until one of the conditions is met
                    print(error)
                    continue
                # elif written to give more instructions for specific conditions.
                elif feeling == "happy":
                    # prints a chosen element from the list and breaks to avoid continuous repetition when condition is met.
                    print(songlist[6])
                    # webbrowser.open used to open the url in a web browser and play music video
                    webbrowser.open("https://youtu.be/5U_rbLPhY9U")
                    break
                # elif written to give more instructions for specific conditions.
                elif feeling == "sad":
                    # prints a chosen element from the list and breaks to avoid continuous repetition when condition is met.
                    print(songlist[7])
                    # webbrowser.open used to open the url in a web browser and play music video
                    webbrowser.open("https://youtu.be/fiGSDywrX1Y")
                    break
        # Break for final finish of running the program to break the weather loop when all conditions are met.
        break


# Bring function for execution
recommendation(songlist)
# input created to finish the program manually
input('Press ENTER to exit')
