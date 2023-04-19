import { defineStore } from 'pinia'

export const useLivroStore = defineStore('Livro', {
    state: () => {
      return {
        livro:{id:'',nome:'',editora:'',capa:''}, //Usado apenas pelo putLivro e Getlivro
        livrosDados: {PageActive:null,quantidadePagina:0,livros:[],nextPageNumber:null,previousPageNumber:null},
      }
    },
  
    actions:{  
      async GetLivros(page,nome,editora){
        
        if(page != null){

          // Url base do back-end
          // Não fica disponivel no url /
          const config = useRuntimeConfig()
          
          let url = `${config.apiBase}createlivro/`

          if(nome || editora){
            url = url + `?nome=${nome}&editora=${editora}`
          }
          else{
            url = url + `?page=${page}`
          }

          const response = await $fetch(url,{
                  method:'GET',
                  headers:{'Content-Type':'application/json'}
          });

          const livros = response.results
        
          this.livrosDados.livros = livros
          this.livrosDados.nextPageNumber = response.links.nextPageNumber
          this.livrosDados.previousPageNumber = response.links.previousPageNumber
          this.livrosDados.quantidadePagina = response.links.TotalPages
          this.livrosDados.PageActive = response.links.PageActive
       }
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

        await $fetch(`${config.apiBase}createlivro/`,{
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body:form
          });
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