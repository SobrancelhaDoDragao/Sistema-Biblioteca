<template>
    <main id="main-livro" class="conteiner-padrao">

       <div id="img-conteiner">
          <nuxt-img :src="livro.livro.capa"  format="png" sizes="sm:50vw md:10vw lg:320px"/>
       </div>
    
        <div id="livro-informacao">

            <div v-if="!editar">

                <h1 id='nome-livro'>{{ livro.livro.nome }}</h1>

                <p id="descricao">{{ livro.livro.descricao }}</p>
               
                <div id='livro-dados'>
                 <span>Autor: {{ livro.livro.autor }}</span> <span>Editora: {{ livro.livro.editora }}</span> <span>Gênero: {{ livro.livro.genero }}</span>
                </div>
                
            </div>

            <form v-else class="form-padrao">

                <h1 id="h1Editar">Editar</h1>

                        <div>
                        <label for="nome">Nome</label>
                        <input type="text" id="nome" v-model="nome">
                        </div>
                        

                        <div id="input-editora-livro">
                        <label for="editora">Editora</label>
                        <input type="text" id="editora" v-model="editora" >
                        </div>
                        
                        <div id="input-autor-livro">
                        <label for="autor">Autor</label>
                        <input type="text" id="autor" v-model="autor">
                        </div>
                        
                        <div>
                        <label for="genero">Gênero</label>
                        <input type="text" id="genero" v-model="genero">
                        </div>

                        <div id="descricaoDiv">
                            <label for="descricao">Sinopse</label>
                   
                            <textarea id="descricao" v-model="descricao">
                  
                            </textarea>
                        </div>
                        <div id="capaDiv" >
                            <label for="capa">Capa</label>
                            <input type="file" name="" id="capa" ref="capa">
                        </div>

            </form>
  
            <div id="acoes-livro">
                <NuxtLink to="/auth/acervo/livros" class="btn-padrao" id='btn-voltar-livro'><nuxt-img src="icons/arrow-left-solid.svg" width="25" height="25"/></NuxtLink> 

                <button v-if="!editar" id='btn-salvar-livro' class="btn-padrao" v-on:click="showEditarInput">Editar</button>
                <button v-else id='btn-salvar-livro' class="btn-padrao" v-on:click="showEditarInput">Cancelar</button>

                <button v-if="!editar" id='btn-emprestimo-livro' class="btn-padrao">Emprestar</button>
                <button v-else id="btn-acervo" class="btn-padrao" @click.prevent="EditarLivro">Salvar</button>

                <button v-if="editar" id='btn-excluir-livro' v-on:click="DeleteLivro" class="btn-danger"><nuxt-img src="icons/trash-can-solid.svg" width="25" height="25"/></button>
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
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

form{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: .3rem;
}

span{
    background: var(--colorFive);
    padding: .2rem;
    border-radius: 5px;
    font-weight: var(--medium-weight);
}

#descricao{
    margin-top: 1rem;
    overflow: auto;
}

#descricaoDiv{
/*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
  grid-area: 4 / 1 / 4 / 4;
}

#capaDiv{
  /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
  grid-area: 3 / 2 / 4 / 4;
}


#nome-livro{
  text-align: left;
  font-size: 2.5rem;
  border-bottom: solid 2px var(--colorFive);
  width: 100%;
}


#livro-dados{
    font-size: 1.2rem;
    margin-top: 1rem;
    margin-bottom: 1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
}

#acoes-livro{
    display: flex;
    gap: .5rem;
    border-top: solid 2px var(--colorFive);
    padding-top: .5rem;
    flex-wrap: wrap;
}

#h1Editar{
    margin-bottom: 1rem;
    /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
    grid-area: 1 / 1 / 1 / 4;
}

#btn-voltar-livro{
    text-decoration: none;
}

#img-conteiner{
   margin: auto;
}

textarea {
    font-size: 1rem;
    width: 100%;
    height:20vh;
    max-width: 100%;
    border-radius: 5px;
    border: 1px solid #ccc;
    box-shadow: 1px 1px 1px #999;
}

@media only screen and (max-width:550px){
    #main-livro{
        flex-direction: column;
    }

    #nome-livro{
        text-align: center;
    }

    form{
        grid-template-columns: 1fr 1fr;
    }

    #input-editora-livro{
        grid-column: 1 / 2;
        grid-row: 3
    }

    #input-autor-livro{
        grid-column: 2 / 4;
        grid-row: 3
    }

    #descricaoDiv{
    /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
        grid-column: 1 / 4;
        grid-row: 5;
    }

    #capaDiv{
        grid-column: 1 / 4;
        grid-row: 4;
    }

    #acoes-livro{
      justify-content: center;
    }
    
}
</style>

<script setup>

const route = useRoute()

let livro = useLivroStore()

await livro.GetLivro(route.params.id)

let nome = ref(livro.livro.nome)
let editora = ref(livro.livro.editora)
let capa = ref(null)
let autor = ref(livro.livro.autor)
let genero = ref(livro.livro.genero)
let descricao = ref(livro.livro.descricao)

// Variavel input para editar
let editar = ref(false)

const showEditarInput = ()=>{
    editar.value = !editar.value
}

const EditarLivro = async()=>{

    let formData = new FormData()
    
    if(nome.value != livro.livro.nome){ 
        formData.append('nome',nome.value) 
    } 
    if(capa.value.files[0]){
        formData.append('capa',capa.value.files[0]) 
    } 
    if(autor.value != livro.livro.autor){ 
        formData.append('autor',autor.value)
    } 
    if(editora.value != livro.livro.editora){ 
        formData.append('editora',editora.value) 
    } 
    if(genero.value != livro.livro.genero){
         formData.append('genero',genero.value) 
    } 
    if(descricao.value != livro.livro.descricao){ 
        formData.append('descricao',descricao.value) 
    }
    
    await livro.PutLivro(route.params.id,formData)
    editar.value = !editar.value
}

const DeleteLivro = async()=>{
    await livro.DeleteLivro(route.params.id)
    navigateTo('/auth/acervo/livros')
}

</script>



