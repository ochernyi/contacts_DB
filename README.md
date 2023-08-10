# API Project Nimble

A simple Flask API for searching contacts using a full-text search feature.

## Getting Started

This Flask API allows you to perform a full-text search on contacts stored in a PostgreSQL database.

### Prerequisites

- Python (3.6+)
- Pip (Python package manager)
- PostgreSQL database (with appropriate schema and tables)


### Installation

1. Clone the repository:

   ```bash
    git clone https://github.com/ochernyi/contacts_DB.git
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt

2. Create a .env file in the root directory and add your database and API credentials. 
3. Add API_KEY for Authorization
   ```bash
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=DB_PORT
   
    API_KEY=API_KEY
    
4. Run the Flask development server:
   ```bash
   python api.py

Your API will be available at http://localhost:5000

### API Endpoints

1. GET /contacts

- http://localhost:5000/contacts

2. GET /search

- http://localhost:5000/search

Search for contacts using a full-text search query.

Parameters:

query (string): The search query.
Example:

- http://localhost:5000/search?query=John

### Updating Contacts
Contacts are updated daily at 3 AM using the schedule library. 
The script update_contacts.py contains the logic for fetching contacts from the Nimble API and updating the database.

- To start the automatic daily update, run:
   ```bash
  python update_contacts.py

         
### Contributing

Contributions are welcome! Please create an issue or pull request if you find any improvements or fixes.