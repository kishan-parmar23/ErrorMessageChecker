# ErrorMessageChecker

## Background 

As a User Experience specialist, one of the more common and miscellaneous tasks I find myself helping developers with is checking and improving their validation messages (the text shown when the user hits an error, warning or requires more info). 

With the introduction of AI, i believe it is the perfect fit for this task, Its ability to handle text input and follow critical rules and guidelines make it a perfect fit. 

As such, I built a tool to help developers with this task 

## How It Works 

The tool takes a set of clear guidelines defined by me (based on common best practice) and reviews any validation message provided by the user and provide feedback as well as an example improved statement. 

## How To Guide 

    1. Replace the *constants.User_API_KEY* (index.py, line 6) with a string containing your Google Gemini API Key (E.g. "Asbfibfi3fsdjbJFjbsfbdfU54AKJFB")
    2. Run Script. 
    3. Provide the validation message you have written into the terminal. 
    4. Act on the improvements. 

## What Next 

Some additional functionality I would like to add includes:

    1. providing a help command to allow users to see the rules by which their validation messages will be reviewed.
    2. Provide multi-turn conversations allowing user to understand more about the why their validation message did not meat the criteria
    3. Provide a scoring system giving developers and users a clear go / no go decision point. 
    4. Using googles [here](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe) to improve the readability of the AI's output. 


## AI Usage Statement 

AI was used as a review tool and to aid with bug fixing but the code and prompts where written by me. 

