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

                    <nuxt-img  v-if="user.foto == ''" src="icons/user-solid.svg" width="100" height="139"/>
                    <nuxt-img  v-else :src="`http://localhost:8000/static/img/FotoPerfil/${user.foto}`" sizes="sm:80vw lg:20vw" placeholder/>
                    <input type="file" v-on:change="filechange">
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
let foto = ref(user.foto)
let password = ref(user.password)


let filechange = (event)=>{

const reader = new FileReader()

reader.addEventListener("load",() => {

            // Armazenando o valor data url da imagem na variavel capa
            foto.value = reader.result
         },

);

// Convertendo a imagem em data url
reader.readAsDataURL(event.target.files[0]);

} 

const enviar = async () => {
    //Atualizando dados
    await user.PutUserData(nome,email,foto,password)
    await user.GetUserData()
}

</script>