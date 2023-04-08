import { defineStore } from 'pinia'

export const useLivroStore = defineStore('User', {
    state: () => {
      return {
        nome:'',
        editora:'',
        capa:'dededed',
      }
    },
  
    actions:{
      async GetToken(){
  
        this.access = useCookie('access')
        this.refresh = useCookie('refresh')
  
        let bearer = 'Bearer ' + this.access;
  
        return bearer
      },
  
      async GetLivros(){

        // Url base do back-end
        // Não fica disponivel no url /
        const config = useRuntimeConfig()
    
        const response = await $fetch(`${config.apiBase}livro/`,{
                method:'GET',
                headers:{'Content-Type':'application/json'}
        });

        const livros = response
      },
  
      async CreateLivro(nome,editora){
  
      }
  
    }
  
  })