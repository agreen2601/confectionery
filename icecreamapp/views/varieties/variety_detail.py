import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from icecreamapp.models import Variety, Flavor, VarietyFlavor
from ..connection import Connection

variety = Variety()
# variety.flavors = []

def create_variety(cursor, row):
    _row = sqlite3.Row(cursor, row)

    variety.id = _row["variety_id"]
    variety.name = _row["variety_name"]
    variety.country_of_origin = _row["country_of_origin"]

    return (variety)


def create_variety_flavors(cursor, row):
    _row = sqlite3.Row(cursor, row)

    flavor = Flavor()
    flavor.id = _row["flavor_id"]
    flavor.name = _row["flavor_name"]
    flavor.alcohol_percent = _row["alcohol_percent"]
    flavor.toppings = _row["toppings"]

    return flavor


def get_variety(variety_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_variety
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            v.id as variety_id,
            v.name as variety_name,
            v.country_of_origin
        FROM 
            icecreamapp_variety v
        WHERE 
            v.id = ?
        """, (variety_id,))

    data = db_cursor.fetchone()

    return data


def get_variety_flavors(variety_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_variety_flavors
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            f.name as flavor_name,
            f.alcohol_percent,
            f.id as flavor_id,
            vf.toppings
        FROM 
            icecreamapp_variety v
            JOIN icecreamapp_varietyflavor vf on vf.variety_id = v.id
            LEFT JOIN icecreamapp_flavor f on f.id = vf.flavor_id
        WHERE 
            v.id = ?
        """, (variety_id,))

        data = db_cursor.fetchall()

        return data


def variety_detail(request, variety_id):
    if request.method == 'GET':
        variety = get_variety(variety_id)
        flavors = get_variety_flavors(variety_id)
        template_name = 'varieties/variety_details.html'
        context = {
            "variety": variety,
            "flavors": flavors
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE icecreamapp_variety
                SET country_of_origin = ?
                WHERE id = ?
                """,
                (
                    form_data['country_of_origin'], variety_id,
                ))

        return redirect(reverse('icecreamapp:varieties'))