<template>

    <div class="main-login">
        
        <div class="explicao">
            
                <h1>Projeto biblioteca</h1>
                <h2>Este projeto foi criado para fins de estudos e tem como objetivo criar uma aplicação web completa para gerenciar o acervo, empréstimos e devoluções de livros em uma biblioteca.</h2>

                <div>
                    <NuxtLink class="btn" to="/cadastro">Crie seu cadastro aqui</NuxtLink> <a class="btn" href="https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca" >Veja o código</a>
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


<style>

* {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
    font-family: var(--main-font);
    font-weight: var(--regular-weight);
}

.main-login{
   width: 100vw;
   height: 100vh;
   background: var(--colorOne);
   display: flex;
   justify-content: center;
   align-items: center; 
}

.explicao{
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  margin-top: 1rem;
}

.explicao h1{
    color: var(--colorThree);
    text-align: center;
}

.explicao h2{
    text-align:justify;
    margin: 1rem;
    color: var(--main-background-color-conteiner);
}

.explicao div{
    display: flex;
}

.btn{
    width: 100%;
    text-align: center;
    padding: 1rem;
    text-decoration: none;
    margin: 1rem;
    border: none;
    border-radius: 10px;
    display: block;
    outline: none;
    text-transform: uppercase;
    font-weight: var(--bold-weight);
    color:var(--main-background-color-conteiner);
    background: var(--colorThree);
    font-size: 1rem;
    cursor: pointer;
}

.fomularioLogin{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card_login{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 20px;
    background:var(--main-background-color-conteiner);
    border-radius: 20px;
    box-shadow: 0px 10px 40px var(--colorFour);
}

.card_login h1{
    color:var(--colorThree);
    font-weight: var(--bold-weight);
    margin: 0;
}


.text_field{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
}

.text_field > input{
    width: 100%;
    border:none;
    border-radius: 10px;
    padding: 15px;
    background:var(--main-background-color-conteiner);
    color: var(--colorFour);
    font-size: 12pt;
    outline: none;
    border: solid var(--colorSix) 1px;
}

.text_field > label{
    color: var(--colorFour);
    margin: 5px 0 5px 0;
    width: 100%;
}


.butaoLogin{
    width: 100%;
    padding: 16px;
    margin: 25px;
    border: none;
    border-radius: 8px;
    display: block;
    outline: none;
    text-transform: uppercase;
    font-weight: var(--bold-weight);
    letter-spacing: 4px;
    color:var(--colorFour);
    background: var(--colorThree);
    cursor: pointer;
}


img{
    border-radius: 40px;
    border: solid var(--colorThree) 5px;
    width: 20vw;
}

#erro{
    margin-top: 1rem;
    color: rgba(255, 0, 0, 0.788);
}

@media only screen and (max-width: 950px){
    .card_login{
        width: 85%;
    }
}

@media only screen and (max-width: 600px){
    .main-login{
        flex-direction: column;
    }

    .btn{
        margin:.5rem;
    }

    .explicao{
        width:100%;
        height: auto;
    }

    .fomularioLogin{
        width: 80%;
        height: auto;
    }

    img{
        display: none;
    }

    .card_login{
        padding: 15px 20px;
    }

}

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
 const access = useCookie('access')
 const refresh = useCookie('refresh')
 

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