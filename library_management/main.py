from flask import Flask, jsonify
from app.presentation.routes.book_routes import book_bp
from app.presentation.routes.member_routes import member_bp
from app.helper.exceptions import *
from pydantic import ValidationError



app = Flask(__name__)

#Register Blueprints
#connects route files to the main app.
app.register_blueprint(book_bp, url_prefix="/books")

#rl_prefix="/books": Means every route in book_routes.py will start with:
app.register_blueprint(member_bp, url_prefix="/members")




#Global error handler for ValueError from Service Layer 
#It works whenever Service Layer raises ValueError message
#Flask here is automatically returns the message I have defined in the Service Layer
@app.errorhandler(ValueError)
def handle_value_error(e):
    return jsonify({"error": str(e)}), 400

#Global error handler that Catch ANY unexpected error,
#e.g: Database connection crash,Bug in code,Missing fields, .. the return code is 500 means Internal Server Error

@app.errorhandler(ValidationError)
def handle_pydantic_error(e):
    return {"error": e.errors()}, 400



@app.errorhandler(NotFoundError)
def handle_not_found(e):
    return jsonify({"error": str(e)}), 404


@app.errorhandler(AlreadyExistsError)
def handle_exists(e):
    return jsonify({"error": str(e)}), 400


@app.errorhandler(BorrowError)
def handle_borrow_error(e):
    return jsonify({"error": str(e)}), 400


@app.errorhandler(Exception)
def handle_general_error(e):
    return jsonify( {"error": "Internal server error"}), 500



if __name__ == "__main__":
    app.run(debug=True)
