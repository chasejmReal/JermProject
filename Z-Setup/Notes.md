## NOTES ##

# Making changes to models
- delete Delete the migration files in the migrations/ directory for each app. Or just delete the folder 
- Re-run the following 
    - python manage.py makemigrations
    - python manage.py migrate


# Opening the app from another Device
to access your Django server from another device, you'll need to 
make the server listen on a public IP address instead of just 127.0.0.1 (localhost). Here's how you can do it:
    ...super long process that I found on ChatGPT...in toher words, its complicated 

# CODE FOR LATER: 

# C1
<!-- home.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jerm.io</title>
    <link rel="icon" type="germ/jpg" href="Images/germ.jpg">
    <style>
        /* Reset and Base Styling */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        body {
            background: linear-gradient(to bottom, #ff7eb3, #ff758c);
            color: white;
            text-align: center;
        }
        header {
            padding: 20px;
            font-size: 1.5rem;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 0.3);
        }
        .container {
            margin: 50px auto;
            width: 80%;
            max-width: 600px;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        }
        .container h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        .input-group {
            margin: 15px 0;
        }
        input[type="text"],
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 10px;
            outline: none;
            font-size: 1rem;
        }
        button {
            background: #ff5757;
            color: white;
            font-size: 1rem;
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        button:hover {
            background: #ff1e56;
        }
        .footer {
            margin-top: 30px;
            font-size: 0.9rem;
        }
        .footer a {
            color: #fff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        ❤️ Welcome to Jerm-Sexy-Chat ❤️
    </header>
    <div class="container">
        <h1>Talk with a REAL man</h1>
        <form>
            <div class="input-group">
                <input type="text" placeholder="Enter your name" required>
            </div>
            <div class="input-group">
                <input type="email" placeholder="Enter your email" required>
            </div>
            <div class="input-group">
                <input type="password" placeholder="Create a password" required>
            </div>
            <div class="input-group">
                <button type="submit">Sign Up</button>
            </div>
        </form>
        <p class="footer">Already a member? <a href="{% url 'create_account' %}">Login Here</a></p>   <!-- We define the url here -->
        </a>
    </p>
    </div>
</body>
</html>


# C2
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jerm.io</title>
    <link rel="icon" type="germ/jpg" href="Images/germ.jpg">
    <style>
        /* Reset and Base Styling */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        body {
            background: linear-gradient(to bottom, #ff7eb3, #ff758c);
            color: white;
            text-align: center;
        }
        header {
            padding: 20px;
            font-size: 1.5rem;
            font-weight: bold;
            background-color: rgba(0, 0, 0, 0.3);
        }
        .container {
            margin: 50px auto;
            width: 80%;
            max-width: 600px;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        }
        .container h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        .input-group {
            margin: 15px 0;
        }
        input[type="text"],
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 10px;
            outline: none;
            font-size: 1rem;
        }
        button {
            background: #ff5757;
            color: white;
            font-size: 1rem;
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        button:hover {
            background: #ff1e56;
        }
        .footer {
            margin-top: 30px;
            font-size: 0.9rem;
            text-align: center;
        }
        .footer a {
            color: #fff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .footer img {
            display: block;
            margin: 0 auto;
            max-width: 100px; /* Adjust the size as needed */
            height: auto;
        }
    </style>
</head>
<body>
    <header>
        ❤️ Welcome to Jerm-Sexy-Chat ❤️
    </header>
    <div class="container">
        <h1>Talk with a REAL man</h1>
        <form>
            <div class="input-group">
                <input type="text" placeholder="Enter your name" required>
            </div>
            <div class="input-group">
                <input type="email" placeholder="Enter your email" required>
            </div>
            <div class="input-group">
                <input type="password" placeholder="Create a password" required>
            </div>
            <div class="input-group">
                <button type="submit">Sign Up</button>
            </div>
        </form>
    </div>
    <div class="footer">
        <img src="Images/germ.jpg" alt="Germ Image">
        <p>© 2023 Jerm.io. All rights reserved.</p>
    </div>
</body>
</html>