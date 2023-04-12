<template>
    <main  id="main-user-detail"  class="conteiner-padrao" >
        <h1>Perfil</h1>

        <div id="UserDetailConteiner">
            <form class="form-padrao">
                <label for="nome">Nome</label>
                <input type="text" id="nome" v-model="nome" >

                <label for="email">Email</label>
                <input type="email" id="email" v-model="email" >

                <button  id="btn-user-detail"  class="btn-padrao" @click.prevent="enviar">Salvar</button>
            </form>

            <div id="FotoPerfil">
                <nuxt-img src="img/user-solid.svg" format="webp" width="100" height="150"/>
                <button id="btn-user-foto" class="btn-padrao" >Alterar foto</button>
            </div>
        </div>

       

         <div id="linha"></div>
   </main>
</template>

<style scoped>

#main-user-detail{
    flex: 4;
}

main h1,h3{
    font-weight: var(--thin-weight);
    margin-bottom: 1rem;
}

#linha{
    margin-top: 1rem;
    border-bottom: solid 2px var(--colorSix);
}
#UserDetailConteiner{
    display: flex;
    align-items: center;
}

form{
    display: flex;
    flex-direction: column;
    width: 50%;
}

#btn-user-detail{
    margin-top: 1rem;
}

#btn-user-foto{
  margin-top: 1rem;
  width: 10rem;
}

#FotoPerfil{
 display: flex;
 flex-direction: column;
 margin-left: 1rem;
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