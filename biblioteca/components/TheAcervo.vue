<template>
    <main id="main-acervo" class="conteiner-padrao" >
               <div id="Filtro">
                  Filtro
               </div>
                  

               <!--Essa div só deve ser visivel para admins-->
               <div id="AcervoForm">
                  <h1>Cadastrar livro</h1>

                  <form class="form-padrao">

                     <label for="nome">Nome</label>
                     <input type="text" id="nome" v-model="nome" >

                     <label for="editora">Editora</label>
                     <input type="text" id="editora" v-model="editora" >
                     
                     <label for="capa">Capa</label>
                     <input type="file" name="" id="capa" v-on:change="filechange" >

                     <button id="btn-acervo" class="btn-padrao" @click.prevent="cadastrolLivro">Cadastrar</button>

                  </form>
               </div>

               <div id="LivroConteiner">

                  <h1>Acervo</h1>
                        
                     <div class="Livros">

                        <div v-for="livro in livros.livros" :key="livro.id" >

                           <NuxtLink :to="'/auth/acervo/livro/'+livro.id"> 
                           <nuxt-img class="livro" :src="'http://localhost:8000/static/img/'+livro.capa" format="webp" width="100" height="150"/>
                           </NuxtLink>

                        </div>
 
                     </div>
                    

               </div>
   </main>
</template>

<style scoped>
/**Colocar no lugar do sidebar um filtro de livros e formulario para cadastrar livros */

#main-acervo{
   flex: 4;
   display: grid;
   grid-template-columns: 1fr 2fr;
   grid-template-areas: "filtro livro"
                         "form livro"
   ;
   gap: 1rem;
}

#filtro{
   grid-area: filtro;
}

#LivroConteiner{
   grid-area: livro;
   padding: 1rem;
   border-left:solid var(--colorOne)10px;
   border-right: solid var(--colorOne) 10px;
   border-radius: 30px;
   background: var(--main-background-color);
}

.Livros{
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
  align-content: center;
  height: 90%;
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

#btn-acervo{
   margin-top: 1rem;
}

#AcervoForm{
   grid-area: form;
   padding: .5rem;
}


</style>

<script setup>

      let nome = ref()
      let editora = ref()
      let capa = ref()
       
      let livros = useLivroStore()

      livros.GetLivros()
      
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
     
            await livros.CreateLivro(nome,editora,capa)
            await livros.GetLivros()        
      }
    
</script>