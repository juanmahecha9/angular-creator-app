def navbarHtml(pwd):
    file = open(
        f"{pwd}/src/app/project/common/components/navbar/navbar.component.html", "w")
    file.write('''<nav id="navigation" class="navbar navbar-expand-sm navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand">
      <img
        src="assets/images/BannerTeleperformance.png"
        alt="TP logo"
        class="icon-navbar"
      />
    </a>
  </div>
  <button
    class="navbar-toggler collapsed"
    type="button"
    data-toggle="collapse"
    data-target="#navbarsExample03"
    aria-controls="navbarsExample03"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="navbar-collapse collapse" id="navbarsExample03" style="">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" routerLink=""
          >Home <span class="sr-only">(current)</span></a
        >
      </li>
      <li class="nav-item dropdown">
        <a
          class="nav-link dropdown-toggle"
          id="dropdown03"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
          >Dropdown</a
        >
        <div class="dropdown-menu" aria-labelledby="dropdown03">
          <a class="dropdown-item" routerLink="">Action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" routerLink="">Another action</a>
          <a class="dropdown-item" routerLink="">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link" routerLink="">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" routerLink="">Disabled</a>
      </li>
    </ul>
  </div>
</nav>
'''
               )
    file.close()


def navbarScss(pwd):
    file = open(
        f"{pwd}/src/app/project/common/components/navbar/navbar.component.scss", "w")
    file.write('''#navigation {
  .container-fluid {
    .navbar-brand {
      .icon-navbar {
        width: 50%;
      }
    }
  }
  .collapse {
    .navbar-nav {
      .nav-item {
        .nav-link {
          font-size: 1rem;
          &:hover {
            color: #fff;
            font-size: 1.1rem;
          }
        }
      }
    }
  }
}
'''
               )
    file.close()
