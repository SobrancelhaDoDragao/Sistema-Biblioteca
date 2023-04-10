export default defineNuxtRouteMiddleware(async ({redirect}) => {

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

        return redirect = "auth/home";
        
    } catch (error) {
        console.log('Nao esta autenticado')
    }
 
})