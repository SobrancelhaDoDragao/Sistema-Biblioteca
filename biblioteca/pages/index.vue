<template>

    <div class="main-login">
        
        <div class="explicao">
            
                <h1>Projeto biblioteca</h1>
                <h2>Uma aplicação web para gerenciar acervo de livros de uma biblioteca e tambem emprestimo de livros feito pelo os usuarios.</h2>
                <h2><NuxtLink to="/cadastro">Crie seu cadastro aqui</NuxtLink></h2>
    
                <img src="~/assets/img/meninoLendo.png" alt="Menindo lendo um livro em cima da lua">
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

                        
                        <button class="butaoLogin"  @click.prevent="login()" >Login</button>
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
  width: 50vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
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

.fomularioLogin{
    width: 50vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card_login{
    width: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 30px 35px;
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
    margin: 10px 0 10px 0;
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


@media only screen and (max-width: 950px){
    .card_login{
        width: 85%;
    }
}

@media only screen and (max-width: 600px){
    .main-login{
        flex-direction: column;
    }

    .explicao{
        width:100%;
        height: auto;
    }

    .fomularioLogin{
        width: 100%;
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

<script>
    export default{
        data(){
            return{
                email:'',
                password:'',
            }
        },

        methods: {
          
            async login(){

                const credentials = {
                email:this.email,
                password:this.password
                } 

                const response = await fetch('http://127.0.0.1:8000/api/token/',{
                    method:'POST',
                    headers:{'Content-Type':'application/json'},
                    body:JSON.stringify(credentials)
                });

                let teste = await response.json()

                console.log(teste)
            }   
        },
    }
</script>