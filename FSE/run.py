from fse import app, db

if __name__ == '__main__':
    db.create_all()
    app.run(host="localhost", port=8000, debug=True)
