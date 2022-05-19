from sgp import app, db
from sgp.models import Student, SuperAdmin, admin

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Student': Student, 'SuperAdmin': SuperAdmin, 'admin': admin}

if __name__ == "__main__":
    app.run(debug=True)