from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]



#      <!--
# <p>
#   <label for="id_last_name">Apellido:</label>
#   <input type="text" name="last_name" maxlength="150" id="id_last_name" />
# </p>

# <p>
#   <label for="id_username">Nombre de usuario:</label>
#   <input type="text" name="username" maxlength="150" autofocus required id="idusername" />

#   <span class="helptext"
#     >Obligatorio. Longitud máxima de 150 caracteres. Solo puede estar formado
#     por letras, números y los caracteres @/./+/-/.</span>
# </p>

# <p>
#   <label for="id_email">Dirección de email:</label>
#   <input type="email" name="email" maxlength="254" id="id_email" />
# </p>

# <p>
#   <label for="id_password1">Contraseña:</label>
#   <input
#     type="password"
#     name="password1"
#     autocomplete="new-password"
#     required
#     id="id_password1"
#   />

#   <span class="helptext"
#     ><ul>
#       <li>
#         Su contraseña no puede ser similar a otros componentes de su información
#         personal.
#       </li>
#       <li>Su contraseña debe contener por lo menos 8 caracteres.</li>
#       <li>Su contraseña no puede ser una contraseña usada muy comúnmente.</li>
#       <li>Su contraseña no puede estar formada exclusivamente por números.</li>
#     </ul></span
#   >
# </p>

# <p>
#   <label for="id_password2">Confirmación de contraseña:</label>
#   <input
#     type="password"
#     name="password2"
#     autocomplete="new-password"
#     required
#     id="id_password2"
#   />

#   <span class="helptext"
#     >Introduzca la misma contraseña nuevamente, para poder verificar la
#     misma.</span
#   >
# </p> -->
