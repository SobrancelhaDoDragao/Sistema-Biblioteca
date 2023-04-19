export default defineNuxtRouteMiddleware(async ({redirect}) => {
    
    // Vai ser executado somente no server para não sobrecarregar o servidor
    if (process.client) return

    // Url base do back-end
    const config = useRuntimeConfig()

    let token = useCookie('access')
  
    var bearer = 'Bearer ' + token.value;
   
    try {
        // Verificando se está logado
        const response = await $fetch(`${config.public.apiBase}VerifyAuthenticated`,{
            method:'POST',
            headers:{'Content-Type':'application/json',
            'Authorization': bearer,
            },
        });
        
    } catch (error) {
        return redirect = "/";
    }

})
 