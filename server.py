from flask import Flask,jsonify,request
app = Flask(__name__)

list_of_users = dict()

current_user = 'dibya'
active_user = 'dibya'

options = [('fullName','Full Name','Dibya Ghosh'), ('AC','Preferred AC Temperature','80'),\
	 ('FavSong','Favorite Song','Bad Things'),('bedtime','Bed Time','10:00 PM'),('coffee','Coffee Brewing Time','8:30 AM'),('huecolor','Hue Color','blue')]

default_configuration = {i[0]:i[2] for i in options}
list_of_users['dibya'] = default_configuration.copy()
list_of_users['akilesh'] = default_configuration.copy()
list_of_users['akilesh']['fullName'] = 'Akilesh Bapu'
list_of_users['blake'] = default_configuration.copy()
list_of_users['blake']['fullName'] = 'Blake Tickell'




@app.route('/options')
def get_options():
	return jsonify(data=options)

@app.route('/users')
def list_users():
	return jsonify(data=list(list_of_users.items()))

@app.route('/add/<username>')
def add_user(username):
	list_of_users[username] = default_configuration.copy()

@app.route('/set/<username>')
def set_user(username):
	global current_user
	if username not in list_of_users:
		list_of_users[username] = default_configuration.copy()
	current_user = username
	return 'Current authenticated user is %s'%username

@app.route('/get/<username>')
def get_user(username):
	if username not in list_of_users:
		list_of_users[username] = default_configuration.copy()
	dataStyle2 = list(list_of_users[username].items())
	return jsonify(name=username,data=list_of_users[username],data2=dataStyle2)


@app.route('/modify',methods=['POST'])
def modify_active():
	print("I got it!")
	new_dict = {k:v for k,v in request.form.items()}
	list_of_users[active_user].update(new_dict)
	return str(new_dict)

@app.route('/activate/<username>')
def activate_user(username):
	global active_user
	active_user = username
	return ''

@app.route('/preferences/<name>')
def get_preference(name):
	return list_of_users[current_user][name]

@app.route('/current')
def get_current():
	return get_user(current_user)


@app.route('/active')
def get_active():
	return get_user(active_user)

@app.route('/')
def index():
	return open('mapv2.html').read()

if __name__ == '__main__':
	app.run(debug=True)
