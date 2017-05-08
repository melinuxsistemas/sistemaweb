/*function criar_usuario_contratante(){
  NProgress.start();

  if (validar_formulario()){

    success_notify("Usuário Cadastrado","Você receberá um email em instantes.")
    NProgress.done();
    return true;
  }
  else{
    NProgress.done();
    return false;
  }
}*/

function validar_formulario(){
  return (validar_email() && validar_senha());
}

function verificar_senhas(senha, confirma_senha){
  return (senha === confirma_senha ? true : false);
}

function verificar_formato_senha(senha){
  return ((contains_alpha("senha") && contains_numeric("senha") && contains_minimal_size("senha",8)) ? true : false);
}

function validar_senha(){
  var senha = document.getElementById("senha").value;
  var re_senha = document.getElementById("confirma_senha").value;

  if (is_empty('senha') || (is_empty('confirma_senha'))){
    return false;
  }

  if(!verificar_senhas(senha, re_senha)){
    return error_notify("confirma_senha","Senhas não conferem","Verifique as senhas informadas.");
  }

  if (!verificar_formato_senha()){
    return error_notify("senha","Senhas Insegura","Informe uma senha com ao menos 8 caracteres contendo letras e numeros.");
  }

  return true;
  
  /*if(senha === re_senha) {
    var senha_vazia = is_empty('senha');
    if(!senha_vazia && contains_alpha("senha") && contains_numeric("senha") && contains_minimal_size("senha",8)){
      return true;
    }
    else{
      if(!senha_vazia){
        return error_notify("senha","Senha insegura","Informe uma senha com ao menos 8 caracteres contendo letras e numeros.")
      }
      else{
        return false;
      }
    }
  }
  else{
    return error_notify("senha","Senhas não conferem","Verifique as senhas informadas.")
  }*/
}

function validar_email() {
  var filter = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
  if(!is_empty('email')){
    if(filter.test(document.getElementById("email").value)){
      return true;
    }
    else{
      return error_notify("email","Email Inválido","Verifique se o email foi digitado corretamente.")
    }
  }
  else{
    return false;
  }
}

