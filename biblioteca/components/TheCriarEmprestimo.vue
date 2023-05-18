<template>

        <Teleport to="body">
            <Transition name="bounce">
               <div v-if="modal" id="modalCriarEmprestimo">
                  <h1>Pesquisar livro</h1>
                         
                <form class="form-padrao">
                  <input type="text" v-model="searchLivro" placeholder="Pesquisar por nome, editora, autor e id" >
                  <button v-on:click.prevent="PesquisarLivro" class="btn-padrao">Procurar</button>
                </form>


               

                <fieldset id="resultado">

                    <legend>Resultado</legend>
                     
                     <div id="LivroResultado">
                           <nuxt-img v-on:click="livroEscolhiodo(livro.id)" v-for="livro in livro.livrosDados.livros" :key="livro.id" class="livro" :src="livro.capa" format="webp" placeholder width="110" height="170" />
                     </div>
                </fieldset>
            
               
                <button v-on:click.prevent="modal = false" class="btn-padrao">Fechar</button>
               </div>
            </Transition>
        </Teleport>


    <main  id="conteinerCriarEmprestimo" class="conteiner-padrao" >
       
        <h1 id="TituloNovoEmprestimo">Novo empréstimo</h1>
        
        <div id='conteiner-formularios-emprestimo'>

            <form class="form-padrao" id="form1" >
                <h1>Usuario</h1>

                <div v-if="user" >
                    
                    <h2>{{ user.nome }}</h2>
                    
                    <nuxt-img v-if="user.foto" :src="user.foto" placeholder width="220" height="200" />

                    <nuxt-img v-else src="icons/user-solid.svg" placeholder width="220" height="200" />

                </div>
                
                <input type="text" v-model="searchUsuario" placeholder="Pesquisar por email ou Id" > <button  v-on:click.prevent="PesquisarUsuario" class="btn-padrao">Pesquisar</button>
            </form>

            <form id="form2">
                <h1>Livro do empréstimo</h1>
                <div v-if="livroEmprestimo">
                    <h2>{{livroEmprestimo.nome}}</h2>
                    
                    <nuxt-img :src="livroEmprestimo.capa" placeholder width="100" height="150" />
                </div>
                <button v-on:click.prevent="modal = true" class="btn-padrao">Escolher livro</button>
            </form>

        </div>
        
        <button id="ComfirmarEmprestimo" class="btn-padrao"  @click="CriarEmprestimo">Comfirmar emprestimo</button>

   </main>
</template>

<style>

#conteinerCriarEmprestimo{
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

#conteiner-formularios-emprestimo{
    display: flex;
    gap: 1rem;
    flex: 1;
}


#TituloNovoEmprestimo{
  text-align: center;
}

#form1{
    /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
    border: solid var(--colorFive) 3px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: .5rem;
    text-align: center;
    justify-content: center;
    padding: .3rem;
    border-radius: 1rem;

    flex: 1;
}

#form2{
    border: solid var(--colorFive) 3px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: .5rem;
    text-align: center;
    justify-content: center;
    padding: .3rem;
    border-radius: 1rem;
    flex:1;
}

#ComfirmarEmprestimo{
     /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
     width: 50%;
     justify-self: center;
     align-self: center;
     height: 3rem;
}

h2{
    font-weight:var(--thin-weight);
}

#modalCriarEmprestimo{
  top: 5%;
  left: 50%;  
  width: 80vw;
  height: 75vh;
  position: absolute;
  z-index: 999;
  /*margin-top: -30vh; /* Metade da altura */
  margin-left: -40vw; /* Metade da largura */
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  background: var(--main-background-color-conteiner);
  padding: 1rem;
  border-radius: 10px;
}

#modalCriarEmprestimo h1{
    text-align: center;
}

#modalCriarEmprestimo form{
    margin-top: 1rem;
    margin-bottom: .5rem;
    display: flex;
    gap: 1rem;
    justify-content: center;
}

#resultado{
    height: 65%;
    padding: .5rem;
    background:var(--main-background-color);
    border: solid var(--colorFive) 2px;
    margin-bottom: .5rem;  
}

#LivroResultado{
    display: flex;
    gap: .5rem;
    overflow: auto;
    padding: .5rem; 
    max-width: 76vw;
    justify-content: flex-start;
}

.livro:hover{
   border: solid var(--colorTwo) 4px;
   cursor: pointer;
}


@media only screen and (max-width:550px){
    #conteiner-formularios-emprestimo{
     flex-direction: column;
     min-height: 70vh;
    }

    #ComfirmarEmprestimo{
        width: 100%;
    }

    #modalCriarEmprestimo{
        width: 90vw;
        margin-left: -45vw; /* Metade da largura */
    }

    #LivroResultado{
        max-width: 75vw;
        justify-content: flex-start;
    }
}
</style>


<script setup>
// UseState
let emprestimo = useEmprestimoStore()
let livro = useLivroStore()

//Campos de pesquisa
let searchLivro = ref()
let searchUsuario = ref()

let user = ref()
let livroEmprestimo = ref()

// Modal
let modal = ref(false)

// Limpando variaveis
livro.livrosDados.livros = 0

let PesquisarLivro = () =>{
    livro.GetLivros(1,searchLivro.value)
}

let PesquisarUsuario = async ()=>{
    user.value = await emprestimo.GetUsuarioEmprestimo(searchUsuario.value)
}

const livroEscolhiodo = async (id)=>{
    livroEmprestimo.value = await emprestimo.GetLivroEmprestimo(id)
    modal.value = false
}

const CriarEmprestimo = async () =>{
    await emprestimo.CriarEmprestimo(livroEmprestimo.value.id,user.value.id,)
    navigateTo('/auth/gerenciar-emprestimos/emprestimos')
}


</script>

