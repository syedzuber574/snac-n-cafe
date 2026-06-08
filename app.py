from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    url_for
)

import sqlite3
import os

from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "snac_n_cafe_secret"

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    app.config["UPLOAD_FOLDER"],
    exist_ok=True
)


# -------------------------
# DATABASE
# -------------------------

def init_db():

    conn = sqlite3.connect(
        "database/menu.db"
    )

    cursor = conn.cursor()

    # MENU ITEMS

    cursor.execute("""
CREATE TABLE IF NOT EXISTS menu_items(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    price INTEGER NOT NULL,

    image TEXT NOT NULL,

    category TEXT NOT NULL,

    combo_contents TEXT
)
""")

    try:

        cursor.execute("""
        ALTER TABLE menu_items
        ADD COLUMN combo_contents TEXT
        """)

    except:

        pass

    # ORDERS

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        customer_name TEXT,

        phone TEXT,

        address TEXT,

        items TEXT,

        total INTEGER,

        date TEXT
    )
    """)

    conn.commit()

    conn.close()


# -------------------------
# GET CATEGORY ITEMS
# -------------------------

def get_items(category):

    conn = sqlite3.connect(
        "database/menu.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM menu_items
        WHERE category=?
        """,
        (category,)
    )

    items = cursor.fetchall()

    conn.close()

    return items


# -------------------------
# GET ALL ITEMS
# -------------------------

def get_all_items():

    conn = sqlite3.connect(
        "database/menu.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM menu_items
        ORDER BY id DESC
        """
    )

    items = cursor.fetchall()

    conn.close()

    return items


# -------------------------
# GET SINGLE ITEM
# -------------------------

def get_item(item_id):

    conn = sqlite3.connect(
        "database/menu.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM menu_items
        WHERE id=?
        """,
        (item_id,)
    )

    item = cursor.fetchone()

    conn.close()

    return item


# -------------------------
# GET ORDERS
# -------------------------

def get_orders():

    conn = sqlite3.connect(
        "database/menu.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM orders
        ORDER BY id DESC
        """
    )

    orders = cursor.fetchall()

    conn.close()

    return orders


# -------------------------
# ANALYTICS
# -------------------------

def analytics_data():

    conn = sqlite3.connect(
        "database/menu.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM menu_items"
    )

    total_items = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM orders"
    )

    total_orders = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT SUM(total)
        FROM orders
        """
    )

    revenue = cursor.fetchone()[0]

    if revenue is None:
        revenue = 0

    conn.close()

    return {
        "total_items": total_items,
        "total_orders": total_orders,
        "revenue": revenue
    }
# -------------------------
# HOME PAGE
# -------------------------

@app.route('/')
def home():
    return render_template(
        'index.html'
    )


# -------------------------
# CATEGORY PAGE FUNCTION
# -------------------------

@app.route('/burger')
def burger():

    items = get_items(
        "burger"
    )

    return render_template(
        'category.html',
        title="Burger",
        category="burger",
        items=items
    )


@app.route('/pizza')
def pizza():

    items = get_items(
        "pizza"
    )

    return render_template(
        'category.html',
        title="Pizza",
        category="pizza",
        items=items
    )


@app.route('/falooda')
def falooda():

    items = get_items(
        "falooda"
    )

    return render_template(
        'category.html',
        title="Falooda",
        category="falooda",
        items=items
    )


@app.route('/mojito')
def mojito():

    items = get_items(
        "mojito"
    )

    return render_template(
        'category.html',
        title="Mojito",
        category="mojito",
        items=items
    )


@app.route('/lemonade')
def lemonade():

    items = get_items(
        "lemonade"
    )

    return render_template(
        'category.html',
        title="Lemonade",
        category="lemonade",
        items=items
    )


@app.route('/smoothie')
def smoothie():

    items = get_items(
        "smoothie"
    )

    return render_template(
        'category.html',
        title="Smoothie",
        category="smoothie",
        items=items
    )


