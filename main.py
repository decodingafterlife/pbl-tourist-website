from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def default():
    return 'default'

#url = "predict?people=<num>&days=<days>&rooms=<rooms>"
@app.route('/predict')
def predict():
    data = request.args.to_dict()
    return data


@app.route('/predictt/<ppl>/<days>/<rooms>')
def prednorm(ppl,days,rooms):
    #model.pred...
    return ppl+days+rooms

if __name__=='__main__':
    app.run(debug=True)