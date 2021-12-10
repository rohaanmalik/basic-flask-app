from flask import Flask, make_response, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route("/access-body", methods=["GET"])
def access_body():
    request_data = request.get_json()
    print(request_data)
    print(request.data)
    return request_data

@app.route("/access-params", methods=["POST"])
def accessingParam():
    print(request.args) # dict of params
    data = request.args.to_dict(flat=False)
    return jsonify(data)

@app.route("/access-form-data", methods=["POST"])
def access_form_data():
    print(request.form.get("form-data")) # access form data (kinda like body)
    data = request.form.to_dict(flat=False)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)