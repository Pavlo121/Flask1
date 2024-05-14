from flask import Flask

app = Flask(__name__)


@app.post('/register')
def new_user_register():
    return 'new user register'


@app.get('/register')
def user_register_invitation():
    return 'please sing in to register'


@app.post('/login')
def user_login():
    return 'new user loggen in'


@app.get('/login')
def user_login_form():
    return 'please enter credentials'


@app.post('/user')
def new_user():
    return 'user data has been created'


@app.get('/user')
def user_info():
    return 'user information'


@app.put('/user')
def user_editing():
    return 'user information edited'


@app.post('/funds')
def add_funds():
    return 'account financing'


@app.get('/funds')
def deposit_info():
    return 'user deposit value'


@app.post('/reservations')
def reservations_service():
    return 'data  reservations'


@app.get('/reservations')
def data_reservation():
    return 'receive detailed data'


@app.post('/checkout')
def user_checkout():
    return 'payment verification'


@app.get('/checkout')
def checkout_info():
    return 'receiving a transfer'


@app.put('/checkout')
def edit_checkout():
    return 'edit sum'


@app.get('/fitness_center')
def user_fitness_center():
    return 'choosing a fitness center'


@app.get('/fitness_center/<gem_id>/services/<service_id>')
def get_service_info(gem_id, service_id):
    return f'fitness center {gem_id} service {service_id} info'


@app.get('/fitness_center/<gem_id>/services')
def get_service(gem_id):
    return f'fitness center {gem_id} services'


@app.get('/user/reservations/<reservation_id>')
def reservation_info(reservation_id):
    return f'user reservations {reservation_id} info'


@app.put('/user/reservations/<reservation_id>')
def reservation_edit_info(reservation_id):
    return f'user reservations {reservation_id} edit'


@app.delete('/user/reservations/<reservation_id>')
def delete_info_reservation(reservation_id):
    return f'user reservations {reservation_id} delete'


@app.get('/fitness_center/<gem_id>')
def fitness_center_info(gem_id):
    return f'fitness center {gem_id} our center'


@app.get('/fitness_center/<gem_id>/trainer')
def get_trainers(gem_id):
    return f'fitness center {gem_id} trainers list'


@app.get('/fitness_center/<gem_id>/trainer/<coach_id>')
def get_coach_info(gem_id, coach_id):
    return f'fitness center {gem_id} trainer {coach_id} info'


@app.get('/fitness_center/<gem_id>/trainer/<coach_id>/rating')
def get_coach_rating(gem_id, coach_id):
    return f'fitness center {gem_id} trainer {coach_id} rating'


@app.post('/fitness_center/<gem_id>/trainer/<coach_id>/rating')
def set_coach_rating(gem_id, coach_id):
    return f'fitness center {gem_id} trainer {coach_id} rating was added'


@app.put('/fitness_center/<gem_id>/trainer/<coach_id>/rating')
def update_coach_rating(gem_id, coach_id):
    return f'fitness center {gem_id} trainer {coach_id} rating was updated'


@app.get('/fitness_center/<gem_id>/loyality_programs')
def user_loyality_programs(gem_id):
    return f'fitness center {gem_id} loyality programs info'



if __name__ == '  main  ':
    app.run()










