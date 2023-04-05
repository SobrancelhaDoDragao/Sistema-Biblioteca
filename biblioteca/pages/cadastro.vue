<template>

    <div id="conteiner">

  
        <form>
            
           <h1>Cadastro</h1>

           <label for="nome">Nome</label>
           <input type="text" name="" id="nome" v-model="formulario.nome">

           <label for="email">Email</label>
           <input type="email" name="" id="email" v-model="formulario.email">

           <label for="senha">Senha</label>
           <input type="password" name="" id="senha" v-model="formulario.password">

           <label for="senha">Repetir senha</label>
           <input type="password" name="" id="senha2" v-model="formulario.password2">

           <label for="tipoConta">Criar conta como</label>

            <select name="TipoConta" id="TipoConta"  v-model="formulario.is_admin">

                <option value=0 selected>Usuário</option>
                <option value=1>Funcionário</option>

            </select>
            

            <p v-if="erros" id="erros" >{{ erros }}</p>
             
            <button v-on:click.prevent="validate()">Cadastrar</button>

        </form>
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

#conteiner{
   height: 100vh;
   background: var(--colorOne);
   display: flex;
   justify-content: center;
   align-items: center; 
}

#conteiner form{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 50%;
}

form h1{
    color: var(--colorThree);
    font-weight: var(--bold-weight);
    font-size: 3.5rem;
    text-align: center;
    width: 100%;
    letter-spacing: 4px;
}


form > input{
    width: 100%;
    border:none;
    border-radius: 10px;
    padding: 10px;
    background:var(--main-background-color-conteiner);
    color: var(--colorFour);
    font-size: 1rem;
    outline: none;
    border: solid var(--colorSix) 1px;
}

form > label{
    color: var(--colorFour);
    margin: 10px 0 10px 0;
    width: 100%;
    font-size: 1.5rem;
    color: var(--main-background-color-conteiner);
}

form button{
    width: 50%;
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

#erros{
    margin-top: 1rem;
    color: rgb(255, 0, 0);
    font-weight: var(--bold-weight);
}

form select{
    width: 100%;
    border:none;
    border-radius: 5px;
    padding: 5px;
    background:var(--main-background-color-conteiner);
    color: var(--colorFour);
    font-size: 1rem;
    outline: none;
    border: solid var(--colorSix) 1px;
}

/* Mobile */
@media only screen and (max-width: 600px){
    #conteiner form{
        width: 90%;
    }

    form h1{
       font-size: 2.5rem;
    }


    form > label{
       font-size: 1rem;
    }

    form button{
        width: 100%;
    }
}
</style>

<script setup>

    useHead({
    title: 'Biblioteca|Cadastro',
    })

    // Url base do back-end
    const config = useRuntimeConfig()

    const formulario = reactive({
        nome:'',
        email:'',
        password:'',
        password2:'',
        foto:'teste',
        is_admin:''
    })
    
    let erros = ref()

    const validate = ()=>{
        if(formulario.nome == ''||formulario.email == ''||formulario.password ==''||formulario.password2 ==''){
          erros.value = 'Preencha todos os dados'
        }
        else if(formulario.password != formulario.password2){
            erros.value = 'As senhas não são iguais'
        }
        else{
          erros.value = ''
          //Create user pode retornar dois erros: 1º: O email já existe no banco de dados 2º: A senha criada não é aceita  
          CreateUser()
        }
    }
    const CreateUser = async ()=>{
             
            let response = await fetch(`${config.apiBase}createuser`,{
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify(formulario)
            });
               
            let resultado = await response.json();
            console.log(JSON.stringify(formulario))
            if(resultado.nome){
               await navigateTo('/')
            }
            else{
                erros.value = resultado['email'][0]
            }
            
    
        }

</script>