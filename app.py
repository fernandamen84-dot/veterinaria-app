from flask import Flask, render_template, request, redirect, url_for
from db import get_db_connection

app = Flask(__name__)


# =========================
# READ - Mostrar pacientes
# =========================
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM pacientes ORDER BY id DESC")
    pacientes = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', pacientes=pacientes)


# =========================
# CREATE - Agregar paciente
# =========================
@app.route('/agregar', methods=['POST'])
def agregar():

    nombre = request.form['nombre']
    especie = request.form['especie']
    dueno = request.form['dueno']
    telefono = request.form['telefono']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO pacientes
        (nombre, especie, dueno, telefono)
        VALUES (%s, %s, %s, %s)
        """,
        (nombre, especie, dueno, telefono)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('index'))


# =========================
# UPDATE - Editar paciente
# =========================
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':

        nombre = request.form['nombre']
        especie = request.form['especie']
        dueno = request.form['dueno']
        telefono = request.form['telefono']

        cursor.execute(
            """
            UPDATE pacientes
            SET nombre=%s,
                especie=%s,
                dueno=%s,
                telefono=%s
            WHERE id=%s
            """,
            (nombre, especie, dueno, telefono, id)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    cursor.execute(
        "SELECT * FROM pacientes WHERE id = %s",
        (id,)
    )

    paciente = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template(
        'editar.html',
        paciente=paciente
    )


# =========================
# DELETE - Eliminar paciente
# =========================
@app.route('/eliminar/<int:id>')
def eliminar(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM pacientes WHERE id = %s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('index'))


# =========================
# Ejecutar aplicación
# =========================
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=80,
        debug=True
    )

