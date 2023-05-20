<template>
    <main id="main-acervo" class="conteiner-padrao" >
               
               <div id="LivroConteiner">
               
                  <h1>Acervo</h1>

                  <div  id="btn-modal-group">
                  <TheModalCadastro></TheModalCadastro>  <TheModalFiltro></TheModalFiltro>     
                  </div>
                   

                  <div class="Livros">

                        <div v-for="livro in livros.livrosDados.livros" :key="livro.id" >

                           <NuxtLink :to="'/auth/acervo/livro/'+livro.id">
                              <nuxt-img class='sobre-livros' :src="livro.capa" format="webp" sizes="sm:30vw md:15vw lg:10vw"/>
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
   height: 100%;
}

#LivroConteiner{
   grid-area: livro;
   border-left:solid var(--colorFive)10px;
   border-right: solid var(--colorFive) 10px;
   border-top: solid var(--colorFive) 5px;
   border-bottom:solid var(--colorFive) 5px;
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

.imagem-none{
   width: 100%;
   height: 100%;
   display: flex;
   align-items: center;
   text-align: center;
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
flex-wrap: wrap;
}

.active{
   background: var(--colorOne);
}

</style>

<script setup>

   let livros = useLivroStore()
   
      
   if(livros.livrosDados.PageActive){
      livros.GetLivros(livros.livrosDados.PageActive)
   }
   else{
      livros.GetLivros(1) //Primeira pagina
   }

     
</script>
