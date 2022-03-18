import management
from flask import Flask, request
from spartan import Spartan

flask_obj = Flask(__name__)


@flask_obj.route("/", methods=["GET"])
def homepage():
    return f"HOMEPAGE\n An API call is the process of a client application submitting a request to a server's API." \
           f" An API call also comprises everything that happens after the request is submitted, including when the API" \
           f" retrieves information from the server and delivers it back to the client."


@flask_obj.route("/spartan/add", methods=["POST"])
def spartan_add():
    spartan_details = request.json
    if len(spartan_details["first_name"]) >= 2:
        spartan_first_name = spartan_details["first_name"]
    else:
        return "Error, the Spartans First Name should be at least 2 Characters"
    if len(spartan_details["last_name"]) >= 2:
        spartan_last_name = spartan_details["last_name"]
    else:
        return "Error, the Spartans Second Name should be at least 2 Characters"
    if int(spartan_details["birth_year"]) in range(1900, 2004):
        spartan_birth_year = spartan_details["birth_year"]
    else:
        return "ERROR, the Spartans birth year should be a number between 1900 and 2004."
    if int(spartan_details["birth_month"]) in range(1, 13):
        spartan_birth_month = spartan_details["birth_month"]
    else:
        return "ERROR, the Spartans birth month should be a number between 1 and 12."
    if int(spartan_details["birth_day"]) in range(1, 32):
        spartan_birth_day = spartan_details["birth_day"]
    else:
        return "ERROR, the Spartans birth day should be a number between 1 and 31."
    if len(spartan_details["course"]) >= 2:
        spartan_course = spartan_details["course"]
    else:
        return "ERROR, the Spartans Course name should have at least 2 characters."
    if len(spartan_details["stream"]) >= 2:
        spartan_stream = spartan_details["stream"]
    else:
        return "ERROR, the Spartans Stream name should have at least 2 characters."
    if int(spartan_details["id"] > 1):
        if spartan_details["id"] in management.spartan_dict:
            return "ID already in database."
    else:
        spartan_id = spartan_details["sparta_id"]

    return f"ID: {spartan_id}\nfirst name: {spartan_first_name}\nlast name: {spartan_last_name}\nDOB: {spartan_birth_day}/" \
           f"{spartan_birth_month}/{spartan_birth_year}" \
           f"\ncourse: {spartan_course}\nstream: {spartan_stream}"


@flask_obj.route('/spartan/<spartan_id>', methods=['GET'])
def get_id():


if __name__ == "__main__":
    flask_obj.run()

# if __name__ == "__main__":
#
#     while True:
#         user_input = management.read_option()
#
#         if user_input == '1':
#             management.add_spartan()
#             management.save_add_to_json()
#         elif user_input == '2':
#             management.remove_spartan()
#         elif user_input == '3':
#             management.list_spartans()
#         elif user_input == '4':
#             management.retrieve_spartan()
#         elif user_input == '5':
#             break
