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
    Displays the application homepage.
    """
    return render_template("homepage.html", title="Home")


# Render existing posts function
@app.route("/get_posts")
def get_posts():
    """
    Fetches all blog posts from the database, renders the
    main blog posts page and displays all existing blog posts
    to the page.
    """
    posts = list(coll_posts.find())
    favourites = coll_users.find_one(
            {"username": session["user"]})["fav_posts"]
    return render_template(
        "posts.html",
        posts=posts,
        favourites=favourites,
        title="Blogs")


# Search function
@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Enables the user to search within the Post Title and Post Content
    for all existing blog posts. Renders the main blog post page with
    returned posts.
    """
    query = request.form.get("query")
    posts = list(coll_posts.find(
        {"$text": {"$search": query}}))
    return render_template("posts.html", posts=posts, title="Blogs")


# Create account function
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Checks if the submitted username already exists in the database.
    If it does then user is presented with flash message. Otherwise,
    inputted user info is collated and passed to the databse. The new
    user is then put into session, with the Profile page rendered.
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

    return render_template("signup.html", title="Sign Up")


# Login function
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks if the submitted username exists in the database. If
    username doesn't exist, flash message appears. If username
    does exits, it checks that the input password matches with
    the username. If it does match, user is put into a user
    session. If the password does not match, a flash message is
    presented to user.
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
                    "profile", username=session["user"], title="Profile"))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login", title="Login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html", title="Login")


# Render user's profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Accesses user's name from database and displays on
    profile page.
    If user is in session, identifies user's own blog
    posts and those user has "favourited" and displays
    them on the rendered Profile page.
    """
    if session["user"]:
        current_user = coll_users.find_one(
            {"username": session["user"]})["_id"]
        user_id = coll_users.find_one(
            {"username": username})["_id"]

        if current_user == user_id:
            # Grab session user's name from database
            first_name = coll_users.find_one(
                {"username": session["user"]})["first_name"]

            # Grabs user posts and favourites from database
            own_posts = coll_users.find_one(
                {"username": username})["user_posts"]
            fav_posts = coll_users.find_one(
                {"username": username})["fav_posts"]

            favourites = coll_users.find_one(
                {"username": session["user"]})["fav_posts"]

            user_posts = coll_posts.find(
                {"_id": {"$in": own_posts}})
            user_favs = coll_posts.find(
                {"_id": {"$in": fav_posts}})

            return render_template(
                "profile.html",
                first_name=first_name,
                user_posts=user_posts,
                user_favs=user_favs,
                favourites=favourites,
                title="Profile")

        else:
            flash("Sorry! You're not authorised to view that page")
            return redirect(url_for("get_posts"))

    else:
        flash("Sorry! You need to be logged in to view that page")
        return redirect(url_for("login"))


# Logout function
@app.route("/logout")
def logout():
    """
    Logs user out, deleting the user's session cooke.
    Renders the Login page.
    """
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Create new post function
@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    """
    Identifies the current user's id. Collates the blog
    post inputs and inserts them to the database - both
    in the Posts collection and in the Users user_posts
    section. Renders the main blog posts page and displays
    the new post, along with all other existing posts.
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

        flash("Post Successfully Published!")
        return redirect(url_for("get_posts", post_id=insertPost.inserted_id))

    categories = coll_categories.find().sort("category_name", 1)
    return render_template(
        "new_post.html",
        categories=categories,
        title="New Post")


# Edit user's post function
@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """
    Takes submitted user inputs, updates to database and
    displays updated post on main blog post page, along
    with other existing posts.
    """
    if request.method == "POST":
        publish = {
            "category_name": request.form.get("category_name"),
            "post_title": request.form.get("post_title"),
            "post_content": request.form.get("post_content"),
            "created_by": session["user"]
        }
        coll_posts.update({"_id": ObjectId(post_id)}, publish)
        flash("Post Updated!")
        return redirect(url_for("get_posts"))

    post = coll_posts.find_one({"_id": ObjectId(post_id)})
    categories = coll_categories.find().sort("category_name", 1)
    return render_template(
        "edit_post.html",
        post=post,
        categories=categories,
        title="Edit Post")


# Delete user's post function
@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    """
    Identifies current user. Accesses posts on
    database and deletes the post with the identified
    ObjectId. Also deletes post from User's user_posts
    section. Displays flash message and renders main
    blog post page, now without deleted post.
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
    Identifies the current user's ObjectId and the "liked"
    post's ObjectId. Pushes the "liked" post's ObjectId
    to the user's fav_posts document in the User Collection
    in MongoDB. Also increments the post's favourites
    document in the Posts Collection by one.
    """
    if session["user"]:
        user = coll_users.find_one(
            {"username": session["user"]})["_id"]
        coll_users.update_one(
            {"_id": ObjectId(user)},
            {"$push": {"fav_posts": ObjectId(post_id)}})
        coll_posts.update(
            {"_id": ObjectId(post_id)}, {"$inc": {"favourites": 1}})
        return redirect(url_for("get_posts", post_id=post_id))


# Remove post from user's favourites function
@app.route("/remove_favourite/<post_id>")
def remove_favourite(post_id):
    """
    Identifies the current user's ObjectId and the
    "unliked" post's ObjectId. Pulls the "unliked" post's
    ObjectId from the user's fav_posts document in the User
    Collection in MongoDB. Also decrements the post's
    favourites
    document in the Posts Collection by one.
    """
    if session["user"]:
        user = coll_users.find_one(
            {"username": session["user"]})["_id"]
        coll_users.update_one(
            {"_id": ObjectId(user)},
            {"$pull": {"fav_posts": ObjectId(post_id)}})
        coll_posts.update(
            {"_id": ObjectId(post_id)}, {"$inc": {"favourites": -1}})
        return redirect(url_for("get_posts", post_id=post_id))


# Display categories function
@app.route("/get_categories")
def get_categories():
    """
    Accesses list of categories from database, sorts into
    alphabetical order, and displays categories page.
    """
    categories = list(coll_categories.find().sort("category_name", 1))
    return render_template(
        "categories.html",
        categories=categories,
        title="Blog Categories")


# Create new category function
@app.route("/new_category", methods=["GET", "POST"])
def new_category():
    """
    Takes new category name submitted via form and inserts
    to categories collection on database. Then, renders
    the categories page, now updated with the new category.
    Flash message appears to confirm update was successful.
    """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        coll_categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))
    return render_template("new_category.html", title="New Category")


# Edit category function
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    Takes submitted user inputs, updates to database and
    displays updated category on categories page, along
    with other existing categories.
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        coll_categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Updated")
        return redirect(url_for("get_categories"))

    category = coll_categories.find_one({"_id": ObjectId(category_id)})
    return render_template(
        "edit_category.html",
        category=category,
        title="Edit Category")


# Delete category function
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    Identifies category via ObjectId and removes from
    categories section in the database. Flash message
    displayed to confirm deletion and main categories
    page rendered, now without the deleted category.
    """
    coll_categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
