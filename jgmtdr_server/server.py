from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json
from recipes_db import RecipesDB

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("The Path is:", self.path)
        parts = self.path.split('/')
        collection = parts[1]
        if len(parts) > 2:
            member_id = parts[2]
        else:
            member_id = None
        if collection == "recipes":
            if member_id:
                self.handleGetOneRecipe(member_id)
            else:
                self.handleGetRecipes()
        if collection == "users":
            if member_id:
                self.handleGetOneUser(member_id)
            else:
                self.handleNotFound()

    def do_POST(self):
        if self.path == "/recipes":
            self.handleCreateRecipe()
        elif self.path == "/users":
            self.handleCreateUser()
        else:
            self.handleNotFound()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


    def do_DELETE(self):
        print("The Path is:", self.path)
        parts = self.path.split('/')
        collection = parts[1]
        if len(parts) > 2:
            member_id = parts[2]
        else:
            member_id = None
        if collection == "recipes":
            if member_id:
                self.handleDeleteOneRecipe(member_id)
            else:
                self.handleNotFound()
        if collection == "users":
            if member_id:
                self.handleDeleteOneUser(member_id)
            else:
                self.handleNotFound()

    def do_PUT(self):
        print("The Path is:", self.path)
        parts = self.path.split('/')
        collection = parts[1]
        if len(parts) > 2:
            member_id = parts[2]
        else:
            member_id = None
        if collection == "recipes":
            if member_id:
                self.handleUpdateOneRecipe(member_id)
            else:
                self.handleNotFound()
        if collection == "users":
            if member_id:
                self.handleUpdateOneUser(member_id)
            else:
                self.handleNotFound()

    def handleNotFound(self):
            self.send_response(404)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes("Not Found", "utf-8"))

    def handleForbidden(self):
            self.send_response(403)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes("Forbidden", "utf-8"))

    def handleUnprocessableEntity(self):
            self.send_response(422)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes("Unprocessable Entity", "utf-8"))
#################Get Functions#####################################
    
    def handleGetRecipes(self):
            # 1. Send a status code
            self.send_response(200)
            # 2. Send any headers
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            # 3. Finish headers (whether we have headers or not)
            self.end_headers()
            # 4. Send a body to the client.
            db = RecipesDB()
            allRecipes = db.getAllRecipes()
            self.wfile.write(bytes(json.dumps(allRecipes), "utf-8"))

    def handleGetOneRecipe(self, member_id):
            db = RecipesDB()
            one_recipe = db.getOneRecipe(member_id)
            if one_recipe != None:
                # 1. Send a status code 
                self.send_response(200)
                # 2. Send any headers
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                # 3. Finish headers (whether we have headers or not)
                self.end_headers()
                # 4. Send a body to the client.
                self.wfile.write(bytes(json.dumps(one_recipe), "utf-8"))
            else:
                self.handleNotFound()

    def handleGetOneUser(self, email):
            db = RecipesDB()
            one_user = db.getOneUser(email)
            if one_user != None:
                # 1. Send a status code 
                self.send_response(200)
                # 2. Send any headers
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                # 3. Finish headers (whether we have headers or not)
                self.end_headers()
                # 4. Send a body to the client.
                self.wfile.write(bytes(json.dumps(one_user), "utf-8"))
            else:
                self.handleNotFound()

############################Delete Functions#############################

    def handleDeleteOneRecipe(self, member_id):
            db = RecipesDB()
            one_recipe = db.getOneRecipe(member_id)
            if one_recipe != None:
                db.deleteOneRecipe(member_id)
                # 1. Send a status code
                self.send_response(200)
                # 2. Send any headers
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                # 3. Finish headers (whether we have headers or not)
                self.end_headers()
            else:
                self.handleNotFound()

    def handleDeleteOneUser(self, email):
            db = RecipesDB()
            one_user = db.getOneUser(email)
            if one_user != None:
                db.deleteOneUser(email)
                # 1. Send a status code
                self.send_response(200)
                # 2. Send any headers
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                # 3. Finish headers (whether we have headers or not)
                self.end_headers()
            else:
                self.handleNotFound()

##########################Update Functions#############################

    def handleUpdateOneRecipe(self, member_id):
            db = RecipesDB()
            one_recipe = db.getOneRecipe(member_id)
            if one_recipe != None:
                #1. read the request body
                length = self.headers['Content-length']
                body = self.rfile.read(int(length)).decode("utf-8")
                print("the Body:", body)

                #2. Parse the body into usable data
                parsed_body = parse_qs(body)
                print("parsed BODY:", parsed_body)

                #3. append the new data to our data
                title = parsed_body["title"][0]
                diet = parsed_body["diet"][0]
                ingredients = parsed_body["ingredients"][0]
                instructions = parsed_body["instructions"][0]
                db = RecipesDB()
                db.updateRecipe(title, diet, ingredients, instructions, member_id)

                #4. send a response to the client
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
            else:
                self.handleNotFound()

    def handleUpdateOneUser(self, email):
            db = RecipesDB()
            one_user = db.getOneUser(email)
            if one_user != None:
                #1. read the request body
                length = self.headers['Content-length']
                body = self.rfile.read(int(length)).decode("utf-8")
                print("the Body:", body)

                #2. Parse the body into usable data
                parsed_body = parse_qs(body)
                print("parsed BODY:", parsed_body)

                #3. append the new data to our data
                firstName = parsed_body["firstName"][0]
                lastName = parsed_body["lastName"][0]
                email = parsed_body["email"][0]
                db = RecipesDB()
                db.updateUser(firstName, lastName, email)

                #4. send a response to the client
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
            else:
                self.handleNotFound()

###################################Create Functions##############################

    def handleCreateRecipe(self):
            #1. read the request body
            length = self.headers['Content-length']
            body = self.rfile.read(int(length)).decode("utf-8")
            print("the Body:", body)

            #2. Parse the body into usable data
            parsed_body = parse_qs(body)
            print("parsed BODY:", parsed_body)

            #3. append the new data to our data
            title = parsed_body["title"][0]
            diet = parsed_body["diet"][0]
            ingredients = parsed_body["ingredients"][0]
            instructions = parsed_body["instructions"][0]
            db = RecipesDB()
            db.insertRecipe(title, diet, ingredients, instructions)

            #4. send a response to the client
            self.send_response(201)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

    def handleCreateUser(self):
            #1. read the request body
            length = self.headers['Content-length']
            body = self.rfile.read(int(length)).decode("utf-8")
            print("the Body:", body)

            #2. Parse the body into usable data
            parsed_body = parse_qs(body)
            print("parsed BODY:", parsed_body)

            #3. append the new data to our data
            firstName = parsed_body["firstName"][0]
            lastName = parsed_body["lastName"][0]
            email = parsed_body["email"][0]
            password = parsed_body["password"][0]
            db = RecipesDB()
            if db.getOneUser(email) == None:
                db.insertUser(firstName, lastName, email, password)

                #4. send a response to the client
                self.send_response(201)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
            else:
                self.handleUnprocessableEntity()

def run():
    listen = ("127.0.0.1", 8080)
    server = HTTPServer(listen, MyHTTPRequestHandler)
    server.serve_forever()

run()
