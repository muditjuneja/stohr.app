import os
import time
import json
import subprocess
from googleapiclient import discovery
from google.oauth2 import service_account
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from adapters.vercel import deploy_site

credentialsFile = os.getenv('CREDENTIALS_FILE', '/app/credentials.json')
spreadsheet_id = os.getenv('SPREADSHEET_ID', '15FFsH49Aqe4m1JpEKwxMBTX7BJF0aWLkgQzxiP0JTzg')
querySheet = os.getenv('QUERY_SHEET', 'query')
vercel_token = os.getenv('VERCEL_TOKEN')

# Init git repo
# subprocess.run('cd my-store && git init', shell=True)    


if not os.path.isfile(credentialsFile):
    raise Exception("Credentials file not found. Exiting now...")


app = Flask(__name__)
CORS(app)


@app.route('/update-sheets', methods=['get'])
def update_sheets():
    try:
        _data = process_sheets()
        return jsonify({'message': 'Update completed','_data':_data}), 200
    except Exception as e:
        return jsonify({'message': 'Error updating sheets'}), 500

@app.route('/submit-query', methods=['POST'])
def submit_query():
    data = request.get_json()
    firstName = data.get('first-name')
    lastName = data.get('last-name')
    email = data.get('email')
    phone = data.get('phone')
    country = data.get('country')
    region = data.get('region')
    city = data.get('city')
    postalCode = data.get('postal-code')
    address = data.get('street-address')

    query = data.get('query')
    items = data.get('items')

    # Load credentials and create service
    _credentials = service_account.Credentials.from_service_account_file(credentialsFile)
    service = discovery.build('sheets', 'v4', credentials=_credentials)

    
    # The range to update which is the query sheet
    range_ = querySheet + '!A1:A'
    # The new values
    values = [[firstName,lastName, email, phone, country, region, city, postalCode, address, query, items, time.strftime("%Y-%m-%d %H:%M:%S")]]

    # Create the request body
    body = {
        'values': values
    }

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_, body=body, valueInputOption='USER_ENTERED').execute()

    return jsonify({'message': 'Query submitted successfully'}), 200

def process_sheets():
    # Load credentials and create service
    credentials = service_account.Credentials.from_service_account_file(credentialsFile)
    service = discovery.build('sheets', 'v4', credentials=credentials)
    sheets = ['products', 'categories','meta']
    data = {"categories":None, "products":None, "meta":None}
    triggerRebuild = False

    for sheet in sheets:
        sheet_json_file = './data/' + '_' + sheet + '.json'
        if os.path.isfile(sheet_json_file):
            with open(sheet_json_file, 'r') as f:
                data[sheet] = json.load(f)
        else:
            print(f"File {sheet_json_file} does not exist.")

    for sheet in sheets:
        sheet_json_file = './data/' + '_' + sheet + '.json'
        print("sheet: ", sheet)
        # Get the values from the spreadsheet
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=sheet).execute()
        values = result.get('values', [])

        # Ensure all rows have the same number of columns
        max_columns = max(len(row) for row in values)
        for row in values:
            while len(row) < max_columns:
                row.append(None)

        # Create a pandas DataFrame from the values
        df = pd.DataFrame(values[1:], columns=values[0])
        _data = df.to_dict(orient='records')
        if _data !=data[sheet]:
            data[sheet] = _data
            triggerRebuild = True
            print("writing to file", sheet_json_file)
            with open(sheet_json_file, 'w') as f:
                json.dump(data[sheet], f, indent=4)
            subprocess.run(['cp', sheet_json_file, './my-store/_data/'])
        
    

    if(triggerRebuild):
        if vercel_token is not None:
            deploy_site(vercel_token)
        else:
            if not os.path.isdir('./my-store/node_modules'):
                subprocess.run('cd my-store && npm install', shell=True)    
            subprocess.run('cd my-store && npm run build', shell=True)

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=8003, debug=True)
