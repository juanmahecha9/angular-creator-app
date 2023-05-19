def scripts(type: str):
    # Ingresa el tipode script a crear
    script = {
        # Archivo creador comunes
        'common': '''#!/bin/bash
echo 'Ingresar nombre de cada componente a crear (Comunes)'
echo 'Si se quiere crear una carpeta contenedora de cada uno, agragarla al comienzo del las opciones.'
echo 'ex. formulario input-field text-field ...'
togenerate='component'
# Codigo
# Leer variables a crear
read string
echo "******************'$togenerate'***********************"
echo ""
# Separar en un vector
set -f                     
array=(${string// / })
# Contar cuantas son
value=$(echo -n "$string" | wc -w)

# Validar
if [ $value -gt 1 ]
then
  # Crear con carpeta contenedora
  echo "Generando varios componentes"
for ((idx=1; idx<${#array[@]}; ++idx)); do
    npx ng g $togenerate project/common/${array[0]}/${array[idx]} --module app
    shift 
done
else
  # Crear sin carpeta 
   npx ng generate $togenerate project/common/components/${array[0]} --module app
   shift 
fi''',
        # Archivo creador  componentes
        'components': '''#!/bin/bash
echo 'Ingresar nombre de cada componente a crear (Componentes)'
echo 'Si se quiere crear una carpeta contenedora de cada uno, agragarla al comienzo del las opciones.'
echo 'ex. formulario input-field text-field ...'
togenerate='component'
# Codigo
# Leer variables a crear
read string
echo "******************'$togenerate'***********************"
echo ""
# Separar en un vector
set -f                     
array=(${string// / })
# Contar cuantas son
value=$(echo -n "$string" | wc -w)

# Validar
if [ $value -gt 1 ]
then
  # Crear con carpeta contenedora
  echo "Generando varios componentes"
for ((idx=1; idx<${#array[@]}; ++idx)); do
    npx ng g $togenerate project/components/${array[0]}/${array[idx]} --module app
    shift 
done
else
  # Crear sin carpeta 
   npx ng generate $togenerate project/components/${array[0]} --module app
   shift 
fi''',
        # Servicios
        'services': '''#!/bin/bash
echo 'Ingresar nombre de cada componente a crear (Servicios)'
echo 'Si se quiere crear una carpeta contenedora de cada uno, agragarla al comienzo del las opciones.'
echo 'ex. formulario input-field text-field ...'
togenerate='service'
# Codigo
# Leer variables a crear
read string
echo "******************'$togenerate'***********************"
echo ""
# Separar en un vector
set -f                     
array=(${string// / })
# Contar cuantas son
value=$(echo -n "$string" | wc -w)

# Validar
if [ $value -gt 1 ]
then
  # Crear con carpeta contenedora
  echo "Generando varios componentes"
for ((idx=1; idx<${#array[@]}; ++idx)); do
    npx ng generate $togenerate util/services/${array[0]}/${array[idx]}
    shift 
done
else
  # Crear sin carpeta 
   npx ng generate $togenerate util/services/${array[0]}
   shift 
fi''',
        # Guardianes
        'guards': '''#!/bin/bash
echo 'Ingresar nombre de cada componente a crear (Guardianes)'
echo 'Si se quiere crear una carpeta contenedora de cada uno, agragarla al comienzo del las opciones.'
echo 'ex. formulario input-field text-field ...'
togenerate='guard'
# Codigo
# Leer variables a crear
read string
echo "******************'$togenerate'***********************"
echo ""
# Separar en un vector
set -f                     
array=(${string// / })
# Contar cuantas son
value=$(echo -n "$string" | wc -w)

# Validar
if [ $value -gt 1 ]
then
  # Crear con carpeta contenedora
  echo "Generando varios componentes"
for ((idx=1; idx<${#array[@]}; ++idx)); do
    npx ng generate $togenerate util/guards/${array[0]}/${array[idx]}
    shift 
done
else
  # Crear sin carpeta 
   npx ng generate $togenerate util/guards/${array[0]}
   shift 
fi''',
        'models': '''#!/bin/bash
echo 'Ingresar nombre de cada componente a crear (Modelos)'
echo 'Si se quiere crear una carpeta contenedora de cada uno, agragarla al comienzo del las opciones.'
echo 'ex. formulario input-field text-field ...'
togenerate='class'
# Codigo
# Leer variables a crear
read string
echo "******************'$togenerate'***********************"
echo ""
# Separar en un vector
set -f                     
array=(${string// / })
# Contar cuantas son
value=$(echo -n "$string" | wc -w)

# Validar
if [ $value -gt 1 ]
then
  # Crear con carpeta contenedora
  echo "Generando varios componentes"
for ((idx=1; idx<${#array[@]}; ++idx)); do
    npx ng generate $togenerate util/models/${array[0]}/${array[idx]}
    shift 
done
else
  # Crear sin carpeta 
   npx ng generate $togenerate util/models/${array[0]}
   shift 
fi''',
        # Modulos
        'modules': '''#!/bin/bash
echo 'Ingresar nombre de cada componente a crear (Modulos)'
echo 'Si se quiere crear una carpeta contenedora de cada uno, agragarla al comienzo del las opciones.'
echo 'ex. formulario input-field text-field ...'
togenerate='module'
# Codigo
# Leer variables a crear
read string
echo "******************'$togenerate'***********************"
echo ""
# Separar en un vector
set -f                     
array=(${string// / })
# Contar cuantas son
value=$(echo -n "$string" | wc -w)

# Validar
if [ $value -gt 1 ]
then
  # Crear con carpeta contenedora
  echo "Generando varios componentes"
for ((idx=1; idx<${#array[@]}; ++idx)); do
    npx ng generate $togenerate project/modules/${array[0]}/${array[idx]} --module app --route ${array[0]}
    shift 
done
else
  # Crear sin carpeta 
   npx ng generate $togenerate project/modules/${array[0]} --module app --route ${array[0]}
   shift 
fi''',
        # Modulos con componentes
        'module-components': '''

'''
    }
    return script[type]
