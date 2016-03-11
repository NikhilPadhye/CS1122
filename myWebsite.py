#Nikhil Padhye
#MyWebsite.py
from Flask import Flask
app = Flask(__name__)

@app.route(“/“)
def greetinb():
	return (“Hi, this is Nikhil's website!”)

if __name__ == (__main__):
	app.run(
	host = “0.0.0.0”, 
	port = 5000
)
