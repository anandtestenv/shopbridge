
import sqlite3 as sql

# Add product utility function

def create_product(product):
    prod_created = {}
    try:
        con=sql.connect("shopbridge.db")
        cur=con.cursor()
        cur.execute("insert into products(name,description,price,quantity) values (?,?,?,?)",(product['name'],product['description'],product['price'],product['quantity']))
        con.commit()
        prod_created= get_product_by_id(cur.lastrowid)
    except:
        prod_created={}
        con().rollback()

    finally:
        con.close() 

    return prod_created  


# Get single product by product ID
def get_product_by_id(pid):
    prod = {}
    try:
        con=sql.connect("shopbridge.db")
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute("select * from products where pid = ?",(pid,))
        row = cur.fetchone()
        # convert sql row object to prod dictionary
        prod["pid"] = row["pid"]
        prod["name"] = row["name"]
        prod["price"] = row["price"]
        prod["description"] = row["description"]
        prod["quantity"] = row["quantity"]
        
    except:
        prod = {}

    return prod            

# Get all product list utility         
def get_products():
    products =[]
    try:
        con=sql.connect("shopbridge.db")
        con.row_factory=sql.Row
        cur=con.cursor()
        cur.execute("select * from products")
        data=cur.fetchall()
        for row in data:
            prod={}
            prod['pid'] = row['pid']
            prod['name'] = row['name']
            prod['description'] = row['description']
            prod["price"] = row["price"]
            prod['quantity'] = row['quantity']
            products.append(prod)
        
    except Exception as e:
        products=[]
    return products

# update product utility        
def  update_product(product):
    prod_updated = {}
    try:
        con=sql.connect("shopbridge.db")
        cur=con.cursor()
        cur.execute("update products set name=?,description=?,price=?,quantity=? where pid=?",(product['name'],product['description'],product['price'],product['quantity'],product['pid']))
        con.commit()
        prod_updated= get_product_by_id(product['pid'])
    except:
        prod_updated={}
        con().rollback()

    finally:
        con.close() 

    return product

# delete product utility
     
def delete_product(pid):
    message = {}
    try:
        con=sql.connect("shopbridge.db")
        cur=con.cursor()
        cur.execute("delete from products where pid=?",(pid,))
        con.commit()
        message["status"] = "Product deleted successfully"
    except:
        con.rollback()
        message["status"] = "Product cannot be deleted"
    finally:
        con.close()

    return message



