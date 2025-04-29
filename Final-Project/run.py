from app import create_app, seed_movies

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        seed_movies()
    app.run(debug=True)