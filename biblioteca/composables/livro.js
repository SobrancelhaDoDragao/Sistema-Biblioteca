import { defineStore } from 'pinia'

export const useLivroStore = defineStore('Livro', {
    state: () => {
      return {
        livro:{id:'',nome:'',capa:'',autor:'',editora:'',genero:'',descricao:''}, //Usado apenas pelo putLivro e Getlivro
        livrosDados: {PageActive:null,quantidadePagina:0,livros:[],nextPageNumber:null,previousPageNumber:null},
        novoslivros: []
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
          return "http://127.0.0.1:8000/"
        }  
      },

      async GetToken(){

        let access = useCookie('access')
        //let refresh = useCookie('refresh')
       
        let bearer = 'Bearer ' + access.value;
  
        return bearer
      },

      async GetLivros(page,search){
        
        if(page != null){

          const urlBase = await this.GetUrlBaseRuntimeConfig()
          const token = await this.GetToken()
          
          let url = `${urlBase}livros/`

          if(search){
            url = url + `?search=${search}`
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


      async CreateLivro(form){

        const url = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        let response = await $fetch(`${url}livros/`,{
          method:'POST', 
          headers:{'Authorization': token},   
          body:form
          });

      },

      async GetLivro(id){

        const url = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        let response = await $fetch(`${url}livros/${id}`,{
                  method:'GET',
                  headers:{'Content-Type':'application/json',
                  'Authorization': token},
        });
        
       this.livro = response

      },

      async PutLivro(id,form){

        const url = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        let response = await $fetch(`${url}livros/${id}/`,{
                  method:'PATCH',
                  headers:{'Authorization': token},
                  body:form
        });
        
        this.livro.id = response.id
        this.livro.nome = response.nome
        this.livro.capa = response.capa
        this.livro.autor = response.autor
        this.livro.editora = response.editora
        this.livro.genero = response.genero
        this.livro.descricao = response.descricao
      },


      async DeleteLivro(id){

        const url = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()
        
        let response = await $fetch(`${url}livros/${id}`,{
                  method:'DELETE',
                  headers:{'Content-Type':'application/json',
                  'Authorization': token},
        });
      },

      async GetNovosLivros(){

        const url = await this.GetUrlBaseRuntimeConfig()

        const response = await $fetch(`${url}novoslivros/`,{
                      method:'GET',
                      headers:{'Content-Type':'application/json'}
        });
  
        this.novoslivros = response.results
      }
  
    }
  
  })