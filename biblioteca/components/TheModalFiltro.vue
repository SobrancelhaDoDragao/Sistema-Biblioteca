<template>

        <Teleport to="body">
      

            <Transition name="bounce">
               <div v-if="modalFiltro" id="modalFiltro" class="modal">
                  <h1>Filtrar</h1>

                  <form class="form-padrao">

                     <label for="nome">Nome</label>
                     <input type="text" id="nome" v-model="NomeFiltro" >

                     <label for="editora">Editora</label>
                     <input type="text" id="editora" v-model="EditoraFiltro" >
                     
                  <div id="group-btn-filtro">
                    <button class="btn-padrao" @click.prevent="filtrar">Filtrar</button>  <button class="btn-padrao" @click.prevent="livros.GetLivros(1)">Resetar filtro</button>  <button class="btn-padrao" @click.prevent="modalFiltro = false">Cancelar</button>  
                  </div>
                  </form>
               </div>
            </Transition>
         </Teleport>

        <button class="btn-padrao" id="btn-modal-filter" @click.prevent="modalFiltro = true">Filtrar</button> 

</template>


<style scoped>

#modalFiltro{
  top: 20%;
  left: 50%;  
  width: 50vw;
  height: auto;
  position: absolute;
  z-index: 999;
  /*margin-top: -30vh; /* Metade da altura */
  margin-left: -25vw; /* Metade da largura */
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  background: var(--main-background-color-conteiner);
  padding: 1rem;
  border-radius: 10px;
}

#modalFiltro{
   padding: .5rem;
   background: var(--main-background-color-conteiner);
   border-radius: 10px;
}

#btn-modal-filter{
   width: 5rem;
   margin-bottom: 1rem;
   padding: .5rem;
}

#modalFiltro h1{
    text-align: center;
}


#group-btn-filtro{
   display: flex;
   justify-content: space-between;
   margin-top: 1rem;
}

</style>


<script setup>

let livros = useLivroStore()

// Modal filtro e seus input
let modalFiltro = ref(false)

let NomeFiltro = ref('')
let EditoraFiltro = ref('')

const filtrar = async ()=>{
   let page = 0
   await livros.GetLivros(page,NomeFiltro.value,EditoraFiltro.value)
   modalFiltro.value = false
}

</script>