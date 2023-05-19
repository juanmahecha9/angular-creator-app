def appComponentHtml(pwd):
    file = open(f"{pwd}/src/app/app.component.html", 'w')
    file.write("""<teleperformance-rpa-navbar></teleperformance-rpa-navbar>
<div class="container">
  <router-outlet></router-outlet>
</div>
<teleperformance-rpa-footer></teleperformance-rpa-footer>              
"""
               )
    file.close()


def indexHtmlBootstrap(pwd, projectName):
    file = open(f"{pwd}/src/app/app.component.html", 'w')
    file.write(f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{projectName}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="assets/icons/TpLogo.png">
</head>
<body>
  <teleperformance-rpa-root>
  </teleperformance-rpa-root>
</body>
<!--Links bootstrap js-->
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
</html>
"""
               )
    file.close()

def indexHtml(pwd, projectName):
    file = open(f"{pwd}/src/app/app.component.html", 'w')
    file.write(f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{projectName}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="assets/icons/TpLogo.png">
</head>
<body>
  <teleperformance-rpa-root>
  </teleperformance-rpa-root>
</body>
</html>
"""
               )
    file.close()
