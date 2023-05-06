<template>
   <NuxtLoadingBar/>
    <div class="main-login">
        
        <div class="explicao">
            
                <h1>Projeto biblioteca</h1>
                <h2>Este projeto foi criado para fins de estudos e tem como objetivo criar uma aplicação web completa para gerenciar o acervo, empréstimos e devoluções de livros em uma biblioteca. Criador: <a href="https://www.linkedin.com/in/eudsonduraes/" target="_blank" rel="noopener noreferrer">Eudson Durães</a>, licença MIT.</h2>

                <div>
                    <NuxtLink class="btn" to="/cadastro">Crie seu cadastro aqui</NuxtLink> <a class="btn" href="https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca" target="_blank">Veja o código</a>
                </div>
                
    
                <!--<img src="~/assets/img/meninoLendo.png" alt="Menindo lendo um livro em cima da lua">-->
        </div>

        <div class="fomularioLogin">

            <div class="card_login">

                <h1>Login</h1>

         
                <form>
                                  
                    <div class="text_field">   
              
                        <label for="email">Email</label>
                        <input type="email" name="email" id="email" v-model="email" >
    
                        <label for="senha">Senha</label>
                        <input type="password" name="senha" id="senha" v-model="password" >
                        
                        <p v-if="erro" id="erro" >{{erro}}</p>
                        
                        <button class="butaoLogin" @click.prevent="login"  >Login</button>
                    </div>

                    
                </form>  

            </div>
            
        </div>

    </div>

</template>

<style scoped>
@import '~/assets/css/index.css';
</style>

<script setup>
 useHead({
  title: 'Biblioteca|Login',
})

definePageMeta({
   middleware: 'redirect-auth'
})

 // Url base do back-end
 const config = useRuntimeConfig()
  
 const password = ref('')
 const email = ref('')
 
 // Criando cookies para salvar os tokens
 const access = useCookie('access', {maxAge: 60 * 60 * 24 * 7}) // Uma semana em segundos
 const refresh = useCookie('refresh',{maxAge: 60 * 60 * 24 * 7})
 

 let erro = ref()
 
 const login = async () =>{
    
                const credentials = {
                    email:email.value,
                    password:password.value
                };
               
                try {
                    const response = await $fetch(`${config.apiBase}token/`,{
                        method:'POST',
                        headers:{'Content-Type':'application/json'},
                        body:JSON.stringify(credentials)
                    });
                    
                    let token = response
                    // Salvando tokens
                    access.value = token.access
                    refresh.value = token.refresh
                    
                    navigateTo('/auth/home');
                    
                } catch (error) {
                    erro.value = `Algo foi digitado errado`
                }
                
 } 

 
</script>