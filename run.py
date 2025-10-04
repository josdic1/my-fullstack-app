from backend import create_app

# Call the factory function to create the app instance
app = create_app()

if __name__ == '__main__':
    # Add the port argument here
    app.run(host='0.0.0.0', port=5555, debug=True)