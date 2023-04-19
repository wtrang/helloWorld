from app import app, db
from models import Customer, User, Product
from werkzeug.security import generate_password_hash

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of customers
    customers = [
        {'user_id': 1}
    ]

    for each_customer in customers:
        print(f'{each_customer["user_id"]} inserted into customer')
        a_customer = Customer(each_customer["user_id"])
        db.session.add(a_customer)
        db.session.commit()

    # Initial loading of users
    users = [
        {'username': 'olive', 'email': 'opurchess@gmail.com', 'first_name':'Olive', 'last_name':'Perchases',
            'password': generate_password_hash('olive', method='sha256'), 'role':'CUSTOMER'},
        {'username': 'admin', 'email': 'abyer@my-store.com', 'first_name':'Anita', 'last_name':'Byer',
            'password': generate_password_hash('adminpw', method='sha256'), 'role':'ADMIN'}
    ]

    for each_user in users:
        print(f'{each_user["username"]} inserted into user')
        a_user = User(username=each_user["username"], email=each_user["email"], first_name=each_user["first_name"],
                      last_name=each_user["last_name"], password=each_user["password"], role=each_user["role"])
        db.session.add(a_user)
        db.session.commit()

    # Initial loading of products
    products = [
        {'product_name':'Hat', 'product_code':'PROD-0555', 'product_description':'Show your Terp spirit by wearing this stylish hat.',
            'product_image':'PROD-0555-hat.png', 'product_price':14.95},
        {'product_name': 'Men\'s Pullover Jacket', 'product_code': 'PROD-0123', 'product_description': 'This jacket will keep you warm and snuggly on those cold nights.',
            'product_image': 'PROD-0123-pullover-jacket.png', 'product_price':39.99},
        {'product_name': 'Prep School Ringspun T-Shirt', 'product_code': 'PROD-0987', 'product_description': 'Maryland Terrapins Prep School Ringspun S/S Tee red',
            'product_image': 'PROD-0987-t-shirt.png', 'product_price':31.48},
        {'product_name': 'Framing Success 13 x 17 Greystone Gold Medallion Bachelors, Masters Diploma Frame', 'product_code': 'PROD-0407',
         'product_description': 'FSC certified hardwood from well-managed forests features an anthracite veneer with an inner accent trim. Our Grey Suede/Gold mat features a gold-minted medallion of the official University seal and embossed University name. Made in the USA.',
         'product_image': 'PROD-0407-diploma.png', 'product_price': 235.00}
    ]

    for each_product in products:
        print(f'{each_product["product_name"]} inserted into product')
        a_product = Product(product_name=each_product['product_name'], product_code=each_product['product_code'],
                            product_description=each_product['product_description'], product_image=each_product['product_image'],
                            product_price=each_product['product_price'])
        db.session.add(a_product)
        db.session.commit()

