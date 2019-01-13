<html>
    <head>
        <title>Wiki - home</title>
    </head>

    <body>
        <h1><a href="/">BasicWiki</a></h1>
        <h2>Creating page</h2>
        <form action="/update/" method="post" id="usrform">
            Title (replace article by using the same title)<br>
            <input type="text" name="article_name"><br>
            Article text<br>
            <textarea name="article_content" form="usrform" cols="60" rows="20"></textarea><br><br>
            <input type="submit" value="Skicka">
        </form>
    </body>
</html>