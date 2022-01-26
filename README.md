# GeoComply Job Audition
## Requirements
Building a backend service to serve requests invoked by the web application for retrieving service information, filtering, sorting, and searching. Customers' activities (search, filter, view info) need to be recorded in a database for
future references. 
**The Challenge**:
- Able to use any familiar Python libraries and frameworks open source type is recommended.
- Follow **Pep8** or **Pylint** standards for coding and is recommended.
- Expect some levels of testing (Unit Test, Function Test, Integration Test) delivered along with the base code.
- The system is required to be designed for High Availability and Horizontal Scalability.

**Prefered Output**:
- A High-Level solution diagram for the components.
- Entity-relationship diagram for database design.
- Sample code for some business workflows of the backend services.
- A Readme file explains:
	- A brief explanation for the code structure.
	- Installation steps to set up and run the application on a local
computer.
	- CURL commands to test and verify API endpoints.

## Solution explanation
Using Django Restframework to implement solution. Project coming with two main apps  `geo_product` coming with model present product and `geo_customer_action` coming with some models will present action of customer.  Customer action scope contains *search, filtering, ordering, view info*, each of them is present as GET request and each of them also present as query parameters of url, so we will store action information based on key value pair from query parameters. 
Let assume that all request will have sucessful reponse, so that very time request come to server, a signal `request_coming`will be send with query parameters to `geo_customer_action` app, when it received, it will create action information base on query parameters. For usage of other future apps, `core` app is created, it contains `request_coming` signal.

**Database Diagram**

![enter image description here](https://bit.ly/3GWJ4nn)

## Set up
**Python 3.7** or higher is required

"*Just keep using current terminal and every thing will be fine*"

Clone this repo with git command:
```
git clone https://github.com/F2i/geo_hub.git
```
Direct to project folder:
```
cd geo_hub
```
Create virtual enviroment:
```
python -m venv .venv
```
Activate virtual enviroment, just copy and paste to terminal:
- For Windows user:
	```
	.\.venv\Scripts\activate.bat
	```
- For Unix/Linux user:
	```
	source .venv\Scripts\activate
	```
Install dependencies:
```
pip install -r requirements.txt
```

## Run project locally

After successfully install dependencies, at first, migrate data to create an SQLite database file name`db.sqlite3` in project folder:
```
python manage.py migrate
```
Then populate sample product data to created SQLite database :
```
python manage.py populate_product_data
```
Then now, run server:
```
python manage.py runserver
```
Output on terminal when successfully run server:

> ...

> Django version 4.0.1, using settings 'geo_hub.settings'

> Starting development server at http://127.0.0.1:8000/

> Quit the server with CTRL-BREAK.

## Verify API Endpoints
**Note:**  From now, use new terminal for typing command because django application is running on current terminal.

For more readable json data on terminal, install `jsontool` package wih `npm`, if you already know it, just skip this part:
- Install Nodejs latest verision, you can download it here https://nodejs.org/en/download/ .
If you've already installed it, skip this step
- Open new terminal and typing this command:
	```
	npm install -g jsontool
	```
**Activities**
Endpoint Description:

\- HTTP Method: : `GET`  

\- Path for List: `/geo-hub/geo-products/`

\- Path for Detail: `/geo-hub/geo-products/{product_id}/`


CURL command to get product list with no parameter:
```
curl --header "content-type:application/json" --request GET "http://localhost:8000/geo-hub/geo-products/" | json
```
CURL command to get product list with parameter, this example contain *search, ordering, filtering* action:
```
curl --header "content-type:application/json" --request GET "http://localhost:8000/geo-hub/geo-products/?min_price=12&ordering=price&os_platform=Window&os_platform=Linux&search=Product+1" | json
```
CURL command to get product detail also known as *view info* action, this example get product have id **3**, you can change it if you want:
```
curl --header "content-type:application/json" --request GET "http://localhost:8000/geo-hub/geo-products/3/" | json
```
*Example Reponse*:
```js
[
    {
        "id": 1,
        "title": "Product 1",
        "price": "12.12",
        "os_platform": "Window",
        "description": "Description 1"
    }
]
```
**Action Data**
Enpoint Description:

\- HTTP Method: `GET`

\- Path for List: `/customer-action/actions/`

\- Path for Latest: `/customer-action/actions/latest/`

Everytime after you perform activities, you can check list of action information:
```
curl --header "content-type:application/json" --request GET "http://localhost:8000/customer-action/actions/" | json
```
Or you can check latest action:
```
curl --header "content-type:application/json" --request GET "http://localhost:8000/customer-action/actions/latest/" | json
```
*Example Reponse*:
```js
{
    "id": 37,
    "action_type": {
        "function_name": "list",
        "description": "View a list of objects"
    },
    "object_info": {
        "model": {
            "model": "geoproduct",
            "app_label": "geo_product"
        },
        "object_id": null
    },
    "path": "http://localhost:8000/geo-hub/geo-products/",
    "data": {
        "os_platform": [
            "Window",
            "Linux"
        ],
        "min_price": "12"
    },
    "action_time": "2022-01-25T21:19:56.118887Z"
}
```
## Testing
"*Just keep using current terminal and every thing will be fine*"

For PEP8 check:
```
flake8
```
For automation testing:
```
pytest
```