@app.route('/fries')
def fries():

    items = get_items(
        "fries"
    )

    return render_template(
        'category.html',
        title="Fries",
        category="fries",
        items=items
    )


@app.route('/quick_bites')
def quick_bites():

    items = get_items(
        "quick_bites"
    )

    return render_template(
        'category.html',
        title="Quick Bites",
        category="quick_bites",
        items=items
    )


@app.route('/momos')
def momos():

    items = get_items(
        "momos"
    )

    return render_template(
        'category.html',
        title="Momos",
        category="momos",
        items=items
    )


@app.route('/chinese')
def chinese():

    items = get_items(
        "chinese"
    )

    return render_template(
        'category.html',
        title="Chinese",
        category="chinese",
        items=items
    )


@app.route('/fried_chicken')
def fried_chicken():

    items = get_items(
        "fried_chicken"
    )

    return render_template(
        'category.html',
        title="Fried Chicken",
        category="fried_chicken",
        items=items
    )


@app.route('/rolls')
def rolls():

    items = get_items(
        "rolls"
    )

    return render_template(
        'category.html',
        title="Rolls",
        category="rolls",
        items=items
    )


@app.route('/sandwiches')
def sandwiches():

    items = get_items(
        "sandwiches"
    )

    return render_template(
        'category.html',
        title="Sandwiches",
        category="sandwiches",
        items=items
    )


@app.route('/milk_shakes')
def milk_shakes():

    items = get_items(
        "milk_shakes"
    )

    return render_template(
        'category.html',
        title="Milk Shakes",
        category="milk_shakes",
        items=items
    )


@app.route('/fresh_juices')
def fresh_juices():

    items = get_items(
        "fresh_juices"
    )

    return render_template(
        'category.html',
        title="Fresh Juices",
        category="fresh_juices",
        items=items
    )


@app.route('/combo')
def combo():

    items = get_items(
        "combo"
    )

    return render_template(
        'category.html',
        title="Combo",
        category="combo",
        items=items
    )


# -------------------------
# ABOUT
# -------------------------

@app.route('/about')
def about():
    return render_template(
        'about.html'
    )


# -------------------------
# CONTACT
# -------------------------

@app.route('/contact')
def contact():
    return render_template(
        'contact.html'
    )


# -------------------------
# CART
# -------------------------

@app.route('/cart')
def cart():
    return render_template(
        'cart.html'
    )


# -------------------------
# CHECKOUT
# -------------------------

@app.route('/checkout')
def checkout():
    return render_template(
        'checkout.html'
    )


# -------------------------
# ADMIN LOGIN
# -------------------------

@app.route(
    '/admin',
    methods=['GET', 'POST']
)
def admin():

    if request.method == 'POST':

        username =request.form[
                'username'
            ]

        password =request.form[
                'password'
            ]

        if (
            username == "admin"
            and
            password == "snac123"
        ):

            session[
                'admin_logged_in'
            ] = True

            return redirect(
                url_for(
                    'admin_dashboard'
                )
            )

    return render_template(
        'admin_login.html'
    )


# -------------------------
# DASHBOARD
# -------------------------
@app.route(
    '/admin-dashboard'
)
def admin_dashboard():

    if not session.get(
        'admin_logged_in'
    ):
        return redirect(
            url_for('admin')
        )

    return render_template(
        'admin_dashboard.html'
    )
