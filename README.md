# CS361-Information-Microservice
Microservice to Push Information about an application to the user.

This program uses python FLASK, and JSON to run the information microservice.

Create contextual information within the DATA.JSON file in order to pull details for your applicaiton.
Example input:

    "context info": {
        "title": "Title of your help information",
        "purpose": "What is the help infromations purpose",
        "tips": [
            "Tips to utilize the following context."
        ]
        "Notes": (Optional)
    },

Steps to run program:

Step 1) 
Before running program make sure to run the following pip command.

"pip install -r requirements.txt"
or 
"pip3 install -r requirements.txt"

Step 2)
Run the microservice using the following:

"python app.py"
or
"python3 app.py"