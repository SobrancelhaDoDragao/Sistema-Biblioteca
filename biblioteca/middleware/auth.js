export default defineNuxtRouteMiddleware(async ({redirect}) => {

    // Url base do back-end
    const config = useRuntimeConfig()

    let token = useCookie('access')
  
    var bearer = 'Bearer ' + token.value;
    
    //Isso é desnecessario
    const data = {teste:'teste'}
    
    try {
        // Verificando se está logado
        const response = await $fetch(`${config.apiBase}VerifyAuthenticated`,{
            method:'POST',
            headers:{'Content-Type':'application/json',
            'Authorization': bearer,
            },
            body:JSON.stringify(data)
        });
        
    } catch (error) {
        return redirect = "/";
    }
 
})
 