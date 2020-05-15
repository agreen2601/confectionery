import sqlite3
from django.shortcuts import render
from icecreamapp.models import Variety
from ..connection import Connection
from django.urls import reverse
from django.shortcuts import redirect

def variety_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                v.id,
                v.name,
                v.country_of_origin
            FROM
                icecreamapp_variety v
            ORDER BY "name"
            """)

            all_varieties = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                variety = Variety()
                variety.id = row['id']
                variety.name = row['name']
                variety.country_of_origin = row['country_of_origin']

                all_varieties.append(variety)

        template = 'varieties/varieties_list.html'
        context = {
            'varieties': all_varieties
        }

        return render(request, template, context)

    # elif request.method == 'POST':
    #     form_data = request.POST

    #     with sqlite3.connect(Connection.db_path) as conn:
    #         db_cursor = conn.cursor()

    #         db_cursor.execute("""
    #         INSERT INTO hrapp_employee (first_name, last_name, start_date, department_id, is_supervisor)
    #         VALUES (?, ?, ?, ?, 0)
    #         """,
    #         (form_data['first_name'], form_data['last_name'], form_data['start_date'], form_data['department']))

    #     return redirect(reverse('hrapp:employees'))