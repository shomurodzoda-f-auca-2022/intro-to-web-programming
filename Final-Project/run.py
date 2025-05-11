from app import create_app, seed_movies

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        seed_movies()