#JSON POST REQUEST
from flask import Flask, request
import pandas as pd 
app = Flask(__name__)

@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json(force=True)
        #timestamp = json["timestamp"]
        #status = json["status"]
        #no_of_people = json["total_number"]
        #dataframe = pd.DataFrame()
        df = pd.DataFrame(json)
        csvdf = df.to_csv()
        return(csvdf)

        #return json
    
app.run(port=5000,debug=False)