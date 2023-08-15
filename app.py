from flask import Flask,render_template,request,redirect
from flask_migrate import Migrate
from models import db, EmployeeModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://grossak:password@localhost:5432/one_model_flask_crud"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://<username>:<password>@<server>:5432/<db_name>"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/data/create', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = EmployeeModel(name=name, age=age, position = position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def RetrieveDataList():
    employees = EmployeeModel.query.all()
    return render_template('datalist.html',employees = employees)

@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with id ={id} Doesn't exist"

@app.route('/data/<int:id>/update')
def updateRoute(id):
    employee = EmployeeModel.query.get(id)
    if employee:
        return render_template('update.html', employee=employee)
    return f"Employee with id = {id} Doesn't exist"

@app.route('/data/<int:id>/update', methods=['POST'])
def update(id):
    employee = EmployeeModel.query.get(id)
    if employee:
        form = request.form
        name = form.get('name')
        age = form.get('age')
        position = form.get('position')
        employee.name = name
        employee.age = age
        employee.position = position
        db.session.commit()
    return redirect('/data')

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = EmployeeModel.query.get(id)
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        return f"Employee with id = {id} doesn't exist"

    return render_template('delete.html')

if __name__ == "__main__":
    app.run(debug=True)
