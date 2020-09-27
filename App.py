from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    currentTimeStampString = 'Started at: ' + timestampStr

    print(currentTimeStampString)

    f = open("logfile.txt", "wt")
    f.write(currentTimeStampString)
    f.close()

    app.run(host="0.0.0.0", port=57777, debug=True)