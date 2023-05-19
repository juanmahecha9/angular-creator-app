def authUserInterface(pwd):
    file = open(f"{pwd}/src/app/util/models/auth-user.ts", "w")
    file.write('''//Modelo de datos para la autenticacion de un usuario, donde se ingresa el userName y la contraseña.
//Modelo de datos para la respueta de la autenticacion, capturando token, Rol del usuario, etc
 
//Auth
export class AuthUser {
    userName!: String;
    password!: String;
}

//Login
export class AuthUserResponse {
    token!: String;
    Rol!: String;
}''')
    file.close()