<template>
    <main>
               <div id="Filtro">
                  Filtro
               </div>
                  

               <!--Essa div só deve ser visivel para admins-->
               <div id="AcervoForm">
                  <h1>Cadastrar livro</h1>

                  <form>

                     <label for="nome">Nome</label>
                     <input type="text" id="nome" v-model="nome" >

                     <label for="editora">Editora</label>
                     <input type="text" id="editora" v-model="editora" >
                     
                     <label for="capa">Capa</label>
                     <input type="file" name="" id="capa" v-on:change="filechange" >

                     <button id="btn-acervo" @click.prevent="cadastrolLivro">Cadastrar</button>

                  </form>
               </div>

               <div id="LivroConteiner">

                  <h1>Acervo</h1>
                        
                     <div class="Livros">

                        <div class="Livro" v-for="livro in livros.livros" :key="livro.id" >
                        
                           <nuxt-img :src="'http://localhost:8000/static/img/'+livro.capa" format="webp" width="100" height="150"/>
                           
                           <h5 class="livro-title">{{ livro.nome }}</h5>

                        </div>
 
                     </div>
                    

               </div>
   </main>
</template>

<style scoped>
/**Colocar no lugar do sidebar um filtro de livros e formulario para cadastrar livros */

main{
   background-color: var(--main-background-color-conteiner);
   padding: 1rem;
   border-radius: 10px;
   flex: 4;
   border: solid var(--colorSix) 2px;
   
   display: grid;
   grid-template-columns: 1fr 2fr;
   grid-template-areas: "filtro livro"
                         "form livro"
   ;
   gap: 1rem;
}

main h1{
   font-weight: var(--thin-weight);
   text-align: center;
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
  gap: 2rem;
  flex-wrap: wrap;
  margin-top: .5rem;
}

.Livro{
   width: 90px;
   height: 140px;
   background: rgb(173, 162, 162);
}

.imagem-none{
   width: 100%;
   height: 100%;

   display: flex;
   align-items: center;
   text-align: center;
}

.livro-title{
   text-align: center;
   font-weight: var(--thin-weight);
   font-size: 1rem;
}

#AcervoForm{
   grid-area: form;
   padding: .5rem;
}

label{
    color: var(--colorFour);
    font-weight: var(--thin-weight);
}

input{
    width: 100%;
    border:none;
    border-radius: 10px;
    padding: 15px;
    color: var(--colorFour);
    font-size: 1rem;
    outline: none;
    border: solid var(--colorSix) 1px;
    font-weight: var(--thin-weight);
}

#btn-acervo{
   background: var(--colorOne);
   color:var(--colorThree);
   font-weight: var(--bold-weight);
   padding: 8px 18px;
   border: none;
   border-radius: 10px;
   font-size: 1rem;
   margin-top: 1rem;
   cursor: pointer;
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