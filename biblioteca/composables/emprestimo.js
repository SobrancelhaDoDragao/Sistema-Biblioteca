import { defineStore } from 'pinia'


export const useEmprestimoStore = defineStore('Emprestimo', {
    state: () => {
      return {
        emprestimosDados: {PageActive:null,quantidadePagina:0,emprestimos:[],nextPageNumber:null,previousPageNumber:null},
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

      async getEmprestimos(page,search){

        if(page != null){

          const urlBase = await this.GetUrlBaseRuntimeConfig()
          const token = await this.GetToken()
                
          let url = `${urlBase}emprestimos/`

          if(search){
            url = url + `?search=${search}`
          }
          else{
            url = url + `?page=${page}`
          }
      
    
          const response = await $fetch(url,{
                    method:'GET',
                    headers:{'Content-Type':'application/json',
                    'Authorization': token}   
          });

          const emprestimos = response.results

          this.emprestimosDados.emprestimos = emprestimos

          this.emprestimosDados.nextPageNumber = response.links.nextPageNumber
          this.emprestimosDados.previousPageNumber = response.links.previousPageNumber
          this.emprestimosDados.quantidadePagina = response.links.TotalPages
          this.emprestimosDados.PageActive = response.links.PageActive

        }
      },
      async getEmprestimo(id){

        const urlBase = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        const response = await $fetch(`${urlBase}emprestimos/${id}`,{
                method:'GET',
                headers:{'Content-Type':'application/json', 'Authorization': token} 
        });

        return response
           
      },

      async CriarEmprestimo(livro, user){

        const urlBase = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        let form = {
              "livro":livro,
              "usuario":user
        } 
        
        const response = await $fetch(`${urlBase}emprestimos/`,{
                method:'POST',
                headers:{'Content-Type':'application/json','Authorization': token},
                body:form
        });
           
      },


      async GetUsuarioEmprestimo(searchUsuario){

        const urlBase = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        const response = await $fetch(`${urlBase}/users/?search=${searchUsuario}`,{
            method:'GET',
            headers:{'Content-Type':'application/json','Authorization': token}
        });

        // Sempre ira retornar apenas um
        return response.results[0]
      },

      async GetLivroEmprestimo(id){

        const urlBase = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        let response = await $fetch(`${urlBase}livros/${id}`,{
                  method:'GET',
                  headers:{'Content-Type':'application/json',
                  'Authorization': token},
        });
             
        return response
      },

      async PutEmprestimo(id,status){

        const urlBase = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        const response = await $fetch(`${urlBase}emprestimos/${id}/`,{
                method:'PATCH',
                headers:{'Content-Type':'application/json','Authorization': token},
                body:{ "status": status }
        });

      },

      async DeleteEmprestimo(id){

        const urlBase = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()

        const response = await $fetch(`${urlBase}emprestimos/${id}/`,{
                method:'DELETE',
                headers:{'Content-Type':'application/json','Authorization': token}
        });

      }
    }
  
  })