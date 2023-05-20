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
                    <nuxt-img  v-if="user.foto == null" src="icons/user-solid.svg" width="100" height="139"/>
                    <nuxt-img  v-else :src="user.foto" width="100" height="139"/>
                    <input type="file" ref="foto">
            </div>
        </div>

       

         <div id="linha"></div>
   </main>
</template>

<style scoped>

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
    gap: 1rem;
}

form{
    display: flex;
    flex-direction: column;
    width: 60%;
}

#btn-user-detail{
    margin-top: 1rem;
}

#FotoPerfil{
 display: flex;
 flex-direction: column;
 width: 40%;
}

@media only screen and (max-width: 700px){
    #UserDetailConteiner{
        display: flex;
        flex-direction: column;
    }

    form{
        width: 100%;
    }

    #FotoPerfil{
        width: 100%;
    }
  
}
</style>

<script setup>

// Dados do usuário logado
const user = useUserStore()

let nome = ref(user.nome)
let email = ref(user.email)
let foto = ref(null)

const enviar = async () => {
    //Atualizando dados

    let formData = new FormData()
    
    if(nome.value != user.nome){
        formData.append('nome',nome.value)
    }
    if(email.value != user.email){
        formData.append('email',email.value)
    }

    if(foto.value.files[0]){
        formData.append('foto',foto.value.files[0])
    }
     
    await user.PutUserData(formData)
    await user.GetUserData()
}

</script>