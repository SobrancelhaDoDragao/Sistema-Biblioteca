import Cookie from 'js-cookie';


export default async function(context){

    // Restrinzindo o middleware a somente ao client, o cookie só fica disponivel no client
    if (process.server) return

    const token = Cookie.get('access');

    var bearer = 'Bearer ' + token;
    
    const data = {teste:'teste'}
   
    const response = await fetch('http://127.0.0.1:8000/api/VerifyAuthenticated',{
                    method:'POST',
                    headers:{'Content-Type':'application/json',
                    'Authorization': bearer,
                    },
                    body:JSON.stringify(data)
                });
    
    
    const teste = await response.json()

    console.log(token)

    if(!teste.Authenticated){
     //Funciona no servidor
     //return redirect = "/";
     //Funciona no client
     return navigateTo('/');
    }

  }
 