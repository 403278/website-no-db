from flask import (
    Flask,
    g,
    jsonify,
    redirect, 
    render_template, 
    url_for, request, 
    make_response,
    session,
    url_for
)

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Mr.Robot', email='mrrobot@email.nl', password='anonymous'))
users.append(User(id=2, username='Pickle Rick', email='picklerick@email.nl', password='swifty'))
users.append(User(id=3, username='Elon Musk', email='elonmusk@email.nl', password='spacex'))

print(users)

app = Flask(__name__)
app.secret_key = '$uper$ecretP@ssword'

items = [
    {
        'category': 'Boards',
        'name': 'Raspberry Pi 4 8GB RAM',
        'model': '385190',
        'condition': 'Brand New!',
        'discription': 'This is a 8GB LPDDR4-3200 SDRAM with 2.4 GHz and 5.0 GHz IEEE 802.11ac wireless, Bluetooth 5.0, BLE',
        'price': '$75.00'
    },
    {
        'category': 'Parts',
        'name': 'Raspberry Pi HQ Camara',
        'model': '294683',
        'condition': 'Brand New!',
        'discription': 'This is a 12.3 megapixel Sony IMX477 sensor with 1.55μm × 1.55μm pixel size – double the pixel area of IMX219',
        'price': '$50.00'
    },
    {
        'category': 'PC',
        'name': 'MSI GE75 Raider 8SE',
        'model': '935285',
        'condition': 'Used',
        'discription': 'This is a laptop with Intel Core i7-8750H @ 2.2 GHz and 16GB (2 x 8GB SODIMM) 2667 MHz DDR4 using NVIDIA GeForce RTX 2060 6GB GDDR6',
        'price': '$1200.00'
    }
]

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


@app.route('/')
@app.route('/home')
def home():
    print("you are in home end-point")
    if not g.user:
        return redirect(url_for('login'))
    
    return render_template('home.html', title='Home')


@app.route('/inventory')
def inventory():
    print("you are in inventory end-point")
    return render_template('inventory.html', title='Inventory', items=items)


@app.route('/about')
def about():
    print("you are in about end-point")
    return render_template('about.html', title='About')


# @app.route('/login')
# def login():
#     print("you are in login end-point")
#     auth = request.authorization

#     if auth and auth.password == 'password':
#         return ''

#     return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm"Login Required"'})


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("you are in login end-point")

    if request.method == 'POST':
        session.pop('user_id', None)
        print("this is a POST request")

        username = request.form['username']
        #email = request.form['email']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))

        return redirect(url_for('login'))

    return render_template('login.html', title='Login')


@app.route('/register', methods =['GET', 'POST'])
def register():
    print("you are in register end-point")
    if request.method == 'GET':
        print("this is a GET request")
        return render_template('register.html')
    else:
        session.pop('user_id', None)
        print("this is a POST request")

        username = request.form['username']
        #email = request.form['email']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))

        return redirect(url_for('register'))
        
    return render_template('register.html', title='Register')

@app.route('/logout', methods =['GET'])
def logout():
    print("you are in logout end-point")
    if request.method == 'GET':
        print("this is a GET request")
        session.clear()
        return redirect(url_for('home'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
