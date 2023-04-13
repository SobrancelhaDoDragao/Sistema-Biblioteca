import { defineStore } from 'pinia'

export const useLivroStore = defineStore('Livro', {
    state: () => {
      return {
        livro:{id:'',nome:'',editora:'',capa:''},
        livros: []
      }
    },
  
    actions:{  
      async GetLivros(){

        // Url base do back-end
        // Não fica disponivel no url /
        const config = useRuntimeConfig()
    
        const response = await $fetch(`${config.apiBase}createlivro/`,{
                method:'GET',
                headers:{'Content-Type':'application/json'}
        });

        const livros = response

        this.livros = livros
      },


      async CreateLivro(nome,editora,capa){

        // Url base do back-end
        // Não fica disponivel no url /
        const config = useRuntimeConfig()
        
        let form = {
          nome: nome.value,
          editora: editora.value,
          capa: capa.value
        }

      
        let response = await $fetch(`${config.apiBase}createlivro/`,{
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body:form
          });


        this.livros.push(response)

      },

      async GetLivro(id){

        const config = useRuntimeConfig()

        const form = {id:id}

        let response = await $fetch(`${config.apiBase}livro/`,{
                  method:'POST',
                  headers:{'Content-Type':'application/json'},
                  body:form
        });
        
        this.livro.id = response.id
        this.livro.nome = response.nome
        this.livro.capa = response.capa
        this.livro.editora = response.editora
      },

      async PutLivro(id,nome,editora,capa,){

        const config = useRuntimeConfig()

        const form = {
          id:id,
          nome: nome.value,
          editora: editora.value,
          capa: capa.value
        }

        let response = await $fetch(`${config.apiBase}livro/`,{
                  method:'PUT',
                  headers:{'Content-Type':'application/json'},
                  body:form
        });
        
        this.livro.id = response.id
        this.livro.nome = response.nome
        this.livro.capa = response.capa
        this.livro.editora = response.editora
      },


      async DeleteLivro(id){

        const config = useRuntimeConfig()

        const form = {id:id}

        let response = await $fetch(`${config.apiBase}livro/`,{
                  method:'DELETE',
                  headers:{'Content-Type':'application/json'},
                  body:form
        });
      }
  
    }
  
  })