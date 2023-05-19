def footerHtml(pwd):
    file = open(f"{pwd}/src/app/project/common/components/footer/footer.component.html", "w")
    file.write('''<div class="container mb-1">
  <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <div class="col-md-4 d-flex align-items-center">
      <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
        <svg class="bi" width="30" height="24">
          <use xlink:href="#bootstrap"></use>
        </svg>
      </a>
      <span class="text-muted">© 2022 teleperformance, Each interaction matters</span>
    </div>
    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
      <li class="ms-3">
        <a class="text-muted" target="_blank" href="http://linkedin.com/company/teleperformance">
          <img src="assets/icons/icons8-linkedin-48.png" alt="Linkedin">
        </a>
      </li>
      <li class="ms-3">
        <a class="text-muted" target="_blank" href="/">
          <img src="assets/icons/icons8-instagram-48.png" alt="Linkedin">
        </a>
      </li>
    </ul>
  </footer>
</div>
'''
               )
    file.close()


    file = open(f"{pwd}/src/app/project/common/components/navbar/navbar.component.scss","w")
    file.write('''nav {
  //position: fixed;
  top: 0;
  //z-index: 1;
  background: radial-gradient(
        circle at 100% 100%,
        #ffffff 0,
        #ffffff 3px,
        transparent 3px
      )
      0% 0%/8px 8px no-repeat,
    radial-gradient(circle at 0 100%, #ffffff 0, #ffffff 3px, transparent 3px)
      100% 0%/8px 8px no-repeat,
    radial-gradient(circle at 100% 0, #ffffff 0, #ffffff 3px, transparent 3px)
      0% 100%/8px 8px no-repeat,
    radial-gradient(circle at 0 0, #ffffff 0, #ffffff 3px, transparent 3px) 100%
      100%/8px 8px no-repeat,
    linear-gradient(#ffffff, #ffffff) 50% 50% / calc(100% - 10px)
      calc(100% - 16px) no-repeat,
    linear-gradient(#ffffff, #ffffff) 50% 50% / calc(100% - 16px)
      calc(100% - 10px) no-repeat,
    linear-gradient(90deg, #f500e8 0%, #ff008d 100%);
  border-radius: 8px;
  //box-sizing: border-box;
}

.container-nav {
  //width: 1280px;
  margin: auto;
}

.nav_checkbox {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  padding: 10px 0px;
}

.logo {
  margin-left: 10px;
  .image-navbar-logo {
    display: none;
    //width: 70px;
  }
  .image-navbar {
    display: block;
    //width: 70px;
  }
}

.tab-nav {
  outline: none;
  display: none;
}

.label {
  display: none;
  color: #000;
}

.burger {
  width: 35px;
  height: 5px;
  background-color: #000;
  margin-top: 5px;
  transition: all 0.5s ease;
}

input[type="checkbox"]:checked ~ .label {
  #burg0 {
    opacity: 0;
  }

  #burg1 {
    transform: rotate(45deg) translate(7px, 7px);
    opacity: 1;
  }

  #burg2 {
    transform: rotate(-45deg) translate(7px, -7px);
  }
}

.content_nav {
  grid-column: 3;
  list-style: none;
  margin-right: 10px;
  padding: 0;

  li {
    display: inline-block;
    padding-right: 10px;

    a {
      text-decoration: none;
      color: #000;
      position: relative;

      &::after {
        content: "";
        display: block;
        height: 2px;
        background-color: #000;
        position: absolute;
        left: 0;
        right: 0;
        transform-origin: left;
        transform: scale(0, 1);
        transition: transform ease-in-out 0.5s;
      }

      &:hover::after {
        transform: scale(1, 1);
      }
    }
  }
}

@media screen and (max-width: 1280px) {
  .container-nav {
    width: 100%;
  }
}

@media screen and (max-width: 770px) {
  .logo {
    .image-navbar-logo {
      display: block;
      //width: 70px;
    }
    .image-navbar {
      display: none;
      //width: 70px;
    }
  }
  .label {
    display: grid;
    cursor: pointer;
    grid-column: 3;
    padding-right: 10px;
  }

  .content_nav {
    display: grid;
    grid-template-columns: 1fr;
    grid-column: 1/4;
    text-align: center;
    max-height: 0;
    overflow: hidden;
    transition: all ease-in-out 0.6s;
  }

  .nav_checkbox input:checked ~ .content_nav {
    max-height: 300px;
  }

  .content_nav li {
    padding: 15px 0px;
  }
}
'''
               )
    file.close()