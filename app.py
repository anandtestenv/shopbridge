from flask import Flask,render_template,request,jsonify,request,redirect,url_for,flash
import sqlite3 as sql
from CustomException import NonNumericException

from model import *
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    try:
        con=sql.connect("shopbridge.db")
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute("select * from products")
        data=cur.fetchall()
        return render_template("index.html",prods=data)
    except Exception as e:
        return "Something went wrong: "+str(e)
    
@app.route("/add_product",methods=['POST','GET'])
def add_product_view():

    if request.method=='POST':
        try:
            pname=request.form['pname']
            description=request.form['description']
            price=request.form['price']
            if not price.isnumeric():
                raise NonNumericException("Price must be numeric")
                
            quantity=request.form['quantity']
            if not quantity.isnumeric():
                raise NonNumericException("Quantity must be numeric")
                
            con=sql.connect("shopbridge.db")
            cur=con.cursor()
            cur.execute("insert into products(name,description,price,quantity) values (?,?,?,?)",(pname,description,price,quantity))
            con.commit()
            flash('Product Added','success')
            return redirect(url_for("index"))
        except NonNumericException as ce:
            return "Something went wrong :"+str(ce)    
        except Exception as e:
            return "Something went wrong :"+(str(e))
    return render_template("add_product.html")

@app.route("/update_product/<string:pid>",methods=['POST','GET'])
def update_product_view(pid):
    try:
        if request.method=='POST':
            pname=request.form['pname']
            description=request.form['description']
            price=request.form['price']
            quantity=request.form['quantity']
            con=sql.connect("shopbridge.db")
            cur=con.cursor()
            cur.execute("update products set name=?,description=?,price=?,quantity=? where pid=?",(pname,description,price,quantity,pid))
            con.commit()
            flash('Product Updated','success')
            return redirect(url_for("index"))
        con=sql.connect("shopbridge.db")
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute("select * from products where pid=?",(pid,))
        data=cur.fetchone()
        return render_template("update_product.html",datas=data)
    except Exception as e:
            return "Something went wrong "+(str(e))

@app.route("/delete_product/<string:pid>",methods=['GET'])
def delete_product_view(pid):
    try:
        con=sql.connect("shopbridge.db")
        cur=con.cursor()
        cur.execute("delete from products where pid=?",(pid,))
        con.commit()
        flash('Product Deleted','warning')
        return redirect(url_for("index"))
    except Exception as e:
        return "Something went wrong "+(str(e))  
        
         

# API


@app.route("/api/products",methods = ['GET'])
def get_product_api():
    
    return jsonify(get_products())

@app.route("/api/product/add",methods=['POST','GET'])
def add_product_api():
    prod = request.get_json()
    return jsonify(create_product(prod))

@app.route("/api/product/<string:pid>",methods=['POST','GET'])
def get_product_byid(pid):
         
    return jsonify(get_product_by_id(pid))

@app.route("/api/product/update/",methods=['POST','GET'])
def update_product_api():
    product = request.get_json()
    return jsonify(update_product(product))


@app.route("/api/product/delete/<string:pid>",methods=['GET'])
def delete_product_api(pid):

    return jsonify(delete_product(pid))         
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)