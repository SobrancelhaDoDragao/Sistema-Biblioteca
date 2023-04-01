<template>
    <main>
        <h1>Perfil</h1>

         <label for="nome">Nome</label>
         <input type="text" name="" id="nome" v-model="nome" >

         <label for="email">Email</label>
         <input type="email" name="" id="email" v-model="email" >

         <button id="btn-perfil" >Salvar</button>
   </main>
</template>

<style>
main{
   background-color: var(--main-background-color-conteiner);
   padding: 1rem;
   border-radius: 10px;
   flex: 4;
   border: solid var(--colorFour) 2px;
}

input{
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

label{
    color: var(--colorFour);

    width: 100%;

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
import { useUserStore } from '~/stores/user'

// Dados do usuário logado
const user = useUserStore()

let nome = ref(user.nome)
let email = ref(user.email)

</script>