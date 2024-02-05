<!DOCTYPE html>
<html>

<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap" rel="stylesheet">

    <title>ToxicBrowser</title>
    <style type="text/css">
        .center {
            text-align: center;
        }

        .navbar {
            background-color: #f2f2f2;
            padding: 10px;
        }

        .navbar ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }

        .navbar li {
            float: left;
        }

        .navbar li a {
            display: block;
            color: #333;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }

        .navbar li a:hover {
            background-color: #ddd;
        }

        * {
            margin: 0px;
            padding: 0px;
        }

        #header {
            margin: auto;
            width: 500px;
            font-family: Arial, Helvetica, sans-serif;
        }

        ul,
        ol {
            list-style: none;
        }

        .nav {
            width: 140px;
            margin: 50px auto;
        }

        .nav>li {
            float: left;
        }

        .nav li a {
            background-color: #000;
            color: #fff;
            text-decoration: none;
            padding: 20px 12px;
            display: block;
        }

        .nav li a:hover {
            background-color: #434343;
        }

        .nav li ul {
            display: none;
            position: absolute;
            min-width: 140px;
        }

        .nav li:hover ul {
            display: block;
        }

        .nav li ul li {
            position: relative;
        }

        .nav li ul li ul {
            right: -142px;
            top: 0px;
        }

        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #f5f5f5;
            padding: 10px;
            text-align: center;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 50px;
        }

        input[type="text"] {
            padding: 20px;
            width: 70%;
            border: 1px solid #ddd;
            border-radius: 5px 5px 0 0;
            outline: none;
        }

        button[type="submit"] {
            background-color: #007bff;
            color: #fff;
            border: 1px solid #007bff;
            padding: 15px;
            border-radius: 0 0 5px 5px;
            cursor: pointer;
            outline: none;
            margin-top: 10px;
            width: 20%;

        }

        button[type="submit"]:hover {
            background-color: #0056b3;
            border-color: #0056b3;
        }

        #header h1 {
            font-family: 'Roboto', sans-serif; 
            font-weight: 500;
            font-size: 2em;
            margin-top: 20px;
        }

        .collapsible {
            background-color: #777;
            color: white;
            cursor: pointer;
            padding: 20px;
            width: 50%;
            border: none;
            text-align: left;
            outline: none;
            font-size: 15px;
            text-align: center;
            margin-left: 450px;
            margin-top: 20px;

        }

        .active,
        .collapsible:hover {
            background-color: #555;

        }

        .content {
            padding: 0 18px;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.2s ease-out;
            background-color: #f1f1f1;
            width: 48%;
            margin-left: 450px;

        }

        .submenu {
            display: flex;
            justify-content: space-between;
            padding: 10px;
        }

        .submenu a {
            color: black;
            text-decoration: none;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-right: 10px;
        }

        .submenu a:hover {
            background-color: #ddd;
        }
    </style>

</head>

<body>
    <nav class="navbar">
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About Us</a></li>
            <li><a href="#">User Guide</a></li>
            <li><a href="#">Contact</a></li>
            <li style="float: right;"><a href="#">Login</a></li>
            <li style="float: right;"><a href="#">Sign Up</a></li>
        </ul>
    </nav>

    <header>
        <div class="center">
            <h1>Tox DB</h1>
        </div>
    </header>

    <div class="center">
        <form action="#" method="GET">
            <input type="text" name="search" placeholder="Introduce a compound">
            <button type="submit">Search</button>
        </form>
    </div>

    <button class="collapsible">Advanced search</button>
    <div class="content">
        <div class="submenu">
            <div class="nav">
                <ul>
                    <li><a href="#">Organ Toxicity</a>
                        <ul>
                            <li><a href="#">Submenu1</a></li>
                            <li><a href="#">Submenu2</a></li>
                            <li><a href="#">Submenu3</a></li>
                            <li><a href="#">Submenu4</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div class="nav">
                <ul>
                    <li><a href="#">Component Type</a>
                        <ul>
                            <li><a href="#">Submenu1</a></li>
                            <li><a href="#">Submenu2</a></li>
                            <li><a href="#">Submenu3</a></li>
                            <li><a href="#">Submenu4</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <script>
        var coll = document.getElementsByClassName("collapsible");
        var i;

        for (i = 0; i < coll.length; i++) {
            coll[i].addEventListener("click", function () {
                this.classList.toggle("active");
                var content = this.nextElementSibling;
                if (content.style.maxHeight) {
                    content.style.maxHeight = null;
                } else {
                    content.style.maxHeight = content.scrollHeight + "px";
                }
            });
        }
    </script>
    <footer>
        <p>&copy; 2024 ToxicBrowser. All rights reserved.</p>
    </footer>
</body>

</html>
