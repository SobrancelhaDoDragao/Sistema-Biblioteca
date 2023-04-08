<template>
    <main>
        <h1>Perfil</h1>

         <label for="nome">Nome</label>
         <input type="text" name="" id="nome" v-model="nome" >

         <label for="email">Email</label>
         <input type="email" name="" id="email" v-model="email" >

         <button id="btn-perfil" @click.prevent="enviar" >Salvar</button>

         <div id="linha"></div>
   </main>
</template>

<style scoped>
main{
   background-color: var(--main-background-color-conteiner);
   padding: 1rem;
   border-radius: 10px;
   flex: 4;
   border: solid var(--colorSix) 2px;
}

main h1{
    font-weight: var(--thin-weight);
    margin-bottom: 1rem;
}

#linha{
    margin-top: 1rem;
    border-bottom: solid 2px var(--colorSix);
}

input{
    width: 100%;
    border:none;
    border-radius: 10px;
    padding: 15px;
    color: var(--colorFour);
    font-size: 12pt;
    outline: none;
    border: solid var(--colorSix) 1px;
    font-weight: var(--thin-weight);
}

label{
    color: var(--colorFour);
    font-weight: var(--thin-weight);
}

#btn-perfil{
   background: var(--colorOne);
   color:var(--colorThree);
   font-weight: var(--bold-weight);
   padding: 8px 18px;
   border: none;
   border-radius: 10px;
   font-size: 1rem;
   margin-top: 1rem;
   cursor: pointer;
}
</style>

<script setup>

// Dados do usuário logado
const user = useUserStore()

let nome = ref(user.nome)
let email = ref(user.email)
let foto = ""
let password = ref(user.password)

const enviar =  async () => {
    //Atualizando dados
    await user.PutUserData(nome,email,foto,password)
    await user.GetUserData()
}

</script>