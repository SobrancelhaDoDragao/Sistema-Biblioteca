<template>
   <NuxtLoadingBar/>
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

<style scoped>
@import '~/assets/css/cadastro.css';
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
        is_admin:0
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
             
            let response = await fetch(`${config.apiBase}cadastro/`,{
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify(formulario)
            });
               
            let resultado = await response.json();
            
            if(resultado.nome){
               await navigateTo('/')
            }
            else{
                erros.value = resultado['email'][0]
            }
            
    
        }

</script>