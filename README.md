# CS361-Information-Microservice
Contributers: Gerardo, Matthew, Daniel, Thampanhaboth
Microservice to Push Information about an application to the user.

## What it does
This program uses python FLASK, and JSON to run the information microservice.
- Users can send a http request to this microservce and receive contextualized help information about features about a certain application.

Created contextual information within the DATA.JSON file in order to pull details for your applicaiton.
Example input:
```JSON
    "context info": {
        "title": "Title of your help information",
        "purpose": "What is the help infromations purpose",
        "tips": [
            "Tips to utilize the following context."
        ]
        "Notes": (Optional)
    },
```
## Steps to run program:
This program utilizes python and flask

### Step 1) 
Before running program make sure to run the following pip command within the base terminal.
```
pip install -r requirements.txt
```
or 
```
pip3 install -r requirements.txt
```

### Step 2)
Run the microservice using the following commande:
```
python service/app.py
```
or
```
python3 service/app.py
```

### Success when the following message appears
Running on http://127.0.0.1:5004

## Users can test by using cURL in a new terminal
```
curl http://localhost:5004/info/add_customer_lugoge
curl http://localhost:5004/info/main_menu_lugoge
curl http://localhost:5004/info
```

## Request Data Example
```
curl http://localhost:5004/info/main_menu_lugoge
```

## Recieve Data Example
```JSON
{
  "context": "main_menu_lugoge",
  "purpose": "Navigate to different areas of the application.",
  "tips": [
    "Enter the number next to each option",
    "Enter 0 to return to the previous menu"
  ],
  "title": "Main Menu"
}
```
## UML 
<img width="760" height="657" alt="UML" src="https://github.com/user-attachments/assets/97edc7fc-315b-4876-a36a-37e5a60e278f" />
