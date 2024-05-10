<!-- index.html -->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Calculator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6 text-center">
                <h3 class="text-center">Calculator</h3>
                <p class="text-center">Using this service you can perform arithmetic operations.</p>
                <form method="POST" action="<?php echo $_SERVER['PHP_SELF'];?>">
                    <div class="mb-4">
                        <input type="text" name="expression" class="form-control" placeholder="1 + 1" autocomplete="off">
                    </div>
                    <button type="submit" name="submit" value="submit" class="btn btn-primary mb-4">Calculate</button>
                    </br>
                </form>
                <?php
                if (isset($_POST['submit'])) {
                    $expression = $_POST['expression'];
                    echo "<h3 class='text-center'>Result:</h3>";
                    echo "<pre>";
                    echo eval('return '. $expression. ';'); // cool code happen
                    echo "</pre>";
                }
                ?>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>