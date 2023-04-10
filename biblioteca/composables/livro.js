import { defineStore } from 'pinia'

export const useLivroStore = defineStore('Livro', {
    state: () => {
      return {
        livros: []
      }
    },
  
    actions:{  
      async GetLivros(){

        // Url base do back-end
        // Não fica disponivel no url /
        const config = useRuntimeConfig()
    
        const response = await $fetch(`${config.apiBase}livro/`,{
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

        console.log(form)

        let response = await $fetch(`${config.apiBase}livro/`,{
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body:form
          });

        this.livros.push(form)

      }
  
    }
  
  })