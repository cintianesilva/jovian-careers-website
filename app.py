from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
  {
  'id': 1,
  'title': "Data Analyst",
  'location': "São Paulo, Brazil",
  'salary': "R$ 3.000,00"
  },
  {
    'id': 2,
    'title': "Data Scientis",
    'location': "Rio de Janeiro, Brazil",
    'salary': "R$ 4.500,00"
    },
  {
    'id': 3,
    'title': "Frontend Engineer",
    'location': "Remote",
    'salary': "R$ 3.500,00"
    },
  {
    'id': 4,
    'title': "Backend Engineer",
    'location': "San Francisco, USA",
    'salary': "$120,000"
    }
]

@app.route("/")
def hello_jovian():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
