<!DOCTYPE html>
<html>

<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap" rel="stylesheet">

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
