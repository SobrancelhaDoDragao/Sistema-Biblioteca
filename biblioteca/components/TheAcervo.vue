<template>
    <main>
               <div id="Filtro">
                  Filtro
               </div>
                  

               <!--Essa div só deve ser visivel para admins-->
               <div id="AcervoForm">
                  <h1>Cadastrar livro</h1>

                  <form action="">

                     <label for="nome">Nome</label>
                     <input type="text" id="nome" v-model="nome" >

                     <label for="editora">Editora</label>
                     <input type="text" id="editora" v-model="editora" >

                     <button id="btn-acervo" @click.prevent="cadastrolLivro">Cadastrar</button>

                  </form>
               </div>

               <div id="LivroConteiner">

                  <h1>Acervo</h1>
                        
                     <div class="Livros">

                        <div class="Livro" v-for="livro in livros.livros" :key="livro.id" >
                           <div class="imagem-none">
                              Sem imagem
                           </div>
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
   border-left:solid var(--colorSix)10px;
   border-right: solid var(--colorSix) 10px;
   border-radius: 30px;
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
      let capa = ref('rfderf0uj')
   
      let livros = useLivroStore()

      livros.GetLivros()
      
      let cadastrolLivro = async()=>{
     
            livros.CreateLivro(nome,editora,capa)
             
            // Aqui deve estar dando erro
            nome = ''
            editora = ''
      }
    
      
      

</script>