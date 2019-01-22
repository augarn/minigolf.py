<html>
    <head>
        <title>Wiki - home</title>
        <meta charset="UTF-8">
    </head>

    <body>
        <h1><a href="/">Basic Wiki</a></h1>
        <h2>All Articles</h2>
        <ul>
            %for idx, item in enumerate(pages):
                <li><a href="./wiki/{{item}}/">{{item}}</a></li>
            %end
        </ul>
        <hr>
        <a href="/create/">Create or edit article</a>
    </body>
</html>