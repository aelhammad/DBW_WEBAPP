<!DOCTYPE html>
<html>

<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <title>ToxicBrowser</title>

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
        <div class="center" style="margin-top: 150px;">
            <h1>ToxicBrowser</h1>
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
                    <li><a href="#">ComponentType</a>
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

    <script src="scripts.js"></script>
    <footer>
        <p>&copy; 2024 ToxicBrowser. All rights reserved.</p>
    </footer>
</body>

</html>
