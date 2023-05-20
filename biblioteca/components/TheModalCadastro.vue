<template>

<Teleport to="body">
               <!--Essa div só deve ser visivel para admins-->

            <Transition name="bounce">
               <div v-if="modal" id="modalCadastro">
                  <h1>Cadastrar Livro</h1>

                  <form id="formCadastroLivro" class="form-padrao">
                    
                        <div>
                        <label for="nome">Nome <span>*Obrigatório</span></label>
                        <input type="text" id="nome" v-model="nome">
                        </div>
                        

                        <div>
                        <label for="editora">Editora</label>
                        <input type="text" id="editora" v-model="editora" >
                        </div>
                        
                        <div>
                        <label for="autor">Autor <span>*Obrigatório</span></label>
                        <input type="text" id="autor" v-model="autor">
                        </div>
                        
                        <div>
                        <label for="genero">Gênero</label>
                        <input type="text" id="genero" v-model="genero">
                        </div>

                        <div id="descricaoDiv">
                            <label for="descricao">Descrição</label>
                   
                            <textarea id="descricao" v-model="descricao">
                  
                            </textarea>
                        </div>
                        <div id="capaDiv" >
                            <label for="capa">Capa <span>*Obrigatório</span></label>
                            <input type="file" id="capa" ref="capa">
                        </div>
                    
                </form>  

                  <p id="ErroCadastroForm" v-if="ErroCadastroForm" >{{ErroCadastroForm}}</p>

                  <div id="group-btn-cadastro">
                    <button class="btn-padrao" @click.prevent="cadastrolLivro">Cadastrar</button> <button class="btn-padrao" @click.prevent="modal = false">Cancelar</button>  
                  </div>
               
               </div>
            </Transition>
         </Teleport>

         <button class="btn-padrao" id="btn-modal-acervo" @click.prevent="modal = true">Cadastrar livro</button> 

</template>

<style scoped>

#modalCadastro{
  top: 5%;
  left: 50%;  
  width: 80vw;
  height: auto;
  position: absolute;
  z-index: 999;
  /*margin-top: -30vh; /* Metade da altura */
  margin-left: -40vw; /* Metade da largura */
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  background: var(--main-background-color-conteiner);
  padding: 1rem;
  border-radius: 10px;
}

#formCadastroLivro{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    align-items: last baseline;
}


#descricaoDiv{
/*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
  grid-area: 3 / 1 / 3 / 3;
}

#capaDiv{
  /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
  grid-area: 4 / 1 / 4 / 3;
}

#modalCadastro h1{
    text-align: center;
    margin-bottom: .5rem;
}

#modalCadastrol h1{
    text-align: center;
    font-size: 3rem;
    margin-bottom: 1rem;
}

form{
    outline: solid 1px var(--colorFive);
    padding: 1rem;
    background: var(--main-background-color);
    border-radius: 10px;
}

textarea {
    font-size: 1rem;
    width: 100%;
    height: 15vh;
    padding: 5px;
    max-width: 100%;
    border-radius: 5px;
    border: 1px solid #ccc;
    box-shadow: 1px 1px 1px #999;
}

#group-btn-cadastro{
   display: flex;
   justify-content: space-between;
   margin-top: 1rem;
}

#btn-modal-acervo{
   width: 10rem;
   margin-bottom: 1rem;
   padding: .2rem;
}

#ErroCadastroForm{
  color: red;
  text-align: center;
}

@media only screen and (max-width:550px){

  #modalCadastro{
    width: 90vw;
    margin-left: -45vw; /* Metade da largura */
  }
  
}
</style>


<script setup>
let livros = useLivroStore()

// Modal cadastro e seus input
let modal = ref(false)

let nome = ref('')
//let capa = ref('')
let autor = ref('')
let editora = ref('')
let genero = ref('')
let descricao = ref('')
let ErroCadastroForm = ref()

let capa = ref(null)

let cadastrolLivro = async()=>{
      
      if(nome.value == ''|| autor.value == ''){
         ErroCadastroForm.value = 'Preecha todos os campos obrigatórios'
      }

      else{
         let formData = new FormData()

         formData.append('nome',nome.value)
         formData.append('capa',capa.value.files[0])
         formData.append('autor',autor.value)
         formData.append('editora',editora.value)
         formData.append('genero',genero.value)
         formData.append('descricao',descricao.value)

         
         await livros.CreateLivro(formData)
         await livros.GetLivros(livros.livrosDados.PageActive)
         modal.value = false
      }    
}
</script>