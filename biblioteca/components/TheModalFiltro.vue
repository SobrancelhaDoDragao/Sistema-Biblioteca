<template>

        <Teleport to="body">
      

            <Transition name="bounce">
               <div v-if="modalFiltro" id="modalFiltro" class="modal">
                  <h1>Pesquisar</h1>

                  <form class="form-padrao">
                      
                  <div id="conteiner-search">
                     <input type="text" id="search" v-model="search" > <button class="btn-padrao" @click.prevent="filtrar"> <nuxt-img src="icons/magnifying-glass-solid.svg"  width="20" height="20" ></nuxt-img></button>
                  </div>
                
                     
                  <div id="group-btn-filtro">
                     <button class="btn-padrao" @click.prevent="livros.GetLivros(1)">Limpar pesquisa</button>  <button class="btn-padrao" @click.prevent="modalFiltro = false">Cancelar</button>  
                  </div>
                  </form>
               </div>
            </Transition>
         </Teleport>

        <button class="btn-padrao" id="btn-modal-filter" @click.prevent="modalFiltro = true">Pesquisar</button> 

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
   padding: 1rem;
   background: var(--main-background-color-conteiner);
   border-radius: 10px;
}

#btn-modal-filter{
   width: 8rem;
   margin-bottom: 1rem;
   padding: .5rem;
}

#modalFiltro h1{
    text-align: center;
    margin-bottom: 1rem;
}


#group-btn-filtro{
   display: flex;
   justify-content: space-between;
   margin-top: 1rem;
}
#conteiner-search{
  display: flex;
  gap: 1rem;
}
</style>


<script setup>

let livros = useLivroStore()

// Modal filtro e seus input
let modalFiltro = ref(false)

let search = ref('')

const filtrar = async ()=>{
   let page = 0
   await livros.GetLivros(page,search.value)
   modalFiltro.value = false
}

</script>