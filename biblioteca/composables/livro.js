import { defineStore } from 'pinia'

export const useLivroStore = defineStore('Livro', {
    state: () => {
      return {
        livro:{id:'',nome:'',editora:'',capa:''}, //Usado apenas pelo putLivro e Getlivro
        livrosDados: {PageActive:null,quantidadePagina:0,livros:[],nextPageNumber:null,previousPageNumber:null},
      }
    },
  
    actions:{  

      async GetUrlBaseRuntimeConfig(){
        // Nem sempre está disponivel no server por isso usarei try e catch
        try {
          const config = useRuntimeConfig()
  
          return config.public.apiBase
  
        } catch (error) {
          
          console.log('RuntimeConfig ainda não está disponivel')
          return "http://127.0.0.1:8000/api/"
        }  
      },

      async GetToken(){

        let access = useCookie('access')
        //let refresh = useCookie('refresh')
       
        let bearer = 'Bearer ' + access.value;
  
        return bearer
      },

      async GetLivros(page,nome,editora){
        
        if(page != null){

          const urlBase = await this.GetUrlBaseRuntimeConfig()
          const token = await this.GetToken()
          
          let url = `${urlBase}createlivro/`

          if(nome || editora){
            url = url + `?nome=${nome}&editora=${editora}`
          }
          else{
            url = url + `?page=${page}`
          }

          const response = await $fetch(url,{
                  method:'GET',
                  headers:{'Content-Type':'application/json',
                  'Authorization': token,
                  },      
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

        const url = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        let form = {
          nome: nome.value,
          editora: editora.value,
          capa: capa.value
        }

        await $fetch(`${url}createlivro/`,{
          method:'POST',
          headers:{'Content-Type':'application/json',
                  'Authorization': token},    
          body:form
          });
      },

      async GetLivro(id){

        const url = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        const form = {id:id}

        let response = await $fetch(`${url}livro/`,{
                  method:'POST',
                  headers:{'Content-Type':'application/json',
                  'Authorization': token},
                  body:form
        });
        
        this.livro.id = response.id
        this.livro.nome = response.nome
        this.livro.capa = response.capa
        this.livro.editora = response.editora
      },

      async PutLivro(id,nome,editora,capa,){

        const url = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        const form = {
          id:id,
          nome: nome.value,
          editora: editora.value,
          capa: capa.value
        }

        let response = await $fetch(`${url}livro/`,{
                  method:'PUT',
                  headers:{'Content-Type':'application/json',
                  'Authorization': token},
                  body:form
        });
        
        this.livro.id = response.id
        this.livro.nome = response.nome
        this.livro.capa = response.capa
        this.livro.editora = response.editora
      },


      async DeleteLivro(id){

        const url = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()
        
        const form = {id:id}

        let response = await $fetch(`${url}livro/`,{
                  method:'DELETE',
                  headers:{'Content-Type':'application/json',
                  'Authorization': token},
                  body:form
        });
      }
  
    }
  
  })