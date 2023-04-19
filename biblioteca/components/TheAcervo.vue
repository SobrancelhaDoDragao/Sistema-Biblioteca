<template>
    <main id="main-acervo" class="conteiner-padrao" >
               

      <Teleport to="body">
               <!--Essa div só deve ser visivel para admins-->

            <Transition name="bounce">
               <div v-if="modal" id="AcervoForm" class="modal">
                  <h1>Cadastrar Livro</h1>

                  <form class="form-padrao">

                     <label for="nome">Nome</label>
                     <input type="text" id="nome" v-model="nome" >

                     <label for="editora">Editora</label>
                     <input type="text" id="editora" v-model="editora" >
                     
                     <label for="capa">Capa</label>
                     <input type="file" name="" id="capa" v-on:change="filechange" >
                     

                  <p id="ErroCadastroForm" v-if="ErroCadastroForm" >{{ErroCadastroForm}}</p>

                  <div id="group-btn-cadastro">
                    <button class="btn-padrao" @click.prevent="cadastrolLivro">Cadastrar</button> <button class="btn-padrao" @click.prevent="modal = false">Cancelar</button>  
                  </div>
                  </form>
               </div>
            </Transition>
         </Teleport>



         <Teleport to="body">
               <!--Essa div só deve ser visivel para admins-->

            <Transition name="bounce">
               <div v-if="modalFiltro" id="modalFiltro" class="modal">
                  <h1>Filtrar</h1>

                  <form class="form-padrao">

                     <label for="nome">Nome</label>
                     <input type="text" id="nome" v-model="NomeFiltro" >

                     <label for="editora">Editora</label>
                     <input type="text" id="editora" v-model="EditoraFiltro" >
                     
                  <div id="group-btn-cadastro">
                    <button class="btn-padrao" @click.prevent="filtrar">Filtrar</button> <button class="btn-padrao" @click.prevent="modalFiltro = false">Cancelar</button>  
                  </div>
                  </form>
               </div>
            </Transition>
         </Teleport>

               <div id="LivroConteiner">
               
                  <h1 id="h1Acervo">Acervo</h1>

                  <div  id="btn-modal-group">
                     <button class="btn-padrao" id="btn-modal-acervo" @click.prevent="modal = true">Cadastrar livro</button> <button class="btn-padrao" id="btn-modal-filter" @click.prevent="modalFiltro = true">Filtrar</button> 
                  </div>
                   

                     <div class="Livros">

                        <div v-for="livro in livros.livrosDados.livros" :key="livro.id" >

                           <NuxtLink :to="'/auth/acervo/livro/'+livro.id"> 
                           <nuxt-img class="livro" :src="'/serverImage/'+livro.capa" format="webp" width="100" height="150" placeholder />
                           </NuxtLink>

                        </div>
                        
                     </div>

                  <div id="btn-group-pagination">

                  
                     <button class="btn-pagination" v-on:click="livros.GetLivros(livros.livrosDados.previousPageNumber)">Voltar</button>
                       
                     <button :class="{ active: livros.livrosDados.PageActive == pagina }" class="btn-pagination" v-on:click="livros.GetLivros(pagina)" v-for="pagina in livros.livrosDados.quantidadePagina">{{ pagina }}</button>

                     <button class="btn-pagination" v-on:click="livros.GetLivros(livros.livrosDados.nextPageNumber)">Proxima</button>

                  </div>
               </div>
   </main>
</template>

<style scoped>
/**Colocar no lugar do sidebar um filtro de livros e formulario para cadastrar livros */

#main-acervo{
   flex: 4;
   display: grid;
   grid-template-columns: 1fr 1fr;
   grid-template-areas: "livro livro";
   gap: 1rem;
   max-height: 78vh;
}

#LivroConteiner{
   grid-area: livro;
   border-left:solid var(--colorOne)10px;
   border-right: solid var(--colorOne) 10px;
   border-radius: 30px;
   background: var(--main-background-color);
   overflow: auto;
   display: flex;
   flex-direction: column;
   padding: .5rem 1rem;
}

.Livros{
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
  align-content: center;
  flex: 1;
}

#h1Acervo{
   text-align: center;
}

.livro:hover{
   border: solid var(--colorTwo) 4px;
   cursor: pointer;
}

.imagem-none{
   width: 100%;
   height: 100%;
   display: flex;
   align-items: center;
   text-align: center;
}

#AcervoForm{
   padding: .5rem;
   background: var(--main-background-color-conteiner);
   padding: 1rem;
   border-radius: 20px;
   border: solid var(--colorOne) 2px;
}

#modalFiltro{
   padding: .5rem;
   background: var(--main-background-color-conteiner);
   padding: 1rem;
   border-radius: 20px;
   border: solid var(--colorOne) 2px;
}


#btn-group-pagination{
   display: flex;
   justify-content: center;
   margin-top: .5rem;
   gap: 5px;
}

.btn-pagination{
  background: var(--main-background-color-conteiner);
  color:var(--colorTwo);
  font-weight: var(--bold-weight);
  padding:.5rem;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  font-size: 1rem;
}

#btn-modal-group{
display: flex;
justify-content: space-between;
}

.active{
   background: var(--colorOne);
}

.modal {
  position: fixed;
  z-index: 999;
  top: 20%;
  left: 50%;
  width: 300px;
  margin-left: -150px;
}

#group-btn-cadastro{
   display: flex;
   justify-content: space-between;
   margin-top: 1rem;
}

#btn-modal-acervo{
   width: 8rem;
   margin-bottom: 1rem;
   padding: .5rem;
}
#btn-modal-filter{
   width: 5rem;
   margin-bottom: 1rem;
   padding: .5rem;
}

#ErroCadastroForm{
  color: var(--colorTwo);
  text-align: center;
}
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}
</style>

<script setup>
      
      // Modal cadastro e seus input
      let modal = ref(false)

      let nome = ref('')
      let editora = ref('')
      let capa = ref('')

      let ErroCadastroForm = ref()


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

      let cadastrolLivro = async()=>{
            
            if(nome.value == ''|| editora.value == ''){
               ErroCadastroForm.value = 'Preecha todos os campos'
            }
            else if(capa.value == ''){
               ErroCadastroForm.value = 'Nenhuma imagem foi enviada'
            }
            else{
               await livros.CreateLivro(nome,editora,capa)
               await livros.GetLivros(livros.livrosDados.PageActive)
               modal.value = false
            }    
      }
 
      // Modal filtro e seus input
      let modalFiltro = ref(false)

      let NomeFiltro = ref('')
      let EditoraFiltro = ref('')

      const filtrar = async ()=>{
         let page = 0
         await livros.GetLivros(page,NomeFiltro.value,EditoraFiltro.value)
         modalFiltro.value = false
      }
       
      let livros = useLivroStore()

      
      if(livros.livrosDados.PageActive){
         livros.GetLivros(livros.livrosDados.PageActive)
      }
      else{
         livros.GetLivros(1) //Primeira pagina
      }
      
</script>
