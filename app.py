import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Collections
coll_users = mongo.db.users
coll_posts = mongo.db.posts
coll_categories = mongo.db.categories


# Render homepage function
@app.route("/")
@app.route("/homepage")
def homepage():
    """
    """
    return render_template("homepage.html", title="Home")


# Render existing posts function
@app.route("/get_posts")
def get_posts():
    """
    """
    posts = list(coll_posts.find())
    return render_template("posts.html", posts=posts, title="Blogs")


# Search function
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    """
    query = request.form.get("query")
    posts = list(coll_posts.find(
        {"$text": {"$search": query}}))
    return render_template("posts.html", posts=posts, title="Blogs")


# Create account function
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    """
    if request.method == "POST":
        # Check if username already exists in database
        existing_user = coll_users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        user = {
            "first_name": request.form.get("firstname").lower(),
            "last_name": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "user_posts": [],
            "fav_posts": []
        }
        coll_users.insert_one(user)

        # Put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


# Login function
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    """
    if request.method == "POST":
        # Check if username exists in database
        existing_user = coll_users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Render user's profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    """
    # Grab session user's name from database
    first_name = coll_users.find_one(
        {"username": session["user"]})["first_name"]
    
    if session["user"]:
        return render_template("profile.html", first_name=first_name)

    return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    """
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Create new post function
@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    """
    """
    if request.method == "POST":

        poster = coll_users.find_one({"username": session["user"]})["_id"]

        post = {
            "category_name": request.form.get("category_name"),
            "post_title": request.form.get("post_title"),
            "post_content": request.form.get("post_content"),
            "created_by": session["user"],
            "poster": poster,
            "favourites": 0
        }
        insertPost = coll_posts.insert_one(post)
        coll_users.update_one(
            {"_id": ObjectId(poster)},
            {"$push": {"user_posts": insertPost.inserted_id}}
        )
        coll_categories.update_one(
            {"category_name": "post.category_name"},
            {"$push": {"category_posts": insertPost.inserted_id}}
        )
        flash("Post Successfully Published!")
        return redirect(url_for("get_posts", post_id=insertPost.inserted_id))

    categories = coll_categories.find().sort("category_name", 1)
    return render_template("new_post.html", categories=categories)


# Edit user's post function
@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """
    """
    if request.method == "POST":
        publish = {
            "category_name": request.form.get("category_name"),
            "post_title": request.form.get("post_title"),
            "post_content": request.form.get("post_content"),
            "created_by": session["user"]
        }
        coll_posts.update({"_id": ObjectId(post_id)}, publish)
        flash("Post Successfully Updated")
        return redirect(url_for("get_posts"))

    post = coll_posts.find_one({"_id": ObjectId(post_id)})
    categories = coll_categories.find().sort("category_name", 1)
    return render_template("edit_post.html", post=post, categories=categories)


# Delete user's post function
@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    """
    """
    user = coll_posts.find_one(
        {"_id": ObjectId(post_id)})["poster"]
    coll_posts.remove(
        {"_id": ObjectId(post_id)})
    coll_users.update_one(
        {"_id": ObjectId(user)},
        {"$pull": {"user_posts": ObjectId(post_id)}}
    )
    flash("Post Successfully Deleted")
    return redirect(url_for("get_posts"))


# Add post to user's favourites function
@app.route("/add_favourite/<post_id>")
def add_favourite(post_id):
    """
    """
    if "user" in session:
        user = coll_users.find_one(
            {"username": session["user"]})["_id"]
        coll_users.update_one(
            {"_id": ObjectId(user)}, 
            {"$push": {"fav_posts": ObjectId(post_id)}})
        coll_posts.update(
            {"_id": ObjectId(post_id)}, {"$inc": {"favourites": 1}})
        return redirect(url_for("get_posts", post_id=post_id))
    else:
        flash("Log in to like this blog")


# Remove post from user's favourites function
@app.route("/remove_favourite/<post_id>")
def remove_favourite(post_id):
    """
    """
    if "user" in session:
        user = coll_users.find_one(
            {"username": session["user"]})["_id"]
        coll_users.update_one(
            {"_id": ObjectId(user)}, 
            {"$pull": {"fav_posts": ObjectId(post_id)}})
        coll_posts.update(
            {"_id": ObjectId(post_id)}, {"$inc": {"favourites": -1}})
        return redirect(url_for("get_posts", post_id=post_id))
    else:
        flash("Log in to complete this action")


# Render categories function
@app.route("/get_categories")
def get_categories():
    """
    """
    categories = list(coll_categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Create new category function
@app.route("/new_category", methods=["GET", "POST"])
def new_category():
    """
    """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_posts": []
        }
        coll_categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))
    return render_template("new_category.html")


# Edit category function
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        coll_categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = coll_categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete category function
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    """
    coll_categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
