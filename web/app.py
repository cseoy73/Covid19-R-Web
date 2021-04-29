from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main1.html')
def main1():
    return render_template('main1.html')

@app.route('/confirmed_cases_region.html')
def confirmed_cases():
    return render_template('confirmed_cases_region.html')

@app.route('/population.html')
def population():
    return render_template('population.html')


@app.route('/medical.html')
def medical():
    return render_template('medical.html')

@app.route('/covid_response.html')
def covid_response():
    return render_template('covid_response.html')

# 
@app.route('/main2.html')
def main2():
    return render_template('main2.html')

@app.route('/industry.html')
def industry():
    return render_template('industry.html')

@app.route('/online_mobile.html')
def online_mobile():
    return render_template('online_mobile.html')

@app.route('/employment.html')
def employment():
    return render_template('employment.html')

@app.route('/CPI.html')
def price_index():
    return render_template('CPI.html')

if __name__ == "__main__":
    app.run(debug=True)