@app.route(
    '/admin-add-item',
    methods=['GET', 'POST']
)
def admin_add_item():

    if not session.get(
        'admin_logged_in'
    ):
        return redirect(
            url_for('admin')
        )

    if request.method == 'POST':

        name = request.form['name']

        price = request.form['price']

        category = request.form['category']

        combo_contents = request.form.get(
            'combo_contents',
            ''
        )

        image_file = request.files['image']

        filename = ""

        if image_file:

            filename = secure_filename(
                image_file.filename
            )

            image_file.save(
                os.path.join(
                    app.config[
                        "UPLOAD_FOLDER"
                    ],
                    filename
                )
            )

        conn = sqlite3.connect(
            "database/menu.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO menu_items
            (
                name,
                price,
                image,
                category,
                combo_contents
            )
            VALUES
            (?, ?, ?, ?, ?)
            """,
            (
                name,
                price,
                filename,
                category,
                combo_contents
            )
        )

        conn.commit()

        conn.close()

        return redirect(
            url_for(
                'manage_items'
            )
        )

    return render_template(
        'admin_add_item.html'
    )
@app.route(
    '/manage-items'
)
def manage_items():

    if not session.get(
        'admin_logged_in'
    ):
        return redirect(
            url_for('admin')
        )

    items = get_all_items()

    return render_template(
        'manage_items.html',
        items=items
    )
@app.route(
    '/delete-item/<int:item_id>'
)
def delete_item(item_id):

    if not session.get(
        'admin_logged_in'
    ):
        return redirect(
            url_for('admin')
        )

    conn = sqlite3.connect(
        "database/menu.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM menu_items
        WHERE id=?
        """,
        (item_id,)
    )

    conn.commit()

    conn.close()

    return redirect(
        url_for('manage_items')
    )
@app.route(
    '/edit-item/<int:item_id>',
    methods=['GET', 'POST']
)
def edit_item(item_id):

    if not session.get(
        'admin_logged_in'
    ):
        return redirect(
            url_for('admin')
        )

    item = get_item(item_id)

    if request.method == 'POST':

        name = request.form['name']

        price = request.form['price']

        category = request.form['category']

        combo_contents = request.form.get(
            'combo_contents',
              ''
        )


        image_file = request.files['image']

        filename = item["image"]

        if image_file and image_file.filename:

            filename = secure_filename(
                image_file.filename
            )

            image_file.save(
                os.path.join(
                    app.config[
                        "UPLOAD_FOLDER"
                    ],
                    filename
                )
            )

        conn = sqlite3.connect(
            "database/menu.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE menu_items

            SET
            name=?,
            price=?,
            image=?,
            category=?,
            combo_contents=?

            WHERE id=?
            """,
            (
                name,
                price,
                filename,
                category,
                combo_contents,
                item_id
            )
        )

        conn.commit()

        conn.close()

        return redirect(
            url_for(
                'manage_items'
            )
        )

    return render_template(
        'edit_item.html',
        item=item
    )
@app.route(
    '/orders'
)
def orders():

    if not session.get(
        'admin_logged_in'
    ):
        return redirect(
            url_for('admin')
        )

    orders = get_orders()

    return render_template(
        'orders.html',
        orders=orders
    )
@app.route(
    '/analytics'
)
def analytics():

    if not session.get(
        'admin_logged_in'
    ):
        return redirect(
            url_for('admin')
        )

    data = analytics_data()

    return render_template(
        'analytics.html',
        data=data
    )
@app.route(
    '/save-order',
    methods=['POST']
)
def save_order():

    customer_name = request.form[
        'customer_name'
    ]

    phone = request.form[
        'phone'
    ]

    address = request.form[
        'address'
    ]

    items = request.form[
        'items'
    ]

    total = request.form[
        'total'
    ]

    date = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )

    conn = sqlite3.connect(
        "database/menu.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO orders
        (
            customer_name,
            phone,
            address,
            items,
            total,
            date
        )

        VALUES
        (?, ?, ?, ?, ?, ?)
        """,
        (
            customer_name,
            phone,
            address,
            items,
            total,
            date
        )
    )

    conn.commit()

    conn.close()

    return "success"
# -------------------------
# LOGOUT
# -------------------------

@app.route('/logout')
def logout():

    session.pop(
        'admin_logged_in',
        None
    )

    return redirect(
        url_for('admin')
    )


# -------------------------
# RUN APP
# -------------------------

if __name__ == '__main__':

    init_db()

    app.run(debug=True)