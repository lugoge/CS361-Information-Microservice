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
After running the application, in a new terminal run the following test file.
```
python3 test/info_client.py
```
### Request Data Example Code:
```PYTHON
def get_info(self, context):
        """Request help information from the microservice."""
        url = f"{self.base_url}/info/{context}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()

            elif response.status_code == 404:
                return {"error": "Context not found"}

            else:
                return {"error": f"Unexpected status code: {response.status_code}"}

        except requests.exceptions.ConnectionError:
            return {"error": "Unable to connect to microservice"}
        except Exception as e:
            return {"error": str(e)}
```
### Data Display Example Code:
```PYTHON
def display_info(self, data):
        """Display formatted help information."""
        if "error" in data:
            print("\nERROR:", data["error"])
            return

        print("\n===================================")
        print(f" {data.get('title', 'No Title')}")
        print("===================================\n")

        if "purpose" in data:
            print("Purpose:")
            print(data["purpose"], "\n")

        if "steps" in data:
            print("Steps:")
            for i, step in enumerate(data["steps"], start=1):
                print(f"{i}. {step}")
            print()

        if "tips" in data:
            print("Tips:")
            for tip in data["tips"]:
                print(f"- {tip}")
            print()

        if "notes" in data:
            print("Notes:")
            print(data["notes"], "\n")
```

### Prompt to enter context

The following prompt will show up:
```
=== Information Microservice Test Client ===

Enter context (or 'exit' to quit):
```
Enter
```
add_customer_lugoge
```
### Recieve Data Example
```
===================================
 Add Customer
===================================

Purpose:
Create a customer profile so bikes and maintenance can be tracked. 

Steps:
1. Enter the customer's full name
2. Enter phone number
3. Enter email address
4. Confirm to save the customer

Notes:
All fields except notes are required. 
```
## UML 
<img width="760" height="657" alt="UML" src="https://github.com/user-attachments/assets/97edc7fc-315b-4876-a36a-37e5a60e278f" />
