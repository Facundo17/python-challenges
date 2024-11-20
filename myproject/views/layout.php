<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi sitio web</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>

    <body>

    <nav class="navbar navbar-expand-lg navbar-light bg-light mb-4">
        <div class="container">
            <a href="/" class="navbar-brand h1">FM</a>
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                  <a href="/about" class="navbar-brand h1">Home</a>
                </li>
                <li class="nav-item">
                  <a href="/about" class="navbar-brand h1">About</a>
                </li>
                <li class="nav-item">
                  <a href="/contact" class="navbar-brand h1">Contact</a>
                </li>
            </ul>
        </div>
    </nav>
        
    <div class="container">
        <div class="row">
            <!-- content es la variable en el archivo Response -->
            <!-- aquí se imprime home.php por ejemplo -->
            <?php echo $content; ?>
        </div>
    </div>

    </body>
</html>