from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return 'server is Connected'
@app.route('/Ammu')
def Ammu():
    return 'server is hosted by Ammu'
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)