<template>
    <main id="main-livro" class="conteiner-padrao">

       <div id="img-conteiner">
          <nuxt-img :src="'http://localhost:8000/static/img/CapasLivros/'+livro.livro.capa" fit="fill" sizes='xs:50vw sm:40vw md:35vw lg:28vw xl:300px' placeholder/>
       </div>
      
        <div id="livro-informacao">

            <div v-if="!editar">

                <h1>{{ livro.livro.nome }}</h1>

                <h2>Editora: {{ livro.livro.editora }}</h2>
            
            </div>

            <form v-else class="form-padrao">

                <h1 id="h1Editar">Editar</h1>

                <label for="nome">Nome</label>
                <input type="text" id="nome" v-model="nome">

                <label for="editora">Editora</label>
                <input type="text" id="editora" v-model="editora" >

                <label for="capa">Capa</label>
                <input type="file" id="capa" v-on:change="filechange" >

                <button id="btn-acervo" class="btn-padrao" @click.prevent="EditarLivro">Salvar</button>

            </form>

            <div id="acoes-livro">
                <NuxtLink to="/auth/acervo/livros" class="btn-padrao" id='btn-voltar-livro'><nuxt-img src="icons/arrow-left-solid.svg" width="25" height="25"/></NuxtLink> 

                <button v-if="!editar" id='btn-salvar-livro' class="btn-padrao" v-on:click="showEditarInput"><nuxt-img src="icons/pen-solid.svg" width="25" height="25"/></button>
                <button v-else id='btn-salvar-livro' class="btn-danger" v-on:click="showEditarInput">Cancelar</button>

                <button id='btn-excluir-livro' v-on:click="DeleteLivro" class="btn-danger"><nuxt-img src="icons/trash-can-solid.svg" width="25" height="25"/></button>
                <button id='btn-emprestimo-livro' class="btn-padrao" >Emprestar</button>
            </div>
            
        </div>
        
    </main>
</template>

<style scoped>
#main-livro{
    flex: 4;
    display: flex;
    align-content: center;
    justify-content: center;
    gap: 1rem;
}

#livro-detail{
   border: solid 5px var(--colorFive);
}

#livro-informacao{
    width: 70%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

h1{
  font-size: 2.5rem;
  border-bottom: solid 2px var(--colorFive);
  width: 100%;
}

h2{
    margin-top: 1rem;
}

#acoes-livro{
    display: flex;
    gap: .5rem;
    border-top: solid 2px var(--colorFive);
    padding-top: 1rem;
    flex-wrap: wrap;
}

#h1Editar{
    margin-bottom: 1rem;
}

#btn-acervo{
  margin-top: 1rem;
}

#btn-voltar-livro{
    text-decoration: none;
}

#img-conteiner{
   margin: auto;
}
</style>

<script setup>

const route = useRoute()

let livro = useLivroStore()

await livro.GetLivro(route.params.id)

let nome = ref(livro.livro.nome)
let editora = ref(livro.livro.editora)
let capa = ref(livro.livro.capa)

// Variavel input para editar
let editar = ref(false)

const showEditarInput = ()=>{
    editar.value = !editar.value
}

const EditarLivro = async()=>{
    await livro.PutLivro(route.params.id,nome,editora,capa)
    editar.value = !editar.value
}
const DeleteLivro = async()=>{
    await livro.DeleteLivro(route.params.id)
    navigateTo('/auth/acervo/livros')
}


let filechange = (event)=>{

const reader = new FileReader()

reader.addEventListener("load",() => {
            // Armazenando o valor data url da imagem na variavel capa
            capa.value = reader.result
         },
);
// Convertendo a imagem em data url
reader.readAsDataURL(event.target.files[0]);
} 
</script>



