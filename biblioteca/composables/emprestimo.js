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

      FormatarData(dataString){

        const data = new Date(dataString);
        const ano = data.getFullYear();
        const mes = ("0" + (data.getMonth() + 1)).slice(-2); // Adiciona um zero à esquerda do mês, se necessário
        const dia = ("0" + data.getDate()).slice(-2); // Adiciona um zero à esquerda do dia, se necessário
        const dataFormatada = dia + '/' + mes + '/' + ano;

        return dataFormatada
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

          // Formatando data
          for (let index = 0; index < emprestimos.length; index++) {
            
            const dataFormatada = this.FormatarData(emprestimos[index].data_devolucao);
            
            emprestimos[index].data_devolucao = dataFormatada
          }
          
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

        const dataFormatada = this.FormatarData(response.data_devolucao);

        response.data_devolucao = dataFormatada

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

        const response = await $fetch(`${urlBase}all_users/?search=${searchUsuario}`,{
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

      async PutEmprestimo(id,status,data){

        const urlBase = await this.GetUrlBaseRuntimeConfig()
        const token = await this.GetToken()
        
        let form = { "status": status}

        if(data){
          form = { "status": status, "data_devolucao":data}
        }
       
        const response = await $fetch(`${urlBase}emprestimos/${id}/`,{
                method:'PATCH',
                headers:{'Content-Type':'application/json','Authorization': token},
                body:form
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