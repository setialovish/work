import flask
import time
import pandas as pd
import numpy as np
from flask import request,Response

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


def create_new_file(address_to_Check):
    #address_to_Check = pd.read_csv(source_filepath)
    splitted_Address = address_to_Check['Address'].str.split(',')
    df  = pd.read_csv(r'Townlands__OSi_National_Placenames_Gazetteer.csv', usecols=(0,1,3,12))
    df = df.drop_duplicates(subset=['County','English_Name'])
    time_start = time.time()
    for i in range(0,len(splitted_Address)):
        #print (splitted_Address[i])
        for j in range(0,len(splitted_Address[i])-1):
            #print (splitted_Address[i][j].upper(),str(splitted_Address[i][-1]).upper())
            x = df[(df.English_Name == str(splitted_Address[i][j]).upper().strip()) & (df.County == str(splitted_Address[i][-1]).upper().strip())]
            #print (x)
            if len(x):
                splitted_Address[i].append(x.iloc[0]['X'])
                splitted_Address[i].append(x.iloc[0]['Y'])
                break
    time_end = time.time()
    print("Time taken for "+str(len(splitted_Address))+" address is:",time_end - time_start)
    #splitted_Address.to_csv(dest_filepath,)
    return splitted_Address

@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1>Geocoder</h1>
                <p>Please select the file with addresses to check (csv format only)</p>
                <form action="/submit" method="post" enctype="multipart/form-data">
                    
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

@app.route('/submit', methods=["POST"])
def transform_view():
    request_file = request.files['data_file']
    if not request_file:
        return "No file"

    file_contents = request_file.stream.read()#.decode("utf-8")
    file_contents = file_contents.replace('"','')
    #print (type(file_contents.splitlines()))
    #print(file_contents)
    df = pd.DataFrame(np.array(file_contents.splitlines()[1:]).reshape(-1,1),columns=['Address'])
    #print (df)
    result = create_new_file(df)
    result = result.to_csv()
    #print(result)
    return Response(
        result,
        mimetype="text/csv",
        headers={"Content-disposition":
                     "attachment; filename=GeoCodes.csv"})

app.run()
